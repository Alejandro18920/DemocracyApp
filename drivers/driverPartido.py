from models.partido import Partido
from repos.repoPartido import RepoPartido

class DriverPartido():
    def __init__(self):
        self._repo_partido = RepoPartido()

###############LIST PARTIDO################
    def list_partido(self):
        data = self._repo_partido.findAll()
        return data

###############CREATE PARTIDO################
    def create_partido(self,input):
        _partido = Partido(input)
        return self._repo_partido.save(_partido)

###############DELETE PARTIDO################
    def delete_partido(self,id):
        return self._repo_partido.delete(id)
  
###############UPDATE PARTIDO################
    def update_partido(self,id,input):
        _partido_db = self._repo_partido.findById(id)
        _partido_obj = Partido(_partido_db)
        _partido_obj.Nombre = input["Nombre"]
        _partido_obj.Nit = input["Nit"]
        _partido_obj.Resolucion = input["Resolucion"]
        _partido_obj.Direccion = input["Direccion"]
        _partido_obj.ciudadSede = input["ciudadSede"]
        _partido_obj.Telefono = input["Telefono"]
        _partido_obj.email = input["email"]
       

        return self._repo_partido.save(_partido_obj)




