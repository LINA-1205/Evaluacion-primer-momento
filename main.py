from utils import estadisticas

DatosPrueba = [{'cliente': 'A',
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

def main():
    print("Bienvenido al sistema de compras")
    print(f"estadisticas: {estadisticas(DatosPrueba)}") 

if __name__ == "__main__":
    main()
