from engine.document_loader import document_loader
from engine.tokenizer import Tokenizer
from engine.inverted_index import InvertedIndex
from engine.tfidf import TFIDF
from engine.similarity import CosineSimilarity


class SearchEngine:


    def __init__(self, data_path):

        self.loader = document_loader(data_path)

        self.tokenizer = Tokenizer()

        self.indexer = InvertedIndex()

        self.tfidf = TFIDF()

        self.similarity = CosineSimilarity()

        self.documents = {}

        self.index = {}

        self.tfidf_vectors = {}



    def build(self):

        self.documents = self.loader.load_documents()

        tokenized_documents = {}

        for name, text in self.documents.items():

            tokens = self.tokenizer.tokenize(text)

            tokenized_documents[name] = tokens


        self.index = self.indexer.build_index(
            tokenized_documents
        )


        self.tfidf_vectors = self.tfidf.calculate_tfidf(
            tokenized_documents
        )



    def search(self, query):

        query_tokens = self.tokenizer.tokenize(query)


        query_vector = {}

        total_words = len(query_tokens)


        for word in query_tokens:

            query_vector[word] = (
                query_tokens.count(word) / total_words
            )


        scores = {}


        for document, vector in self.tfidf_vectors.items():

            score = self.similarity.calculate(
                query_vector,
                vector
            )


            if score > 0:

                scores[document] = score


        ranked_results = sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True
        )


        return ranked_results
    
    def get_snippet(self, document_name, query):

        import re

        text = self.documents[document_name]

        query_words = self.tokenizer.tokenize(query)


        snippet = text[:200]


        for word in query_words:

            snippet = re.sub(
                 word,
                f"**{word}**",
                snippet,
                flags=re.IGNORECASE
             )


        return snippet