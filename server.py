from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google import genai

app = FastAPI(title="DPI Governance AI Engine")

# Enable CORS so your frontend UI can communicate with this backend easily
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the Gemini Client
client = genai.Client()

class GrievanceRequest(BaseModel):
    text: str

@app.post("/analyze")
async def analyze_grievance(request: GrievanceRequest):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Input text cannot be empty.")
    
    prompt = f"""
    You are an AI core engine for Indian Digital Public Infrastructure (DPI) & Governance.
    Analyze the following citizen development request/grievance:
    
    "{request.text}"
    
    Extract and return the data in a clear structured format with these exact headings:
    - Location (Village/District/State)
    - Sector (e.g., Water, Roads, Electricity, Healthcare)
    - Urgency Level (Low, Medium, High, Critical)
    - Clean Summary
    - Suggested Infrastructure Intervention
    """

    try:
        response = client.models.generate_content(
            model='gemini-3.5-flash',
            contents=prompt,
        )
        return {"status": "success", "analysis": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)


