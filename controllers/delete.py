from .tools import check_db

def delete_user(dni:int,db_user:list=None) -> None:
    if not check_db(db_user):
        return None
    
#    return [
#        user
#        for user in db_user
#        if user["dni"] == dni
#    ]

    for index,user in enumerate(db_user):
        if user["dni"] == dni:
            db_user.pop(index)