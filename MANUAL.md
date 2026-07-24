# Manual Técnico y Guía de Instalación (OT-5 - Versión 3.1)
## Proyecto: El Pulpazo - Sistema de Gestión de Restaurante y Marisquería

Este manual contiene las especificaciones técnicas para configurar el backend en Supabase, los scripts SQL v3.1 y la guía de operación para los 4 roles del personal.

---

## PARTE 1: Manual Técnico y Base de Datos

### 1. Requisitos del Entorno
* **Node.js:** Versión 18 o superior (Recomendado v20+).
* **Python:** Versión 3.12 (con `pytest` y `requests` instalados).
* **Base de Datos:** Proyecto en la nube en **Supabase** (PostgreSQL).

### 2. Configuración de Tablas SQL en Supabase (v3.1)

Para levantar la base de datos completa de v3.1, ejecuta en el **SQL Editor** de Supabase los siguientes scripts ubicados en la carpeta `supabase/`:

1. **`app_tables.sql`:** Crea las tablas de la aplicación (`app_platillos`, `app_mesas`, `app_pedidos`, `app_insumos`, `app_clientes`, `app_gastos`, `app_abonos`).
2. **`app_recetas.sql`:** Crea la tabla de recetas para vincular ingredientes y platillos con cantidades de consumo.
3. **`app_descuentos.sql`:** Crea la tabla de cupones de descuento (% y monto fijo).
4. **`app_notificaciones.sql`:** Crea la tabla de notificaciones flotantes del sistema.
5. **`app_repartidores.sql` y `app_entregas_repartidor.sql`:** Registro de logística a domicilio.
6. **`app_cortes.sql`:** Registro de cortes de caja diarios.
7. **`enable_rls_by_role.sql`:** Habilita las políticas Row Level Security (RLS) para los 4 roles.

---

### 3. Configuración de los 4 Roles de Usuario (Supabase Auth)

En la sección **Authentication** → **Users** de Supabase, crea los siguientes usuarios con sus metadatos de rol:

| Rol Operativo | Email | Contraseña | Metadatos de Usuario (`user_metadata`) |
| :--- | :--- | :--- | :--- |
| **Administrador** | `admin@elpulpazo.com` | `admin@elpulpazo` | `{"full_name": "Administrador", "role": "administrador"}` |
| **Cajera / Cajero** | `Cajero@Pulpazo.com` | `Cajero` | `{"full_name": "Cajera Principal", "role": "cajera"}` |
| **Mesero** | `mesero@elpulpazo.com` | `mesero123` | `{"full_name": "Mesero Turno", "role": "mesero"}` |
| **Cocina** | `cocina@elpulpazo.com` | `cocina123` | `{"full_name": "Jefe de Cocina", "role": "cocina"}` |

---

### 4. Variables de Entorno (.env)

Crea el archivo `.env` en la raíz del proyecto copiando `.env.example`:

```env
VITE_SUPABASE_URL=https://TU-PROYECTO.supabase.co
VITE_SUPABASE_ANON_KEY=tu-anon-key
```

### 5. Ejecución del Proyecto
```bash
npm install
npm run dev
```

---

## PARTE 2: Pruebas Automatizadas en Python (Pytest)

El proyecto cuenta con una suite completa de pruebas unitarias e integración en Python:

```bash
python -m pytest -v tests/test_pulpazo_suite.py
```

Validaciones incluidas en el testsuite:
1. Autenticación y RBAC para los 4 roles.
2. Carrito de compras, cálculo de IVA 16% y descuentos por cupón.
3. Modalidades de división de cuenta (Igual, Porcentaje, Manual).
4. Flujo de cocina Kanban (Pendiente ➔ En preparación ➔ Listo).
5. Descuento automático de inventario por recetas.
6. Notificaciones de alertas de stock.
