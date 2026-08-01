import re


class Tokenizer:
    """
    Converts text into clean words.
    """

    def __init__(self):
        self.stop_words = {
            "is",
            "a",
            "the",
            "and",
            "of",
            "to",
            "in",
            "for",
            "on",
            "with"
        }


    def tokenize(self, text):

        # Convert to lowercase
        text = text.lower()


        # Remove punctuation
        text = re.sub(
            r"[^a-z\s]",
            "",
            text
        )


        # Split into words
        words = text.split()


        # Remove stop words
        filtered_words = []

        for word in words:

            if word not in self.stop_words:
                filtered_words.append(word)


        return filtered_words