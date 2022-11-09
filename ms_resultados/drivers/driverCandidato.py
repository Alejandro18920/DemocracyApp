from models.candidato import Candidato
from models.partido import Partido
from repos.repoCandidato import RepoCandidato
from repos.repoPartido import RepoPartido

class DriverCandidato():
    def __init__(self):
        self._repo_candidato = RepoCandidato()
        self._repo_partido = RepoPartido()

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
        _candidato_obj.Resolucion = input["Resolucion"]
               
        return self._repo_candidato.save(_candidato_obj)

#############ASIGNACION DE PARTIDO A CANDIDATO########################
    def assign_partido(self,id,id_partido):
        candidatoActual=Candidato(self._repo_candidato.findById(id))
        partidoActual=Partido(self._repo_partido.findById(id_partido))
        candidatoActual.Partido=partidoActual
        return self._repo_candidato.save(candidatoActual)





