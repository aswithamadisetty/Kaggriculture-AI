import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.gemini import ask_gemini
import time

class PlannerAgent:
    def create_plan(self, goal):
        print("\n" + "=" * 60)
        print("Planner Agent")
        print("=" * 60)

        prompt = f"""
You are an expert agriculture planner.

Create a practical farming plan.

Goal:
{goal}

Return your answer in markdown.

Use these sections:

## Crop Planning

## Soil Preparation

## Fertilizer Recommendation

## Irrigation Plan

## Pest Management

## Harvest Strategy

Keep the answer concise and practical.
"""

        print("\nGenerating AI farming plan", end="")
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(0.5)
        print("\n")

        answer = ask_gemini(prompt)
        return answer