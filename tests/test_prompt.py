from backend.prompt.prompt_builder import PromptBuilder

builder = PromptBuilder()

prompt = builder.build(
    "Apa yang Mayumi suka?"
)

print(prompt)