from models.resultado import Resultado
from models.partido import Partido
from models.candidato import Candidato
from models.mesa import Mesa
from repos.repoMesa import RepoMesa
from repos.repoPartido import RepoPartido
from repos.repoResultado import RepoResultado
from repos.repoCandidato import RepoCandidato


class DriverResultado():
    def __init__(self):
        self._repo_resultado = RepoResultado()
        self._repo_partido = RepoPartido()
        self._repo_candidato = RepoCandidato()
        self._repo_mesa = RepoMesa()
    
    def index(self):
        return self._repo_resultado.findAll()

###############ASIGNACION CANDIDATO Y MESA A RESULTADO###############3
    def create_resultado(self,input,id_mesa,id_candidato):
        _resultado = Resultado(input)
        elCandidato=Candidato(self._repo_candidato.findById(id_candidato))
        laMesa=Mesa(self._repo_mesa.findById(id_mesa))
        _resultado.candidato=elCandidato
        _resultado.mesa=laMesa
        return self._repo_resultado.save(_resultado)

    def show(self,id):
        elResultado=Resultado(self._repo_resultado.findById(id))
        return elResultado.__dict__

    
###############MODIFICACION DE RESULTADOS (CANDIDATO, MESA)################
    def update_resultado(self,id,input):
        elResultado=Resultado(self._repo_resultado.findById(id))
        elResultado.Votos=input["Votos"]
        return self._repo_resultado.save(elResultado)



###############ELIMINACION DE RESULTADOS################
    
    def delete_resultado(self,id):
        return self._repo_resultado.delete(id)


###############CONSULTA DE RESULTADOS################
     
    def ListarVotosporMesa(self,id_mesa):
        return self._repo_resultado.getVotosporMesa(id_mesa)

    def ListarVotosporCandidato(self,id_candidato):
        return self._repo_resultado.getVotosporCandidato(id_candidato) 

    def TotalVotosCandidato(self):
        return self._repo_resultado.getTotalVotosCandidato() 

    def TotalVotosMesa(self):
        return self._repo_resultado.getTotalVotosMesa()     

    def Prueba(self):
        return self._repo_resultado.getprueba()
        getprueba 


    