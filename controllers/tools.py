def check_db(db_user:(list|None)):
    if db_user is None:
        print("La base de datos no existe")
        return False
    
    return True