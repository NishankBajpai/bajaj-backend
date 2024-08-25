from fastapi import FastAPI, HTTPException
from models import DataRequest
from utils import split_data

app = FastAPI()

USER_ID = "john_doe_17091999"
EMAIL = "john@xyz.com"
ROLL_NUMBER = "ABCD123"

@app.get("/bfhl")
async def get_operation_code():
    return {"operation_code": 1}

@app.post("/bfhl")
async def process_data(request: DataRequest):
    try:
        numbers, alphabets, highest_lowercase = split_data(request.data)
        response = {
            "is_success": True,
            "user_id": USER_ID,
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else []
        }
        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error processing data")
