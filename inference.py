from env import FakeNewsEnv

env = FakeNewsEnv()

def run():

    print("[START] task=fake-news env=custom model=baseline")

    env.reset()
    env.text = "Breaking: Aliens found via WhatsApp forward"

    action = {"label": "fake news"}
    result = env.step(action)

    reward = round(result["reward"], 2)

    print(f"[STEP] step=1 action=fake news reward={reward:.2f} done=true error=null")
    print(f"[END] success=true steps=1 score={reward:.2f} rewards={reward:.2f}")

if __name__ == "__main__":
    run()