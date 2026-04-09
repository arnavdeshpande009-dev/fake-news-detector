from fastapi import FastAPI
from env import FakeNewsEnv

app = FastAPI()

env = FakeNewsEnv()

@app.get("/")
def root():
    return {"message": "Server running"}

@app.post("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: dict):
    return env.step(action)
