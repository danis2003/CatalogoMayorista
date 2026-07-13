def crear_indice_por_codigo(productos):

    indice = {}

    for producto in productos:
        indice[producto["codigo"]] = producto

    return indice