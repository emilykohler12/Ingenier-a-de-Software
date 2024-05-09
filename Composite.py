from abc import ABC, abstractmethod

# Componente
class Personaje(ABC):
    @abstractmethod
    def atacar(self):
        pass

# Personaje individual
class Heroe(Personaje):
    def __init__(self, nombre):
        self.nombre = nombre

    def atacar(self):
        print(f"{self.nombre} ataca a los enemigos.")

# Composite (Grupo de personajes)
class GrupoHeroes(Personaje):
    def __init__(self):
        self.heroes = []

    def agregar_heroe(self, heroe):
        self.heroes.append(heroe)

    def remover_heroe(self, heroe):
        self.heroes.remove(heroe)

    def atacar(self):
        print("El grupo de héroes ataca a los enemigos:")
        for heroe in self.heroes:
            heroe.atacar()

# Cliente
if __name__ == "__main__":
    # Crear héroes individuales
    guerrero = Heroe("Guerrero")
    mago = Heroe("Mago")
    arquero = Heroe("Arquero")

    # Crear un grupo de héroes
    grupo_heroes = GrupoHeroes()
    grupo_heroes.agregar_heroe(guerrero)
    grupo_heroes.agregar_heroe(mago)
    grupo_heroes.agregar_heroe(arquero)

    # Atacar con el grupo de héroes
    grupo_heroes.atacar()
