# Plan de Pruebas y Estrategia de QA (OT-3 - Versión 3.1)
## Proyecto: El Pulpazo - Sistema de Gestión de Restaurante y Marisquería

Este documento establece la estrategia y los casos de prueba para validar el funcionamiento integrado de la versión 3.1 del sistema "El Pulpazo" con Supabase y las pruebas automatizadas en Python (Pytest).

---

## 1. Alcance y Ambientes de Prueba

* **Ambiente Web Local:** `http://localhost:5173/pescaderia_V3/`
* **Ambiente Web Producción:** `https://santiagopech490-alt.github.io/pescaderia_V3/`
* **Framework de Pruebas Backend:** Python 3.12 + `pytest`.
* **Usuarios de Prueba por Rol:**
  * **Administrador:** `admin@elpulpazo.com` / `admin@elpulpazo`
  * **Cajera / Cajero:** `Cajero@Pulpazo.com` / `Cajero`
  * **Mesero:** `mesero@elpulpazo.com` / `mesero123`
  * **Cocina:** `cocina@elpulpazo.com` / `cocina123`

---

## 2. Casos de Prueba (Checklist v3.1)

### 2.1 Caso de Prueba 01: Autenticación y RBAC (4 Roles)
* **Pasos:** Iniciar sesión con cada una de las 4 cuentas.
* **Resultado Esperado:** Redirección a la vista predeterminada según rol y filtrado automático de opciones del Sidebar.

### 2.2 Caso de Prueba 02: Vista de Cocina Kanban
* **Pasos:** Como usuario de Cocina, mover una comanda de "Pendiente" a "En preparación" y finalmente a "Listo".
* **Resultado Esperado:** Cambio de columna exitoso y emisión de notificación "Pedido listo" al mesero.

### 2.3 Caso de Prueba 03: Inventario Automático con Recetas
* **Pasos:** Confirmar la venta de 3 Ceviches Mixtos.
* **Resultado Esperado:** El sistema descuenta automáticamente 600g de Pulpo Fresco de la tabla de inventario en base a la receta.

### 2.4 Caso de Prueba 04: Aplicación de Cupones de Descuento
* **Pasos:** En la pantalla de cobro, aplicar el cupón `MARISCO10`.
* **Resultado Esperado:** Aplica un 10% de descuento sobre el subtotal y recalcula el IVA del 16% sobre la cantidad neta a pagar.

### 2.5 Caso de Prueba 05: División de Cuenta
* **Pasos:** En el checkout de una cuenta de $300, seleccionar la modalidad "División Igual" entre 3 personas.
* **Resultado Esperado:** Genera 3 cuotas exactas de $100.00 cada una.

### 2.6 Caso de Prueba 06: Suite Automatizada de Pytest
* **Ejecución:** `python -m pytest -v tests/test_pulpazo_suite.py`
* **Resultado Esperado:** 12 pruebas unitarias e integración aprobadas al 100% (PASSED) en consola.
