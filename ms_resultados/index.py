from flask import Flask
from flask import request
from flask import jsonify
from waitress import serve
import json

from drivers.driverMesa import DriverMesa
from drivers.driverCandidato import DriverCandidato
from drivers.driverPartido import DriverPartido
from drivers.driverResultado import DriverResultado

democracy_app = Flask(__name__)

_driver_mesa = DriverMesa()
_driver_candidato = DriverCandidato()
_driver_partido = DriverPartido()
_driver_resultado = DriverResultado()

"""___________________PATH PARA ADMINISTRAR MESAS_______________"""
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

#UPDATE - ACTUALIZAR MESAS
@democracy_app.route('/mesas/<string:id>',methods=['PUT'])
def update_mesa(id):
    input = request.get_json()
    output = _driver_mesa.update_mesa(id,input)
    return jsonify(output)

"""___________________PATH PARA ADMINISTRAR CANDIDATOS_______________"""
#GET - LISTAR CANDIDATOS 
@democracy_app.route('/candidatos',methods=['GET'])
def get_candidatos():
    output = _driver_candidato.list_candidato()
    return jsonify(output)

#POST - CREAR CANDIDATOS
@democracy_app.route('/candidatos',methods=['POST'])
def create_candidato():
    input = request.get_json()
    output = _driver_candidato.create_candidato(input)
    return jsonify(output)

#DELETE - ELIMINAR CANDIDATOS
@democracy_app.route('/candidatos/<string:id>',methods=['DELETE'])
def delete_candidato(id):
    output = _driver_candidato.delete_candidato(id)
    return jsonify(output)

#UPDATE - ACTUALIZAR CANDIDATOS
@democracy_app.route('/candidatos/<string:id>',methods=['PUT'])
def update_candidato(id):
    input = request.get_json()
    output = _driver_candidato.update_candidato(id,input)
    return jsonify(output)    


#UPDATE - ASIGNAR PARTIDO A CANDIDATOS
@democracy_app.route("/candidatos/<string:id>/partido/<string:id_partido>", methods=['PUT'])
def asignarPartidoaCandidato(id,id_partido):
    json=_driver_candidato.assign_partido(id,id_partido)
    return jsonify(json)

"""___________________PATH PARA ADMINISTRAR PARTIDOS_______________"""

#GET - LISTAR PARTIDOS 
@democracy_app.route('/partidos',methods=['GET'])
def get_partidos():
    output = _driver_partido.list_partido()
    return jsonify(output)

#POST - CREAR PARTIDOS
@democracy_app.route('/partidos',methods=['POST'])
def create_partido():
    input = request.get_json()
    output = _driver_partido.create_partido(input)
    return jsonify(output)

#DELETE - ELIMINAR PARTIDOS
@democracy_app.route('/partidos/<string:id>',methods=['DELETE'])
def delete_partido(id):
    output = _driver_partido.delete_partido(id)
    return jsonify(output)

#UPDATE - ACTUALIZAR PARTIDOS
@democracy_app.route('/partidos/<string:id>',methods=['PUT'])
def update_partido(id):
    input = request.get_json()
    output = _driver_partido.update_partido(id,input)
    return jsonify(output)    


"""___________________PATH PARA ADMINISTRAR RESULTADOS_______________"""

#GET - LISTAR RESULTADOS 
@democracy_app.route('/resultados',methods=['GET'])
def get_resultado():
    output = _driver_resultado.index()
    return jsonify(output)
    
@democracy_app.route('/resultados/<string:id>',methods=['GET'])
def get_resultados(id):
    output = _driver_resultado.show(id)
    return jsonify(output)

#POST - CREAR RESULTADOS
@democracy_app.route('/resultados/mesa/<string:id_mesa>/candidato/<string:id_candidato>',methods=['POST'])
def create_resultados(id_mesa,id_candidato):
    input = request.get_json()
    output = _driver_resultado.create_resultado(input,id_mesa,id_candidato)
    return jsonify(output)

#DELETE - ELIMINAR RESULTADOS
@democracy_app.route('/resultados/<string:id>',methods=['DELETE'])
def delete_resultado(id):
    output = _driver_resultado.delete_resultado(id)
    return jsonify(output)

#UPDATE - ACTUALIZAR RESULTADOS
@democracy_app.route('/resultados/<string:id_resultado>',methods=['PUT'])
def update_resultado(id_resultado):
    input = request.get_json()
    output = _driver_resultado.update_resultado(id_resultado,input)
    return jsonify(output)    

@democracy_app.route('/resultados',methods=['POST'])
def filtrar_candidato():
    input=request.get_json()
    output = _driver_resultado.filtrarCandidato(input)
    return jsonify(output)
    

def configuration():
    with open("config.json") as config:
        config_data = json.load(config)
    return config_data


if __name__ == '__main__':
    config_data = configuration()

    print("(●'◡'●) Up and runnig (～￣▽￣)～")
    serve(democracy_app, host=config_data["host"], port=config_data["port"])
    democracy_app.run()

