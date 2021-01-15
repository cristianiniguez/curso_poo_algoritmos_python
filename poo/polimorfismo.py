class Persona():
    def __init__(self, nombre):
        self.nombre = nombre

    def avanzar(self):
        print('Ando caminando')


class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def avanzar(self):
        print('Ando moviendome en mi bicicleta')


def main():
    persona = Persona('Cristian')
    persona.avanzar()  # Ando caminando

    ciclista = Ciclista('Daniela')  # Ando moviendome en mi bicicleta
    ciclista.avanzar()


if __name__ == "__main__":
    main()
