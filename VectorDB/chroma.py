import chromadb
from chromadb import Collection
from chromadb import Client

from openai import OpenAI


class vectordb:

    def __init__(self, db_path: str, collec_name: str, openai_key: str, dist: str = "cosine") -> None:

        self.db_path = db_path
        self.collec_name = collec_name
        self.dist = dist
        self.openai_key = openai_key

        self.vector_client = chromadb.PersistentClient(path=rf"{self.db_path}")
        self.collection = self.vector_client.get_or_create_collection(name=self.collec_name, metadata={"hnsw:space": self.dist})

        self.openai_client = OpenAI(api_key = self.openai_key)


    def get_embeddings(self, text: str, model: str = "text-embedding-3-small"):
        return self.openai_client.embeddings.create(input = [text], model = model).data[0].embedding
    
    
    def add_embeddings(self, ids: str|list, text: str|list, path: str, model: str = "text-embedding-3-small"):
         
        if isinstance(text, list):
            embeddings = []
            metadatas = []
            for index, element in enumerate(text):
                embeddings.append(self.get_embeddings(element, model=model))
                metadatas.append({"path": path[index]})
            self.collection.add(
                documents = text,
                ids = ids,
                embeddings = embeddings,
                metadatas = metadatas
            )
        
        elif isinstance(text, str):
            self.collection.add(
                documents = [text],
                ids = [ids],
                embeddings = [self.get_embeddings(text, model = model)],
                metadatas = [{"path": path}]
            )

        else:
            raise Exception(" INVALID DATATYPE!!!!!! Only 'str' and 'list' are allowed. ")
        
        print("Collection updated")
        
        
    def query(self, text: str):
        embedding = self.get_embeddings(text)
        result = self.collection.query(
            query_embeddings = embedding
        )
        
        return (result['documents'][0][0], result["metadatas"][0][0])
    