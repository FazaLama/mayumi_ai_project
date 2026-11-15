class MemoryRanker:

    CATEGORY_BONUS = {
        "user_identity": 0.30,
        "user_location": 0.20,
        "preference": 0.15,
        "favorite_drink": 0.15,
        "favorite_food": 0.15,
        "favorite_game": 0.15,
        "favorite_anime": 0.15,
        "fact": 0.10
    }

    def rank(self, memories):

        ranked = []

        for mem in memories:

            score = 0

            # Importance
            score += mem.get("importance", 0)

            # Category Bonus
            score += self.CATEGORY_BONUS.get(
                mem.get("category"),
                0
            )

            mem["score"] = score

            ranked.append(mem)

        ranked.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return ranked