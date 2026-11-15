import json
import os


class StateManager:

    def __init__(self, filename):

        self.path = os.path.join("data", filename)

    def load(self):

        if not os.path.exists(self.path):
            return {}

        with open(
            self.path,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    def save(self, data):

        with open(
            self.path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )