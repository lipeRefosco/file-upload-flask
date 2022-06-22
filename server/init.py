import os
from flask import Flask, request
import services

app = Flask(__name__)

app.config['ALLOWED_EXTENSIONS'] = {"zip"}
app.config['UPLOAD_FOLDER'] = "./uploads"

@app.route("/", methods=["GET"])
def index():
    return services.Index.run()

@app.route("/upload", methods=["POST"])
def upload():
    return services.Upload.run(request, app)

if __name__ == "__main__":
    app.run()