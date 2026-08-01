from engine.inverted_index import InvertedIndex


def test_index():

    documents = {

        "python": [
            "python",
            "programming",
            "language"
        ],

        "java": [
            "java",
            "programming",
            "language"
        ]

    }


    indexer = InvertedIndex()

    index = indexer.build_index(documents)


    for word, docs in index.items():

        print(word, "=>", docs)



if __name__ == "__main__":
    test_index()