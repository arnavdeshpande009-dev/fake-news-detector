from fastapi import FastAPI
from env import FakeNewsEnv

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Server running"}

@app.post("/reset")
def reset():
    env = FakeNewsEnv()
    return env.reset()

@app.post("/step")
def step(action: dict):
    env = FakeNewsEnv()
    return env.step(action)