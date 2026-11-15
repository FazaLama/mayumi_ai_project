from backend.conversation.conversation_manager import ConversationManager
from backend.memory.memory_extractor import MemoryExtractor
from backend.memory.memory_retriever import MemoryRetriever
from backend.prompt.prompt_builder import PromptBuilder
from backend.llm.ollama_client import OllamaClient
from backend.tools.tool_manager import ToolManager
from backend.utils.logger import Logger
from backend.emotion.emotion_manager import EmotionManager
from backend.affinity.affinity_manager import AffinityManager
from backend.decision.decision_engine import DecisionEngine
from backend.pipeline.chat_pipeline import ChatPipeline
from backend.services.response_service import ResponseService
from backend.services.memory_service import MemoryService
from backend.reflection.reflection_engine import ReflectionEngine
from backend.reasoning.reasoning_engine import ReasoningEngine
from backend.planning.planning_engine import PlanningEngine
from backend.profile.profile_question_engine import ProfileQuestionEngine
from backend.summary.conversation_summarizer import ConversationSummarizer
from backend.summary.summary_manager import SummaryManager
from backend.conversation.conversation_style_engine import ConversationStyleEngine


class Brain:

    def __init__(self):

        self.conversation = ConversationManager()

        self.extractor = MemoryExtractor()

        self.memory = MemoryRetriever()

        self.builder = PromptBuilder()

        self.llm = OllamaClient()

        self.tools = ToolManager()

        self.logger = Logger()

        self.emotion = EmotionManager()

        self.affinity = AffinityManager()

        self.decision = DecisionEngine()

        self.pipeline = ChatPipeline(self)

        self.response = ResponseService(
            builder=self.builder,
            llm=self.llm,
            conversation=self.conversation,
            logger=self.logger
        )

        self.memory_service = MemoryService(
            memory=self.memory,
            conversation=self.conversation,
            logger=self.logger
        )

        self.profile_question = ProfileQuestionEngine()

        self.reflection = ReflectionEngine()

        self.reasoning = ReasoningEngine()

        self.planner = PlanningEngine()

        self.summarizer = ConversationSummarizer()

        self.summary = SummaryManager()
        
        self.style = ConversationStyleEngine()

    def _chat(self, user_message: str):

        reflection = self.reflection.analyze(user_message)

        style = self.style.analyze(user_message)

        self.logger.info(
            f"STYLE : {style}"
        )

        reasoning = self.reasoning.analyze(user_message)

        self.logger.info(
            f"REASONING : {reasoning['type']}"
        )

        plan = self.planner.create_plan(user_message)

        self.logger.info(f"PLAN : {plan}")

        # ==========================
        # LOGGING
        # ==========================

        self.logger.info(f"USER : {user_message}")

        # ==========================
        # SHORT TERM MEMORY
        # ==========================

        self.conversation.add_user_message(user_message)

        # ==========================
        # LONG TERM MEMORY
        # ==========================

        self.extractor.process(user_message)

        # ==========================
        # PROFILE QUESTION
        # ==========================

        profile_answer = self.profile_question.answer(user_message)

        if profile_answer:

            self.logger.info("PROFILE QUESTION")

            response = profile_answer

            self.conversation.add_assistant_message(response)

            history = self.conversation.get_history()

            if len(history) >= 20:

                summary = self.summarizer.summarize(history)

                self.summary.save(summary)

            return response

        # ==========================
        # DECISION
        # ==========================

        decision = self.decision.decide(user_message)


        self.logger.info(f"DECISION : {decision}")

        # ==========================
        # MEMORY FIRST
        # ==========================

        if decision == "memory":


            response = self.memory_service.process(
                user_message
            )

            if response:

                return response

        # ==========================
        # EMOTION
        # ==========================

        self.emotion.process(user_message)

        current_emotion = self.emotion.get_emotion()

        # ==========================
        # AFFINITY
        # ==========================

        self.affinity.increase()

        current_affinity = self.affinity.get_level()

        # ==========================
        # TOOL / PLANNING
        # ==========================

        tool_result = None

        if decision == "tool":

            plan = self.planner.create_plan(user_message)

            if plan:

                self.logger.info(f"PLAN : {plan}")

                results = self.tools.execute_plan(plan)

                if results:

                    tool_result = {
                        "tool_used": True,
                        "tool_name": ", ".join(
                            r["tool_name"] for r in results
                        ),
                        "result": "\n".join(
                            r["result"] for r in results
                        )
                    }

                    self.logger.info(
                        f"TOOLS : {tool_result['tool_name']}"
                    )

            else:

                tool_result = self.tools.execute(user_message)

        response = self.response.generate(
            user_message=user_message,
            tool_result=tool_result,
            emotion=current_emotion,
            affinity=current_affinity,
            reflection=reflection,
            style=style
        )

        self.conversation.add_assistant_message(response)

        history = self.conversation.get_history()

        if len(history) >= 20:

            summary = self.summarizer.summarize(history)

            self.summary.save(summary)

        return response  

    def chat(self, user_message: str):

        return self.pipeline.process(user_message)

    def reset(self):

        self.conversation.clear()