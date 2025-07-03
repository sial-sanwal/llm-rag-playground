from langchain_community.document_loaders import TextLoader

loader = TextLoader('../data/poem.txt')

docs = loader.load()

print(type(docs)) # its show the type of docs is list.
print("_______________")

print(docs[0].metadata)
print("_______________")
print(docs[0].page_content)

