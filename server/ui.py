import gradio as gr
import requests

BASE_URL = "http://localhost:7860"

def analyze(text):
    try:
        res = requests.post(f"{BASE_URL}/step", json={"text": text})
        data = res.json().get("observation", {})

        return (
            data.get("prediction", "unknown"),
            data.get("confidence", 0),
            data.get("reason", "No reason")
        )
    except Exception as e:
        return "error", 0, str(e)

with gr.Blocks(theme=gr.themes.Soft(), title="Fake News Detector") as demo:

    gr.Markdown("# 🧠 Fake News Detector AI")
    gr.Markdown("### Paste news article and detect if it's real or fake")

    with gr.Row():
        text_input = gr.Textbox(
            lines=6,
            placeholder="Paste news here...",
            label="News Input"
        )

    btn = gr.Button("🚀 Analyze")

    with gr.Row():
        prediction = gr.Textbox(label="Prediction")
        confidence = gr.Number(label="Confidence")

    reason = gr.Textbox(label="Reason", lines=3)

    btn.click(
        analyze,
        inputs=text_input,
        outputs=[prediction, confidence, reason]
    )

demo.launch(server_name="0.0.0.0", server_port=7860)
