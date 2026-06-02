import pymupdf4llm
from pathlib import Path

def load_pdf(input_dic, process_dic):
    """
    Load a PDF file, convert it to markdown, and safely save it.
    """
    input_file=Path(input_dic) ## make the the path object

    process_dic=Path(process_dic)    ## make the destination path object
    """
        loop for iteration of all pdf file exist into the input_dic
    """
    for file in input_file.glob("*.pdf"):

        file_only_stem=file.stem

        markdown=pymupdf4llm.to_markdown(file)

        target=(process_dic/file_only_stem).with_suffix(".md")
        
        if target.exists():
            target.unlink()  ## if the file exist then delete it before write the new one

        with open(target,"w", encoding="utf-8") as f:
            f.write(markdown) 
