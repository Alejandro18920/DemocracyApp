from models.mesa import Mesa
from repos.repoMesa import RepoMesa

class DriverMesa():
    def __init__(self):
        self._repo_mesa = RepoMesa()

###############LIST MESA################
    def list_mesa(self):
        data = self._repo_mesa.findAll()
        return data

###############CREATE MESA################
    def create_mesa(self,input):
        _mesa = Mesa(input)
        return self._repo_mesa.save(_mesa)

###############DELETE MESA################
    def delete_mesa(self,id):
        return self._repo_mesa.delete(id)
  
###############UPDATE MESA################
    def update_mesa(self,id,input):
        _mesa_db = self._repo_mesa.findById(id)
        _mesa_obj = Mesa(_mesa_db)
        _mesa_obj.municipio=input["Municipio"]
        _mesa_obj.departamento=input["Departamento"]
        _mesa_obj.puesto=input["Puesto"]
        _mesa_obj.numero=input["Numero"]
        _mesa_obj.votantes = input["Votantes"]

        return self._repo_mesa.save(_mesa_obj)




