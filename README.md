# 🏢 SanSpace
**El Sistema Operativo para Espacios Inteligentes**

> **Estado:** Fase 1 (Cimientos de Datos y Estructura)
> **Versión:** 0.1.0

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
```bash
# 1. Clonar el repositorio
git clone <URL_DEL_REPOSITORIO>
cd SanSpace

# 2. Instalar dependencias y crear entorno virtual
uv sync

# 3. Configurar secretos
# Crea un archivo .env en la raíz con tus credenciales (ver docs/iniciar_nuevo_entorno.txt)
```

### 3. Despliegue de Base de Datos
El proyecto incluye un script de **"Zero-Config Database"**. No necesitas ejecutar SQL manual.

```bash
uv run src/scripts/init_database.py
```
*Este comando solicitará tu contraseña de root (postgres) y creará automáticamente el usuario de la aplicación, la base de datos `sanspace_db` y las 26 tablas del esquema definido.*

### 4. 📂 Estructura del Proyecto
* `src/`: Código fuente Python (Modelos, Vistas, Controladores, Scripts).
* `database/`: Definiciones SQL (`schema.sql`).
* `docs/`: Documentación técnica, reglas del proyecto y guías de configuración.
* `assets/`: Recursos gráficos e iconos.

### 5. Arquitectura del Código (Source)
La lógica del sistema se organiza en `src/` bajo los siguientes módulos:

* **`src/scripts/`**: Automatización y mantenimiento.
  * `init_database.py`: Script de aprovisionamiento Zero-Config (Crea DB y Tablas).
* **`src/utils/`**: Herramientas transversales.
  * `connection_database.py`: Clase administradora de la conexión a PostgreSQL (Singleton pattern).
* **`database/`**:
  * `schema.sql`: Definición DDL de las 26 tablas y relaciones del sistema.

---
**SanSpace** - *Donde la Seguridad Física se encuentra con la Inteligencia Digital.*