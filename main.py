import usuarios
import miembros

def menu():
    
    while True:
        print(""" 
==============MENU PRINCIPAL=============
1. Miembros
2. Entrenamientos
3. Asistencias 
4. Pagos de membrecia
5. Reportes mensuales
6. Salir
=========================================
""")
        
        opcion = input("selecciona una opcion: ")
        
        if opcion not in ["1","2","3","4","5","6"]:
            print("opcion invalida")
            
            
        if opcion == "1":
            miembros.menu()
        
        if opcion == "2":
            print("siiiii")
            
        


login = usuarios.inicio()

if login:
    menu()