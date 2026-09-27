import os
from google import genai

# 1. Initialize the GenAI client
client = genai.Client()

def process_citizen_grievance(raw_text_input: str):
    prompt = f"""
    You are an AI core engine for Indian Digital Public Infrastructure (DPI) & Governance.
    Analyze the following citizen development request/grievance:
    
    "{raw_text_input}"
    
    Extract and return the data in a clear structured format with these exact fields:
    - Location (Village/District/State)
    - Sector (e.g., Water, Roads, Electricity, Healthcare)
    - Urgency Level (Low, Medium, High, Critical)
    - Clean Summary (Translate to professional English if needed)
    - Suggested Infrastructure Intervention
    """

    # Updated model string to gemini-3.5-flash
    response = client.models.generate_content(
        model='gemini-3.5-flash',
        contents=prompt,
    )
    
    return response.text

if __name__ == "__main__":
    sample_complaint = "Hamaare gaon Rampur, district Varanasi mein pichle 10 dinon se paani ki pipeline toot gayi hai, aur bacche school nahi ja pa rahe kyunki raste par bahut keechad hai."
    
    print("--- RAW CITIZEN INPUT ---")
    print(sample_complaint)
    print("\n--- PROCESSING WITH GEMINI AI ---")
    
    result = process_citizen_grievance(sample_complaint)
    print(result)

