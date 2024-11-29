from openai import OpenAI


client = OpenAI()

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
