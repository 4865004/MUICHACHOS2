class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def mostrarDatos(self):
        print(f"El nombre es: {self.nombre}")
        print(f"La edad es: {self.edad}")
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
    
    def mostrarGrado(self):
        print(f"El grado es: {self.grado}")
        
estudiante = Estudiante("Juan", 39, 1)
estudiante.mostrarGrado()
estudiante.mostrarDatos()