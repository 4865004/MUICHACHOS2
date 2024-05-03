#LISTA DE MES
meses = [
    "enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
]
#FUNCION DE MES A NUMERO
def ObtenerMesEnNumero(MesMin):
    T = 1
    while T <= 12:
        VT = T - 1
        if(MesMin == meses[VT]):
            return VT + 1 
            break
        T += 1 
def obtener_signo_zodiacal(dia, mes):
    signos_zodiaco = {
        "Capricornio": [(1, 20), (12, 31)],
        "Acuario": [(1, 21), (2, 19)],
        "Piscis": [(2, 20), (3, 20)],
        "Aries": [(3, 21), (4, 19)],
        "Tauro": [(4, 20), (5, 20)],
        "Géminis": [(5, 21), (6, 20)],
        "Cáncer": [(6, 21), (7, 22)],
        "Leo": [(7, 23), (8, 22)],
        "Virgo": [(8, 23), (9, 22)],
        "Libra": [(9, 23), (10, 22)],
        "Escorpio": [(10, 23), (11, 21)],
        "Sagitario": [(11, 22), (12, 21)]
    }

    for signo, (inicio, fin) in signos_zodiaco.items():
        if (mes == inicio[0] and dia >= inicio[1]) or (mes == fin[0] and dia <= fin[1]):
            return signo
    return "Capricornio"  # Por si la fecha no coincide con ninguno de los rangos

# Obtener la fecha de nacimiento del usuario
dia = int(input("Ingresa tu día de nacimiento: "))
mesInde = input("Ingresa tu mes de nacimiento: ")
try:
    # Intenta convertir la entrada a entero
    mes = int(mesInde)
    # Obtener y mostrar el signo zodiacal
    signo = obtener_signo_zodiacal(dia, mes)
    print("Tu signo zodiacal es:", signo)
except ValueError:
    # Si no se puede convertir a entero, imprime la entrada como una cadena
    mesInde = mesInde.lower()
    mes = ObtenerMesEnNumero(mesInde)
    # Obtener y mostrar el signo zodiacal
    signo = obtener_signo_zodiacal(dia, mes)
    print("Tu signo zodiacal es:", signo)