import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from engine.document_loader import document_loader


def test_document_loader():

    loader = document_loader("data")

    documents = loader.load_documents()

    print("Number of documents:", len(documents))

    for name in documents:
        print("Loaded:", name)


if __name__ == "__main__":
    test_document_loader()