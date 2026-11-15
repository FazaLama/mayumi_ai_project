import chromadb

from backend.memory.memory_model import Memory


class MemoryEngine:
    """
    Memory Engine V2

    Bertugas:
    - Menyimpan Memory
    - Mengambil Memory
    - Menghapus Memory
    - Menghitung jumlah Memory
    """

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="./memory"
        )

        self.collection = self.client.get_or_create_collection(
            name="mayumi_memory"
        )

    ####################################################################
    # SAVE
    ####################################################################

    def save(self, memory: Memory):

        self.collection.add(

            ids=[memory.id],

            documents=[memory.content],

            metadatas=[

                {
                    "category": memory.category,
                    "importance": memory.importance,
                    "source": memory.source,
                    "created_at": memory.created_at,
                    "user_id": memory.user_id or "",
                }

            ],
        )

    ####################################################################
    # SEARCH
    ####################################################################

    def search(self, query: str, n_results: int = 3):

        results = self.collection.query(

            query_texts=[query],

            n_results=n_results,

        )

        return results
    
    ####################################################################
    # GET BY CATEGORY
    ####################################################################

    def get_by_category(self, category: str):

        results = self.collection.get(
            where={"category": category}
        )

        return results

    ####################################################################
    # DELETE
    ####################################################################

    def delete(self, memory_id: str):

        self.collection.delete(
            ids=[memory_id]
        )

    ####################################################################
    # UPDATE IMPORTANCE
    ####################################################################

    def update_importance(
        self,
        memory_id: str,
        importance: float
    ):

        data = self.collection.get(
            ids=[memory_id]
        )

        if not data["ids"]:
            return

        document = data["documents"][0]

        metadata = data["metadatas"][0]

        metadata["importance"] = importance

        self.collection.update(

            ids=[memory_id],

            documents=[document],

            metadatas=[metadata]

        )

    ####################################################################
    # COUNT
    ####################################################################

    def count(self):

        return self.collection.count()

    ####################################################################
    # CLEAR
    ####################################################################

    def clear(self):

        self.client.delete_collection("mayumi_memory")

        self.collection = self.client.get_or_create_collection(
            name="mayumi_memory"
        )