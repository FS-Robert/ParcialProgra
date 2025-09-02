class Aparato:
    def __init__(self, nombre, potencia, horas):
        self.nombre = nombre
        self.potencia = potencia  # en Watts
        self.horas = horas  # horas de uso mensual

    def consumo_mensual(self):
        # Consumo en kWh
        return (self.potencia * self.horas) / 1000

    def __str__(self):
        return f"{self.nombre}: {self.potencia}W, {self.horas}h/mes, {self.consumo_mensual():.2f} kWh"
