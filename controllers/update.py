from .tools import check_db
from .read import read_users
from .delete import delete_user

def update_user(dni:int, db_user:list=None) -> None:
    if not check_db(db_user):
        return None
    _user:dict = read_users(dni,db_user)

    if _user is None or len(_user) == 0:
        print("Usuario no existente")
        return
    
    key:str = input("Campos parta modificar son: \n*Nombre\n*Email\nEscriba el campo a modificar: ")
    value:str = input ("Valor nuevo: ")

    _user[key] = value

    delete_user(dni,db_user)

    db_user.append(_user)

    print("Usuario actualizado")
