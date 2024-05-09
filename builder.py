class Pizza:
    def __init__(self, tamaño, queso=False, jamon=False, huevo=False):
        self.tamaño = tamaño
        self.queso = queso
        self.jamon = jamon
        self.huevo = huevo

    def __str__(self):
        ingredientes = []
        if self.queso:
            ingredientes.append('queso')
        if self.jamon:
            ingredientes.append('jamon')
        if self.huevo:
            ingredientes.append('huevo')
        return f"Pizza ({self.tamaño}): " + ', '.join(ingredientes)


class ConstructorPizza:
    def __init__(self, tamaño):
        self.tamaño = tamaño
        self.queso = False
        self.jamon = False
        self.huevo = False

    def agregar_queso(self):
        self.queso = True
        return self

    def agregar_jamon(self):
        self.jamon = True
        return self

    def agregar_huevo(self):
        self.huevo = True
        return self

    def construir(self):
        return Pizza(self.tamaño, self.queso, self.jamon, self.huevo)


# Uso del Constructor para crear pizzas con diferentes ingredientes
constructor = ConstructorPizza("mediana")
pizza_con_queso = constructor.agregar_queso().construir()
print(pizza_con_queso)

pizza_con_jamon = constructor.agregar_jamon().construir()
print(pizza_con_jamon)

pizza_con_huevo = constructor.agregar_huevo().construir()
print(pizza_con_huevo)

pizza_con_todos_los_ingredientes = constructor.agregar_queso().agregar_jamon().agregar_huevo().construir()
print(pizza_con_todos_los_ingredientes)