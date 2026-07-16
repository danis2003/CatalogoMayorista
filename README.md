# Catálogo Mi Mayo

Sistema de administración y publicación del catálogo web del **Mayorista Mi Mayo**, desarrollado en Python.

El proyecto automatiza la actualización del catálogo a partir de la lista de precios enviada por el proveedor, administra las imágenes de los productos y publica automáticamente los cambios en la página web.

---

# Autor

**Daniel García**

---

# Versión

**v1.0.0**

---

# Estado del proyecto

🟢 Proyecto operativo.

Actualmente el sistema permite:

- Actualizar automáticamente los precios del catálogo.
- Mantener un único Excel Maestro.
- Administrar imágenes mediante un asistente gráfico.
- Generar automáticamente el archivo `productos.json`.
- Publicar los cambios directamente en GitHub.
- Ejecutarse mediante aplicaciones de escritorio (.exe).

---

# Índice

1. Descripción
2. Características principales
3. Tecnologías utilizadas
4. Estructura del proyecto
5. Instalación
6. Configuración del entorno (venv)
7. Dependencias
8. Uso diario
9. Panel de Control
10. Asistente de Imágenes
11. Flujo de trabajo
12. Arquitectura del sistema
13. Compilación de ejecutables
14. Solución de problemas
15. Decisiones de diseño
16. Historial de versiones
17. Próximas mejoras

---

# Descripción

Catálogo Mi Mayo nació para eliminar el mantenimiento manual del catálogo web del mayorista.

Anteriormente, cada modificación de precios requería editar manualmente el sitio web.

Con este sistema todo el proceso se encuentra automatizado.

El flujo de trabajo consiste en:

1. Importar el Excel enviado por el proveedor.
2. Comparar automáticamente los precios con el Excel Maestro.
3. Actualizar únicamente los productos que cambiaron.
4. Registrar la fecha de modificación.
5. Regenerar automáticamente el catálogo JSON.
6. Publicar los cambios en GitHub.
7. Actualizar la página web.

El sistema fue diseñado para que el mantenimiento diario pueda realizarse desde una única ventana de control, sin necesidad de ejecutar scripts manualmente.

---

# Características principales

## Administración del catálogo

- Actualización automática de precios.
- Comparación por código de producto.
- Registro de fecha de modificación.
- Conservación del historial del Excel Maestro.

---

## Publicación del catálogo

- Generación automática de `productos.json`.
- Publicación automática en GitHub.
- Sincronización inmediata con el sitio web.

---

## Administración de imágenes

- Asistente gráfico para incorporación de imágenes.
- Renombrado automático.
- Conversión automática al formato correcto.
- Copia de seguridad de imágenes procesadas.
- Organización automática de carpetas.

---

## Aplicación de escritorio

El proyecto dispone de una interfaz gráfica desarrollada con **CustomTkinter**.

Desde ella es posible ejecutar todas las operaciones habituales sin utilizar la consola.

Funciones disponibles:

- Importar Excel del proveedor.
- Actualizar precios.
- Abrir Excel Maestro.
- Abrir Asistente de Imágenes.
- Regenerar JSON.
- Publicar cambios en GitHub.

---

# Tecnologías utilizadas

## Lenguaje

- Python 3.11

---

## Librerías principales

- CustomTkinter
- OpenPyXL
- Pillow
- python-dotenv

---

## Herramientas

- Git
- GitHub
- PyInstaller
- Visual Studio Code

---

## Sitio Web

- HTML5
- CSS3
- JavaScript

---

# Filosofía del proyecto

Durante el desarrollo se siguieron los siguientes principios:

- Una única responsabilidad por módulo.
- Separación entre interfaz gráfica y lógica de negocio.
- Configuración centralizada.
- Código reutilizable.
- Automatización de tareas repetitivas.
- Mínima intervención manual.
- Facilidad de mantenimiento.
- Escalabilidad para futuras funcionalidades.

El objetivo principal no fue únicamente actualizar precios, sino construir una herramienta que centralice toda la administración del catálogo desde una única aplicación.

# Estructura del proyecto

La siguiente organización refleja la estructura actual del proyecto.

```text
CatalogoMayorista/
│
├── app/
│   ├── acciones.py
│   ├── estilos.py
│   ├── main.py
│   └── ui.py
│
├── scripts/
│   ├── actualizar_maestro.py
│   ├── actualizar_precios.py
│   ├── asistente_imagenes.py
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
├── css/
│
├── js/
│
├── data/
│   ├── Excel_Maestro.xlsx
│   ├── excel_proveedor.xlsx
│   └── productos.json
│
├── img/
│   ├── banners/
│   ├── iconos/
│   ├── logos/
│   ├── pendientes/
│   ├── procesadas/
│   ├── productos/
│   └── productos_defectuosos/
│
├── venv/
│
├── build/
├── dist/
│
├── index.html
├── build.bat
├── logo.ico
├── requirements.txt
├── README.md
├── CatalogoMiMayo.exe
└── AsistenteImagenes.exe
```

---

# Descripción de cada carpeta

## app/

Contiene toda la interfaz gráfica del sistema.

Aquí se encuentra el Panel de Control utilizado diariamente.

Responsabilidades:

- interfaz principal;
- botones;
- registro de eventos;
- interacción con el usuario.

---

## scripts/

Contiene toda la lógica de negocio.

Ningún módulo de esta carpeta depende de la interfaz gráfica.

Entre sus responsabilidades se encuentran:

- lectura de Excel;
- actualización de precios;
- validaciones;
- generación del JSON;
- administración de imágenes;
- publicación en GitHub.

---

## data/

Almacena todos los archivos de trabajo.

### Excel_Maestro.xlsx

Es la base de datos principal del catálogo.

Contiene únicamente los productos publicados.

Nunca debe reemplazarse.

---

### excel_proveedor.xlsx

Lista de precios recibida del proveedor.

Se reemplaza cada vez que llega una nueva actualización.

---

### productos.json

Archivo generado automáticamente.

Es consumido directamente por la página web.

No debe editarse manualmente.

---

## img/

Contiene todos los recursos gráficos del catálogo.

### banners/

Imágenes utilizadas por la página principal.

---

### iconos/

Reservada para futuros iconos del sitio.

---

### logos/

Logotipos utilizados por la página.

---

### pendientes/

Imágenes nuevas aún no procesadas.

El Asistente de Imágenes trabaja sobre esta carpeta.

---

### procesadas/

Copia de seguridad de todas las imágenes procesadas.

Permite recuperar imágenes originales.

---

### productos/

Imágenes oficiales utilizadas por el catálogo.

El archivo JSON hace referencia a esta carpeta.

---

### productos_defectuosos/

Imágenes descartadas durante conversiones incorrectas.

Se conservan únicamente como respaldo.

---

## css/

Hojas de estilo del sitio web.

---

## js/

Lógica JavaScript del catálogo.

---

## build/

Archivos temporales generados por PyInstaller.

Puede eliminarse en cualquier momento.

---

## dist/

Carpeta temporal donde PyInstaller genera los ejecutables.

Su contenido se copia automáticamente a la raíz del proyecto mediante `build.bat`.

---

## venv/

Entorno virtual del proyecto.

Aquí se instalan todas las dependencias de Python.

Esta carpeta no debe subirse al repositorio Git.

---

# Instalación del proyecto

## Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
```

Ingresar al proyecto:

```bash
cd CatalogoMayorista
```

---

# Crear el entorno virtual

Ejecutar:

```bash
python -m venv venv
```

Se creará automáticamente la carpeta:

```text
venv/
```

---

# Activar el entorno virtual

## PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

La terminal mostrará:

```text
(venv)
```

indicando que el entorno virtual se encuentra activo.

---

# Instalar dependencias

Con el entorno virtual activado ejecutar:

```bash
pip install -r requirements.txt
```

Esto instalará automáticamente todas las librerías necesarias.

---

# Archivo requirements.txt

El proyecto mantiene todas las dependencias registradas en este archivo.

Cada vez que se incorpore una nueva librería debe actualizarse ejecutando:

```bash
pip freeze > requirements.txt
```

De esta forma cualquier instalación futura podrá recrear exactamente el mismo entorno.

---

# Variables de entorno

El proyecto admite un archivo:

```text
.env
```

Actualmente se utiliza para almacenar configuraciones sensibles sin incorporarlas al repositorio Git.

En caso de no existir, la aplicación continuará funcionando siempre que dichas configuraciones no sean requeridas.

---

# Configuración inicial

Una vez instalado el proyecto se recomienda verificar:

- existencia de `Excel_Maestro.xlsx`;
- existencia de la carpeta `img/productos`;
- funcionamiento del Panel de Control;
- acceso a Git;
- correcta activación del entorno virtual.

Si todos estos puntos son correctos, el sistema se encuentra listo para utilizarse.

# Uso diario

Toda la administración del catálogo se realiza desde la aplicación:

```text
CatalogoMiMayo.exe
```

No es necesario ejecutar scripts manualmente.

La aplicación centraliza todas las tareas necesarias para mantener actualizado el catálogo.

---

# Panel de Control

El Panel de Control constituye el centro de operaciones del sistema.

Desde esta ventana se ejecutan todas las tareas habituales.

Las operaciones deben realizarse en el siguiente orden.

---

# 1. Importar Excel

Botón:

```text
Importar Excel
```

Permite seleccionar la lista de precios enviada por el proveedor.

Al confirmar la selección:

- se copia automáticamente el archivo;
- reemplaza el archivo `excel_proveedor.xlsx`;
- queda listo para la actualización.

No modifica el Excel Maestro.

---

# 2. Actualizar precios

Botón:

```text
Actualizar precios
```

Es la operación más importante del sistema.

Durante este proceso:

- se abre el Excel Maestro;
- se abre el Excel del proveedor;
- se comparan todos los productos por código;
- se detectan diferencias de precio;
- se actualizan únicamente los productos modificados;
- se registra automáticamente la fecha de modificación.

Al finalizar se muestra un resumen con:

- productos actualizados;
- productos sin cambios;
- productos inexistentes en el proveedor.

---

# 3. Abrir Excel Maestro

Botón:

```text
Abrir Excel Maestro
```

Abre el archivo principal del catálogo utilizando Microsoft Excel.

Permite:

- revisar información;
- agregar productos;
- corregir datos;
- verificar imágenes;
- realizar controles administrativos.

El sistema nunca modifica información distinta a los precios y la fecha de actualización.

---

# 4. Abrir Asistente de Imágenes

Botón:

```text
Abrir Asistente
```

Abre la herramienta encargada de administrar las imágenes del catálogo.

El asistente funciona de manera independiente del Panel de Control.

---

# 5. Regenerar JSON

Botón:

```text
Regenerar JSON
```

Reconstruye completamente el archivo:

```text
productos.json
```

utilizando exclusivamente la información del Excel Maestro.

Este proceso resulta útil cuando:

- se agregan productos nuevos;
- se modifica información del Excel;
- se actualizan imágenes;
- se corrigen categorías.

No modifica precios.

---

# 6. Publicar GitHub

Botón:

```text
Publicar
```

Realiza automáticamente:

- git add
- git commit
- git push

Al finalizar, la página web queda actualizada con los últimos cambios.

Este proceso requiere que la aplicación se ejecute desde la carpeta del proyecto que contiene el repositorio Git.

---

# Registro de eventos

La parte inferior del Panel de Control contiene un registro de actividades.

Su finalidad es informar al usuario todo lo que ocurre durante la ejecución.

Ejemplos:

- actualización completada;
- JSON generado;
- publicación realizada;
- errores;
- advertencias.

Este registro constituye la principal fuente de diagnóstico ante cualquier inconveniente.

---

# Asistente de Imágenes

El Asistente de Imágenes automatiza la incorporación de fotografías de productos.

Su objetivo es evitar renombrados manuales y mantener organizada la carpeta de imágenes.

---

# Flujo de trabajo

1. Copiar las imágenes nuevas en:

```text
img/pendientes/
```

2. Abrir el Asistente.

3. Seleccionar el producto correspondiente.

4. Confirmar la asignación.

Automáticamente el sistema:

- renombra la imagen;
- la mueve a `img/productos`;
- crea una copia de seguridad en `img/procesadas`;
- actualiza el nombre utilizado por el catálogo.

---

# Organización de imágenes

## Pendientes

```text
img/pendientes
```

Contiene únicamente imágenes nuevas.

Debe permanecer vacía cuando el trabajo se encuentra terminado.

---

## Productos

```text
img/productos
```

Contiene todas las imágenes utilizadas por la página web.

El archivo JSON hace referencia a esta carpeta.

---

## Procesadas

```text
img/procesadas
```

Conserva una copia de seguridad de todas las imágenes incorporadas mediante el asistente.

Nunca se utiliza en la página web.

Su única finalidad es permitir recuperar imágenes originales.

---

# Flujo recomendado de actualización

Cada vez que el proveedor envía una nueva lista de precios se recomienda seguir exactamente este procedimiento.

## Paso 1

Importar el Excel.

↓

## Paso 2

Actualizar precios.

↓

## Paso 3

Revisar el resumen de actualización.

↓

## Paso 4

Si existen productos nuevos:

- agregarlos al Excel Maestro;
- incorporar sus imágenes mediante el Asistente.

↓

## Paso 5

Regenerar JSON.

↓

## Paso 6

Publicar en GitHub.

↓

## Paso 7

Verificar la página web.

---

# Buenas prácticas

Se recomienda:

- mantener siempre cerrado el Excel Maestro durante las actualizaciones;
- no editar manualmente `productos.json`;
- conservar una copia de seguridad del Excel Maestro;
- no eliminar imágenes de `img/productos` sin verificar previamente el catálogo;
- ejecutar todas las operaciones desde el Panel de Control.

Siguiendo este procedimiento el mantenimiento completo del catálogo puede realizarse en pocos minutos y con mínima intervención manual.

# Arquitectura del sistema

El proyecto fue desarrollado siguiendo una arquitectura modular.

Cada módulo posee una única responsabilidad, facilitando el mantenimiento y la incorporación de nuevas funcionalidades.

La aplicación se divide en cuatro grandes bloques.

---

# 1. Interfaz gráfica

Carpeta:

```text
app/
```

Contiene exclusivamente la interfaz de usuario.

No implementa lógica de negocio.

Su responsabilidad consiste únicamente en:

- mostrar información;
- recibir acciones del usuario;
- ejecutar las operaciones correspondientes.

---

## main.py

Es el punto de entrada de la aplicación.

Responsabilidades:

- iniciar la aplicación;
- configurar CustomTkinter;
- registrar el icono de Windows;
- abrir el Panel de Control.

---

## ui.py

Construye toda la interfaz gráfica.

Responsabilidades:

- crear botones;
- mostrar el registro de eventos;
- organizar los controles;
- interactuar con el usuario.

---

## acciones.py

Funciona como intermediario entre la interfaz gráfica y la lógica del negocio.

Centraliza todas las operaciones ejecutadas desde los botones.

Ejemplos:

- importar Excel;
- actualizar precios;
- abrir el Excel Maestro;
- abrir el Asistente;
- generar JSON;
- publicar en GitHub.

---

# 2. Lógica de negocio

Carpeta:

```text
scripts/
```

Aquí reside toda la lógica del sistema.

Los módulos de esta carpeta no dependen de la interfaz gráfica.

Esto permite reutilizar la lógica desde otros programas o futuras interfaces.

---

Las principales responsabilidades son:

- lectura de Excel;
- validación de información;
- actualización de precios;
- generación del JSON;
- administración de imágenes;
- publicación del sitio.

---

# 3. Datos

Carpeta:

```text
data/
```

Contiene todos los archivos utilizados por la aplicación.

Actualmente:

- Excel Maestro;
- Excel del proveedor;
- productos.json.

Toda modificación realizada por el sistema termina almacenándose aquí.

---

# 4. Sitio Web

El catálogo web consume exclusivamente:

```text
productos.json
```

Nunca accede directamente al Excel.

Esto desacopla completamente la aplicación de escritorio del sitio web.

---

# Configuración centralizada

Todas las rutas del proyecto se encuentran definidas en:

```text
scripts/config.py
```

Esto evita repetir rutas en distintos módulos.

Cuando la estructura del proyecto cambia únicamente es necesario modificar este archivo.

---

# Entorno virtual

Todas las dependencias del proyecto se instalan dentro del entorno virtual.

La carpeta:

```text
venv/
```

no forma parte del proyecto distribuido y no debe incorporarse al repositorio.

---

# Compilación

El proyecto utiliza:

```text
PyInstaller
```

para generar los ejecutables.

Actualmente se generan dos aplicaciones independientes.

---

## Panel de Control

```text
CatalogoMiMayo.exe
```

Aplicación principal.

Permite administrar completamente el catálogo.

---

## Asistente de Imágenes

```text
AsistenteImagenes.exe
```

Aplicación auxiliar utilizada para incorporar imágenes.

Puede ejecutarse de manera independiente, aunque normalmente es iniciada desde el Panel de Control.

---

# build.bat

Toda la compilación del proyecto se realiza mediante:

```text
build.bat
```

No es necesario ejecutar comandos manuales de PyInstaller.

El script automatiza completamente el proceso.

---

## Proceso de compilación

Al ejecutarlo realiza automáticamente:

1. Activa el entorno virtual.

2. Elimina compilaciones anteriores.

3. Genera:

- CatalogoMiMayo.exe
- AsistenteImagenes.exe

4. Copia ambos ejecutables a la carpeta raíz del proyecto.

5. Copia los recursos necesarios.

6. Elimina archivos temporales.

---

# Cuándo ejecutar build.bat

Se recomienda recompilar únicamente cuando existan cambios en el código.

Ejemplos:

- nuevas funcionalidades;
- corrección de errores;
- cambios visuales;
- actualización de iconos.

No es necesario recompilar cuando únicamente cambian:

- Excel Maestro;
- Excel del proveedor;
- imágenes;
- productos.json.

---

# Git

La publicación del catálogo se encuentra integrada dentro del Panel de Control.

La aplicación ejecuta automáticamente:

```text
git add .
git commit
git push
```

Esto permite actualizar el sitio web sin utilizar la consola.

Para que esta funcionalidad opere correctamente la aplicación debe ejecutarse desde la carpeta del proyecto que contiene el repositorio Git.

---

# Distribución

Actualmente el proyecto se distribuye como una carpeta completa.

La estructura debe conservarse.

Los ejecutables trabajan utilizando los archivos presentes en el proyecto.

No se trata de una aplicación independiente compuesta por un único archivo.

---

# Desarrollo futuro

La arquitectura fue diseñada para permitir incorporar nuevas herramientas sin modificar el núcleo del sistema.

Ejemplos:

- administrador de promociones;
- editor de categorías;
- estadísticas;
- reportes;
- copias de seguridad automáticas;
- sincronización con otros proveedores.

Cada nueva herramienta podrá integrarse al Panel de Control manteniendo la misma arquitectura modular.

# Solución de problemas

A continuación se describen los inconvenientes más frecuentes y sus posibles soluciones.

---

## El Excel Maestro está abierto

### Síntoma

Durante la actualización aparece un error indicando que no fue posible guardar el archivo.

### Causa

Microsoft Excel mantiene bloqueado el archivo mientras permanece abierto.

### Solución

1. Cerrar completamente Excel.
2. Verificar que no exista ningún proceso de Excel ejecutándose en segundo plano.
3. Ejecutar nuevamente la actualización.

---

## No se encuentra el Excel Maestro

### Síntoma

El Panel de Control informa que no encuentra `Excel_Maestro.xlsx`.

### Verificar

- existencia del archivo dentro de `data/`;
- nombre correcto del archivo;
- estructura del proyecto.

---

## El Asistente de Imágenes no abre

### Verificar

- existencia de `AsistenteImagenes.exe`;
- existencia del archivo `logo.ico`;
- integridad de la carpeta del proyecto.

---

## No es posible publicar en GitHub

### Síntoma

Se informa:

```text
fatal: not a git repository
```

### Causa

La aplicación fue ejecutada fuera de la carpeta del proyecto.

### Solución

Ejecutar siempre `CatalogoMiMayo.exe` desde la carpeta raíz del proyecto que contiene el repositorio Git.

---

## Faltan imágenes en la página web

Verificar:

- que la imagen exista en `img/productos`;
- que el nombre coincida exactamente con el registrado en el Excel Maestro;
- que posteriormente se haya regenerado `productos.json`.

---

## El JSON no refleja cambios

Recordar que modificar únicamente el Excel Maestro no actualiza automáticamente el catálogo.

Siempre ejecutar:

1. Regenerar JSON.
2. Publicar en GitHub.

---

# Convenciones del proyecto

Durante el desarrollo se adoptaron las siguientes convenciones.

## Código

- nombres descriptivos;
- funciones pequeñas;
- una responsabilidad por módulo;
- evitar duplicación de código.

---

## Rutas

Todas las rutas se encuentran centralizadas en:

```text
scripts/config.py
```

No deben declararse rutas absolutas en otros módulos.

---

## Recursos

Las imágenes del catálogo siempre pertenecen a:

```text
img/productos/
```

Nunca deben almacenarse en otras carpetas.

---

## Datos

El Excel Maestro constituye la única fuente oficial de información.

El archivo `productos.json` siempre debe generarse a partir del Excel Maestro.

Nunca debe editarse manualmente.

---

# Mantenimiento

Para mantener el proyecto actualizado se recomienda:

- actualizar periódicamente las dependencias;
- realizar copias de seguridad del Excel Maestro;
- conservar el repositorio Git sincronizado;
- verificar el funcionamiento del Panel de Control luego de cada modificación importante;
- recompilar los ejecutables únicamente cuando existan cambios en el código.

---

# Historial de versiones

## v1.0.0

Primera versión estable.

Incluye:

- Panel de Control.
- Asistente de Imágenes.
- Actualización automática de precios.
- Generación automática de JSON.
- Publicación integrada en GitHub.
- Compilación mediante PyInstaller.
- Ejecutables independientes.
- Iconos personalizados.
- Uso de entorno virtual (`venv`).
- Automatización mediante `build.bat`.

---

# Roadmap

Las siguientes funcionalidades se encuentran previstas para futuras versiones.

## Aplicación

- Sistema de copias de seguridad automáticas.
- Historial de cambios.
- Estadísticas del catálogo.
- Registro detallado de operaciones.
- Administración de promociones.
- Gestión de categorías.
- Nuevos asistentes de mantenimiento.

---

## Sitio Web

- Placeholder para imágenes inexistentes.
- Lazy Loading.
- Botón "Volver arriba".
- Footer institucional.
- Mensaje legal.
- Botón flotante de WhatsApp.
- Optimización SEO.
- Revisión general de seguridad.
- Mejoras de rendimiento.
- Optimización para dispositivos móviles.

---

# Licencia

Este proyecto fue desarrollado como una herramienta interna para la administración del catálogo web del Mayorista Mi Mayo.

No está destinado a distribución pública ni uso comercial por terceros sin autorización del autor.

---

# Autor

**Daniel García**

Argentina

Desarrollado con Python, CustomTkinter, OpenPyXL y tecnologías web estándar.

---

# Observaciones finales

Este proyecto fue concebido con un objetivo principal:

automatizar completamente el mantenimiento del catálogo web del Mayorista Mi Mayo.

Toda nueva funcionalidad deberá respetar los principios que guiaron el desarrollo desde el inicio:

- simplicidad;
- modularidad;
- automatización;
- facilidad de mantenimiento;
- mínima intervención manual;
- escalabilidad.

Estos criterios deberán preservarse en futuras versiones para garantizar la evolución ordenada del sistema.
