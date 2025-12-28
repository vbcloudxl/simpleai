from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
        <html>
            <head>
                <title>Hello AI</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        padding: 40px;
                        background: #f5f5f5;
                    }
                    .box {
                        background: white;
                        padding: 30px;
                        border-radius: 10px;
                        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                    }
                </style>
            </head>
            <body>
                <div class="box">
                    <h1>Hello, World from AI 👋</h1>
                    <p>Your Flask app is running successfully.</p>
                </div>
            </body>
        </html>
    """

@app.route("/api/hello")
def hello_api():
    return jsonify(message="Hello from your AI-powered Flask API!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)