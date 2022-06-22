from flask import Request, jsonify

class Ip:
    def run(request : Request):
        return jsonify(f"Seu ip é {request.remote_addr}")