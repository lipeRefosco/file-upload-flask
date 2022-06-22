import os
from flask import Flask, request
import services

app = Flask(__name__)

app.config['ALLOWED_EXTENSIONS'] = {"zip"}
app.config['UPLOAD_FOLDER']      = "uploads"
app.config['DB_FOLDER']          = "database"
app.config['DB_FILE']            = "uploads.db"

@app.route("/", methods=["GET"])
def index():
    return services.Index.run()

@app.route("/upload", methods=["POST"])
def upload():
    return services.Upload.run(request, app)

@app.route("/ip", methods=["GET"])
def ip():
    return services.Ip.run(request)

@app.route("/datas", methods=["GET"])
def datas():
    return services.Datas.run(request, app)

if __name__ == "__main__":
    app.run()