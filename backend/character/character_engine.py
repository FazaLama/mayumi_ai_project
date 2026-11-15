class CharacterEngine:

    def build(self, emotion: str, affinity: str):

        style = []

        # Emotion
        if emotion == "happy":
            style.append(
                "- Berbicara dengan nada ceria."
            )
            style.append(
                "- Boleh menggunakan emoji 😊 sesekali."
            )

        elif emotion == "sad":
            style.append(
                "- Berbicara lebih pelan dan lembut."
            )

        else:
            style.append(
                "- Berbicara dengan nada normal."
            )

        # Affinity
        if affinity == "new":
            style.append(
                "- Gunakan bahasa yang sopan."
            )

        elif affinity == "friend":
            style.append(
                "- Gunakan bahasa yang lebih hangat."
            )

        elif affinity == "close":
            style.append(
                "- Berbicara akrab, hangat, sedikit malu-malu, tetapi tetap sopan."
            )

        return "\n".join(style)