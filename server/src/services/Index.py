
from flask import jsonify


class Index:
    
    def run():
        return jsonify({
            "/"     : "Esta página!",
            "/ip"   : "Retorna o Ip do client!",
            "/datas": "Retorna os dados já gravados no banco!",
            "upload": "Rota de upload dos arquivos, apenas no metodo POST!"
        })