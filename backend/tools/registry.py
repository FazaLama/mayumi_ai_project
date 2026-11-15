class ToolRegistry:

    def __init__(self):

        self.tools = {}

    def register(self, name, func):

        self.tools[name] = func

    def execute(self, name):

        if name in self.tools:

            return self.tools[name]()

        return None

    def get_tools(self):

        return list(self.tools.keys())