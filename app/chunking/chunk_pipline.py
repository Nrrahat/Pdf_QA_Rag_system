import json
from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_experimental.text_splitter import SemanticChunker
from langchain_core.runnables import RunnableLambda
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from pathlib import Path


embadding_model=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def _markdown_step(text:str):
    header_to_split_on=[
        ('#',"header1"),
        ('##',"header2"),
    ]
    splitter=MarkdownHeaderTextSplitter(headers_to_split_on=header_to_split_on)
    return splitter.split_text(text)


def _semantic_step(text:list[Document]):

    semantic_splitter=SemanticChunker(
        embadding_model,
        breakpoint_threshold_type="percentile",
        breakpoint_threshold_amount=90.0 
        )
    
    return semantic_splitter.split_documents(text)


_hybrid_chain=RunnableLambda(_markdown_step)|RunnableLambda(_semantic_step )



def hybrid_chunking(input_dir:str,process_dir:str):
   input_path=Path(input_dir)
   process_path=Path(process_dir)
   process_path.mkdir(parents=True,exist_ok=True)

   for file in input_path.glob("*.md"):
       file_stem_only=file.stem
       terget=(process_path/file_stem_only).with_suffix(".json")
       
       if terget.exists():
            continue
       with open(file,"r") as f:
            text=f.read()
            process_doc=_hybrid_chain.invoke(text)
        
       serialized_doc=[
            {
                "page_content":doc.page_content,
                "metadata":doc.metadata
            }
            for doc in process_doc
        ]
       with open(terget,"w",encoding="utf-8") as f:
           json.dump(serialized_doc,f,ensure_ascii=False,indent=4)