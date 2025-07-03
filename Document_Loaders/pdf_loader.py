# | **Use Case**                   | **Recommended Loader**                               |
# | ------------------------------ | ---------------------------------------------------- |
# | Simple, clean PDFs             | `PyPDFLoader`                                        |
# | PDFs with tables/columns       | `PDFPlumberLoader`                                   |
# | Scanned/image PDFs             | `UnstructuredPDFLoader` or `AmazonTextractPDFLoader` |
# | Need layout and image data     | `PyMuPDFLoader`                                      |
# | Want best structure extraction | `UnstructuredPDFLoader`                              |


from langchain_community.document_loaders import PyPDFLoader

loader= PyPDFLoader("../data/document.pdf")

docs = loader.load()

print(len(docs))

print(docs[0].page_content)

print(docs[0].metadata)

