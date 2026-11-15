from difflib import SequenceMatcher

from backend.profile.profile_question_registry import PROFILE_PATTERNS
from backend.services.profile_service import ProfileService


class ProfileQuestionEngine:

    def __init__(self):

        self.profile = ProfileService()

    # ==========================
    # SIMILARITY
    # ==========================

    def similarity(self, a: str, b: str):

        return SequenceMatcher(
            None,
            a.lower(),
            b.lower()
        ).ratio()

    # ==========================
    # DETECT INTENT
    # ==========================

    def detect_intent(self, text: str):

        text = text.lower()

        best_intent = None
        best_score = 0

        for intent, patterns in PROFILE_PATTERNS.items():

            for pattern in patterns:

                # Match persis
                if pattern in text:
                    return intent

                # Fuzzy Match
                score = self.similarity(
                    pattern,
                    text
                )

                if score > best_score:

                    best_score = score
                    best_intent = intent

        # Threshold
        if best_score >= 0.80:
            return best_intent

        return None

    # ==========================
    # ANSWER
    # ==========================

    def answer(self, user_message: str):

        intent = self.detect_intent(user_message)

        # ==========================
        # NAME
        # ==========================

        if intent == "name":

            name = self.profile.get_name()

            if name:
                return f"Namamu {name}."

            return "Maaf, aku belum tahu namamu."

        # ==========================
        # COUNTRY
        # ==========================

        if intent == "country":

            country = self.profile.get_country()

            if country:
                return f"Kamu tinggal di {country}."

            return "Aku belum tahu kamu tinggal di mana."

        # ==========================
        # FAVORITE DRINK
        # ==========================

        if intent == "favorite_drink":

            drink = self.profile.get_favorite_drink()

            if drink:
                return f"Kalau tidak salah kamu suka {drink}."

            return "Aku belum tahu minuman favoritmu."

        return None