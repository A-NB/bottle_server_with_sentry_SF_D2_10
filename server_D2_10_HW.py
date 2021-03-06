import os
# from decouple import config
import sentry_sdk
from bottle import Bottle
from sentry_sdk.integrations.bottle import BottleIntegration

# key = config('key', default='')
# project_id = config('project_id', default='')    

sentry_sdk.init(
    #dsn=f"https://{key}@sentry.io/{project_id}",
    dsn=os.environ['SENTRY_DSN'],
    integrations=[BottleIntegration()]
)

app = Bottle()

@app.route('/')
def index():
    return  '''<!doctype html>
				<html lang="en">
                <head>
                    <title>Сайт на bottle</title>
                </head>
                <body>
                    <h1 style="text-align:center">Вас приветствует главная страница сайта!</h1>\n'''

@app.route('/success')
def page_succes():
    return  '''<h2>This is a success! Status 200</h2>
               <span>Это Вы удачно зашли!</span>'''

@app.route('/fail')
def page_fail():
    raise RuntimeError('Это провал. Вы ошиблись номером, дружище... Вы ошиблись...')
    return

if os.environ.get("APP_LOCATION") == "heroku":
    app.run(
				host="0.0.0.0",
				port=int(os.environ.get("PORT", 5000)),
				server="gunicorn",
				workers=3,
				)
else:
    app.run(host="localhost", port=8080, debug=True)