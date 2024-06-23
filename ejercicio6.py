# Ejercicio 6
#Cree una clase de Python llamada Usuario que use el método init y cree un nombre de usuario y una contraseña. 

class Usuario:
    def __init__(self, nombre_usuario, contrasena):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena

# Crea un objeto usando la clase.
usuario_prueba = Usuario("usuario_ejemplo", "contrasena123")

# Imprimiendo los atributos del objeto para verificar
print(f"Nombre de usuario: {usuario_prueba.nombre_usuario}")
print(f"Contraseña: {usuario_prueba.contrasena}")
