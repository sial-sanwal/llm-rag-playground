from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

"""
.load() reads all documents into memory at once (eager loading), suitable for small files.  
.lazy_load() yields documents one by one (lazy loading), ideal for large datasets and memory efficiency.
"""


loader = DirectoryLoader(
    
    path="../data/",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

docs = loader.load()

print(len(docs))

# print(docs[120].page_content)

# print(docs[120].metadata)

for document in docs:
    print(document.metadata)