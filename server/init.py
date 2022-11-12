from pathlib import Path 
from flask import Flask, request
from flask_cors import CORS
from services import Index, Upload, Ip, Datas

app = Flask(__name__)
CORS(app)

app.config['FILES_FOLDER'] = str(Path(__file__).parent.resolve()) + "/"
app.config['ALLOWED_EXTENSIONS']  = {"zip"}
app.config['UPLOAD_FOLDER']       = app.config['FILES_FOLDER'] + "uploads"
app.config['DB_FOLDER']           = app.config['FILES_FOLDER'] + "database"
app.config['DB_FILE']             = "database.db"

@app.route("/", methods=["GET"])
def index():
    return Index.run()

@app.route("/upload", methods=["POST"])
def upload():
    return Upload.run(request, app)

@app.route("/ip", methods=["GET"])
def ip():
    return Ip.run(request)

@app.route("/datas", methods=["GET"])
def datas():
    return Datas.run(request, app)

if __name__ == "__main__":
    app.run()