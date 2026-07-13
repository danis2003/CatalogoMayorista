# Catálogo Mayorista

**Autor:** Daniel Garcia

Proyecto personal desarrollado para la administración y publicación de un catálogo web mayorista.

## Descripción

Este proyecto automatiza la administración de un catálogo web mayorista.

Su función principal es mantener sincronizados los precios publicados en la página web con la lista de precios enviada por el proveedor, evitando modificaciones manuales en el sitio.

El sistema trabaja con dos archivos Excel:

- **Excel Maestro:** contiene únicamente los productos que forman parte del catálogo web.
- **Excel Proveedor:** contiene la lista completa de precios enviada por el proveedor.

Al ejecutar el proceso de actualización, el sistema:

1. Lee ambos archivos Excel.
2. Busca cada producto del catálogo mediante su código.
3. Actualiza únicamente los precios que hayan cambiado.
4. Registra la fecha de actualización de cada precio modificado.
5. Informa los productos del catálogo que no fueron encontrados en la lista del proveedor.
6. Genera automáticamente el archivo `productos.json`, utilizado por la página web.

---

# Estructura del proyecto

```
CatalogoMayorista/
│
├── css/
│   └── style.css
│
├── data/
│   ├── Excel_Maestro.xlsx
│   ├── excel_proveedor.xlsx
│   └── productos.json
│
├── img/
│   └── productos/
│
├── js/
│   └── script.js
│
├── scripts/
│   ├── actualizar_maestro.py
│   ├── actualizar_precios.py
│   ├── config.py
│   ├── escritor_excel.py
│   ├── exportador_json.py
│   ├── generar_json.py
│   ├── indices.py
│   ├── lector_excel.py
│   ├── lector_proveedor.py
│   ├── normalizadores.py
│   ├── utilidades.py
│   └── validadores.py
│
├── index.html
└── README.md
```

---

# Flujo de trabajo

Cada vez que el proveedor envía una nueva lista de precios:

1. Reemplazar el archivo `excel_proveedor.xlsx` dentro de la carpeta `data`.
2. Ejecutar:

```bash
python scripts/actualizar_precios.py
```

El sistema realizará automáticamente:

- Actualización del Excel Maestro.
- Actualización de las fechas de modificación.
- Generación del archivo `productos.json`.

No es necesario ejecutar ningún otro script.

---

# Scripts Python

## actualizar_precios.py

Es el punto de entrada del proceso de actualización.

Responsabilidades:

- Leer el Excel Maestro.
- Leer el Excel del proveedor.
- Actualizar los precios en memoria.
- Guardar los cambios en el Excel Maestro.
- Mostrar el resumen de la actualización.
- Generar automáticamente el archivo `productos.json`.

Es el único script que normalmente debe ejecutar el usuario.

---

## lector_excel.py

Lee el archivo `Excel_Maestro.xlsx`.

Obtiene todos los productos del catálogo y devuelve una lista de diccionarios con la siguiente estructura:

```python
{
    "fila_excel": 2,
    "codigo": 3226,
    "nombre": "ACELGA 550GR",
    "marca": "Green Life",
    "categoria": "Congelados",
    "precio": 4934.38,
    "imagen": "acelga.png",
    "activo": True
}
```

También conserva el número de fila para poder actualizar posteriormente el Excel sin recorrerlo nuevamente.

---

## lector_proveedor.py

Lee el archivo `excel_proveedor.xlsx`.

Extrae únicamente la información necesaria:

- Código
- Descripción
- Precio

Actualmente supone que:

- la hoja activa contiene los datos;
- los productos comienzan en la fila 7.

---

## actualizar_maestro.py

Contiene la lógica de negocio para actualizar los precios.

Funciones principales:

- actualizar únicamente los productos existentes en el catálogo;
- detectar productos del catálogo que ya no aparecen en la lista del proveedor.

No realiza escritura sobre archivos.

---

## escritor_excel.py

Es el encargado de modificar el Excel Maestro.

Responsabilidades:

- actualizar únicamente los precios que cambiaron;
- registrar la fecha de actualización;
- guardar el archivo;
- informar si el archivo está abierto (PermissionError).

---

## generar_json.py

Genera el archivo `productos.json`.

Antes de exportar:

- lee nuevamente el Excel Maestro;
- valida la información;
- reemplaza imágenes inexistentes por `sin-imagen.png`;
- exporta el JSON utilizado por la página web.

---

## validadores.py

Agrupa todas las validaciones del catálogo.

Actualmente verifica:

- códigos vacíos;
- códigos duplicados;
- nombres vacíos;
- categorías vacías;
- precios inválidos;
- estado Activo válido;
- existencia de imágenes;
- normalización de marcas.

---

## normalizadores.py

Convierte los datos provenientes de Excel a un formato consistente.

Ejemplos:

- texto;
- precio;
- código;
- imagen;
- activo.

---

## indices.py

Genera índices en memoria para acelerar las búsquedas por código.

Esto evita recorrer listas completas para localizar un producto.

---

## config.py

Centraliza todas las rutas utilizadas por el proyecto.

De esta forma ningún script necesita conocer dónde se encuentran los archivos.

---

## utilidades.py

Contiene funciones auxiliares utilizadas por distintos módulos.

Actualmente se utiliza para mostrar errores de validación.

---

## exportador_json.py

Se encarga exclusivamente de escribir el archivo `productos.json`.

No realiza ninguna validación.

---

# Dependencias

El proyecto fue desarrollado con:

- Python 3.11
- openpyxl

Instalación:

```bash
pip install openpyxl
```

---

# Cómo agregar un producto nuevo al catálogo

El alta de nuevos productos es un proceso manual.

Pasos:

1. Agregar el producto en `Excel_Maestro.xlsx`.
2. Completar:
   - Código
   - Nombre
   - Marca
   - Categoría
   - Imagen
   - Activo
3. Conseguir la imagen del producto.
4. Guardarla en:

```
img/productos/
```

5. Escribir exactamente el nombre del archivo en la columna **Imagen**.
6. Ejecutar:

```bash
python scripts/actualizar_precios.py
```

El producto quedará incorporado automáticamente al archivo `productos.json`.

---

# Actualización de precios

Cada vez que el proveedor envía una nueva lista de precios:

1. Reemplazar el archivo:

```
data/excel_proveedor.xlsx
```

2. Ejecutar:

```bash
python scripts/actualizar_precios.py
```

El sistema realizará automáticamente:

- actualización del Excel Maestro;
- actualización de fechas;
- generación de `productos.json`.

No es necesario ejecutar ningún otro script.

---

# Errores frecuentes

## El Excel Maestro está abierto

Mensaje:

```
No se pudo guardar Excel_Maestro.xlsx.
Cierre el archivo en Excel e intente nuevamente.
```

Solución:

Cerrar el archivo Excel y ejecutar nuevamente el script.

---

## Producto no encontrado

El sistema informa:

```
PRODUCTOS NO ENCONTRADOS
```

Esto indica que el código del producto existe en el catálogo, pero no fue encontrado en la lista enviada por el proveedor.

Se recomienda verificar:

- si el código cambió;
- si el producto fue discontinuado;
- si el proveedor modificó el formato del Excel.

---

## Imagen inexistente

Si una imagen no existe dentro de:

```
img/productos/
```

El sistema utilizará automáticamente:

```
sin-imagen.png
```

y mostrará un aviso por consola.

---

# Decisiones de diseño

El proyecto fue diseñado siguiendo los siguientes criterios:

- Cada script tiene una única responsabilidad.
- Las rutas se encuentran centralizadas en `config.py`.
- Las búsquedas se realizan mediante índices en memoria para mejorar el rendimiento.
- Solo se actualizan los precios que realmente cambiaron.
- La fecha de actualización solo cambia cuando el precio fue modificado.
- El archivo JSON siempre se genera a partir del Excel Maestro, nunca directamente desde el Excel del proveedor.

---

# Próximas mejoras

- Detección automática de los encabezados del Excel del proveedor.
- Validación automática del formato del Excel recibido.
- Mejoras en la interfaz web.
- Nuevos filtros y funcionalidades del catálogo.

---

# Versión

Versión actual:

**v1.0**
