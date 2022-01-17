from datetime import datetime

from db_models import users
from app import db

def get_users():
    try:
        query = db.session.query(users).all()
        return query

    except Exception as E:
        print(f"no se pudo hacer la consulta: {E}")
        return  ""

def insert_user(request_data):
    """a json is obtained with fields and his values, with this is instancied variables that will be inserted in the database"""
    if request_data['full_name']  =="" or request_data['email'] =="" or request_data['city']=="":
        error = {"mensaje":"hay un campo vacio"}
        return error
    else:
        full_name = request_data['full_name']
        email = request_data['email']
        city = request_data['city']

        try:
            new_user = users(full_name,email,city)
            db.session.add(new_user)
            db.session.commit()
            message = {"mensaje": "OK, se inserto el usuario correctamente"}
            return message

        except Exception as e:
            message = {"mensaje":"ocurrio el siguiente error:"+str(e)}

            return message

def logs_maker(json_data):
    """
    este metodo escribe los logs en un archivo de texto
    :param json_data:
    :return:
    """
    f = open("logs.txt", 'a')
    now = datetime.now()
    date = str(now.strftime("%Y-%m-%d %H:%M:%S"))
    mensaje = f"\n{date}\n se insertaron los datos:  " \
              f" {str(json_data['full_name'])}" \
              f"\n {str(json_data['email'])}" \
              f"\n {str(json_data['city'])}" \
              f"\n --------------------------------------------------------------------------------"
    f.write(mensaje)
    f.close()

def error_logs_maker(message):
    f = open("logs.txt", 'a')
    now = datetime.now()
    date = str(now.strftime("%Y-%m-%d %H:%M:%S"))
    mensaje = f"\n ocurrio el siguiente error{message} \n"
    f.write(mensaje)
    f.close()