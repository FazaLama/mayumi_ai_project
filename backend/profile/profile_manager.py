import json
import os

from backend.profile.profile_model import UserProfile


class ProfileManager:

    FILE = "database/profile.json"

    def __init__(self):

        os.makedirs("database", exist_ok=True)

        if not os.path.exists(self.FILE):

            self.save(UserProfile())

    def load(self):

        with open(self.FILE, "r", encoding="utf-8") as f:

            data = json.load(f)

        return UserProfile(**data)

    def save(self, profile: UserProfile):

        with open(self.FILE, "w", encoding="utf-8") as f:

            json.dump(
                profile.__dict__,
                f,
                indent=4,
                ensure_ascii=False
            )