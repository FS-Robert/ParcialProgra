from consumo import ConsumoManager
from aparato import Aparato

def main():
    print("Sistema de Control de Gasto Eléctrico - El Salvador")
    tarifa = float(input("Ingrese el costo por kWh en dólares: "))
    manager = ConsumoManager(tarifa)

    while True:
        nombre = input("Nombre del aparato (o 'fin' para terminar): ")
        if nombre.lower() == 'fin':
            break
        potencia = float(input("Potencia del aparato en Watts: "))
        horas = float(input("Horas de uso mensual: "))
        aparato = Aparato(nombre, potencia, horas)
        manager.agregar_aparato(aparato)

    print("\nConsumo y costo por aparato (ordenados por consumo):")
    for aparato in manager.aparatos_ordenados():
        consumo = aparato.consumo_mensual()
        costo = consumo * tarifa
        print(f"{aparato.nombre}: {consumo:.2f} kWh, ${costo:.2f}")

    print("\nResumen:")
    print(f"Consumo total: {manager.total_consumo():.2f} kWh")
    print(f"Gasto mensual total: ${manager.total_costo():.2f}")

if __name__ == "__main__":
    main()
