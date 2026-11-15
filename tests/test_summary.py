from backend.summary.conversation_summarizer import ConversationSummarizer


history = [

    {"role": "user", "content": "Halo"},

    {"role": "assistant", "content": "Halo juga"},

    {
        "role": "user",
        "content": "Aku sedang membuat AI Mayumi."
    },

    {
        "role": "user",
        "content": "Hari ini berhasil membuat Memory System."
    },

    {
        "role": "user",
        "content": "Sekarang sedang belajar Conversation Summarizer."
    }

]

summary = ConversationSummarizer()

print(summary.summarize(history))