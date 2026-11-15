from backend.brain.brain import Brain

brain = Brain()

print(type(brain.memory))

print("=" * 50)
print("      Mayumi AI")
print("=" * 50)
print("Ketik 'exit' untuk keluar.")
print()

while True:

    user = input("You : ")

    if user.lower() == "exit":
        break

    response = brain.chat(user)

    print()
    print("Mayumi :", response)
    print()