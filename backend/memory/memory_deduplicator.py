import re
from difflib import SequenceMatcher


class MemoryDeduplicator:

    def normalize(self, text: str):

        text = text.lower()

        replacements = [
            "user",
            "aku",
            "saya",
            "suka",
            "minum",
            "makan",
            "adalah",
            "loh",
            "dong",
            "deh",
            "daripada",
            "lebih",
            "lebih suka",
            "banget",
            "sekali"
        ]

        for word in replacements:
            text = text.replace(word, "")

        text = re.sub(
            r"[^\w\s]",
            "",
            text
        )

        text = " ".join(text.split())

        return text

    def is_duplicate(
        self,
        new_memory,
        existing_memories,
        threshold=0.85
    ):

        new_text = self.normalize(new_memory)

        for old_text in existing_memories:

            old_text = self.normalize(old_text)

            similarity = SequenceMatcher(
                None,
                new_text,
                old_text
            ).ratio()

            # ==========================
            # DEBUG
            # ==========================

            DEBUG = False

            if DEBUG:
                print()
                print("NEW :", new_text)
                print("OLD :", old_text)
                print("SIM :", similarity)

            if similarity >= threshold:

                print(
                    "[MEMORY] Duplicate ditemukan:",
                    old_text
                )

                return True

        return False