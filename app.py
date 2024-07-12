from fun import asignar_sueldos_aleatorios, menu, clasificar_sueldos, estadisticas, reporte_de_sueldos
op = 0
listaapp = []

while True:
    op = menu()
    if op == 1:
        asignar_sueldos_aleatorios(listaapp)  
    elif op == 2:
        clasificar_sueldos(listaapp)  
    elif op == 3:
        estadisticas(listaapp) 
    elif op == 4:
        reporte_de_sueldos(listaapp)
    elif op == 5:
        print("Finalizando programa...")
        print("Desarrollado por Francisco Alcayaga Caroca")
        print("Rut: 19.557.041-8")
        print("")
        break