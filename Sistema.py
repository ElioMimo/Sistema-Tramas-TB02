servicios = []
tipos_seguro = []
meses_facturacion = []
anios = []
totales_expedientes = []
fechas_carga = []
codigos_lote = []
codigos_solicitud = []
rechazados_lista = []
aceptados_lista = []
tickets_lista = []
estados = []


servicios_validos = ["TELECONSULTAS", "CHEQUEOS PREVENTIVOS", "MEDICO DE CABECERA", "NUTRICION", "PSICOLOGIA"]
tipos_seguro_validos = ["EPS", "SEGUROS"]
meses_validos = ["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO", "SETIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"]


def registrar_trama():
    print("\n--- REGISTRAR TRAMA ---")
    seguir = "s"
    
    while seguir == "s":
        servicio = input("Servicio:").strip().upper()
        while servicio not in servicios_validos:
            print("\nServicio inválido.")
            servicio = input("Servicio:").strip().upper()
            
        tipo_seguro = input("Tipo de seguro (EPS/Seguros):").strip().upper()
        while tipo_seguro not in tipos_seguro_validos:
            print("\nTipo de seguro inválido. Debe ser EPS o Seguros.")
            tipo_seguro = input("Tipo de seguro (EPS/Seguros):").strip().upper()
            
        mes_facturacion = input("Mes de facturación:").strip().upper()
        while mes_facturacion not in meses_validos:
            print("\nMes inválido.")
            mes_facturacion = input("Mes de facturación:").strip().upper()
            
        anio = input("Año de facturación: ")
        total_expedientes = int(input("Cantidad total de expedientes: "))
        fecha_carga = input("Fecha de carga (dd/mm/aaaa): ")
        codigo_lote = input("Código de lote: ")
        codigo_solicitud = input("Código de solicitud: ")
        
        #Pendiente revisar si lista funciona al correr el proceso 2. Faltan listas
        servicios.append(servicio)
        tipos_seguro.append(tipo_seguro)
        meses_facturacion.append(mes_facturacion)
        anios.append(anio)
        totales_expedientes.append(total_expedientes)
        fechas_carga.append(fecha_carga)
        codigos_lote.append(codigo_lote)
        codigos_solicitud.append(codigo_solicitud)
        rechazados_lista.append(None)
        aceptados_lista.append(None)
        tickets_lista.append(None)
        estados.append("PENDIENTE DE PROCESAMIENTO")
        
        print("\nTrama registrada correctamente.")
        print("Estado: Pendiente de procesamiento")
        
        seguir = input("\n¿Desea registrar otra trama? (s/n): ").lower()
            
            
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
        print("\nSISTEMA DE CONTROL DE TRAMAS\n")
        print("1. Registrar trama")
        print("2. Consultar trama")
        print("3. Actualizar estado")
        print("4. Registrar ticket")
        print("5. Reportes")
        print("6. Salir")
        
        opcion = input("\nSeleccione una opcion:")
        
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
            print("\nSaliendo del sistema")
            
        else:
            print("\nOpción inválida. Intente nuevamente")
            
menu_principal()
