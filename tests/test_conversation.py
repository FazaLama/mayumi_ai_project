from backend.conversation.conversation_manager import ConversationManager

conversation = ConversationManager()

conversation.add_user_message("Halo Mayumi.")

conversation.add_assistant_message("Halo! Senang bertemu denganmu.")

conversation.add_user_message("Apa kabar?")

conversation.add_assistant_message("Aku baik. Bagaimana denganmu?")

for chat in conversation.get_history():

    print(chat)