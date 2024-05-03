class Estudiande:
    def __init__(self, Nombre, Edad, Grado):
        self.nombre = Nombre
        self.edad = Edad
        self.grado = Grado
    def estudiar(self):
        print("Estudiando...")

nombre = input("Digame su nombre: ")
edad = input("Digame su edad: ")
grado = input("Digame su grado: ")

estudiante = Estudiande(nombre,edad,grado)
print(f"""
      DATOS DEL ESTUDIANTE: \n\n
      Nombre: {estudiante.nombre}\n
      Edad: {estudiante.edad}\n
      Grado: {estudiante.grado}\n
      """)
while True:
    estudiar = input()
    if(estudiar.lower() == "estudiar"):
        estudiante.estudiar()
