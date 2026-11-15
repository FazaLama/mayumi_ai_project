from backend.profile.profile_question_engine import ProfileQuestionEngine

engine = ProfileQuestionEngine()

print(engine.answer("Siapa nama saya?"))

print(engine.answer("Saya tinggal dimana?"))

print(engine.answer("Minuman favoritku apa?"))