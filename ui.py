import gradio as gr
import requests

BASE_URL = "http://localhost:7860"

def call_api(text):
    try:
        res = requests.post(
            f"{BASE_URL}/step",
            json={"label": text}
        )
        data = res.json()
        obs = data.get("observation", {})

        pred = obs.get("prediction", "Unknown")
        conf = obs.get("confidence", 0)
        reason = obs.get("reason", "No reason")

        # Styling output
        if "fake" in pred.lower():
            badge = "🚨 FAKE NEWS"
            color = "red"
        else:
            badge = "✅ REAL NEWS"
            color = "green"

        return badge, conf, reason

    except Exception as e:
        return "❌ Error", 0, str(e)


with gr.Blocks(theme=gr.themes.Soft(primary_hue="blue")) as demo:

    gr.Markdown("""
    # 📰 Fake News Detector AI
    ### ⚡ Detect misinformation instantly using AI
    """)

    with gr.Row():
        text_input = gr.Textbox(
            lines=6,
            placeholder="Paste news article here...",
            label="📝 Input News"
        )

    analyze_btn = gr.Button("🔍 Analyze", variant="primary")

    with gr.Row():
        prediction = gr.Textbox(label="📢 Result")
        confidence = gr.Slider(0, 1, label="📊 Confidence", interactive=False)

    reason = gr.Textbox(label="🧠 Explanation")

    analyze_btn.click(
        call_api,
        inputs=text_input,
        outputs=[prediction, confidence, reason]
    )

    gr.Markdown("""
    ---
    💡 Tip: Try both real and fake headlines to test accuracy  
    🚀 Built for AI Hackathon
    """)

demo.launch(server_name="0.0.0.0", server_port=7860)
