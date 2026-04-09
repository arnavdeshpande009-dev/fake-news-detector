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


# ✅ REQUIRED FOR VALIDATION (THIS IS WHY YOU FAILED)
def main():
    return app


# ✅ REQUIRED ENTRY POINT
if __name__ == "__main__":
    main()
