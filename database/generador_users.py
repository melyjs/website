import random

_names:list = [
    "Anna", "Benjamin", "Caroline", "David", "Eva", "Felix", "Greta",
    "Hans", "Isabella", "Jakob", "Klara", "Lukas", "Maria", "Niko",
    "Olivia", "Paul", "Quirin", "Rosa", "Simon", "Theresa", "Ursula",
    "Valentin", "Wilma", "Xaver", "Yvonne", "Zacharias"
]

def generate_german_email(name):
    domains = ["gmail.com", "yahoo.de", "web.de", "t-online.de", "outlook.de"]
    random_domain = random.choice(domains)
    return f"{name.lower()}_{random.randint(100, 999)}@{random_domain}"


_dni:list = [random.randint(50_000_000, 99_000_000) for _ in range(10)]



def create_user(nombre:str = None, email:str = None, dni:int = None) ->(dict):
    if nombre is None  and email is None and dni is None:
        nombre_random:str = random.choice(_names)
        return {
            "nombre":nombre_random,
            "email":generate_german_email(nombre_random),
            "dni":random.choice(_dni)
        }
    return{
        "nombre":nombre,
        "email":email,
        "dni":dni
    }

def create_database(cant_user:int = 10):
    return [
        create_user()
        for _ in range(cant_user)
    ]