from backend.memory.memory_engine import MemoryEngine
from backend.memory.memory_ranker import MemoryRanker

print("LOADED MEMORY RETRIEVER")

class MemoryRetriever:

    def __init__(self):
        self.memory = MemoryEngine()
        self.ranker = MemoryRanker()

    def normalize_query(self, query: str):

        text = query.lower()

        if "minuman" in text:
            return "favorite_drink"

        if (
            "makanan" in text
            or "makan" in text
        ):
            return "favorite_food"

        if (
            "game" in text
            or "main" in text
        ):
            return "favorite_game"

        return query

    def search(self, query, limit=5):
        print(">>> MemoryRetriever.search() DIPANGGIL <<<")

        original_query = query

        category_query = self.normalize_query(query)

        results = self.memory.search(original_query, limit)

        

        documents = results.get("documents", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]
        ids = results.get("ids", [[]])[0]

        memories = []

        for i in range(len(documents)):

            metadata = metadatas[i] if i < len(metadatas) else {}

            memories.append({
                "id": ids[i],
                "content": documents[i],
                "category": metadata.get("category", ""),
                "importance": metadata.get("importance", 0),
                "source": metadata.get("source", ""),
                "created_at": metadata.get("created_at", "")
            })

        # ==========================
        # CATEGORY BONUS
        # ==========================

        print()
        print("========== MEMORY DARI CHROMA ==========")

        for memory in memories:

            print(
                memory["content"],
                "|",
                memory["category"],
                "|",
                memory["importance"]
            )

        print("========================================")
        print()

        if category_query != original_query:

            for memory in memories:

                if memory["category"] == category_query:

                    memory["importance"] += 0.5

                    print(
                        "[CATEGORY BONUS]",
                        memory["category"],
                        memory["importance"]
                    )

        # ==========================
        # RANK
        # ==========================

        memories = self.ranker.rank(memories)

        return memories
    
    def best(self, query):

        memories = self.search(query, limit=1)

        if not memories:
            return None

        return memories[0]

