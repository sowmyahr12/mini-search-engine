import math
from collections import Counter


class TFIDF:

    """
    Calculates TF-IDF scores for documents.
    """


    def __init__(self):

        self.document_vectors = {}



    def calculate_tf(self, tokens):

        """
        Calculate term frequency.
        """

        total_words = len(tokens)

        frequency = Counter(tokens)

        tf = {}

        for word, count in frequency.items():

            tf[word] = count / total_words


        return tf



    def calculate_idf(self, documents):

        """
        Calculate inverse document frequency.
        """

        total_documents = len(documents)

        idf = {}


        all_words = set()


        for tokens in documents.values():

            all_words.update(tokens)



        for word in all_words:

            count = 0


            for tokens in documents.values():

                if word in tokens:
                    count += 1


            idf[word] = math.log(
                total_documents / count
            )


        return idf



    def calculate_tfidf(self, documents):

        """
        Create TF-IDF vectors.
        """

        idf = self.calculate_idf(documents)


        for name, tokens in documents.items():

            tf = self.calculate_tf(tokens)

            vector = {}


            for word in tf:

                vector[word] = (
                    tf[word] * idf[word]
                )


            self.document_vectors[name] = vector


        return self.document_vectors