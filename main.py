"""
=========================================================
Kaggriculture-AI
Main Entry Point

Author : Aswitha Madisetty
Course : Kaggle + Google AI Agents Intensive
=========================================================
"""

from config.settings import PROJECT_NAME, VERSION
from agents.planner import PlannerAgent
from agents.research import ResearchAgent
from agents.crop_analysis import CropAnalysisAgent
from agents.advisor import AdvisorAgent


def banner():
    print("=" * 60)
    print(PROJECT_NAME)
    print(f"Version : {VERSION}")
    print("=" * 60)


def main():
    banner()

    print("\n🌱 Welcome to Kaggriculture-AI")
    print("Initializing AI Agriculture Assistant...\n")

    print("Modules")
    print("-------")
    print("1. Planner Agent")
    print("2. Research Agent")
    print("3. Crop Analysis Agent")
    print("4. Advisor Agent")
    print("5. Exit")

    while True:

        choice = input("\nSelect an option : ")

        if choice == "1":
             goal = input("\nEnter your farming goal: ")
             planner = PlannerAgent()
             planner.create_plan(goal)

        elif choice == "2":
            question = input("\nEnter your agriculture question: ")
            researcher = ResearchAgent()
            researcher.research(question)

        elif choice == "3":
            crop = input("\nCrop: ")
            soil = input("Soil Type: ")
            location = input("Location: ")
            season = input("Season: ")
            analyzer = CropAnalysisAgent()
            analyzer.analyze(crop, soil, location, season)

        elif choice == "4":
            crop = input("Crop: ")
            problem = input("Problem: ")
            advisor = AdvisorAgent()
            advisor.diagnose(crop, problem)

        elif choice == "5":
            print("\nThank you for using Kaggriculture-AI")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()