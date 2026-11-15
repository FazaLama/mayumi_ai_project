import json
import os

class SummaryManager:

    FILE_PATH = "backend/data/summary.json"

    def __init__(self):

        os.makedirs("backend/data", exist_ok=True)

        if not os.path.exists(self.FILE_PATH):

            with open(
                self.FILE_PATH,
                "w",
                encoding="utf-8"
            ) as f:

                json.dump(
                    {
                        "summary": ""
                    },
                    f,
                    ensure_ascii=False,
                    indent=4
                )

    def save(self, content: str):

        with open(
            self.FILE_PATH,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                {
                    "summary": content
                },
                f,
                ensure_ascii=False,
                indent=4
            )

    def get(self):

        with open(
            self.FILE_PATH,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)

        return data.get("summary", "")