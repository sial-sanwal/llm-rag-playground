from langchain_community.document_loaders import WebBaseLoader

url='https://myshop.pk/apple-macbook-air-2020-13-m1-chip-256gb-with-touch-id-s-pakistan.html'

loader = WebBaseLoader(url)

docs = loader.load()

print(len(docs))

print(docs[0].page_content)

print(docs[0].metadata)
