# 🏢 SanSpace
**El Sistema Operativo para Espacios Inteligentes**

> **Estado:** Fase 1 (Infraestructura de Datos Automatizada y Poblada)
> **Versión:** 0.1.2

## 📖 Visión del Proyecto
SanSpace es una plataforma unificada diseñada para administrar "Edificios Inteligentes" (Oficinas, Coworkings, Escuelas). Fusiona tres pilares operativos en una sola interfaz para resolver el problema del "Edificio Ciego":

1.  **Seguridad Física (Módulo CloudGate):** Control de accesos mediante QR dinámicos, roles y registros de auditoría.
2.  **Infraestructura de Red (Módulos NetHealth & OmniIP):** Monitoreo de conectividad, gestión de IPs y dispositivos IoT.
3.  **Gestión de Activos (Módulo SanStore):** Inventario detallado, ubicación física exacta y auditoría de movimientos.

El objetivo es eliminar la gestión fragmentada (Excel, llaves físicas, sistemas aislados) y centralizar la operación mediante una arquitectura escalable y moderna.

## 🛠️ Stack Tecnológico
Este proyecto está construido con estándares modernos para garantizar su escalabilidad hasta el final de la carrera:

* **Lenguaje:** Python 3.14.0
* **Interfaz Gráfica:** PyQt6 (Desktop)
* **Base de Datos:** PostgreSQL 18 (Arquitectura Normalizada 4FN)
* **Gestión de Paquetes:** uv (Modern Python Packaging)
* **Arquitectura:** Modular (MVC - Model View Controller)

## 🚀 Guía de Instalación Rápida

### 1. Pre-requisitos
* PostgreSQL 18 corriendo en local.
* `uv` instalado en el sistema.
* Git instalado.

### 2. Configuración Inicial

    # 1. Clonar el repositorio
    git clone <URL_DEL_REPOSITORIO>
    cd SanSpace

    # 2. Instalar dependencias y crear entorno virtual
    uv sync

    # 3. Configurar secretos
    # Crea un archivo .env en la raíz con tus credenciales (ver docs/iniciar_nuevo_entorno.txt)

### 3. Despliegue Total (Zero-Config)
El proyecto cuenta con un script maestro `init_database.py` que realiza todo el aprovisionamiento en un solo paso. Al ejecutarlo:
1.  Crea el usuario y la base de datos (si no existen).
2.  Limpia esquemas antiguos (Hard Reset) y crea las 26 tablas.
3.  **Ejecuta automáticamente el Seeder** para poblar la base de datos con catálogos, usuarios de prueba y activos.

Ejecuta el siguiente comando en tu terminal:

    uv run src/scripts/init_database.py

### ⚠️ Solución de Problemas al Ejecutar Scripts
Si el comando anterior falla (error de ruta o módulo no encontrado), prueba estas alternativas según tu sistema operativo:

* **Opción A (Ruta estándar Linux/Mac/GitBash):**
  uv run src/scripts/init_database.py

* **Opción B (Ruta Windows PowerShell/CMD con backslash):**
  uv run src\scripts\init_database.py

* **Opción C (Ejecución como Módulo - Recomendada si hay problemas de imports):**
  uv run -m src.scripts.init_database

## 📂 Estructura del Proyecto
* `src/`: Código fuente Python (Modelos, Vistas, Controladores, Scripts).
* `database/`: Definiciones SQL (`schema.sql`).
* `docs/`: Documentación técnica, reglas del proyecto y guías de configuración.
* `assets/`: Recursos gráficos e iconos.

### 5. Arquitectura del Código (Source)
La lógica del sistema se organiza bajo los siguientes módulos:

* **`src/scripts/`**: Automatización y mantenimiento.
  * `init_database.py`: Orquestador maestro. Prepara la BD y ejecuta internamente el `seed_data.py`.
  * `seed_data.py`: Lógica de inserción de datos de prueba y catálogos (invocado por el init).
* **`src/utils/`**: Herramientas transversales.
  * `connection_database.py`: Singleton para gestión eficiente de conexiones PostgreSQL.
* **`database/`**:
  * `schema.sql`: Definición DDL de las 26 tablas y relaciones del sistema.

---
**SanSpace** - *Donde la Seguridad Física se encuentra con la Inteligencia Digital.*