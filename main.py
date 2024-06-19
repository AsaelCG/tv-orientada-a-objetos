import time
from tv import TV

television1 = TV ("Samsung", 56)
television2 = TV ("LG", 86)

while True: 
    print(television1.estatus_actual())
    print("\tControl remoto")
    print("1. Encender")
    print("2. Subir Volumen")
    print("3. Bajar Volumen")
    print("4. Cambiar canal")
    boton = input("Presiona un botón: ")
    if boton == "1":
        if television1.prendida:
            print(f"Apagando {television1}")
        else: 
            print(f"Encendiendo {television1}")
        television1.power()
    if boton == "2":
        television1.cambiar_volumen(1)
        print("Subiendo volumen")
    if boton == "3":
        television1.cambiar_volumen(-1)
        print("Bajando volumen")
        
    
    time.sleep(1)

