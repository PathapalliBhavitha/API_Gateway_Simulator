from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random
import time

app = FastAPI()

class RequestData(BaseModel):
    user_id: int
    score: int

@app.get("/")
def home():
    return {
        "message": "API Gateway Simulator Running"
    }

# -------------------------
# Evaluation Module
# -------------------------
@app.post("/evaluation")
def evaluation(data: RequestData):

    if data.score < 0:
        raise HTTPException(status_code=400, detail="Invalid score")

    responses = [
        {"evaluation": "approved"},
        {"evaluation": "rejected"},
        {"unexpected": "invalid_response"}
    ]

    return random.choice(responses)

# -------------------------
# Decision Module
# -------------------------
@app.post("/decision")
def decision(data: RequestData):

    if data.user_id == 999:
        time.sleep(5)

    return {
        "decision": "accepted"
    }

# -------------------------
# Monitoring Module
# -------------------------
@app.post("/monitoring")
def monitoring(data: RequestData):

    return {
        "monitoring": "logged"
    }

# -------------------------
# Gateway
# -------------------------
@app.post("/gateway")
def gateway(data: RequestData):

    try:

        evaluation_result = evaluation(data)
        decision_result = decision(data)
        monitoring_result = monitoring(data)

        return {
            "flow": "simulated",
            "status": "success",
            "evaluation": evaluation_result,
            "decision": decision_result,
            "monitoring": monitoring_result
        }

    except Exception as e:

        return {
            "flow": "simulated",
            "status": "failed",
            "error": str(e)
        }