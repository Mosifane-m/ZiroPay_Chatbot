from openai import OpenAI

#openai.api_key = "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"

client = OpenAI(api_key="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")

def generate_answer(prompt: str):
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return completion.choices[0].message
    except Exception as e:
        return f"Error: {str(e)}"
