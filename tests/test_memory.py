from backend.memory.memory_engine import MemoryEngine


memory = MemoryEngine()

print("=" * 40)
print("MAYUMI MEMORY TEST")
print("=" * 40)

# Bersihkan database
memory.clear()

# Simpan beberapa memory
memory.save("Namaku Mayumi.")
memory.save("Aku adalah AI Virtual Assistant.")
memory.save("Aku suka minum teh.")
memory.save("Aku dibuat menggunakan Ollama.")
memory.save("Aku senang membantu pengguna.")

print()
print("Jumlah Memory :", memory.count())

print()

print("Pencarian 1")
print(memory.search("Siapa Mayumi?"))

print()

print("Pencarian 2")
print(memory.search("Apa yang Mayumi suka?"))

print()

print("Pencarian 3")
print(memory.search("Mayumi dibuat menggunakan apa?"))