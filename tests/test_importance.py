from backend.memory.memory_importance import MemoryImportance

importance = MemoryImportance()

tests = [

    "Aku suka teh.",

    "Aku sangat suka teh.",

    "Aku suka teh banget.",

    "Teh adalah minuman favoritku.",

    "Aku paling suka kopi."

]

for t in tests:

    print("----------------")

    print(t)

    print(importance.calculate(t))