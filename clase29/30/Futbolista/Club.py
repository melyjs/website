class Club:
    def __init__(self,**kwargs):
        self.nombre = kwargs.get("nombre")
        self.lugar = kwargs.get("lugar","barrio")

    def mostrar_definicion(self):
        return f"""
        Soy el club: {self.nombre}
        Estoy en: {self.lugar}
        """

class ClubReal(Club):
    pass

class ClubBarrio(Club):
    pass
       
class ListClub:
    def __init__(self,**kwargs):
        self.list_club:list[Club] = kwargs.get("clubes",[])

    def insert_club(self,club:ClubReal)->None:
        self.list_club.append(club)

    def insert_club_barrio(self,club_barrio:ClubBarrio):
        self.list_club.append(club_barrio)

        