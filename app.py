from flask import Flask, request, jsonify, render_template
from openai_utils import generate_reply
import csv
import uuid

app = Flask(__name__)
CSV_FILE = 'storage.csv'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/reply', methods=['POST'])
def reply():
    data = request.get_json()
    message = data.get("message")
    brand = data.get("brand", "default")

    if not message:
        return jsonify({"error": "Missing message"}), 400

    reply_text = generate_reply(message, brand)

    with open(CSV_FILE, "a", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([str(uuid.uuid4()), brand, message, reply_text])

    return jsonify({"reply": reply_text})

if __name__ == '__main__':
    app.run(debug=True)
