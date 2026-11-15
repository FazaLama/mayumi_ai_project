class ResponseService:

    def __init__(
        self,
        builder,
        llm,
        conversation,
        logger
    ):

        self.builder = builder
        self.llm = llm
        self.conversation = conversation
        self.logger = logger

    def generate(
        self,
        user_message,
        tool_result,
        emotion,
        affinity,
        reflection=None,
        style=None
    ):

        prompt = self.builder.build(
            user_message=user_message,
            conversation_history=self.conversation.get_history(),
            tool_result=tool_result,
            emotion=emotion,
            affinity=affinity,
            style=style
        )

        response = self.llm.chat(prompt)

        self.logger.info(f"MAYUMI : {response}")

        self.conversation.add_assistant_message(response)

        return response