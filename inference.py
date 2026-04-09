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
            {"role": "system", "content": "Classify news as real or fake. Give short reason."},
            {"role": "user", "content": text}
        ]
    )

    output = response.choices[0].message.content

    return {
        "prediction": output,
        "confidence": 0.9,
        "reason": output
    }
