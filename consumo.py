from aparato import Aparato

class ConsumoManager:
    def __init__(self, tarifa):
        self.aparatos = []
        self.tarifa = tarifa  # costo por kWh

    def agregar_aparato(self, aparato):
        self.aparatos.append(aparato)

    def calcular_costos(self):
        return [(a, a.consumo_mensual(), a.consumo_mensual() * self.tarifa) for a in self.aparatos]

    def total_consumo(self):
        return sum(a.consumo_mensual() for a in self.aparatos)

    def total_costo(self):
        return self.total_consumo() * self.tarifa

    def aparatos_ordenados(self):
        return sorted(self.aparatos, key=lambda a: a.consumo_mensual(), reverse=True)
