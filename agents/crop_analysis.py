from config.gemini import ask_gemini


class CropAnalysisAgent:

    def analyze(self, crop, soil, location, season):

        print("\n" + "=" * 60)
        print("Crop Analysis Agent")
        print("=" * 60)

        prompt = f"""
You are an experienced agricultural scientist.

Analyze the following farming details.

Crop:
{crop}

Soil:
{soil}

Location:
{location}

Season:
{season}

Provide:

1. Crop suitability
2. Soil analysis
3. Climate suitability
4. Fertilizer recommendation
5. Irrigation schedule
6. Pest & Disease Risks
7. Expected Yield
8. Overall Recommendation

Return the answer in a clean numbered format.
"""

        print("\nAnalyzing crop...\n")

        answer = ask_gemini(prompt)

        print(answer)