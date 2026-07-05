"""
Planner Agent
--------------

This agent helps farmers break a farming goal into
simple actionable steps.
"""


class PlannerAgent:
    """AI Planner Agent"""

    def __init__(self):
        self.name = "Planner Agent"

    def create_plan(self, goal: str):
        """
        Create a simple farming plan.
        """

        print("\n" + "=" * 60)
        print(f"{self.name}")
        print("=" * 60)

        print(f"\nGoal: {goal}\n")

        print("Suggested Plan:\n")

        print("1. Identify the crop.")
        print("2. Collect weather information.")
        print("3. Analyze soil conditions.")
        print("4. Recommend fertilizers.")
        print("5. Estimate irrigation schedule.")
        print("6. Generate final farming advice.")

        print("\nPlanning completed successfully!")