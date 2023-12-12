from Futbolista import FutbolistaArgentino
from Futbolista import FutbolistaBrasil
from Futbolista import Club, ClubBarrio

def main():

    barcelona:Club = Club(nombre="Barcelona", lugar="Sevilla")
    sacachispas:ClubBarrio = ClubBarrio(nombre="Sacachispas")

    alvarez:FutbolistaArgentino = FutbolistaArgentino(
        nombre="Julian"
        ,   Habilidades = ["tiro","cabezazo"]
        ,   list_club = []
    )
    print(alvarez)
    alvarez.get_nombre()
    alvarez.agregar_super_tiro("Tiro de la araña")
    alvarez.agregar_cabezazo("Mega cabezon")

    alvarez.mostrar_habilidades()

    alvarez.insert_club(barcelona)
    alvarez.insert_club_barrio(sacachispas)

    alvarez.mostrar_clubs()

#    pele:FutbolistaBrasil = FutbolistaBrasil(nombre="Pele")
#    pele.get_nombre()

if __name__ == "__main__":
    main()
