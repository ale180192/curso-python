class User:

    def __init__(self, nombre, semestre) -> None:
        self.nombre = nombre
        self.semestre = semestre

    def get_nombre(self):
        return self.nombre


# if __name__ == "__main__":

def func():
    user = User("Juan", 5)
    nuevo_nombre = "Maria"
    user.nombre = nuevo_nombre
    if len(user.nombre) >= 4:
        print("El nombre tiene mas de 4 caracteres")
        user.nombre = user.nombre[:4]

    print(f"nombre es: {user.nombre}")

# func()
