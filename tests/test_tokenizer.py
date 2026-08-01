from engine.tokenizer import Tokenizer


def test_tokenizer():

    tokenizer = Tokenizer()


    text = """
    Python is a high-level programming language.
    """


    tokens = tokenizer.tokenize(text)


    print(tokens)



if __name__ == "__main__":
    test_tokenizer()