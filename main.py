from utils import cargar_compras, estadisticas

datos_prueba = [{'cliente': 'A',
                'fecha': '2025-07-01',
                'producto': 'laptop',
                'cantidad': 1,
                'precio_unitario': 3500000},
                {'cliente': 'B',
                'fecha': '2025-07-02',
                'producto': 'mouse',
                'cantidad': 3,
                'precio_unitario': 45000},
                {'cliente': 'A',
                'fecha': '2025-07-05',
                'producto': 'monitor',
                'cantidad': 2,
                'precio_unitario': 780000},
                {'cliente': 'C',
                'fecha': '2025-07-06',
                'producto': 'teclado',
                'cantidad': 1,
                'precio_unitario': 120000},
                {'cliente': 'B',
                'fecha': '2025-07-06',
                'producto': 'laptop',
                'cantidad': 1,
                'precio_unitario': 3200000},
                {'cliente': 'D',
                'fecha': '2025-07-07',
                'producto': 'monitor',
                'cantidad': 1,
                'precio_unitario': 800000}]

from utils import cargar_compras

def main():
    print("Bienvenido al sistema de compras")
    ruta_csv = "data/compras.csv"
    datos = cargar_compras(ruta_csv)
    print(f"Datos filtrados: {datos}")
    print(f"estadisticas: {estadisticas(datos_prueba)}")

if __name__ == "__main__":
    main()
