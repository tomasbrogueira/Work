from pathlib import Path
from llama_index import download_loader, VectorStoreIndex

PDFReader = download_loader("PDFReader")

loader = PDFReader()
documents = loader.load_data(file=Path('data/1.pdf'))

print(documents)


