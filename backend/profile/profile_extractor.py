import re

from backend.profile.profile_manager import ProfileManager


class ProfileExtractor:

    def __init__(self):

        self.manager = ProfileManager()

        DRINKS = [
            "kopi",
            "teh",
            "teh hijau",
            "susu",
            "jus",
            "air putih"
        ]

        FOODS = [
            "bakso",
            "mie ayam",
            "nasi goreng",
            "sate",
            "rendang",
            "pizza",
            "burger",
            "sushi"
        ]

        GAMES = [
            "valorant",
            "minecraft",
            "genshin impact",
            "mobile legends",
            "pubg",
            "free fire",
            "dota 2"
        ]

    def process(self, text: str):

        profile = self.manager.load()

        text = text.strip()

        # ==========================
        # Nama
        # ==========================

        patterns = [
            r"nama saya adalah (.+)",
            r"nama saya (.+)",
            r"namaku (.+)",
            r"saya bernama (.+)"
        ]

        for pattern in patterns:

            match = re.search(pattern, text, re.IGNORECASE)

            if match:

                profile.name = match.group(1).strip()

                self.manager.save(profile)

                return

        # ==========================
        # Negara
        # ==========================

        patterns = [
            r"saya tinggal di (.+)",
            r"aku tinggal di (.+)"
        ]

        for pattern in patterns:

            match = re.search(pattern, text, re.IGNORECASE)

            if match:

                profile.country = match.group(1).strip()

                self.manager.save(profile)

                return

        # ==========================
        # Minuman Favorit
        # ==========================

        patterns = [
            r"saya suka (.+)",
            r"aku suka (.+)"
        ]

        for pattern in patterns:

            match = re.search(pattern, text, re.IGNORECASE)

            if match:

                like = match.group(1).strip().lower()

                drinks = [
                    "kopi",
                    "teh",
                    "teh hijau",
                    "susu",
                    "jus",
                    "air putih"
                ]

                if like in self.DRINKS:

                        profile.favorite_drink = like

                    elif like in self.FOODS:

                        profile.favorite_food = like

                    elif like in self.GAMES:

                        profile.favorite_game = like

                    else:

                        if like not in profile.hobbies:

                            profile.hobbies.append(like)

                    self.manager.save(profile)
                    return