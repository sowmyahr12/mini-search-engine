from engine.search_engine import SearchEngine


def test_search_engine():

    engine = SearchEngine("data")

    engine.build()

    print("Index built successfully")
    

    results = engine.search("programming")

    print("Search results:")

    for i, result in enumerate(results, start=1):

      document, score = result

      print(
        f"{i}. {document}  Score: {score:.4f}"
      )


if __name__ == "__main__":
    test_search_engine()