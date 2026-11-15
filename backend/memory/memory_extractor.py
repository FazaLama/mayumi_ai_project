import re

from backend.memory.memory_engine import MemoryEngine
from backend.memory.memory_model import Memory
from backend.memory.memory_deduplicator import MemoryDeduplicator
from backend.memory.memory_normalizer import MemoryNormalizer
from backend.entity.entity_extractor import EntityExtractor
from backend.memory.memory_importance import MemoryImportance

class MemoryExtractor:

    def __init__(self):
        self.memory = MemoryEngine()
        self.deduplicator = MemoryDeduplicator()
        self.normalizer = MemoryNormalizer()
        self.entity = EntityExtractor()
        self.importance = MemoryImportance()

    def process(self, text: str):

        # ==========================
        # PREPROCESS
        # ==========================

        text = text.strip().lower()

        # Pisahkan beberapa fakta dalam satu kalimat
        text = text.replace(" dan ", ". ")
        text = text.replace(",", ".")

        sentences = text.split(".")

        # ==========================
        # PROCESS SETIAP KALIMAT
        # ==========================

        for sentence in sentences:

            sentence = sentence.strip()

            if not sentence:
                continue

            # ==========================
            # Nama User
            # ==========================

            patterns_name = [
                r"nama saya adalah (.+)",
                r"nama saya (.+)",
                r"namaku (.+)",
                r"saya bernama (.+)"
            ]

            for pattern in patterns_name:

                match = re.search(pattern, sentence, re.IGNORECASE)

                if match:

                    name = match.group(1).strip()

                    if "?" in sentence:
                        break

                    if name.lower() in [
                        "siapa",
                        "apa",
                        "siapa?",
                        "apa?"
                    ]:
                        break

                    existing = self.memory.get_by_category("user_identity")

                    if existing["ids"]:
                        self.memory.delete(existing["ids"][0])

                    self.memory.save(
                        Memory(
                            content=f"Nama user adalah {name}.",
                            category="user_identity",
                            importance=1.0,
                            source="user"
                        )
                    )

                    break

            # ==========================
            # Tempat Tinggal
            # ==========================

            patterns_location = [
                r"saya tinggal di (.+)",
                r"aku tinggal di (.+)"
            ]

            for pattern in patterns_location:

                match = re.search(pattern, sentence, re.IGNORECASE)

                if match:

                    location = match.group(1).strip()

                    if "?" in sentence:
                        break

                    if location.lower() in [
                        "mana",
                        "mana?",
                        "apa",
                        "apa?"
                    ]:
                        break

                    existing = self.memory.get_by_category("user_location")

                    if existing["ids"]:
                        self.memory.delete(existing["ids"][0])

                    self.memory.save(
                        Memory(
                            content=f"User tinggal di {location}.",
                            category="user_location",
                            importance=0.95,
                            source="user"
                        )
                    )

                    break

            # ==========================
            # Kesukaan
            # ==========================

            patterns_like = [
                r"saya suka (.+)",
                r"saya sangat suka (.+)",
                r"aku suka (.+)",
                r"aku sangat suka (.+)"

            ]

            for pattern in patterns_like:

                match = re.search(pattern, sentence, re.IGNORECASE)

                if match:

                    like = self.normalizer.normalize_preference(
                        match.group(1)
                    )

                    entity = self.entity.extract(sentence)

                    if entity:

                        like = entity["value"]

                    print(
                        "[ENTITY]",
                        entity
                    )

                    

                    if not like:

                        break

                    # ==========================
                    # CATEGORY
                    # ==========================

                    if "?" in sentence:
                        break

                    if like.lower() in [
                        "apa",
                        "siapa",
                        "apa?",
                        "siapa?"
                    ]:
                        break

                    category = "preference"

                    if entity:

                        category = f"favorite_{entity['type']}"

                    print("[ENTITY]", entity)

                    print("[CATEGORY]", category)

                    existing = self.memory.get_by_category(category)

                    importance = self.importance.calculate(sentence)

                    is_duplicate = self.deduplicator.is_duplicate(

                        new_memory=f"User suka {like}.",

                        existing_memories=existing["documents"]

                    )

                    if not is_duplicate:

                        self.memory.save(

                            Memory(

                                content=f"User suka {like}.",

                                category=category,

                                importance=importance,

                                source="user"

                            )

                        )

                    else:

                        # ==========================
                        # UPDATE IMPORTANCE
                        # ==========================

                        if existing["ids"]:

                            memory_id = existing["ids"][0]

                            old_importance = existing["metadatas"][0]["importance"]

                            print("OLD :", old_importance)
                            print("NEW :", importance)
                            print(type(old_importance))
                            print(type(importance))

                            if importance > old_importance:

                                self.memory.update_importance(

                                    memory_id,

                                    importance

                                )

                                print(

                                    "[MEMORY] Importance diperbarui",

                                    old_importance,

                                    "->",

                                    importance

                                )

                    break