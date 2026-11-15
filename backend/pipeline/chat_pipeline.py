class ChatPipeline:

    def __init__(self, brain):

        self.brain = brain

    def process(self, user_message):

        return self.brain._chat(user_message)