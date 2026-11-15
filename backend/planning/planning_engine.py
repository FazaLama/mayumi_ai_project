class PlanningEngine:

    def create_plan(self, user_message: str):

        text = user_message.lower()

        steps = []

        if "notepad" in text:
            steps.append("open_notepad")

        if "calculator" in text or "kalkulator" in text:
            steps.append("open_calculator")

        return steps