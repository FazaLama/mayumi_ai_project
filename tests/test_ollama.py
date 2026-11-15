from backend.llm.ollama_client import OllamaClient

llm = OllamaClient()

response = llm.chat("Halo, siapa kamu?")

print("=" * 50)
print(response)