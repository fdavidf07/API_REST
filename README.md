<img width="549" height="385" alt="image" src="https://github.com/user-attachments/assets/26734dfa-91a6-4e38-974a-e494e3cdd91a" />


# 🏢 API de Gestión de Reservas de Espacios

Este proyecto es una **REST API** robusta desarrollada con **Django** y **Django REST Framework (DRF)**. Está diseñada para gestionar la reserva de salas y espacios físicos, implementando un sistema de permisos jerárquico y validaciones de disponibilidad en tiempo real.

---

## 🚀 Funcionalidades Principales

* **Gestión de Inventario:** CRUD completo de espacios y salas con control de capacidad.
* **Sistema de Reservas:** Motor de reservas con validación lógica para evitar solapamientos de horarios en un mismo espacio.
* **Seguridad y Roles:** * **Administradores:** Control total sobre espacios, usuarios y visualización de datos sensibles.
    * **Clientes:** Permisos restringidos para crear y ver sus propias reservas.
* **Privacidad de Datos (Data Masking):** Los usuarios tipo "Cliente" pueden ver la disponibilidad de las salas, pero la identidad de otros usuarios está anonimizada por seguridad.
* **Autenticación:** Sistema basado en el modelo de usuarios de Django y grupos de permisos.

## 🛠️ Stack Tecnológico

* **Backend:** Python 3.x, Django 5.x
* **API:** Django REST Framework (DRF)
* **Base de Datos:** SQLite (Desarrollo) / PostgreSQL (Producción)
* **Herramientas:** Git, Entornos Virtuales (venv)

## 🏗️ Arquitectura de Permisos y Grupos

El proyecto utiliza un sistema de **Autorización basado en Grupos**:
1.  **Grupo `Admins_Espacios`:** Personal con permisos para gestionar el catálogo de salas.
2.  **Grupo `Clientes`:** Usuarios finales que interactúan con la API para realizar reservas personales.

> Se ha implementado una lógica personalizada en los **Serializers** y **ViewSets** para asegurar que los datos sensibles (como quién reserva qué) solo sean visibles para el personal autorizado.

## ⚙️ Instalación y Uso

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/fdavidf07/API_REST.git](https://github.com/fdavidf07/API_REST.git)
