import random
import csv
trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez",
                "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

def asignar_sueldos_aleatorios(lista):
    for nombre in trabajadores:
        sueldo = random.randrange(300000, 2500000)
        asignado = {
                    "nombre": nombre, 
                    "sueldo":sueldo
                    }
        lista.append(asignado)
    for e in lista:
        print(f"Nombre: {e["nombre"]}, Sueldo: {e["sueldo"]}")

def clasificar_sueldos(lista):
    bajos = []
    medios = []
    altos = []
    for trabajador in lista:
        if trabajador["sueldo"]<=800000:
            bajos.append(trabajador)
        elif trabajador["sueldo"]>800000 and trabajador["sueldo"]<=2000000:
            medios.append(trabajador)
        else:
            altos.append(trabajador)
    totalb = len(bajos)
    totalm = len(medios)
    totala = len(altos)
    print("EMPLEADOS CON SUELDO MENOR A $800.000:")
    print(f"Total : {totalb}")
    print()

    for i in bajos:
        print(f"{i["nombre"]} : ${i["sueldo"]:,.0f}")
    print("----------------------------------------")

    print("EMPLEADOS CON SUELDO ENTRE $800.000 Y $2.000.000")
    print(f"Total : {totalm}")
    print()

    for i in medios:
        print(f"{i["nombre"]} : ${i["sueldo"]:,.0f}")
    print("----------------------------------------")

    print("EMPLEADOS CON SUELDO MAYORES A $2.000.000:")
    print(f"Total : {totala}")
    print()

    for i in altos:
        print(f"{i["nombre"]} : ${i["sueldo"]:,.0f}")

def estadisticas(lista):
    sueldos = [i["sueldo"] for i in lista]
    sueldo_minimo = min(sueldos)
    sueldo_maximo = max(sueldos)
    sueldo_promedio = sum(sueldos) / len(sueldos)
    print("-----------------------")
    print("Estadísticas de sueldos:")
    print("-----------------------")
    print(f"Sueldo mínimo: ${sueldo_minimo:,.0f}")
    print(f"Sueldo máximo: ${sueldo_maximo:,.0f}")
    print(f"Sueldo promedio: ${sueldo_promedio:,.2f}")
    print("-----------------------")

def reporte_de_sueldos(lista):

    reporte = []
    for trabajador in lista:
        sueldo_bruto = trabajador["sueldo"]
        afp = int(sueldo_bruto * 0.12)
        salud = int(sueldo_bruto * 0.07)
        sueldo_liquido = sueldo_bruto - afp - salud
        agregar = {"nombre":trabajador["nombre"],
                   "sueldo_bruto":sueldo_bruto,
                   "afp":afp,
                   "salud":salud,
                   "sueldo_liquido":sueldo_liquido}
        reporte.append(agregar)
    nombre_campos = ["nombre","sueldo_bruto","afp","salud","sueldo_liquido"]
    with open('Reporte_Sueldos.csv','w', newline = "") as archivo:
        escritor = csv.DictWriter(archivo,fieldnames = nombre_campos)
        escritor.writeheader()
        escritor.writerows(reporte)

def menu():
    menu = """MENU SUELDOS
    ***********************************
    1.- Asignar sueldos aleatorios.
    2.- Clasificar sueldos.
    3.- Ver estadisticas.
    4.- Reporte de sueldos.
    5.- Salir del programa.
    --> """
    print(menu,end="")
    while True:
        try:
            op = int(input())
            if op >= 1 and op <= 5:
                return op
            else:
                print("Opcion no valida")
                print("Selecciona una opcion valida. --> ",end="")
        except ValueError:
            print("Selecciona una opcion valida. --> ",end="") 