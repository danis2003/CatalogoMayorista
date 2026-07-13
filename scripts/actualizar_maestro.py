def actualizar_precios(productos_proveedor, indice_maestro):

    productos_catalogo = 0

    for producto in productos_proveedor:

        codigo = producto["codigo"]

        if codigo in indice_maestro:

            indice_maestro[codigo]["precio"] = producto["precio"]
            productos_catalogo += 1

    return productos_catalogo

def buscar_productos_faltantes(productos_maestro, indice_proveedor):

    faltantes = []

    for producto in productos_maestro:

        if producto["codigo"] not in indice_proveedor:

            faltantes.append(producto)

    return faltantes

