from engine.similarity import CosineSimilarity


def test_similarity():

    cosine = CosineSimilarity()


    query = {
        "python": 1,
        "programming": 1
    }


    document = {
        "python": 0.5,
        "programming": 0.5
    }


    score = cosine.calculate(
        query,
        document
    )


    print("Similarity:", score)



if __name__ == "__main__":
    test_similarity()