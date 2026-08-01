from engine.tfidf import TFIDF


def test_tfidf():


    documents = {

        "python":[
            "python",
            "programming",
            "language"
        ],


        "java":[
            "java",
            "programming",
            "language"
        ]

    }


    tfidf = TFIDF()


    result = tfidf.calculate_tfidf(documents)


    for doc, values in result.items():

        print(doc)

        print(values)



if __name__ == "__main__":
    test_tfidf()