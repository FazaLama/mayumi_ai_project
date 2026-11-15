from collections import deque

from backend.config.settings import Settings


class ConversationManager:

    def __init__(self, max_history=None):

        if max_history is None:
            max_history = Settings.MAX_HISTORY

        self.max_history = max_history
        self.history = deque(maxlen=max_history)

    def add_user_message(self, message):

        self.history.append({
            "role": "user",
            "content": message
        })

    def add_assistant_message(self, message):

        self.history.append({
            "role": "assistant",
            "content": message
        })

    def get_history(self):

        return list(self.history)

    def clear(self):

        self.history.clear()