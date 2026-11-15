from backend.memory.memory_engine import MemoryEngine

engine = MemoryEngine()

data = engine.get_by_category("favorite_drink")

if data["ids"]:

    memory_id = data["ids"][0]

    engine.update_importance(

        memory_id,

        1.0

    )

    print("Berhasil update.")