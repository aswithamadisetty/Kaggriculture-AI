import google.generativeai as genai
import os

# Replace with your actual API key
GEMINI_API_KEY = "AQ.Ab8RN6LgfinOV-tm6fRi3sn301YskTKnHbirbOkRh4QF-WhaEg"

# Cache the model to avoid checking every time
_available_model = None

def get_available_model():
    """Get the first available Gemini model for content generation"""
    global _available_model
    
    if _available_model:
        return _available_model
    
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        
        # List all available models
        models = list(genai.list_models())
        
        # Filter for models that support generateContent
        available_models = [
            m.name for m in models 
            if 'generateContent' in m.supported_generation_methods
        ]
        
        # Priority order for models
        model_priority = [
            'gemini-1.5-flash',
            'gemini-1.5-pro', 
            'gemini-1.0-pro',
            'gemini-pro'
        ]
        
        # Try to find the best available model
        for model_name in model_priority:
            for available in available_models:
                if model_name in available:
                    _available_model = model_name
                    print(f"✅ Using model: {_available_model}")
                    return _available_model
        
        # If no priority model found, use the first available
        if available_models:
            _available_model = available_models[0]
            print(f"✅ Using model: {_available_model}")
            return _available_model
        
        raise Exception("No available models found")
        
    except Exception as e:
        print(f"❌ Error listing models: {e}")
        # Fallback to a common model name
        return 'gemini-1.5-flash'

def ask_gemini(prompt):
    """
    Send a prompt to Gemini and get response
    """
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        
        # Get available model
        model_name = get_available_model()
        model = genai.GenerativeModel(model_name)
        
        response = model.generate_content(prompt)
        return response.text
        
    except Exception as e:
        return f"Error: {str(e)}\n\nPlease check:\n1. Your API key is correct\n2. You have access to Gemini API\n3. Your internet connection is working"