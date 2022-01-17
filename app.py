from datetime import datetime

from flask import Flask, request, Response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask import Flask, request, Response, render_template, make_response

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
ma = Marshmallow(app)

from db_models import *
from helper import insert_user, get_users,logs_maker,error_logs_maker

db.create_all()


@app.route('/', methods=['GET'])
def return_home(error=""):
    """
    muestra el formulario para insertar usuarios y la lista de estos
    :return:
    """
    users = get_users()
    return make_response(render_template("index.html",users=users,error=error), 200)


@app.route('/', methods=['POST'])
def create_user_controller():
    """
    este metodo toma la info de un usuario, la ingresa a la base de datos y almacena en el log
    :return:
    """
    json_data = request.form
    response = insert_user(json_data)

    if "OK" in response["mensaje"]:
        logs_maker(json_data)
        return return_home()
    else:
        error_logs_maker(response['mensaje'])
      #  return make_response(render_template("index.html",error=response), 200)
        return return_home("response")
