from backend.reasoning.reasoning_engine import ReasoningEngine

reason = ReasoningEngine()

tests = [
    "Halo Mayumi",
    "Buka notepad",
    "Saya tinggal di Jepang",
    "Aku suka teh",
    "Jam berapa sekarang?",
    "Hari ini aku capek"
]

for text in tests:

    result = reason.analyze(text)

    print("=" * 40)
    print(text)
    print(result)