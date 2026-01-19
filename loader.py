from langchain_pymupdf4llm import PyMuPDF4LLMLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from shared.vector_store_config import vector_store


file_path = "pdfs/Shri-Ram-Charitmanas-English.pdf"
loader = PyMuPDF4LLMLoader(file_path=file_path)


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1500,
    chunk_overlap=300,
    add_start_index=True,
)

all_splits=[]

for doc in loader.lazy_load():
    print(f"Page {doc.metadata['page']}/{doc.metadata['total_pages']}")
    splits = text_splitter.split_documents([doc])
    all_splits.extend(splits)


print(f"Total chunks created: {len(all_splits)}")


vector_store.add_documents(documents=all_splits, batch_size=100)
