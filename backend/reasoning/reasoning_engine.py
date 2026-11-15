class ReasoningEngine:

    def analyze(self, user_message: str):

        text = user_message.lower()

        # ==========================
        # QUESTION
        # ==========================

        if "?" in text:
            return {
                "type": "question",
                "reason": "User sedang bertanya."
            }

        # ==========================
        # COMMAND
        # ==========================

        command_words = [
            "buka",
            "jalankan",
            "tutup",
            "buat",
            "hapus",
            "cari"
        ]

        if any(word in text for word in command_words):
            return {
                "type": "command",
                "reason": "User memberikan perintah."
            }

        # ==========================
        # SELF DISCLOSURE
        # ==========================

        if text.startswith("saya ") or text.startswith("aku "):
            return {
                "type": "self_info",
                "reason": "User sedang menceritakan dirinya."
            }

        # ==========================
        # GREETING
        # ==========================

        greetings = [
            "halo",
            "hai",
            "hi",
            "selamat pagi",
            "selamat siang",
            "selamat sore",
            "selamat malam"
        ]

        if any(text.startswith(word) for word in greetings):
            return {
                "type": "greeting",
                "reason": "User sedang menyapa."
            }

        # ==========================
        # DEFAULT
        # ==========================

        return {
            "type": "statement",
            "reason": "User sedang menyampaikan sesuatu."
        }