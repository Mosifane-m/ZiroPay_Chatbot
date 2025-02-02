from flask import Flask, request, jsonify

from app.gpt_serives import generate_answer

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt', '')

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    # Generate GPT response
    answer = generate_answer(prompt)
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)
