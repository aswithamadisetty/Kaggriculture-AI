import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.gemini import ask_gemini
import time

class AdvisorAgent:
    def diagnose(self, crop, problem):
        print("\n" + "=" * 60)
        print("🩺 Advisor Agent")
        print("=" * 60)

        prompt = f"""
You are an expert agricultural plant doctor.

Crop:
{crop}

Problem:
{problem}

Return the answer in Markdown.

Include:

# Possible Disease

# Cause

# Confidence Level

# Immediate Solution

# Recommended Pesticide/Fungicide

# Prevention Tips
"""

        print("\nAnalyzing Disease", end="")
        for _ in range(3):
            print(" 🩺", end="", flush=True)
            time.sleep(0.5)
        print("\n")

        answer = ask_gemini(prompt)
        return answer