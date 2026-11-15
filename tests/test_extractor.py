from backend.memory.memory_engine import MemoryEngine
from backend.memory.memory_extractor import MemoryExtractor

memory = MemoryEngine()

memory.clear()

extractor = MemoryExtractor()

extractor.process("Nama saya Faza")

extractor.process("Saya tinggal di Indonesia")

extractor.process("Saya suka kopi")

print(memory.search("Siapa user?"))