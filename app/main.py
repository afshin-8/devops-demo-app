from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return"CI/CD with self-hosted runner is working correct full!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
