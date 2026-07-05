from config.gemini import ask_gemini


class PlannerAgent:

    def create_plan(self, goal):

        print("\n" + "=" * 60)
        print("Planner Agent")
        print("=" * 60)

        prompt = f"""
You are an expert agriculture consultant.

Create a farming plan for the following goal.

Goal:
{goal}

The response should include:

1. Crop Planning
2. Soil Preparation
3. Fertilizer Recommendation
4. Irrigation Plan
5. Pest Management
6. Harvest Strategy

Return the answer in a clean numbered format.
"""

        print("\nGenerating AI farming plan...\n")

        answer = ask_gemini(prompt)

        print(answer)