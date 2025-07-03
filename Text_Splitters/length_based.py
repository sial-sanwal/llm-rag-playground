from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("../data/Building Machine Learning Systems with Python - Second Edition.pdf")

docs = loader.load()


splitter = CharacterTextSplitter(
    
    chunk_size = 100,
    chunk_overlap = 0, # chunk_ovarlap optimal value is 10 to 20 % of the chunk size
    separator=""
)

result = splitter.split_documents(docs)

print(len(result))

print(result[124])