from backend.entity.entity_extractor import EntityExtractor

extractor = EntityExtractor()

tests = [

    "Aku suka teh.",

    "Aku suka Blue Mallow Tea.",

    "Aku suka kopi.",

    "Aku suka Mobile Legends.",

    "Aku suka Naruto.",

    "Aku suka nasi goreng."

]

for text in tests:

    print("--------------------------------")

    print(text)

    print(extractor.extract(text))