import gradio as gr
from env import FakeNewsEnv

env = FakeNewsEnv()

def predict(text):
    env.reset()
    env.text = text

    action = {"label": "fake news"}
    result = env.step(action)

    obs = result["observation"]

    prediction = str(obs["prediction"])
    confidence = float(obs["confidence"])
    reason = str(obs["reason"])

    return prediction, confidence, reason

iface = gr.Interface(
    fn=predict,
    inputs=gr.Textbox(lines=5, placeholder="Enter news text..."),
    outputs=[
        gr.Text(label="Prediction"),
        gr.Number(label="Confidence"),
        gr.Text(label="Reason")
    ],
    title="Fake News Detector",
    description="AI + Rule-based Fake News Detection"
)

iface.launch(server_name="0.0.0.0", server_port=7860)