import os
from flask import Request, Response, jsonify
import sqlite3

class Datas:
    def run(request : Request, app):

        db_folder = app.config["DB_FOLDER"]
        db_file   = app.config["DB_FILE"]

        if not os.path.exists( db_folder ) or not os.path.exists( db_folder + os.path.sep + db_file ):
            return jsonify("Nenhum arquivo enviado!")

        con = sqlite3.connect( db_folder + os.path.sep + db_file )
        cur = con.cursor()

        db_data = cur.execute("SELECT * FROM uploads")

        return jsonify(db_data.fetchall())