from fastapi import FastAPI
from env import FakeNewsEnv

app = FastAPI()

env = FakeNewsEnv()

@app.get("/")
def home():
    return {"message": "Fake News Detector API running"}

# 🔥 REQUIRED: RESET ENDPOINT
@app.post("/reset")
def reset():
    state = env.reset()
    return {"observation": state}

# 🔥 REQUIRED: STEP ENDPOINT
@app.post("/step")
def step(action: dict):
    result = env.step(action)
    return result