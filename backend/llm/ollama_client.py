import requests

from backend.config.settings import Settings


class OllamaClient:

    def __init__(self):

        self.url = Settings.OLLAMA_URL

        self.model = Settings.CHAT_MODEL

    def chat(self, prompt):

        payload = {

            "model": self.model,

            "messages": [

                {

                    "role": "user",

                    "content": prompt

                }

            ],

            "stream": False

        }

        response = requests.post(

            self.url,

            json=payload

        )

        response.raise_for_status()

        return response.json()["message"]["content"]