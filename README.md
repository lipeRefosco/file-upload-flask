# Teste admissional Raioss.com
A meta sua para o mês de testes, basicamente é fazer um script local em python que você deverá compilar para **.exe**, que deverá enviar arquivos para uma outra aplicação em flask, a ser desenvolvida por você também.

Deverá fazer o deploy desta aplicação **Flask** de maneira segura no servidor. Basicamente, um programa a ser rodado no computador local, que envia arquivos para um serviço em **Flask** rodando em nuvem. 

Fazer uma aplicação em **Flask** que receba conexões do tipo **POST** contendo um arquivo e que salve esse arquivo em algum local no servidor. Nesta aplicação, não será necessário configurar usuários ou logins, nem precisa ter interface gráfica...

A aplicação feita em Flask deverá estar acessível pelo navegador, por meio de uma conexão segura pelo endereço "https://albert.raioss.rocks". Este endereço já está configurado para direcionar para o servidor que você usará para testes, descrito abaixo. A aplicação, deverá registrar em um **Sqlite3** o **horário**, o **nome do arquivo** que chegou e de qual **IP** ele recebeu.

Fazer o deploy desta aplicação em um servidor que está rodando **ubuntu 20** (usuário: **root** ; IP: **191.252.177.157**, senha: **raioss@server**). O domínio "**albert.raioss.rocks**" está direcionando para este servidor. É provável que tenha que, por meio de acesso remoto, instalar e configurar um servidor '**apache**' nesta máquina.

Fazer um software executável (sugiro utilizar o **PyInstaller** para compilar python para windows) que rode em Windows que seja capaz de enviar arquivos de uma determinada pasta qualquer, **faça um zip dos arquivos,** **delete os arquivos originais** e **envie para a aplicação flask** que estará no **https://albert.raioss.rocks**. Este software deverá **monitorar** a pasta de modo com que se o usuário colar mais algum outro arquivo lá, ele **automaticamente** irá compactar (zipar), deletar o arquivo original e mandar para o albert.raioss.rocks.

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
- [ ] Compilar com o endereço do servidor correto.

### Server-Side
- [x] Configurar o apache
- [x] Definir uma rota pelo Flask que receba arquivos pelo metodo POST.
- [x] Salvar o arquivo no servidor em uma pasta padrão ("Default") do projeto.
- [x] Salvar no Banco de Dados: **Horário**, **Nome e o "Relative Path" onde o arquivo for salvo**, e o **IP** do request.
- [ ] Ajustar CORS

## Opcional
- [ ] Interface gráfica
- [ ] Configuraçao de usuários