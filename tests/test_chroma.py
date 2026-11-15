import chromadb

client = chromadb.PersistentClient(path="./memory")

collection = client.get_or_create_collection("Mayumi")

collection.add(
    ids=["1"],
    documents=["Halo saya Mayumi"],
)

print(collection.count())