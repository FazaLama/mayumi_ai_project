from backend.state.state_manager import StateManager


class AffinityManager:

    def __init__(self):

        self.state = StateManager("affinity.json")

        data = self.state.load()

        self.affinity = data.get("value", 0)

    def save(self):

        self.state.save({
            "value": self.affinity
        })

    def increase(self, amount=1):

        self.affinity += amount

        if self.affinity > 100:
            self.affinity = 100

        self.save()

    def decrease(self, amount=1):

        self.affinity -= amount

        if self.affinity < 0:
            self.affinity = 0

        self.save()

    def get_level(self):

        if self.affinity >= 70:
            return "close"

        if self.affinity >= 30:
            return "friend"

        return "new"

    def get_value(self):

        return self.affinity