from flask import Flask

app = Flask(__name__)

@app.route("/test")
def test():
    return "Test message"

@app.route("/hello")
def hello():
    return "Hello message"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
