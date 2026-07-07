import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.gemini import ask_gemini
import time

class ResearchAgent:
    def research(self, question):
        print("\n" + "=" * 60)
        print("📚 Research Agent")
        print("=" * 60)

        prompt = f"""
You are an expert agricultural researcher.

Question:
{question}

Answer using proper markdown.

Use these sections:

# Explanation

# Best Practices

# Scientific Reasoning

# Practical Tips

Keep the response professional and well formatted.
"""

        print("\nResearching", end="")
        for _ in range(3):
            print(" 🔍", end="", flush=True)
            time.sleep(0.5)
        print("\n")

        answer = ask_gemini(prompt)
        return answer