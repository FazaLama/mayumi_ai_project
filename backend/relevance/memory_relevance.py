class MemoryRelevance:

    def filter(self, user_message, memories):

        if not memories:
            return []

        text = user_message.lower()

        filtered = []

        STOP_WORDS = {

            "aku",
            "saya",
            "gue",
            "gw",

            "yang",
            "dan",
            "atau",

            "di",
            "ke",
            "dari",

            "itu",
            "ini",

            "adalah",
            "ialah",

            "lagi",
            "loh",
            "dong",
            "deh",

            "apa",
            "siapa",
            "dimana",
            "mana",

            "mayumi"

        }

        CATEGORY_WEIGHT = {

            "user_identity": 100,

            "preference": 90,

            "favorite_drink": 90,

            "favorite_food": 90,

            "favorite_game": 90,

            "favorite_anime": 90,

            "user_location": 80,

            "job": 70,

            "school": 70,

            "summary": 50,

            "others": 10

        }

        for memory in memories:

            content = memory["content"].lower()

            score = 0

            category = memory.get(
                "category",
                "others"
            )

            for word in text.split():

                if word in STOP_WORDS:

                    continue

                if word in content:

                    score += 1

            # Tambahkan bobot hanya jika ada kecocokan
            if score > 0:

                score += CATEGORY_WEIGHT.get(
                    category,
                    10
                )

            memory["score"] = score

            filtered.append(memory)

        filtered.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        filtered = [

            m

            for m in filtered

            if m["score"] > 0

        ]

        return filtered[:3]