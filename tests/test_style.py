from backend.conversation.conversation_style_engine import ConversationStyleEngine

engine = ConversationStyleEngine()

print(engine.analyze("Hari ini aku berhasil membuat AI."))

print(engine.analyze("Hari ini aku sedih."))

print(engine.analyze("wkwkwk lucu sekali"))