import math


class CosineSimilarity:

    """
    Calculates similarity between two vectors.
    """


    def calculate(self, vector1, vector2):

        dot_product = 0

        magnitude1 = 0

        magnitude2 = 0


        # Dot product

        for word in vector1:

            if word in vector2:

                dot_product += (
                    vector1[word] *
                    vector2[word]
                )


        # Magnitude of vector 1

        for value in vector1.values():

            magnitude1 += value ** 2


        magnitude1 = math.sqrt(magnitude1)


        # Magnitude of vector 2

        for value in vector2.values():

            magnitude2 += value ** 2


        magnitude2 = math.sqrt(magnitude2)


        # Avoid division by zero

        if magnitude1 == 0 or magnitude2 == 0:

            return 0


        return dot_product / (magnitude1 * magnitude2)