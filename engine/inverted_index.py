from collections import defaultdict


class InvertedIndex:
    """
    Creates an inverted index from documents.
    """

    def __init__(self):

        self.index = defaultdict(list)


    def build_index(self, documents):

        """
        documents format:

        {
            "python": ["python", "programming"],
            "java": ["java", "programming"]
        }

        """

        for doc_name, tokens in documents.items():

            for token in tokens:

                if doc_name not in self.index[token]:
                    self.index[token].append(doc_name)


        return self.index