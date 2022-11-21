from flask import Flask
from flask import request
from flask import jsonify
from waitress import serve

from flask_jwt_extended import create_access_token, verify_jwt_in_request
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

import requests
import json
import datetime
import re


app = Flask(__name__)
# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "1234"  # Change this!
jwt = JWTManager(app)

@app.route("/login", methods=["POST"])
def inicio_sesion():
    datosEntrada=request.get_json()
    config=cargar_configuracion()
    headers={"Content-Type":'application/json; charset=utf8'}
    print(config["url-ms-usuarios"]+ "/usuarios/login")
    respuesta=requests.post(config["url-ms-usuarios"]+"/usuarios/login",json=datosEntrada,headers=headers)
    print(respuesta.status_code)
    print(jsonify(respuesta.json()))

    if(respuesta.status_code==200):
        expiration_time_token = datetime.timedelta(60 * 60)
        access_token=create_access_token(identity=respuesta.json(),expires_delta=expiration_time_token)
        return jsonify({"access_token":access_token})
    else:
        return jsonify({"mensaje":"Por favor verifique su correo o su contraseña"})

@app.before_request
def verificar_peticion():
    print("callback running ...")
    endPoint = limpiarURL(request.path)
    excludedRoutes = ["/login"]

    if excludedRoutes.__contains__(request.path):
        print("ruta excluida ", request.path)
        pass
    elif verify_jwt_in_request():
        usuario = get_jwt_identity()
        print(usuario["rol"]["_id"])
        if usuario["rol"] is not None:
            tienePermiso = validarPermiso(endPoint, request.method, usuario["rol"]["_id"])
            if not tienePermiso:
                return jsonify({"message": "Permission denied"}), 401
        else:
            return jsonify({"message": "Permission denied"}), 401

def limpiarURL(url):
    partes = url.split("/")
    for laParte in partes:
        if re.search('\\d', laParte):
            url = url.replace(laParte, "?")
    return url


def validarPermiso(endPoint, metodo, _id_Rol):
    config = cargar_configuracion()
    url = config["url-ms-usuarios"] + "/rolpermiso/" + str(_id_Rol)
    print(url)
    print(endPoint)
    print(metodo)
    tienePermiso = False
    headers = {"Content-Type": "application/json; charset=utf-8"}
    body = {
        "url": endPoint,
        "metodo": metodo
    }
    response = requests.post(url, json=body, headers=headers)
    try:
        data = response.json()
        if ("_id" in data):
            tienePermiso = True
        print(tienePermiso)
    except:
        pass
    return tienePermiso

#=============================CONSULTAS============================


#_____________________________MESAS________________________________

@app.route('/mesas', methods=["GET"])
def consulta_mesas():
    #http://localhost:9000/mesas
    headers = {"Content-Type": "application/json; charset=utf8"}
    configuracion = cargar_configuracion()
    url = configuracion["url-ms-resultados"] + "/mesas"
    respuesta = requests.get(url,headers=headers)
    json = respuesta.json()
    return jsonify(json)

@app.route('/mesas/crear', methods=["POST"])
def crear_mesa():
    # http://localhost:9000/mesas
    datosEntrada = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf8"}
    configuracion = cargar_configuracion()
    url = configuracion["url-ms-resultados"] + "/mesas"
    respuesta = requests.post(url,json=datosEntrada,headers=headers)
    json = respuesta.json()
    return jsonify(json)

@app.route('/mesas/eliminar/<string:id>', methods=["DELETE"])
def eliminar_mesa(id):
    # http://localhost:9000/mesas/_id
    headers = {"Content-Type": "application/json; charset=utf8"}
    configuracion = cargar_configuracion()
    url = configuracion["url-ms-resultados"] + "/mesas/"+id
    respuesta = requests.delete(url,headers=headers)
    json = respuesta.json()
    return jsonify(json)

@app.route('/mesas/<string:id>', methods=["PUT"])
def modificar_mesa(id):
    # http://localhost:9000/mesas/id
    datosEntrada = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf8"}
    configuracion = cargar_configuracion()
    url = configuracion["url-ms-resultados"] + "/mesas/"+id
    respuesta = requests.put(url,json=datosEntrada,headers=headers)
    json = respuesta.json()
    return jsonify(json)


#________________________________CANDIDATOS_______________________

@app.route('/candidatos', methods=["GET"])
def consulta_candidatos():
    #http://localhost:9000/candidatos
    headers = {"Content-Type": "application/json; charset=utf8"}
    configuracion = cargar_configuracion()
    url = configuracion["url-ms-resultados"] + "/candidatos"
    respuesta = requests.get(url,headers=headers)
    json = respuesta.json()
    return jsonify(json)

@app.route('/candidatos/crear', methods=["POST"])
def crear_candidato():
    # http://localhost:9000/candidatos
    datosEntrada = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf8"}
    configuracion = cargar_configuracion()
    url = configuracion["url-ms-resultados"] + "/candidatos"
    respuesta = requests.post(url,json=datosEntrada,headers=headers)
    json = respuesta.json()
    return jsonify(json)

@app.route('/candidatos/eliminar/<string:id>', methods=["DELETE"])
def eliminar_candidato(id):
    # http://localhost:9000/candidatos/_id
    headers = {"Content-Type": "application/json; charset=utf8"}
    configuracion = cargar_configuracion()
    url = configuracion["url-ms-resultados"] + "/candidatos/"+id
    respuesta = requests.delete(url,headers=headers)
    json = respuesta.json()
    return jsonify(json)

@app.route('/candidatos/<string:id>', methods=["PUT"])
def modificar_candidatos(id):
    # http://localhost:9000/candidatos/_id
    datosEntrada = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf8"}
    configuracion = cargar_configuracion()
    url = configuracion["url-ms-resultados"] + "/candidatos/"+id
    respuesta = requests.put(url,json=datosEntrada,headers=headers)
    json = respuesta.json()
    return jsonify(json)

#________________________________PARTIDOS_______________________

@app.route('/partidos', methods=["GET"])
def consulta_partidos():
    #http://localhost:9000/partidos
    headers = {"Content-Type": "application/json; charset=utf8"}
    configuracion = cargar_configuracion()
    url = configuracion["url-ms-resultados"] + "/partidos"
    respuesta = requests.get(url,headers=headers)
    json = respuesta.json()
    return jsonify(json)

@app.route('/partidos/crear', methods=["POST"])
def crear_partido():
    # http://localhost:9000/partidos
    datosEntrada = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf8"}
    configuracion = cargar_configuracion()
    url = configuracion["url-ms-resultados"] + "/partidos"
    respuesta = requests.post(url,json=datosEntrada,headers=headers)
    json = respuesta.json()
    return jsonify(json)

@app.route('/partidos/eliminar/<string:id>', methods=["DELETE"])
def eliminar_partido(id):
    # http://localhost:9000/partidos/_id
    headers = {"Content-Type": "application/json; charset=utf8"}
    configuracion = cargar_configuracion()
    url = configuracion["url-ms-resultados"] + "/partidos/"+id
    respuesta = requests.delete(url,headers=headers)
    json = respuesta.json()
    return jsonify(json)

@app.route('/partidos/<string:id>', methods=["PUT"])
def modificar_partidos(id):
    # http://localhost:9000/candidatos/_id
    datosEntrada = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf8"}
    configuracion = cargar_configuracion()
    url = configuracion["url-ms-resultados"] + "/partidos/"+id
    respuesta = requests.put(url,json=datosEntrada,headers=headers)
    json = respuesta.json()
    return jsonify(json)

#________________________________RESULTADOS_______________________

@app.route('/resultados', methods=["GET"])
def consulta_resultados():
    #http://localhost:9000/resultados
    headers = {"Content-Type": "application/json; charset=utf8"}
    configuracion = cargar_configuracion()
    url = configuracion["url-ms-resultados"] + "/resultados"
    respuesta = requests.get(url,headers=headers)
    json = respuesta.json()
    return jsonify(json)

@app.route('/resultados/crear', methods=["POST"])
def crear_resultado():
    # http://localhost:9000/resultados
    datosEntrada = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf8"}
    configuracion = cargar_configuracion()
    url = configuracion["url-ms-resultados"] + "/resultados"
    respuesta = requests.post(url,json=datosEntrada,headers=headers)
    json = respuesta.json()
    return jsonify(json)

@app.route('/resultados/<string:id>', methods=["PUT"])
def modificar_resultados(id):
    # http://localhost:9000/candidatos/_id
    datosEntrada = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf8"}
    configuracion = cargar_configuracion()
    url = configuracion["url-ms-resultados"] + "/resultados/"+id
    respuesta = requests.put(url,json=datosEntrada,headers=headers)
    json = respuesta.json()
    return jsonify(json)

#________________________________PERMISOS_______________________

@app.route('/permisos', methods=["GET"])
def consulta_permisos():
    #http://localhost:9999/permisos
    headers = {"Content-Type": "application/json; charset=utf8"}
    configuracion = cargar_configuracion()
    url = configuracion["url-ms-usuarios"] + "/permisos"
    respuesta = requests.get(url,headers=headers)
    json = respuesta.json()
    return jsonify(json)

@app.route('/permisos/crear', methods=["POST"])
def crear_permiso():
    # http://localhost:9999/permisos/crear
    datosEntrada = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf8"}
    configuracion = cargar_configuracion()
    url = configuracion["url-ms-usuarios"] + "/permisos/crear"
    respuesta = requests.post(url,json=datosEntrada,headers=headers)
    json = respuesta.json()
    return jsonify(json)

@app.route('/permisos/eliminar/<string:id>', methods=["DELETE"])
def eliminar_permiso(id):
    # http://localhost:9999/permisos/eliminar/_id
    headers = {"Content-Type": "application/json; charset=utf8"}
    configuracion = cargar_configuracion()
    url = configuracion["url-ms-usuarios"] + "/permisos/eliminar/"+id
    print(url)
    respuesta = requests.delete(url, headers=headers)
    json = respuesta.json()
    return jsonify(json)

#________________________________ROLES__________________________

@app.route('/rol', methods=["GET"])
def consulta_roles():
    #http://localhost:9999/rol
    headers = {"Content-Type": "application/json; charset=utf8"}
    configuracion = cargar_configuracion()
    url = configuracion["url-ms-usuarios"] + "/rol"
    respuesta = requests.get(url,headers=headers)
    json = respuesta.json()
    return jsonify(json)

@app.route('/rol/crear', methods=["POST"])
def crear_rol():
    # http://localhost:9999/rol/crear
    datosEntrada = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf8"}
    configuracion = cargar_configuracion()
    url = configuracion["url-ms-usuarios"] + "/rol/crear"
    respuesta = requests.post(url,json=datosEntrada,headers=headers)
    json = respuesta.json()
    return jsonify(json)

@app.route('/rol/eliminar/<string:id>', methods=["DELETE"])
def eliminar_rol(id):
    # http://localhost:9999/rol/eliminar/_id
    headers = {"Content-Type": "application/json; charset=utf8"}
    configuracion = cargar_configuracion()
    url = configuracion["url-ms-usuarios"] + "/rol/eliminar/"+ id
    print(url)
    respuesta = requests.delete(url,headers=headers)
    json = respuesta.json()
    print(json)
    return jsonify(json)

#________________________________USUARIOS_______________________

@app.route('/usuarios', methods=["GET"])
def consulta_usuarios():
    #http://localhost:9999/usuarios
    headers = {"Content-Type": "application/json; charset=utf8"}
    configuracion = cargar_configuracion()
    url = configuracion["url-ms-usuarios"] + "/usuarios"
    respuesta = requests.get(url,headers=headers)
    json = respuesta.json()
    return jsonify(json)

@app.route('/usuarios/crear', methods=["POST"])
def crear_usuario():
    # http://localhost:9999/usuarios/crear
    datosEntrada = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf8"}
    configuracion = cargar_configuracion()
    url = configuracion["url-ms-usuarios"] + "/usuarios/crear"
    respuesta = requests.post(url,json=datosEntrada,headers=headers)
    json = respuesta.json()
    return jsonify(json)

#________________________________ROLES-PERMISOS_______________________

@app.route('/rolpermiso', methods=["GET"])
def consulta_rolpermiso():
    #http://localhost:9999/rolpermiso
    headers = {"Content-Type": "application/json; charset=utf8"}
    configuracion = cargar_configuracion()
    url = configuracion["url-ms-usuarios"] + "/rolpermiso"
    respuesta = requests.get(url,headers=headers)
    json = respuesta.json()
    return jsonify(json)

@app.route('/rolpermiso/crear', methods=["POST"])
def crear_rolpermiso():
    # http://localhost:9999/rolpermiso/crear
    datosEntrada = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf8"}
    configuracion = cargar_configuracion()
    url = configuracion["url-ms-usuarios"] + "/usuarios/rolpermiso"
    respuesta = requests.post(url,json=datosEntrada,headers=headers)
    json = respuesta.json()
    return jsonify(json)


@app.route('/')
def home():
    print("Path Home")
    return 'API GATEWAY RUNNING!'

def cargar_configuracion():
    with open("config.json") as archivo:
        datos_configuracion = json.load(archivo)
    return datos_configuracion


if __name__ == '__main__':
    dataConfig = cargar_configuracion()
    print("Server running : " + "http://" + dataConfig["url-api-gateway"] + ":" + str(dataConfig["port-api-gateway"]))
    serve(app, host=dataConfig["url-api-gateway"], port=dataConfig["port-api-gateway"])
