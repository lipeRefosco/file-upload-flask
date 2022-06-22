from flask import Request

class Ip:
    def run(request : Request):
        return f"Seu ip é {request.remote_addr}"