from services import Upload
class TestUpload:

    def test_deve_retornar_true_quando_passado_as_extensoes_esperadas(self):
        inputs = {
            "filename": "filenameTest.zip",
            "extensions": {"zip"}
        }
        expected = True

        result = Upload.allowed_file(
                inputs.get("filename"),
                inputs.get("extensions")
            )

        assert result == expected
    
    def test_deve_retornar_false_quando_não_for_as_extensoes_experadas(self):
        inputs = {
            "filename": "filenameTest.png",
            "extensions": {"zip"}
        }
        expected = False

        result = Upload.allowed_file(
            inputs.get("filename"),
            inputs.get("extensions")
        )

        assert result == expected

    