from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(
    model="all-minilm:l6-v2"
)
vector_store = Chroma(
    collection_name="dharmik",
    embedding_function=embeddings,
    persist_directory="./chroma_langchain_db",
)
