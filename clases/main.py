class Vehiculo:
    _tipo_vehiculo:str = "auto"
    _cantidad_ruedas:int = 4 

    def cantidad_ruedas(self):
        print(f"El vehiculo tiene {self._cantidad_ruedas} ruedas")

    def __srt__(self):
        return f"""
xsara:Vehiculo = Vehiculo()

print(xsara._tipo_vehiculo)
xsara.cantidad_ruedas()

print(xsara)