print ("DINOKOMBAT")
def interfaz():
    while (True):
        menu = ["Bienvenido a  DINOKOMBAT", "1- Kombate", "2- Crear dinosaurio", "3- Dinosaurios creados", "4- Instrucciones", "5- salir"]
        for menus in menu:
            print(f" {menus}")
        kombate = ("Bienvenido al kombate")
        try:
            eleccion = (int(input("Que te gutaria hacer: ")))
            if eleccion == 1:
                print (kombate)
            elif eleccion == 2:
                print ("hola mi bro")
            elif eleccion == 3:
                print ("hola carnal")
            elif eleccion == 4:
                print ("estas son las intrucciones")
            elif eleccion == 5:
                print ("Byeeee")
            else:
                print("no es una opcion")
                return interfaz()
            break
        except ValueError:
                print("no es una opcion")
interfaz()