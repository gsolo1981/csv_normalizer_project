<<<<<<< HEAD
# CSV Normalizer Project

Proyecto Python para normalizar y consolidar múltiples archivos CSV con diferentes estructuras en un archivo Excel unificado.

## Estructura del Proyecto

```
csv_normalizer_project/
├── data/                                    # Carpeta con archivos CSV de entrada
│   ├── SIGAF_CONSULTA_1202506121604.csv
│   ├── MIA_CONSULTA_1202506121540.csv
│   ├── SIGAF_CONSULTA_2202506121605.csv
│   ├── bac mails2.csv
│   └── mails bac1.csv
├── main.py                                  # Script principal
├── requirements.txt                         # Dependencias
└── README.md                               # Este archivo
```

## Instalación

### 1. Clonar o descargar el proyecto

Extrae todos los archivos en una carpeta llamada `csv_normalizer_project`

### 2. Crear entorno virtual (recomendado)

```bash
# Crear entorno virtual
python -m venv csv_normalizer_env

# Activar entorno virtual
# En Windows:
csv_normalizer_env\Scripts\activate
# En Linux/Mac:
source csv_normalizer_env/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

## Configuración

### Preparar los archivos de entrada

1. Crea una carpeta llamada `data` en el directorio del proyecto
2. Coloca los siguientes archivos CSV en la carpeta `data/`:
   - `SIGAF_CONSULTA_1202506121604.csv`
   - `MIA_CONSULTA_1202506121540.csv`
   - `SIGAF_CONSULTA_2202506121605.csv`
   - `bac mails2.csv`
   - `mails bac1.csv`

## Uso

### Ejecutar el script

```bash
python main.py
```

El script procesará todos los archivos CSV y generará un archivo Excel llamado `consolidated_data.xlsx` con los datos normalizados.

## Mapeo de Campos

### Archivo de salida

El archivo Excel resultante tendrá las siguientes columnas:

1. **fullname** - Nombre completo
2. **email** - Correo electrónico
3. **user** - Usuario/ID
4. **application** - Sistema de origen
5. **C_JURIS** - Código jurisdicción
6. **XL_INSTITUCION** - Institución
7. **C_UNID_EJEC** - Código unidad ejecutora
8. **XL_UNID_EJEC** - Unidad ejecutora

### Mapeo por archivo

#### SIGAF_CONSULTA_1202506121604.csv → "SIGAF Internos"
- **fullname**: XC_USER
- **email**: XL_EMAIL
- **user**: C_USER
- **application**: "SIGAF Internos"
- **C_JURIS**: C_JURIS
- **XL_INSTITUCION**: XL_INSTITUCION
- **C_UNID_EJEC**: C_UNID_EJEC
- **XL_UNID_EJEC**: XL_UNID_EJEC

#### MIA_CONSULTA_1202506121540.csv → "MIA"
- **fullname**: FirstName + LastName
- **email**: Email
- **user**: UserName
- **application**: "MIA"
- **C_JURIS**: NULL
- **XL_INSTITUCION**: NULL
- **C_UNID_EJEC**: NULL
- **XL_UNID_EJEC**: NULL

#### SIGAF_CONSULTA_2202506121605.csv → "SIGAF Externos"
- **fullname**: XL_ENTE
- **email**: XL_MAIL
- **user**: N_CUIT
- **application**: "SIGAF Externos"
- **C_JURIS**: NULL
- **XL_INSTITUCION**: NULL
- **C_UNID_EJEC**: NULL
- **XL_UNID_EJEC**: NULL

#### bac mails2.csv → "BAC Externos"
- **fullname**: RazonSocial (o Nombre + Apellido si RazonSocial es NULL)
- **email**: LoweredEmail
- **user**: usuario
- **application**: "BAC Externos"
- **C_JURIS**: NULL
- **XL_INSTITUCION**: NULL
- **C_UNID_EJEC**: NULL
- **XL_UNID_EJEC**: NULL

#### mails bac1.csv → "BAC Internos"
- **fullname**: Nombre + Apellido
- **email**: LoweredEmail
- **user**: usuario
- **application**: "BAC Internos"
- **C_JURIS**: NULL
- **XL_INSTITUCION**: NULL
- **C_UNID_EJEC**: NULL
- **XL_UNID_EJEC**: NULL

## Características

- ✅ **Manejo robusto de encodings**: Automáticamente detecta y maneja UTF-8, CP1252, Latin1
- ✅ **Procesamiento de diferentes delimitadores**: Maneja comas (,) y punto y coma (;)
- ✅ **Limpieza de datos**: Normaliza espacios, convierte emails a minúsculas, maneja valores NULL
- ✅ **Validación de archivos**: Informa archivos faltantes y errores de procesamiento
- ✅ **Reportes detallados**: Muestra progreso y estadísticas por aplicación
- ✅ **Formato de salida Excel**: Genera archivo .xlsx fácil de usar

## Salida del programa

El script mostrará información detallada durante la ejecución:

```
Iniciando proceso de normalización de CSV...
==================================================
Procesando SIGAF Internos: data\SIGAF_CONSULTA_1202506121604.csv
✓ Procesado exitosamente: SIGAF_CONSULTA_1202506121604.csv (X registros)
...
==================================================
Datos consolidados exitosamente
Limpiando datos...
✓ Archivo Excel guardado exitosamente: consolidated_data.xlsx
Total de registros: X

Resumen por aplicación:
  - SIGAF Internos: X registros
  - MIA: X registros
  - SIGAF Externos: X registros
  - BAC Externos: X registros
  - BAC Internos: X registros
==================================================
Proceso completado exitosamente!
```

## Solución de problemas

### Error: "La carpeta data no existe"
- Asegúrate de crear la carpeta `data` en el mismo directorio que `main.py`
- Verifica que los archivos CSV están en la carpeta `data`

### Error: "No se pudo leer el archivo con ningún encoding"
- Verifica que los archivos CSV no estén corruptos
- Asegúrate de que los nombres de archivo coincidan exactamente

### Error al instalar dependencias
- Asegúrate de tener Python 3.7 o superior instalado
- Actualiza pip: `pip install --upgrade pip`

## Requisitos del sistema

- Python 3.7 o superior
- Pandas 2.0.0 o superior
- OpenPyXL 3.1.0 o superior
- NumPy 1.24.0 o superior

## Licencia

=======
# CSV Normalizer Project

Proyecto Python para normalizar y consolidar múltiples archivos CSV con diferentes estructuras en un archivo Excel unificado.

## Estructura del Proyecto

```
csv_normalizer_project/
├── data/                                    # Carpeta con archivos CSV de entrada
│   ├── SIGAF_CONSULTA_1202506121604.csv
│   ├── MIA_CONSULTA_1202506121540.csv
│   ├── SIGAF_CONSULTA_2202506121605.csv
│   ├── bac mails2.csv
│   └── mails bac1.csv
├── main.py                                  # Script principal
├── requirements.txt                         # Dependencias
└── README.md                               # Este archivo
```

## Instalación

### 1. Clonar o descargar el proyecto

Extrae todos los archivos en una carpeta llamada `csv_normalizer_project`

### 2. Crear entorno virtual (recomendado)

```bash
# Crear entorno virtual
python -m venv csv_normalizer_env

# Activar entorno virtual
# En Windows:
csv_normalizer_env\Scripts\activate
# En Linux/Mac:
source csv_normalizer_env/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

## Configuración

### Preparar los archivos de entrada

1. Crea una carpeta llamada `data` en el directorio del proyecto
2. Coloca los siguientes archivos CSV en la carpeta `data/`:
   - `SIGAF_CONSULTA_1202506121604.csv`
   - `MIA_CONSULTA_1202506121540.csv`
   - `SIGAF_CONSULTA_2202506121605.csv`
   - `bac mails2.csv`
   - `mails bac1.csv`

## Uso

### Ejecutar el script

```bash
python main.py
```

El script procesará todos los archivos CSV y generará un archivo Excel llamado `consolidated_data.xlsx` con los datos normalizados.

## Mapeo de Campos

### Archivo de salida

El archivo Excel resultante tendrá las siguientes columnas:

1. **fullname** - Nombre completo
2. **email** - Correo electrónico
3. **user** - Usuario/ID
4. **application** - Sistema de origen
5. **NombreUnidad** - Nombre de la unidad organizacional

### Mapeo por archivo

#### SIGAF_CONSULTA_1202506121604.csv → "SIGAF Internos"
- **fullname**: XC_USER
- **email**: XL_EMAIL
- **user**: C_USER
- **application**: "SIGAF Internos"
- **NombreUnidad**: Concatenación de C_UNID_EJEC + " - " + XL_UNID_EJEC

#### MIA_CONSULTA_1202506121540.csv → "MIA"
- **fullname**: FirstName + LastName
- **email**: Email
- **user**: UserName
- **application**: "MIA"
- **NombreUnidad**: NULL

#### SIGAF_CONSULTA_2202506121605.csv → "SIGAF Externos"
- **fullname**: XL_ENTE
- **email**: XL_MAIL
- **user**: N_CUIT
- **application**: "SIGAF Externos"
- **NombreUnidad**: NULL

#### bac mails2.csv → "BAC Externos"
- **fullname**: RazonSocial (o Nombre + Apellido si RazonSocial es NULL)
- **email**: LoweredEmail
- **user**: usuario
- **application**: "BAC Externos"
- **NombreUnidad**: NULL

#### mails bac1.csv → "BAC Internos"
- **fullname**: Nombre + Apellido
- **email**: LoweredEmail
- **user**: usuario
- **application**: "BAC Internos"
- **NombreUnidad**: Campo NombreUnidad del archivo original

## Características

- ✅ **Manejo robusto de encodings**: Automáticamente detecta y maneja UTF-8, CP1252, Latin1
- ✅ **Procesamiento de diferentes delimitadores**: Maneja comas (,) y punto y coma (;)
- ✅ **Limpieza de datos**: Normaliza espacios, convierte emails a minúsculas, maneja valores NULL
- ✅ **Validación de archivos**: Informa archivos faltantes y errores de procesamiento
- ✅ **Reportes detallados**: Muestra progreso y estadísticas por aplicación
- ✅ **Formato de salida Excel**: Genera archivo .xlsx fácil de usar
- ✅ **Campo NombreUnidad**: Manejo específico por tipo de aplicación

## Salida del programa

El script mostrará información detallada durante la ejecución:

```
Iniciando proceso de normalización de CSV...
==================================================
Procesando SIGAF Internos: data\SIGAF_CONSULTA_1202506121604.csv
✓ Procesado exitosamente: SIGAF_CONSULTA_1202506121604.csv (X registros)
...
==================================================
Datos consolidados exitosamente
Limpiando datos...
✓ Archivo Excel guardado exitosamente: consolidated_data.xlsx
Total de registros: X

Resumen por aplicación:
  - SIGAF Internos: X registros
  - MIA: X registros
  - SIGAF Externos: X registros
  - BAC Externos: X registros
  - BAC Internos: X registros
==================================================
Proceso completado exitosamente!
```

## Cambios en la estructura de datos

### Campos eliminados
- **C_JURIS** - Código jurisdicción
- **XL_INSTITUCION** - Institución
- **C_UNID_EJEC** - Código unidad ejecutora
- **XL_UNID_EJEC** - Unidad ejecutora

### Campo agregado
- **NombreUnidad** - Nombre de la unidad organizacional con lógica específica por aplicación

## Solución de problemas

### Error: "La carpeta data no existe"
- Asegúrate de crear la carpeta `data` en el mismo directorio que `main.py`
- Verifica que los archivos CSV están en la carpeta `data`

### Error: "No se pudo leer el archivo con ningún encoding"
- Verifica que los archivos CSV no estén corruptos
- Asegúrate de que los nombres de archivo coincidan exactamente

### Error al instalar dependencias
- Asegúrate de tener Python 3.7 o superior instalado
- Actualiza pip: `pip install --upgrade pip`

## Requisitos del sistema

- Python 3.7 o superior
- Pandas 2.0.0 o superior
- OpenPyXL 3.1.0 o superior
- NumPy 1.24.0 o superior

## Licencia

>>>>>>> ed20375 (Implement CSV normalization process for multiple input files, including SIGAF, MIA, and BAC data. Add functionality to read, process, and consolidate data into a single Excel output. Update requirements and add logging for successful processing and error handling.)
Este proyecto es de uso libre para fines educativos y comerciales.