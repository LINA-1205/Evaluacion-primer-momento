def estadisticas(data):
    """
    Calcula estadísticas a partir de una lista de compras.

    Args:
        data (list[dict]): Lista de diccionarios con la información de cada compra.
            Cada diccionario debe tener las claves:
                - "cliente" (str) 
                - "producto" (str)
                - "cantidad" (int)
                - "precio_unitario" (int)

    Returns:
        dict: Un diccionario con el resumen de estadísticas:
            - "total_ingresos" (int): Suma de cantidad * precio_unitario para todas las compras.
            - "top_producto_por_ingresos" (str): Producto con mayor ingreso acumulado.
            - "compras_por_cliente" (dict[str, int]): Cantidad total de ítems comprados por cliente.
            - "bono" (bool): True si total_ingresos > 6_000_000, de lo contrario False.
    """
    total_ingresos = 0
    ingresos_por_producto = {}
    compras_por_cliente = {}
    for compra in data:
        ingreso = compra["cantidad"] * compra["precio_unitario"]
        total_ingresos += ingreso
        producto = compra["producto"]
        ingresos_por_producto[producto] = ingresos_por_producto.get(producto, 0) + ingreso
        cliente = compra["cliente"]
        compras_por_cliente[cliente] = compras_por_cliente.get(cliente, 0) + compra["cantidad"]
    top_producto = max(ingresos_por_producto, key=ingresos_por_producto.get)
    resumen = {
        "total_ingresos": total_ingresos,
        "top_producto_por_ingresos": top_producto,
        "compras_por_cliente": compras_por_cliente,
        "bono": total_ingresos > 6_000_000
    }
    return resumen
