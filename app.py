from flask import Flask, render_template_string
import GUEST_GEN_FIXED  # Executes the payload code safely in context

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Deployed Python Application</title>
    <style>
        body { font-family: monospace; background: #0d1117; color: #58a6ff; text-align: center; padding: 50px; }
        .card { background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 20px; display: inline-block; }
    </style>
</head>
<body>
    <div class="card">
        <h2>System Status: Active</h2>
        <p>GUEST_GEN_FIXED.py initialized successfully on Vercel Serverless.</p>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
