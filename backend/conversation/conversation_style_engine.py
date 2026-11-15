class ConversationStyleEngine:

    def analyze(self, user_message: str):

        text = user_message.lower()

        style = {
            "tone": "normal",
            "give_praise": False,
            "show_empathy": False,
            "ask_followup": False,
            "be_playful": False,
            "instruction": ""
        }

        # ==========================
        # SUCCESS
        # ==========================

        success_words = [
            "berhasil",
            "akhirnya",
            "selesai",
            "lulus",
            "menang"
        ]

        if any(word in text for word in success_words):

            style["tone"] = "happy"
            style["give_praise"] = True
            style["ask_followup"] = True

        # ==========================
        # SAD
        # ==========================

        sad_words = [
            "sedih",
            "capek",
            "lelah",
            "kecewa",
            "gagal"
        ]

        if any(word in text for word in sad_words):

            style["tone"] = "soft"
            style["show_empathy"] = True
            style["ask_followup"] = True

        # ==========================
        # JOKE
        # ==========================

        joke_words = [
            "wkwk",
            "haha",
            "awokwok",
            "lol"
        ]

        if any(word in text for word in joke_words):

            style["tone"] = "playful"
            style["be_playful"] = True

        # ==========================
        # STYLE INSTRUCTION
        # ==========================

        instruction = []

        # Tone

        if style["tone"] == "happy":

            instruction.append(
                "Gunakan nada antusias dan positif."
            )

        elif style["tone"] == "soft":

            instruction.append(
                "Gunakan nada lembut dan menenangkan."
            )

        elif style["tone"] == "playful":

            instruction.append(
                "Gunakan nada santai dan sedikit bercanda."
            )

        # Praise

        if style["give_praise"]:

            instruction.append(
                "Berikan apresiasi terhadap pencapaian user."
            )

        # Empathy

        if style["show_empathy"]:

            instruction.append(
                "Tunjukkan empati terhadap perasaan user."
            )

        # Followup

        if style["ask_followup"]:

            instruction.append(
                "Akhiri jawaban dengan satu pertanyaan lanjutan yang relevan."
            )

        # Playful

        if style["be_playful"]:

            instruction.append(
                "Gunakan sedikit candaan yang natural."
            )

        # Simpan menjadi satu string

        style["instruction"] = "\n".join(instruction)

        return style