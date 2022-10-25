from abc import ABCMeta
class Abstract():
    def __init__(self,datos):
        for key, value in datos.items():
            setattr(self,key,value)
            print(f"Se ha creado un objeto con llave {key} y valor {value}")