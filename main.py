from database.generador_users import create_database
from controllers import delete_user
from controllers import read_users
from controllers import create_user
from controllers import update_user

db_user:list[dict] = create_database()

print(db_user)

def main():
    print("Gracias por usar nuestro gestor de usuarios")
    choice_crud:str = input("""
    Ingrese la opcion de operación que quiere realizar
    Opciones:
                - a Leer
                - b Crear
                - c Editar
                - d Borrar
    """)
    if choice_crud == "a":
        _dni:int = input("Ingrese el dni del usuario:\n")
        read_users(int(_dni),db_user)
        return
    if choice_crud == "b":
        _dni:int = input("Ingrese el dni del usuario:\n")
        create_user(int(_dni),db_user)
        print (db_user)
        return
    if choice_crud == "c":
        _dni:int = int(input("Ingrese el dni del usuario:\n"))
        update_user(_dni,db_user)
        print (db_user)
        return
    if choice_crud == "d":
        _dni:int = input("Ingrese el dni del usuario:\n")
        print(len(db_user))
        delete_user(int(_dni),db_user)
        print(len(db_user))

main()