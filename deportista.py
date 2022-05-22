class Deportista:
    def __init__(self,dep,anos):
        self._deporte=dep
        self._añosPracticando=anos
    def  getDeporte(self) :
        return self._deporte
    def setDeporte(self, nombre) :
        self._deporte = nombre
    def  getAñosPracticando(self) :
        return self._añosPracticando
    def setAñosPracticando(self, sexo) :
        self._añosPracticando = sexo

    