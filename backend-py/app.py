from flask import Flask

app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "*"}})

tasks = []

@app.route("/api/v1/", methods=["GET"])
def hello_world():
    tasks.append("Hello, World!")
    return "<p>Hello, World!</p>"

@app.route("/api/v1/tasks", methods=["GET"])
def get_tasks():
    return {"tasks": tasks}, 200
