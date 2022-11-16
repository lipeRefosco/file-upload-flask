# File Upload
O projeto consiste em criar um client compilado em Python para windows. Este client pega todos os arquivos de alguma pasta específica, compacta para a o arquivo e envia para um servidor por https.

O servidor recebe o arquivo, descompacta na pasta *"default"* dos arquivos, exclui o arquivo zip, registra no banco de dados: **Horário**, o ***"Relative Path"*** do arquivo, o **IP** do request.

## Tecnologias
### Client-Side
- Python
- PyIntaller

### Server-Side
- Python (Flask)
- SQLite3
- Apache

## Tarefas
### Client-Side
- [x] Definir uma pasta especifica para varrer os arquivos.
- [x] Zippar todos os arquivos da pasta definida.
- [x] Deletar os arquivos originais.
- [x] Enviar o arquivo para o server pelo metodo POST.
- [x] "Triggar" quando algum arquivo for modificado/adicionado.
- [x] Compilar com o endereço do servidor correto.

### Server-Side
- [x] Configurar o apache
- [x] Definir uma rota pelo Flask que receba arquivos pelo metodo POST.
- [x] Salvar o arquivo no servidor em uma pasta padrão ("Default") do projeto.
- [x] Salvar no Banco de Dados: **Horário**, **Nome e o "Relative Path" onde o arquivo for salvo**, e o **IP** do request.
- [x] Ajustar CORS
- [x] Configurar Certificado SSL

## Opcional
- [ ] Interface gráfica
- [ ] Configuraçao de usuários


## Como testar a aplicação

### Aplicação do Servidor
Na pasta '/server', execute os seguintes comandos:

Criar um virtual enviroment:
```bash
$ python3 -m venv .
```

Ativar o virtual enviroment:
```bash
$ source /bin/activate
```

Instalar os requirements:
```bash
$(venv) python -m pip install -r requirements.txt
```

Rodar a aplicação:
```bash
$(venv) python3 -m flask -A src/init.py run
```