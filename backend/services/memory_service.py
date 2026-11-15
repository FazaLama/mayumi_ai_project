class MemoryService:

    def __init__(
        self,
        memory,
        conversation,
        logger
    ):

        self.memory = memory
        self.conversation = conversation
        self.logger = logger

    def process(self, user_message):

        memory = self.memory.best(user_message)

        if not memory:
            return None

        self.logger.info(
            f"MEMORY : {memory['content']}"
        )

        response = (
            "Kalau berdasarkan yang kuingat,\n\n"
            f"{memory['content']}"
        )

        self.conversation.add_assistant_message(response)

        self.logger.info("RESPONSE : MEMORY")

        return response