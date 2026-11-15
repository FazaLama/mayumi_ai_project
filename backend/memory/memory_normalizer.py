import re


class MemoryNormalizer:

    def normalize_preference(self, text: str):

        text = text.lower().strip()

        # Hilangkan subjek
        remove = [
            "aku",
            "saya",
            "user",
            "suka",
            "lebih",
            "banget",
            "sekali",
            "minum",
            "makan",
            "adalah",
            "loh",
            "dong",
            "deh"
        ]

        for word in remove:

            text = re.sub(
                rf"\b{word}\b",
                "",
                text
            )

        text = re.sub(
            r"[^\w\s]",
            "",
            text
        )

        text = " ".join(text.split())

        return text