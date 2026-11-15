class ConversationSummarizer:

    def summarize(self, history):

        important = []

        for chat in history:

            if chat["role"] != "user":
                continue

            text = chat["content"].strip()

            if len(text) < 20:
                continue

            important.append(text)

        important = important[-5:]

        return "\n".join(
            f"- {text}"
            for text in important
        )