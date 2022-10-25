from models.candidato import Candidato
from repos.repoCandidato import RepoCandidato

class DriverCandidato():
    def __init__(self):
        self._repo_candidato = RepoCandidato()

###############LIST CANDIDATO################
    def list_candidato(self):
        data = self._repo_candidato.findAll()
        return data

###############CREATE CANDIDATO################
    def create_candidato(self,input):
        _candidato = Candidato(input)
        return self._repo_candidato.save(_candidato)

###############DELETE CANDIDATO################
    def delete_candidato(self,id):
        return self._repo_candidato.delete(id)
  
###############UPDATE CANDIDATO################
    def update_candidato(self,id,input):
        _candidato_db = self._repo_candidato.findById(id)
        _candidato_obj = Candidato(_candidato_db)
        _candidato_obj.Nombre = input["Nombre"]
        _candidato_obj.Apellido = input["Apellido"]
        _candidato_obj.Documento = input["Documento"]
        _candidato_obj.Genero = input["Genero"]
        _candidato_obj.Corporacion = input["Corporacion"]
        _candidato_obj.Departamento = input["Departamento"]
        _candidato_obj.Municipio = input["Municipio"]
        _candidato_obj.Partido = input["Partido"]

        return self._repo_candidato.save(_candidato_obj)




