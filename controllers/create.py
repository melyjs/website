from .tools import check_db
from .read import read_users
from database.generador_users import create_user as cu
from database.generador_users import generate_german_email

def create_user(dni:int, db_user:list=None) -> None:
    if not check_db(db_user):
        return None

    _user = read_users(dni,db_user)

    if len(_user) == 0:
        name:str = input("Ingrese el nombre de usuario: \n")
        email:str = generate_german_email(name)
        _user = cu(name,email,dni)
        db_user.append(_user)
        return
    
    print(
        f"""
        El usuario es
        {_user["nombre"]}
        {_user["email"]}
        """
    )