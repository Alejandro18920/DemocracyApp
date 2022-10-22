from flask import Flask
from flask import request
from flask import jsonify
from waitress import serve
import json

from drivers.driverMesa import DriverMesa

democracy_app = Flask(__name__)

_driver_mesa = DriverMesa()

"""PATH PARA ADMINISTRAR MESAS"""
#GET - LISTAR MESAS 
@democracy_app.route('/mesas',methods=['GET'])
def get_mesas():
    output = _driver_mesa.list_mesa()
    return jsonify(output)

#POST - CREAR MESAS
@democracy_app.route('/mesas',methods=['POST'])
def create_mesa():
    input = request.get_json()
    output = _driver_mesa.create_mesa(input)
    return jsonify(output)

#DELETE - ELIMINAR MESAS
@democracy_app.route('/mesas/<string:id>',methods=['DELETE'])
def delete_mesa(id):
    output = _driver_mesa.delete_mesa(id)
    return jsonify(output)

#DELETE - ACTUALIZAR MESAS
@democracy_app.route('/mesas/<string:id>',methods=['PUT'])
def update_mesa(id):
    input = request.get_json()
    output = _driver_mesa.update_mesa(id,input)
    return jsonify(output)



"""
#path de prueba
@democracy_app.route('/saludar')
def saludo():
    return("<h1>Hola Wanna be developer</h1>")
    
@democracy_app.route('/')
def home():
    return("<h1>Inicio</h1>")
"""


def configuration():
    with open("config.json") as config:
        config_data = json.load(config)
    return config_data


if __name__ == '__main__':
    config_data = configuration()

    print("(●'◡'●) Up and runnig (～￣▽￣)～")
    serve(democracy_app, host=config_data["host"], port=config_data["port"])
    democracy_app.run()

