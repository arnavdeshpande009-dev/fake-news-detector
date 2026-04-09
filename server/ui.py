import os
import requests
import gradio as gr

# Your Space base URL (auto works on HF)
BASE_URL = "http://localhost:7860"

def call_api(text):
    try:
        # call /reset
        requests.post(f"{BASE_URL}/reset")

        # call /step
        res = requests.post(
            f"{BASE_URL}/step",
            json={"label": "fake news"}  # dummy, env decides
        )

        data = res.json()

        obs = data.get("observation", {})
        return (
            obs.get("prediction", "unknown"),
            obs.get("confidence", 0.0),
            obs.get("reason", "No reason")
        )

    except Exception as e:
        return "error", 0.0, str(e)


with gr.Blocks(theme=gr.themes.Soft()) as demo:

    gr.Markdown("## 📰 Fake News Detector AI")
    gr.Markdown("Enter news text and detect if it's real or fake")

    text_input = gr.Textbox(
        lines=5,
        placeholder="Paste news article here..."
    )

    btn = gr.Button("🔍 Analyze")

    prediction = gr.Textbox(label="Prediction")
    confidence = gr.Number(label="Confidence")
    reason = gr.Textbox(label="Reason")

    btn.click(
        call_api,
        inputs=text_input,
        outputs=[prediction, confidence, reason]
    )

demo.launch(server_name="0.0.0.0", server_port=7860)