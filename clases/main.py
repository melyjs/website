from vehiculo import Vehiculo
from vehiculo import Manager
#xsara:Vehiculo = Vehiculo()
def main():

    mitsu:Vehiculo = Vehiculo(
    ruedas = 4,
    motor = "V16",
    numero_motor = "1672993"
    )

    xsara:Vehiculo = Vehiculo(
    ruedas = 4,
    motor = "V8",
    numero_motor = 2156312
    )

    local_database:Manager = Manager()
    local_database.insertar_vehiculo(mitsu)
    local_database.insertar_vehiculo(xsara)

    local_database.mostrar_vehiculos()
    local_database.save_vehiculos()

if __name__ == '__main__':
    main()