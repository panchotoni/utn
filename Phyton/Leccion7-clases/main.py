class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


persona1 = Persona("pancho", "toni", 25)

print(type(Persona))
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

persona2 = Persona("Osvlado", "Giordanini", 45)
print(f'El objeto 2 de la clase persona: {persona2.nombre} {persona2.apellido} {persona2.edad}')
print(f'El objeto 2 de la clase persona: {persona1.nombre} {persona1.apellido} {persona1.edad}')