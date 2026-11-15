class DecisionEngine:

    def decide(self, user_message: str):

        text = user_message.lower()
        
        print(text)

        # ==========================
        # Tool
        # ==========================

        tool_keywords = [
            "buka",
            "open",
            "jam",
            "tanggal",
            "calculator",
            "notepad"
        ]

        for keyword in tool_keywords:
            if keyword in text:
                return "tool"

        # ==========================
        # Memory
        # ==========================

        memory_keywords = [

            # ==========================
            # Mengingat
            # ==========================

            "ingat",
            "masih ingat",

            # ==========================
            # Identitas
            # ==========================

            "siapa saya",
            "siapa aku",
            "nama saya",
            "namaku",

            # ==========================
            # Kesukaan
            # ==========================

            "aku suka",
            "saya suka",
            "kesukaan",
            "favorit",
            "favoritku",

            # ==========================
            # Tempat tinggal
            # ==========================

            "aku tinggal",
            "saya tinggal",

            # ==========================
            # Pertanyaan tentang diri user
            # ==========================

            "apa yang kamu tahu",
            "apa yang kau tahu",
            "kamu tahu apa",
            "tentang saya",
            "tentang aku",

            # ==========================
            # Pertanyaan umum
            # ==========================

            "hobiku",
            "hobi saya",
            "minuman",
            "makanan",
            "game favorit"
        ]

        for keyword in memory_keywords:
            if keyword in text:
                print("[DECISION] MEMORY")

                return "memory"

        # ==========================
        # Chat
        # ==========================
        print("[DECISION] CHAT")

        return "chat"