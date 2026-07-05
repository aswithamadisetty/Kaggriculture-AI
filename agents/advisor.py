from config.gemini import ask_gemini

class AdvisorAgent:

    def diagnose(self, crop, problem):

        prompt = f"""
You are an agricultural plant doctor.

Crop:
{crop}

Problem:
{problem}

Provide:

1. Possible disease
2. Cause
3. Confidence level
4. Immediate solution
5. Recommended pesticide/fungicide
6. Prevention tips

Return in a clean format.
"""

        print("\nAnalyzing disease...\n")
        answer = ask_gemini(prompt)
        print(answer)