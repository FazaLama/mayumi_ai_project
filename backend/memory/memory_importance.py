class MemoryImportance:

    def calculate(self, sentence: str):

        text = sentence.lower()

        # Default
        importance = 0.80

        # ==========================
        # Sangat Penting
        # ==========================

        if (
            "favorit" in text
            or "favorite" in text
        ):

            importance = 1.00

        elif (
            "nomor satu" in text
            or "kesukaan utama" in text
        ):

            importance = 0.98

        elif (
            "paling suka" in text
        ):

            importance = 0.95

        elif (
            "sangat suka" in text
            or "suka banget" in text
            or "benar-benar suka" in text
        ):

            importance = 0.90

        elif (
            "lumayan suka" in text
            or "cukup suka" in text
        ):

            importance = 0.85

        print(
            "[IMPORTANCE]",
            importance
        )

        return importance