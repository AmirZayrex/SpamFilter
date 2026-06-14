from flask import Flask, request, render_template_string

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from predictor import predict_message

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Spam Filter</title>
    <style>
        body { font-family: Arial; max-width: 600px; margin: 50px auto; padding: 20px; }
        textarea { width: 100%; height: 100px; margin-bottom: 10px; }
        button { padding: 10px 20px; background: #007bff; color: white; border: none; cursor: pointer; }
        .result { margin-top: 20px; padding: 15px; border-radius: 5px; }
        .spam { background: #ffdddd; color: red; }
        .ham { background: #ddffdd; color: green; }
    </style>
</head>
<body>
    <h1>📧 Spam Message Detector</h1>
    <form method="POST">
        <textarea name="message" placeholder="Enter your message here...">{{ message }}</textarea>
        <button type="submit">Analyze</button>
    </form>
    {% if result %}
    <div class="result {{ result_class }}">
        <strong>{{ result }}</strong><br>
        Ham Probability: {{ ham_prob }}%<br>
        Spam Probability: {{ spam_prob }}%
    </div>
    {% endif %}
</body>
</html>
"""


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    result_class = ""
    ham_prob = spam_prob = 0
    message = ""

    if request.method == 'POST':
        message = request.form['message']
        if message:
            prediction = predict_message(message)
            result = f"{'🚫 SPAM' if prediction['prediction'] == 'spam' else '✅ HAM'}!"
            result_class = 'spam' if prediction['prediction'] == 'spam' else 'ham'
            ham_prob = round(prediction['ham_prob'] * 100, 1)
            spam_prob = round(prediction['spam_prob'] * 100, 1)

    return render_template_string(
        HTML_TEMPLATE,
        result=result,
        result_class=result_class,
        ham_prob=ham_prob,
        spam_prob=spam_prob,
        message=message
    )


def launch_ui():
    app.run(host='0.0.0.0', port=8080, debug=False)


if __name__ == '__main__':
    launch_ui()
    # python3 -m src.ui

# http://127.0.0.1:8080
