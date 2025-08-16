import csv
from datetime import datetime

def cargar_compras(ruta):
    compras_validas = []
    try:
        with open(ruta, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for fila in reader:
                try:
                    cantidad = int(fila["cantidad"])
                    precio_unitario = int(fila["precio_unitario"])
                    if cantidad <= 0 or precio_unitario <= 0:
                        print(f"Advertencia: Fila inválida {fila}")
                        continue
                    try:
                        datetime.strptime(fila["fecha"], "%Y-%m-%d")
                    except ValueError:
                        print(f"Advertencia: Fecha inválida {fila['fecha']}")
                        continue
                    compras_validas.append({
                        "cliente": fila["cliente"],
                        "fecha": fila["fecha"],
                        "producto": fila["producto"],
                        "cantidad": cantidad,
                        "precio_unitario": precio_unitario
                    })
                except Exception as e:
                    print(f"Error procesando fila {fila}: {e}")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta}")
    return compras_validas
