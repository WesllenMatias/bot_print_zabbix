# BOT PARA ENVIO DE PRINT DO ZABBIX


## Primeiro execute no seu servidor a instalação dos modulos necessários:

pip install -r requirements.txt

## Segundo crie um arquivo config.py com as variaveis abaixo:

dash='http://seu_zabbix/zabbix'
usr='seu_usuário'
pwd='sua_senha'
tk = "token do seu bot do telegram"
alvo = [id do telegram do alvo, separado por virgula se for + de 1]

## Terceiro tenha instalado em seu servidor o geckodriver:

### Abaixo tem instruções no item 1.3:

https://selenium-python.readthedocs.io/installation.html

## Feito os 3 passos basta configurar no crontab com a frequencia desejada.

Ex: todo dia as 09:00

0 9 * * * /usr/bin/python3 /local/do/clone_do_projeto/bot_telegram.py #Descrição pra vc lembrar o que é