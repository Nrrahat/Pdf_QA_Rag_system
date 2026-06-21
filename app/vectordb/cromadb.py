from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings

class ChromaDB:
    def __init__(self,db_path:str="./chroma_db",collection_name:str="my_documents_chunk"):
        self.db_path=db_path
        self.collection_name=collection_name

    def save_data(self,documents: list[Document],embedding_model: Embeddings):

        vector_store=Chroma.from_documents(
            embedding=embedding_model,
            persist_directory=self.db_path,
            documents=documents,
            collection_name=self.collection_name
        )