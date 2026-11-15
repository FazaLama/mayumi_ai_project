from backend.decision.decision_engine import DecisionEngine

decision = DecisionEngine()

tests = [
    "Halo",
    "Buka notepad",
    "Jam berapa sekarang?",
    "Siapa saya?",
    "Aku suka teh",
    "Apa itu AI?"
]

for text in tests:
    print(text, "->", decision.decide(text))