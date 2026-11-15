from backend.memory.memory_normalizer import MemoryNormalizer

normalizer = MemoryNormalizer()

tests = [

    "Aku suka teh.",

    "Saya suka minum teh.",

    "User suka kopi.",

    "Aku suka bermain game.",

    "Saya suka makan nasi goreng."

]

for text in tests:

    print("--------------------------------")

    print("INPUT :", text)

    print("OUTPUT:", normalizer.normalize_preference(text))