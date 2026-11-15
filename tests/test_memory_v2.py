from backend.memory.memory_engine import MemoryEngine
from backend.memory.memory_model import Memory


memory = MemoryEngine()

memory.clear()

########################################################

memory.save(

    Memory(

        content="Namaku Mayumi.",

        category="identity",

        importance=1.0,

    )

)

########################################################

memory.save(

    Memory(

        content="Aku suka minum teh.",

        category="preference",

        importance=0.9,

    )

)

########################################################

memory.save(

    Memory(

        content="Aku dibuat menggunakan Ollama.",

        category="fact",

        importance=0.8,

    )

)

########################################################

print("=" * 50)

print("Jumlah Memory")

print(memory.count())

print("=" * 50)

results = memory.search("Apa yang Mayumi suka?")

print()

print("HASIL SEARCH")

print()

print(results)