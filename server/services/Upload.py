import os
from urllib.request import Request
from werkzeug.utils import secure_filename

class Upload:

    def run(request: Request, app):
        """
           File upload reference
           https://flask.palletsprojects.com/en/2.1.x/patterns/fileuploads/
        """
        allowed_extensions = app.config["ALLOWED_EXTENSIONS"]
        upload_folder = app.config["UPLOAD_FOLDER"]

        if not request.files:
            return "Nenhum arquivo encontrado!"

        if 'file' not in request.files:
            return "O arquivo é obrigatório!"

        file = request.files['file']
        if not Upload.allowed_file( file.filename, allowed_extensions ):
            return "Arquivo não aceito!"

        filename = secure_filename( file.filename )
        try:
            file.save( os.path.join( upload_folder, filename ) )
        except Exception as ex:
            return f"Não foi possivel salvar o arquivo.{ex}"

        return "Happy path!"
    
    def allowed_file(filename: str, allowed_extensions: str):
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in allowed_extensions
