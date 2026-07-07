import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.gemini import ask_gemini
import time

class CropAnalysisAgent:
    def analyze(self, crop, soil, location, season):
        print("\n" + "=" * 60)
        print("🌾 Crop Analysis Agent")
        print("=" * 60)

        prompt = f"""
You are an agricultural scientist.

Crop:
{crop}

Soil:
{soil}

Location:
{location}

Season:
{season}

Provide a detailed analysis.

Use markdown headings.

Include:

# Crop Suitability

# Soil Analysis

# Climate Suitability

# Fertilizer Recommendation

# Irrigation Schedule

# Pest & Disease Risks

# Expected Yield

# Overall Recommendation
"""

        print("\nAnalyzing Crop", end="")
        for _ in range(3):
            print(" 🌾", end="", flush=True)
            time.sleep(0.5)
        print("\n")

        answer = ask_gemini(prompt)
        return answer