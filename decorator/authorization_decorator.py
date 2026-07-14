from functools import wraps

def auth(fun):
    
    @wraps(fun) # keep the properties of this funcion received 
    def read(*args, **kwargs):
        with open('cred.txt' , 'r') as file:
            permission = file.read().strip()
            if not permission:
                raise PermissionError("No permissions")
            if "1" in permission:
                print("authorized")

                return fun(*args, **kwargs) #retorna a funcao para ser processada depois de tudo isso 
            else:
                raise Exception("Not authorized")
    return read


# best way to keep the properties of func, use wrap 

# from functools import wraps

# def auth(fun):

#     @wraps(fun)
#     def read(*args, **kwargs):
#         with open("cred.txt", "r") as file:
#             permission = file.read().strip()

#         if not permission:
#             raise PermissionError("No permissions")

#         if permission == "1":
#             print("authorized")
#             return fun(*args, **kwargs)
#         else:
#             raise PermissionError("Not authorized")

#     return read


# from functools import wraps
# from datetime import datetime

# def log_router(func):

#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f"[{datetime.now()}] Iniciando {func.__name__}")
#         print(f"Conectando ao roteador {args[0]}")

#         try:
#             resultado = func(*args, **kwargs)
#             print(f"[{datetime.now()}] Finalizado com sucesso")
#             return resultado

#         except Exception as e:
#             print(f"Erro: {e}")
#             raise

#     return wrapper


# @log_router
# def get_hostname(ip):
#     print("Conectado ao roteador")
#     print("Executando: show running-config | include hostname")
#     return "hostname R1"


# hostname = get_hostname("192.168.1.1")
# print(hostname)