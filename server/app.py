from fastapi import FastAPI
from env import FakeNewsEnv
import uvicorn

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


# 🔥 REQUIRED MAIN FUNCTION
def main():
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)


# 🔥 REQUIRED ENTRY POINT
if __name__ == "__main__":
    main()