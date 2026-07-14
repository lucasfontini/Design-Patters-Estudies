

from authorization_decorator import auth

@auth
def login(username:str):
    """
    Simple doc string
    
    """
    print(f"Welcome {username}")



login("lucas")

