class Person_Acount:
    def __init__(self, nombre="Elias", apellido="Caballero", ingresos=[2000000], gastos= [1000000]):
        self.nombre = nombre
        self.apellido = apellido
        self.ingresos = ingresos
        self.gastos = gastos
    def ingresos_totales(self):
        return sum(self.ingresos)
    def gastos_totales(self):
        return sum(self.gastos)
    def balance(self):
        return self.ingresos_totales() - self.gastos_totales()
    def add_ingreso(self, ingreso):
        self.ingresos.append(ingreso)
    def add_gasto(self, gasto):
        self.gastos.append(gasto)
    def account_info(self):
        return f"Nombre: {self.nombre} {self.apellido}\nIngresos: {self.ingresos_totales()}\nGastos: {self.gastos_totales()}\nBalance: {self.balance()}"

print ("Información de la cuenta de la persona:")
persona = Person_Acount()
print(persona.account_info())
print ("Agregando un ingreso de 5000000")
persona.add_ingreso(5000000)
print(persona.account_info())
print ("Agregando un gasto de 2000000")
persona.add_gasto(2000000)
