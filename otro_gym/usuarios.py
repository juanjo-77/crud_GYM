
import csv

def cargar_usuarios(archivo):
    usuarios = {}         # Diccionario donde guardaremos usuario → (contraseña, rol)

    with open(archivo, encoding="utf-8") as f:         # Abre el archivo CSV
        reader = csv.reader(f)                         # Crea un lector de líneas CSV
        next(reader)                                   # Saltar encabezado

        for fila in reader:                            # Recorre cada fila del archivo
            usuario, contrasena, rol = fila            # Desempaqueta los 3 campos
            usuarios[usuario] = (contrasena, rol)      # Guarda en el diccionario

    return usuarios


def login(usuarios):
    u = input("Usuario: ")
    p = input("Contraseña: ")

    # Verificar usuario
    if u in usuarios and p == usuarios[u][0]:
        print("Acceso permitido")
        print("Rol:", usuarios[u][1])
        return True
    else:
        print("Datos incorrectos")
        return False

def inicio():
    usuarios = cargar_usuarios("csv/usuarios.csv")
    print("Bienvenido.")
    
    if login(usuarios):
        print("Entrando al sistema...\n")
        return True
    else:
        print("No pudiste entrar.")
        return False
