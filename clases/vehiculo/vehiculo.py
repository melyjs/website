def nombre_vehiculo(nombre,cls=None):
    if nombre:
        return nombre
    cls.nombre_vehiculo:str = input("Ingrese nombre del vehiculo: ")

class Vehiculo:
    _tipo_vehiculo:str = "auto"
    _cantidad_ruedas:int = 4 

    def __init__(self,**kwargs):
        print(kwargs)
        self.ruedas:int = kwargs["ruedas"]
        self.motor:str = kwargs["motor"]
        self.numero_motor:str = kwargs["numero_motor"] 
        self.nombre_vehiculo:str = kwargs.get("nombre_vehiculo", None)
        
        self.__nombramiento()

    def __nombramiento(self):
        nombre_vehiculo(self.nombre_vehiculo, self)

    def cantidad_ruedas(self):
        print(f"El vehiculo tiene {self._cantidad_ruedas} ruedas")

    def __str__(self):
        return f"""
            El {self._tipo_vehiculo}:
            Nombre del vehiculo: {self.nombre_vehiculo}
            Cantidad de ruedas: {self.ruedas}
            Numero de motor: {self.numero_motor}
            Tipo de motor: {self.motor}
        """
    
    def to_string(self):
        return f"""
            El {self._tipo_vehiculo}:
            Nombre del vehiculo: {self.nombre_vehiculo}
            Cantidad de ruedas: {self.ruedas}
            Numero de motor: {self.numero_motor}
            Tipo de motor: {self.motor}
            {'-'*50}
        """