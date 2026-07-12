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
    print("\nREGISTRAR TRAMA")
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
    print("\nCONSULTAR TRAMA")
    seguir = "s"
    
    while seguir == "s":
        codigo_buscado = input("Ingrese código de lote:")
        indice = -1
        
        for i in range (len(codigos_lote)):
            if codigos_lote[i] == codigo_buscado:
                indice = i
                
        if indice >= 0:
            print("\nTRAMA ENCONTRADA")
            print("Servicio:",servicios[indice])
            print("Tipo de seguro:",tipos_seguro[indice])
            print("Mes de facturación:",meses_facturacion[indice])
            print("Año:",anios[indice])
            print("Total de expedientes:",totales_expedientes[indice])
            print("Fecha de carga:",fechas_carga[indice])
            print("Código de lote:",codigos_lote[indice])
            print("Código de solicitud",codigos_solicitud[indice])
            print("Rechazados:",rechazados_lista[indice])
            print("Aceptados:",aceptados_lista[indice])
            print("Ticket:",tickets_lista[indice])
            print("Estado:",estados[indice])
            
        else:
            print("Trama no existe")
            
        seguir = input("\n¿Desea consultar otra trama? (s/n):").lower()
      
      
def actualizar_estado():
    print("\nACTUALIZAR ESTADO")
    seguir = "s"
    
    while seguir == "s":
        codigo_buscado = input("Ingrese código de lote:")
        
        
        indice = -1
        for i in range(len(codigos_lote)):
            if codigos_lote[i] == codigo_buscado:
                indice = i
        if indice == -1:
            print("\nTrama no existe")
            return
            
        print("Total de expedientes:",totales_expedientes[indice])
        rechazados = int(input("Cantidad de expedientes rechazados:"))
        
        aceptados = totales_expedientes[indice] - rechazados
        
        rechazados_lista[indice] = rechazados
        aceptados_lista[indice] = aceptados
        
        necesita_ticket = input("¿La trama requiere ticket? (s/n)").lower()
        
        if necesita_ticket == "s":
            estados[indice] = "TICKET PENDIENTE"
        else:
            estados[indice]= "PROCESADA"
        
        print("\nACTUALIZACION GUARDADA CORRECTAMENTE")
        print("Expedientes aceptados:",aceptados)
        print("Expedientes rechazados:",rechazados)
        print("Estado actualizado:",estados[indice])
        seguir = input("\n¿Desea actualizar otra trama? (s/n)").lower()

def registrar_ticket():
    print("\nREGISTRAR TICKET")
    seguir = "s"
    
    while seguir == "s":
        codigo_buscado = input("Ingrese el código de lote:")
        
        indice = -1
        for i in range(len(codigos_lote)):
            if codigos_lote[i] == codigo_buscado:
                indice = i
                
        if indice == -1:
            print("\nTrama no existe")
        elif estados[indice] != "TICKET PENDIENTE":
            print("\nTrama no requiere ticket. Estado actual:",estados[indice])
        else:
            numero_ticket = input("Ingrese el número de ticket:")
            tickets_lista[indice] = numero_ticket
            estados[indice] = "TICKET REGISTRADO"
            print("\nTICKET REGISTRADO CORRECTAMENTE")
            
        seguir = input("\n¿Desea registrar otro ticket? (s/n)").lower()

def reportes():
    print("\nREPORTES")
    seguir = "s"
    
    while seguir == "s":
        servicio_buscado = input("Ingrese el servicio:").strip().upper()
        mes_buscado = input("Ingrese el mes:").strip().upper()
        anio_buscado = input("Ingrese el año:").strip().upper()
        
        cantidad_tramas = 0
        total_enviados = 0
        total_aceptados = 0
        total_rechazados = 0
        cantidad_tickets = 0
        tramas_sin_procesar = 0
        
        for i in range(len(codigos_lote)):
            if servicios[i] == servicio_buscado and meses_facturacion[i] == mes_buscado and anios[i] == anio_buscado:
                cantidad_tramas = cantidad_tramas + 1
                total_enviados = total_enviados + totales_expedientes[i]
                if aceptados_lista[i] is None:
                    tramas_sin_procesar = tramas_sin_procesar + 1
                if aceptados_lista[i] is not None:
                    total_aceptados = total_aceptados + aceptados_lista[i]
                if rechazados_lista[i] is not None:
                    total_rechazados = total_rechazados + rechazados_lista[i]
                if tickets_lista[i] is not None:
                    cantidad_tickets = cantidad_tickets + 1
             
        print("\nREPORTE PARA EL SERVICIO DE",servicio_buscado,"DEL PERIODO",mes_buscado,anio_buscado)            
        
        if cantidad_tramas == 0:
            print("\nNo existen registros")
            
        else:
            print("\nCantidad de tramas registradas:",cantidad_tramas)
            print("Cantidad de tramas sin procesar:",tramas_sin_procesar)
            print("Total de expedientes enviados:",total_enviados)
            print("Total expedientes aceptados:",total_aceptados)
            print("Total de expedientes rechazados:",total_rechazados)
            print("Cantidad de tickets:",cantidad_tickets)
            
        seguir = input("\n¿Desea generar otro reporte? (s/n):").lower()
        
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
