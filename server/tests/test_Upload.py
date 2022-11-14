from services import Upload
from zipfile import ZipFile
import tempfile

class TestUpload:

    def test_deve_retornar_true_quando_passado_as_extensoes_esperadas(self):
        inputs = {
            "filename": "filenameTest.zip",
            "extensions": {"zip"}
        }
        expected = True

        processed = Upload.allowed_file(
                inputs.get("filename"),
                inputs.get("extensions")
            )
         
        result = processed == expected
   
        assert result

    def test_deve_retornar_false_quando_não_for_as_extensoes_experadas(self):
        inputs = {
            "filename": "filenameTest.png",
            "extensions": {"zip"}
        }
        expected = False

        processed = Upload.allowed_file(
            inputs.get("filename"),
            inputs.get("extensions")
        )
        
        result = processed == expected
        
        assert result

    def test_deve_recuperar_a_data_do_nome_do_arquivo(self):
        inputs = "nomearquivo_-_10-10-22_-_00-00.zip"

        expected = "10-10-22"

        processed = Upload.get_date(inputs)
        
        result = processed == expected
        
        assert result

    def test_deve_recuperar_e_formatar_a_hora_e_os_minutos_do_nome_do_arquivo(self):
        inputs = "nomearquivo_-_10-10-22_-_00-00.zip"
        expected = "00:00"

        processed = Upload.get_hours(inputs)
        
        result = processed == expected
        
        assert result
        