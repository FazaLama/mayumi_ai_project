from backend.memory.memory_retriever import MemoryRetriever

retriever = MemoryRetriever()

results = retriever.search("Apa yang Mayumi suka?")

print("=" * 50)

for i, memory in enumerate(results, start=1):

    print(f"Memory {i}")

    print("Content     :", memory["content"])
    print("Category    :", memory["category"])
    print("Importance  :", memory["importance"])
    print("Distance    :", memory["distance"])
    print()