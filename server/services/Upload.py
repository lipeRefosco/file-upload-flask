import os
import sqlite3
from flask import Request
from zipfile import ZipFile
from werkzeug.utils import secure_filename

class Upload:

    def run(request: Request, app):
        """
           File upload reference
           https://flask.palletsprojects.com/en/2.1.x/patterns/fileuploads/
        """
        allowed_extensions = app.config["ALLOWED_EXTENSIONS"]
        upload_folder      = app.config["UPLOAD_FOLDER"]
        
        # Path Exceptions
        if not os.path.exists( upload_folder ):
            os.mkdir( upload_folder )

        os.chdir( upload_folder )

        # Request file exception
        if not request.files:
            return "Nenhum arquivo encontrado!"

        if 'file' not in request.files:
            return "O arquivo é obrigatório!"

        # Handle file
        file = request.files['file']

        # Verify if is a allowed file
        if not Upload.allowed_file( file.filename, allowed_extensions ):
            return "Arquivo não aceito!"
        
        # Define data to DB
        data = {
            "ip"       : request.remote_addr,
            "filename" : secure_filename( file.filename )
        }

        try:
            file.save( data["filename"] )
        except Exception as ex:
            return f"Não foi possivel salvar o arquivo.{ex}"

        # More informations to DB
        data["date"]  = Upload.get_date(data["filename"])
        data["hour"]  = Upload.get_hours(data["filename"])
        data["files"] = Upload.unzip_file( upload_folder, data["filename"] )
        
        os.remove( data["filename"] )

        # Start a connection with DB
        os.chdir('../')
        if not os.path.exists( 'database' ):
            os.mkdir( 'database' )
        os.chdir( 'database' )

        # Start a connection with DB
        con = sqlite3.connect("uploads.db")
        cur = con.cursor()
        # Create table
        cur.execute('CREATE TABLE IF NOT EXISTS uploads (ip, file, date);')
        
        # Insert itch file on DB
        for file in data["files"]:
            cur.execute(f"INSERT INTO uploads (ip, file, date) VALUES ('{data['ip']}', '{file}', '{data['date']} {data['hour']}');")

        cur.execute("SELECT * FROM uploads")

        for db_data in cur.fetchall():
            print(db_data)
        
        return "Happy path"
    
    def allowed_file(filename: str, allowed_extensions: str):
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in allowed_extensions

    def get_date(filename : str):
        infos = filename.split("_-_")
        return infos[1]
    
    def get_hours(filename : str):
        infos = filename.split("_-_")
        hours_formated = infos[2].replace("-", ":").replace(".zip", "")
        return hours_formated

    def unzip_file(folder : str, target : str):
        
        zip_file = target
        
        files_on_target = []

        with ZipFile( zip_file ) as zip:
            files_on_target += zip.namelist()
            zip.extractall()

        return files_on_target