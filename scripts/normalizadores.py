def normalizar_codigo(codigo):

    if codigo is None:
        return None

    if isinstance(codigo, str):
        codigo = codigo.strip()

        if codigo == "":
            return None

    return int(codigo)

def normalizar_texto(texto):

    if texto is None:
        return None

    if isinstance(texto, str):
        texto = texto.strip()

        if texto == "":
            return None

    return texto

def normalizar_precio(precio):

    if precio is None:
        return None

    return float(precio)

def normalizar_activo(activo):

    if activo is None:
        return None

    if isinstance(activo, str):
        activo = activo.strip().lower()

        if activo == "si":
            return True

        if activo == "no":
            return False

    return activo

def normalizar_imagen(imagen):

    imagen = normalizar_texto(imagen)

    if imagen is None:
        return "sin-imagen.png"

    return imagen
