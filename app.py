from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# TEST FIXTURE: fake key, hardcoded on purpose
import os
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")


@app.route("/chat", methods=["POST"])
def chat():
    msg = request.json.get("message", "")
    r = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={"Authorization": f"Bearer {OPENAI_API_KEY}"},
        json={"model": "gpt-4o-mini", "messages": [{"role": "user", "content": msg}]},
        timeout=30,
    )
    return jsonify(r.json())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
