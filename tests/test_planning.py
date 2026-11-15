from backend.planning.planning_engine import PlanningEngine

planner = PlanningEngine()

tests = [
    "Buka notepad",
    "Buka notepad lalu calculator",
    "Halo Mayumi"
]

for t in tests:
    print("=" * 40)
    print(t)
    print(planner.create_plan(t))