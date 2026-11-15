class MemoryConflict:

    def is_conflict(self, sentence: str):

        text = sentence.lower()

        keywords = [

            "lebih suka",

            "daripada",

            "sekarang",

            "tidak lagi",

            "bukan lagi"

        ]

        return any(

            word in text

            for word in keywords

        )