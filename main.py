from utils import cargar_compras

def main():
    print("Bienvenido al sistema de compras")
    ruta_csv = "data/compras.csv"
    datos = cargar_compras(ruta_csv)
    print(f"Datos filtrados: {datos}")

if __name__ == "__main__":
    main()