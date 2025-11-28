import csv
import os
from datetime import datetime, timedelta

miembros = "csv/miembros.csv"

def fecha_inicio():
    return datetime.today().strftime("%Y-%m-%d")

def fecha_final(plan):
    hoy = datetime.today()
    
    if plan == "basico":
        dias = 30
    elif plan == "premium":
        dias = 60
    elif plan == "full":
        dias = 90
    else:
        dias = 30
    
    fecha_fin = hoy + timedelta(days=dias)
    return fecha_fin.strftime("%Y-%m-%d")

def estados(fin):
    hoy = datetime.today().strftime("%Y-%m-%d")
    return "activo" if fin >= hoy else "inactivo"
    
def agregar_id():
    
    if not os.path.exists(miembros):
        return 0
    
    with open(miembros,"r", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        numero = 0
        
        for fila in lector:
            numero = int(fila["id"])
        return numero
    
def registrar_miembro():
    numero = agregar_id()
    nuevo_id = numero + 1
    
    
    nombre = input("Ingrese su nombre: ").strip().lower()
    doc = input("Ingrese su documento: ")
    tel = input("Ingrese su telefono: ")
    correo = input("Ingrese su correo: ")
    plan = input("Ingrese plan (BÁSICO | PREMIUM | FULL)").lower().strip()
    
    if nombre is int:
        print("Error: no se pueden numeros en el nombre")
        
    if doc is str:
        print("Error: no se pueden letras en el documento")
        
    if tel is str:
        print("Error: no se pueden letras en el telefono")
        
    if plan not in ["full","premium","basico"]:
        print("Ese plan no exixte")
        
    inicio = fecha_inicio()
    fin = fecha_final(plan)
    estado = estados(fin)
    
    archivo_no_existe = os.path.exists(miembros)
    with open(miembros,"a", encoding="utf-8", newline= "") as f:
        writer = csv.writer(f)
        
        if not archivo_no_existe:
            writer.writerow(["id","nombre","documento","telefono","correo","plan","inicio","fin","estado"])
        writer.writerow([nuevo_id,nombre,doc,tel,correo,plan,inicio,fin,estado])
        
        print(f"Miembro agregado con {nuevo_id}:")
        
def listar_miembro():
    
    with open(miembros,"r", encoding="utf-8") as f:
        lector = csv.DictReader(f)
    
        print("======LISTA======")
        for fila in lector:
            print(f"ID: {fila['id']}")
            print(f"Nombre: {fila['nombre']}")
            print(f"Documento: {fila['documento']}")
            print(f"Teléfono: {fila['telefono']}")
            print(f"Correo: {fila['correo']}")
            print(f"Plan: {fila['plan']}")
            print(f"Inicio: {fila['inicio']}")
            print(f"Fin: {fila['fin']}")
            print(f"Estado: {fila['estado']}")
            print("==============================================")

def buscar_miembro():
    if not os.path.exists(miembros):             #se mete al csv y si el miembro no esta porne ese mensaje.
        print("No hay miembros registrados.")
        return
    
    print("\n--- BUSCAR MIEMBRO ---")
    print("1. Buscar por ID")
    print("2. Buscar por Nombre")
    opcion = input("Seleccione una opción: ")  
    
    if opcion not in ["1", "2"]:        # Si el usuario ingresa algo diferente de 1 o 2 → opción inválida
        print("Opción inválida")
        return
#---------------------------------------------------------------------------------------
    if opcion == "1":
        busqueda = input("Ingrese el ID a buscar: ").strip()  # Si elige buscar por ID
        
    # Validación: un ID solo puede contener números
        if not busqueda.isdigit():
            print("El ID debe ser un número.")
            return
    
        tipo = "id"  # Guarda el tipo de búsqueda
#---------------------------------------------------------------------------------------
    elif opcion == "2":
        busqueda = input("Ingrese el nombre a buscar: ").lower().strip()
        
        tipo = "nombre"  # Guarda el tipo de búsqueda
#---------------------------------------------------------------------------------------

 # Abre el archivo CSV para leerlo
    with open(miembros, "r", encoding="utf-8") as f:
        lector = csv.DictReader(f)  # Lee el CSV como diccionarios (clave=columna)
        encontrados = [] # Lista donde guardaremos los miembros encontrados
        
    # Recorremos cada fila (cada miembro)
        for fila in lector:
            # Si estamos buscando por ID
            if tipo == "id":
                # Compara el ID exacto
                if fila["id"] == busqueda:
                    encontrados.append(fila)
                    
            # Si estamos buscando por nombre
            elif tipo == "nombre":
                # Compara si el nombre buscado está dentro del nombre del miembro (búsqueda parcial)
                if busqueda in fila["nombre"].lower():
                    encontrados.append(fila)
                    
        if not encontrados:
            print(" No se encontraron coincidencias.")
            return
        
        print(f"Resultados encontrados: {len(encontrados)}")

        for fila in encontrados:
            print(f"ID: {fila['id']}")
            print(f"Nombre: {fila['nombre']}")
            print(f"Documento: {fila['documento']}")
            print(f"Teléfono: {fila['telefono']}")
            print(f"Correo: {fila['correo']}")
            print(f"Plan: {fila['plan']}")
            print(f"Inicio: {fila['inicio']}")
            print(f"Fin: {fila['fin']}")
            print(f"Estado: {fila['estado']}")

    



def menu():  
    
    while True:
        print(""" 
==============MENU MIEMBROS=============
1. Registrar miembros
2. listar miembros
3. Buscar miembros
4. Renovar plan con pago
5. volver al menu principal
=========================================
""")
        
        opciones = input("selecciona una opcion: ")
        
        if opciones not in ["1","2","3","4","5"]:
            print("opcion invalida")
            
            
        if opciones == "1":
            registrar_miembro()
        
        if opciones == "2":
            listar_miembro()
        
        if opciones == "3":
            buscar_miembro()
            
        if opciones == "4":
            print("siiiii")
            
        if opciones == "5":
            print("saliendo")
            return