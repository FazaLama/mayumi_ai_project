from backend.profile.profile_extractor import ProfileExtractor
from backend.profile.profile_manager import ProfileManager

extractor = ProfileExtractor()

manager = ProfileManager()

extractor.process("Nama saya Faza")

extractor.process("Saya tinggal di Indonesia")

extractor.process("Saya suka teh")

profile = manager.load()

print(profile)