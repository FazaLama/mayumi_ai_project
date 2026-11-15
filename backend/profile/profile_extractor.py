import re

from backend.profile.profile_manager import ProfileManager


class ProfileExtractor:

    DRINKS = (
        "teh hijau",
        "air putih",
        "kopi",
        "teh",
        "susu",
        "jus",
    )

    FOODS = (
        "nasi goreng",
        "mie ayam",
        "bakso",
        "sate",
        "rendang",
        "pizza",
        "burger",
        "sushi",
    )

    GAMES = (
        "genshin impact",
        "mobile legends",
        "free fire",
        "valorant",
        "minecraft",
        "pubg",
        "dota 2",
    )

    def __init__(self):
        self.manager = ProfileManager()

    @staticmethod
    def _clean(value: str) -> str:
        return value.strip(" \t\r\n.,!?;:")

    def process(self, text: str):
        text = text.strip()

        # Do not store questions as facts (for example, "siapa nama saya?").
        if not text or "?" in text:
            return

        profile = self.manager.load()

        patterns = (
            r"nama saya adalah (.+)",
            r"nama saya (.+)",
            r"namaku (.+)",
            r"saya bernama (.+)",
        )
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                name = self._clean(match.group(1))
                if name and name.lower() not in {"siapa", "apa"}:
                    profile.name = name
                    self.manager.save(profile)
                return

        patterns = (
            r"saya tinggal di (.+)",
            r"aku tinggal di (.+)",
        )
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                country = self._clean(match.group(1))
                if country:
                    profile.country = country
                    self.manager.save(profile)
                return

        match = re.search(
            r"(?:saya|aku)\s+(?:sangat\s+)?suka\s+(.+)",
            text,
            re.IGNORECASE,
        )
        if not match:
            return

        liked = self._clean(match.group(1)).lower()
        if not liked:
            return

        categories = (
            ("favorite_drink", self.DRINKS),
            ("favorite_food", self.FOODS),
            ("favorite_game", self.GAMES),
        )
        for field, values in categories:
            for value in values:
                if re.search(rf"(?<!\w){re.escape(value)}(?!\w)", liked):
                    setattr(profile, field, value)
                    self.manager.save(profile)
                    return