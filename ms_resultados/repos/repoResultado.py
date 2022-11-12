from models.resultado import Resultado
from repos.interface import Interface
from bson import ObjectId

class RepoResultado(Interface[Resultado]):
    
    ########## VOTOS POR MESA #######
    def getVotosporMesa(self,id_mesa):
        theQuery={"mesa.$id":ObjectId(id_mesa)}
        return self.query(theQuery)

    ########## VOTOS POR CANDIDATO #######
    def getVotosporCandidato(self, id_candidato):
        theQuery={"candidato.$id":ObjectId(id_candidato)}
        return self.query(theQuery)
    
    ########## VOTOS POR PARTIDO #######
    def getVotosporPartido(self, id_partido):
        theQuery={"partido.$id":ObjectId(id_partido)}
        return self.query(theQuery)
    
    ########## TOTAL VOTOS POR CANDIDATO#######
    def getTotalVotosCandidato(self):
        query={
                "$group": {
                    "_id": "$candidato", 
                    "Total_votaciones_por_id": {
                        "$sum": "$Votos"
                        }
                    }
                }
        print(query)
        pipeline=[query]
        return self.queryAggregation(pipeline)


 ########## TOTAL VOTOS POR MESA#######
    def getTotalVotosMesa(self):
        query={
                "$group": {
                    "_id": "$mesa", 
                    "Total_votaciones_por_id": {
                        "$sum": "$Votos"
                        }
                    }
                }
        print(query)
        pipeline=[query]
        return self.queryAggregation(pipeline)


    def getprueba(self):
        query={
            "$lookup":{
                "from": "partido",
                "localField": "candidato",
                "foreignField": "Nombre",
                "as": "Partidos"
                }
        }
        pipeline=[query]
        return self.queryAggregation(pipeline)