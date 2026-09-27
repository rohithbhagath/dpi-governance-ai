from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google import genai
import os

app = FastAPI()

# Add the new root status route here:
@app.get("/api")
def root_status():
    return {"status": "DPI Governance AI Backend is live with Gemini!"}

# Initialize the Gemini client using environment variable
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

class GrievanceRequest(BaseModel):
    text: str

@app.post("/api/analyze")
async def analyze_grievance(request: GrievanceRequest):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=request.text,
        )
        return {"result": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
