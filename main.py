from engine.search_engine import SearchEngine


def main():

    print("============================")
    print("     MINI SEARCH ENGINE")
    print("============================\n")


    engine = SearchEngine("data")


    print("Loading documents...")

    engine.build()


    print(
        f"Indexed {len(engine.documents)} documents.\n"
    )


    while True:

        query = input(
            "Enter query (type 'exit' to quit): "
        )


        if query.lower() == "exit":
            print("Closing search engine...")
            break


        results = engine.search(query)


        if not results:

            print("\nNo results found.\n")
            continue


        print("\nResults:\n")


        for i, (document, score) in enumerate(
            results,
            start=1
        ):

            print(f"{i}. {document}")

            print(
                f"   Score: {score:.4f}"
            )

            print(
            "   Preview:"
            )

            print(
                "   ",
                engine.get_snippet(
                    document,
                    query
        )
    )

    print()



if __name__ == "__main__":
    main()