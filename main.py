from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google import generativeai
import random

# Initialize FastAPI app
app = FastAPI(title="Chicken Suitability Checker API 🌡️🐥")

# API keys for Gemini
API_KEYS = [
    "AIzaSyBvtwP2ulNHPQexfPhhR13U30pvF2OswrU",
    "AIzaSyD0dLXPPrZmLbnHOj3f9twHmT_PZc15wMo",
]

# Configure Gemini with a random API key
api_key = random.choice(API_KEYS)
generativeai.configure(api_key=api_key)

# Initialize Gemini model
model = generativeai.GenerativeModel("gemini-2.0-flash")

# Request model for location and language input
class LocationRequest(BaseModel):
    location: str
    lang: str = "english"  # Default to English

# Endpoint to check chicken suitability
@app.post("/check-suitability")
async def check_chicken_suitability(request: LocationRequest):
    location = request.location
    lang = request.lang.lower()
    
    # Validate language
    if lang not in ["english", "hausa"]:
        raise HTTPException(status_code=400, detail="Invalid language. Use 'english' or 'hausa'.")

    prompt = f"Give me the average predicted temperature in Celsius for the next 7 days in {location}. Just make a prediction. Respond with only 7 comma-separated numbers."

    try:
        # Generate content from Gemini
        response = model.generate_content(prompt)
        raw = response.text.strip()

        # Parse temperatures
        temps = [float(t.strip()) for t in raw.split(",") if t.strip().replace(".", "", 1).isdigit()]

        # Validate response
        if len(temps) != 7:
            raise HTTPException(status_code=400, detail=f"Couldn't get 7 temperatures. Gemini returned: {raw}")

        # Calculate average temperature
        avg_temp = sum(temps) / 7

        # Prepare response based on language
        result = {
            "location": location,
            "average_temperature_celsius": round(avg_temp, 2),
        }

        # English response
        if lang == "english":
            if avg_temp > 40:
                result["suitability"] = "NOT suitable"
                result["message"] = "⚠️ The average temperature is expected to exceed 40°C over the next 7 days. It is NOT suitable to place young poultry chicks."
            else:
                result["suitability"] = "Suitable"
                result["message"] = "✅ The average temperature is expected to NOT exceed 40°C over the next 7 days. It is suitable to place young chickens."
        
        # Hausa response
        else:
            if avg_temp > 40:
                result["suitability"] = "BA A YARDA BA"
                result["message"] = "⚠️ Matsakaicin zafin jiki yana tsammanin ya wuce 40°C a cikin kwanaki 7 masu zuwa. BA A YARDA da sanya ƙananan tsutsayen kaji ba."
            else:
                result["suitability"] = "AN YARDA"
                result["message"] = "✅ Matsakaicin zafin jiki yana tsammanin BA zai wuce 40°C ba a cikin kwanaki 7 masu zuwa. An YARDA da sanya ƙananan tsutsayen kaji."

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error occurred: {str(e)}")

# Root endpoint for welcome message
@app.get("/")
async def root():
    return {
        "message": "Welcome to the Chicken Suitability Checker API! Use POST /check-suitability with a JSON body containing 'location' and optional 'lang' ('english' or 'hausa').",
        "hausa_message": "Barka da zuwa API na Duba Yanayin Kaji! Yi amfani da POST /check-suitability tare da JSON mai ɗauke da 'location' da zaɓin 'lang' ('english' ko 'hausa')."
    }