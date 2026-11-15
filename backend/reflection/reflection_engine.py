class ReflectionEngine:

    def analyze(self, user_message: str):

        text = user_message.lower()

        # User mengoreksi AI
        correction_words = [
            "salah",
            "bukan",
            "keliru",
            "harusnya",
            "seharusnya"
        ]

        for word in correction_words:

            if word in text:

                return {
                    "type": "correction",
                    "message": "User sedang mengoreksi jawaban Mayumi."
                }

        # User bercanda
        joke_words = [
            "wkwk",
            "wk",
            "haha",
            "hahaha",
            "hehe",
            "lol"
        ]

        for word in joke_words:

            if word in text:

                return {
                    "type": "joke",
                    "message": "User sedang bercanda."
                }

        return {
            "type": "normal",
            "message": ""
        }