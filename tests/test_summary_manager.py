from backend.summary.summary_manager import SummaryManager

manager = SummaryManager()

manager.save(
    "Ini adalah summary terbaru."
)

print(manager.get())