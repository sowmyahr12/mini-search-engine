from pathlib import Path


class document_loader:
    """
    Loads all .txt documents from a folder.
    """

    def __init__(self, folder_path):
        self.folder_path = Path(folder_path)

    def load_documents(self):
        documents = {}

        for file in self.folder_path.glob("*.txt"):

            with open(file, "r", encoding="utf-8") as f:

                documents[file.stem] = f.read()

        return documents