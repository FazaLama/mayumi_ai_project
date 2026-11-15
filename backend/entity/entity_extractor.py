from backend.entity.entity_registry import *


class EntityExtractor:

    def extract(self, text: str):

        text = text.lower()

        # ==========================
        # DRINK
        # ==========================

        for drink in DRINKS:

            if drink in text:

                return {

                    "type": "drink",

                    "value": drink

                }

        # ==========================
        # FOOD
        # ==========================

        for food in FOODS:

            if food in text:

                return {

                    "type": "food",

                    "value": food

                }

        # ==========================
        # GAME
        # ==========================

        for game in GAMES:

            if game in text:

                return {

                    "type": "game",

                    "value": game

                }

        # ==========================
        # ANIME
        # ==========================

        for anime in ANIME:

            if anime in text:

                return {

                    "type": "anime",

                    "value": anime

                }

        return None