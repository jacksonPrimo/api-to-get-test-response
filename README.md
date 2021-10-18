## :computer: Sobre o Projeto 
Esta é uma api desenvolvida em python com a finalidade de receber uma imagem de teste impresso e por meio da sua análise exibir a pontuação da mesma. O teste consiste em marcar uma forma retangular de forma completa ou apenas sua metade, cada uma representando uma escolha e portanto possuindo um valor distinto
# Como usar
### use este comando para criar seu ambiente virtual
```
$ virtualenv 'nome_do_seu_ambiente_virtual'
```
### use o comando a seguir para ativalo
```
$ nome_do_seu_ambiente_virtual/Scripts/activate.ps1
```
### use o comando a seguir para instalar todas as depêndencias necessárias para executar o projeto
```
$ pip install -r requirements.txt
```
### use o comando a seguir para selecionar o arquivo que será usado pelo flask
``` 
$env:FLASK_APP='main.py'
```
### use o comando a seguir para estartar o servidor
```
$ flask run
```