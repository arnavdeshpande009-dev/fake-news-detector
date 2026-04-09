import os
from openai import OpenAI

def predict(text):
    client = OpenAI(
        base_url=os.environ["API_BASE_URL"],
        api_key=os.environ["API_KEY"]
    )

    response = client.chat.completions.create(
        model=os.environ["MODEL_NAME"],
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a fake news detector.\n"
                    "Return STRICT JSON only in this format:\n"
                    "{\n"
                    '  "prediction": "real" or "fake",\n'
                    '  "confidence": number between 0 and 1,\n'
                    '  "reason": "short explanation"\n'
                    "}"
                )
            },
            {"role": "user", "content": text}
        ]
    )

    output = response.choices[0].message.content

    import json
    try:
        parsed = json.loads(output)
        return parsed
    except:
        # fallback (important to avoid crash)
        return {
            "prediction": "fake",
            "confidence": 0.5,
            "reason": output
        }