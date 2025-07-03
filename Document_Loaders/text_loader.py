from langchain_community.document_loaders import TextLoader

loader= TextLoader('../data/poem.txt')

docs=loader.load()
print(docs)