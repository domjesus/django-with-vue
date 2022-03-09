# vue-django-webpack-boilerplate

Aplicação Web com Backend Django (Python)
Frontend com Vue funcionando juntamente com esquema de templates padrão do Django

O vue (com vuerouter) carrega na rota /vue, sendo que as demais rotas são gerenciadas normalmente pelo Django

## Faça o clone do projeto

git clone https://github.com/domjesus/django-with-vue.git .

# Instale o Vue e suas dependências

npm install OU yarn install
npm run dev OU yarn dev
O frontend sobe no endereço http://localhost:8080

# Instale o Django

Para instalar o Django e suas dependências rode o comanod

pip install -r requirements.txt

# Inicie o servidor

py manage.py runserver OU sh server.sh
O backend (e aplicação Django) sobe na porta 8000 do localhost

# Ready to deploy

Para deploy no heroku siga os passos
Baixe o heroku cli

heroku apps:create name_of_app

#Gere uma nova SECRET_KEY
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

Copie o conteúdo do print e cole nas variáveis de ambiente de seu SO sob a chave APP_KEY.

Para esta chave refletir no heroku dê o comando
heroku config:set APP_KEY=content_of_the_key

git push heroku master

And enjoy.
