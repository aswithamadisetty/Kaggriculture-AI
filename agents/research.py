from config.gemini import ask_gemini
import time


class ResearchAgent:

    def research(self, question):

        print("\n" + "=" * 60)
        print("Research Agent")
        print("=" * 60)

        prompt = f"""
You are an expert agricultural researcher.

Answer the following farming question clearly.

Question:
{question}

Provide:

1. Explanation
2. Best Practices
3. Scientific Reasoning
4. Practical Tips

Return the answer in a clean numbered format.
"""

        print("\nResearching", end="")
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(0.5)
        print("\n")

        answer = ask_gemini(prompt)

        print(answer)