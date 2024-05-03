class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def hablar(self):
        print("Hola estoy hablando un poco")

class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario ):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

roberto = Empleado("Roberto", "34", "Guatemalteco", "Programador", 100000)

print(roberto.nacionalidad)