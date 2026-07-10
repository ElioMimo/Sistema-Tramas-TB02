def registrar_trama():
    #proceso 1
    pass

def consultar_trama():
    #proceso 2
    pass

def actualizar_estado():
    #proceso 3
    pass

def registrar_ticket():
    #proceso 4
    pass

def reportes():
    #proceso 5
    pass


def menu_principal():
    opcion = ""
    while opcion != "6":
        print("\nSISTEMA DE CONTROL DE TRAMAS")
        print("1. Registrar trama")
        print("2. Consultar trama")
        print("3. Actualizar estado")
        print("4. Registrar ticket")
        print("5. Reportes")
        print("6. Salir")
        
        opcion = input("Seleccione una opcion:")
        
        if opcion == "1":
            registrar_trama()
            
        elif opcion == "2":
            consultar_trama()
        
        elif opcion == "3":
            actualizar_estado()
            
        elif opcion == "4":
            registrar_ticket()
            
        elif opcion == "5":
            reportes()
            
        elif opcion == "6":
            print("Saliendo del sistema")
            
        else:
            print("Opción inválida. Intente nuevamente")
            
menu_principal()
