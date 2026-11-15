from backend.intent.intent_classifier import IntentClassifier
from backend.tools.registry import ToolRegistry
from backend.tools.desktop_tools import DesktopTools
from backend.tools.system_tools import SystemTools


class ToolManager:

    def __init__(self):

        self.intent = IntentClassifier()

        self.registry = ToolRegistry()

        # ==========================
        # REGISTER TOOLS
        # ==========================

        self.registry.register(
            "open_notepad",
            DesktopTools.open_notepad
        )

        self.registry.register(
            "open_calculator",
            DesktopTools.open_calculator
        )

        self.registry.register(
            "get_time",
            SystemTools.get_time
        )

        self.registry.register(
            "get_date",
            SystemTools.get_date
        )

    # ==========================
    # SINGLE TOOL
    # ==========================

    def execute(self, user_message: str):

        intent = self.intent.classify(user_message)

        if intent is None:
            return None

        result = self.registry.execute(intent)

        if result is None:
            return None

        return {
            "tool_used": True,
            "tool_name": intent,
            "result": result
        }

    # ==========================
    # MULTI TOOL (Planning Engine)
    # ==========================

    def execute_plan(self, plan):

        results = []

        for step in plan:

            result = self.registry.execute(step)

            if result is None:
                continue

            results.append({
                "tool_name": step,
                "result": result
            })

        return results