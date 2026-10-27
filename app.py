from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Git Docker Integration!"

app.run(host="0.0.0.0", port=3000)
