"""
=========================================================
Kaggriculture-AI
Main Entry Point

Author : Aswitha Madisetty
Course : Kaggle + Google AI Agents Intensive
=========================================================
"""

from config.settings import PROJECT_NAME, VERSION


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
            print("\nPlanner Agent coming soon...")

        elif choice == "2":
            print("\nResearch Agent coming soon...")

        elif choice == "3":
            print("\nCrop Analysis Agent coming soon...")

        elif choice == "4":
            print("\nAdvisor Agent coming soon...")

        elif choice == "5":
            print("\nThank you for using Kaggriculture-AI")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()