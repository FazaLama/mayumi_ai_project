from backend.prompt.prompt_builder import PromptBuilder
from backend.llm.ollama_client import OllamaClient
from backend.conversation.conversation_manager import ConversationManager
from backend.memory.memory_extractor import MemoryExtractor

builder = PromptBuilder()
llm = OllamaClient()
conversation = ConversationManager()
extractor = MemoryExtractor()

while True:

    user = input("You : ")

    if user.lower() in ["exit", "quit"]:
        break

    conversation.add_user_message(user)
    extractor.process(user)

    prompt = builder.build(
        user,
        conversation.get_history()
    )

    response = llm.chat(prompt)

    conversation.add_assistant_message(response)

    print()
    print("Mayumi :", response)
    print()