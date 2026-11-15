from backend.state.state_manager import StateManager


class EmotionManager:

    def __init__(self):

        self.state = StateManager("emotion.json")

        data = self.state.load()

        self.mood = data.get("mood", 0)

    def save(self):

        self.state.save({
            "mood": self.mood
        })

    def process(self, text: str):

        text = text.lower()

        positive = [
            "terima kasih",
            "makasih",
            "bagus",
            "keren",
            "hebat"
        ]

        negative = [
            "bodoh",
            "jelek",
            "tolol",
            "payah"
        ]

        for word in positive:

            if word in text:
                self.mood += 1

        for word in negative:

            if word in text:
                self.mood -= 1

        if self.mood > 10:
            self.mood = 10

        if self.mood < -10:
            self.mood = -10

        self.save()

    def get_emotion(self):

        if self.mood >= 3:
            return "happy"

        if self.mood <= -3:
            return "sad"

        return "neutral"