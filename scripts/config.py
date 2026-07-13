from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RUTA_EXCEL = BASE_DIR / "data" / "Excel_Maestro.xlsx"
RUTA_JSON = BASE_DIR / "data" / "productos.json"
RUTA_PROVEEDOR = BASE_DIR / "data" / "excel_proveedor.xlsx"
RUTA_IMAGENES = BASE_DIR / "img" / "productos"

HOJA_PRODUCTOS = "Productos"