# Documento de Alcance y Requisitos (OT-1 - Versión 3.1)
## Proyecto: El Pulpazo - Sistema de Gestión de Restaurante y Marisquería

Este documento define formalmente el alcance de la versión 3.1 del sistema de operación del restaurante "El Pulpazo", integrando el frontend en React y el backend en la nube con Supabase.

---

## 1. Módulos y Alcance del Sistema (v3.1)

El sistema está compuesto por las siguientes vistas interactivas conectadas a Supabase:

### 1.1 Autenticación y Control de Acceso por Roles (RBAC)
* **Supabase Auth:** Inicio de sesión seguro con correo electrónico y contraseña.
* **4 Roles Operativos Reales:**
  * 👑 **Administrador (`admin@elpulpazo.com` / `admin@elpulpazo`):** Acceso total a todas las vistas, configuración de recetas, mapa de mesas, cupones, inventario, corte de caja y analítica.
  * 💵 **Cajera / Cajero (`Cajero@Pulpazo.com` / `Cajero`):** Gestión de cobros, corte de caja, gastos, abonos, clientes, cupones y seguimiento de comedores.
  * 🍽️ **Mesero (`mesero@elpulpazo.com` / `mesero123`):** Consulta del plano de mesas, toma de pedidos en el menú digital y carrito de compras.
  * 👨‍🍳 **Cocina (`cocina@elpulpazo.com` / `cocina123`):** Vista Kanban de pedidos en cocina y consulta de comandas.
* **Protección de Rutas:** Enforcement en 3 capas mediante `ProtectedRoute`, filtrado de menú en el Sidebar y componentes con permisos restringidos.

### 1.2 Vista de Cocina (Kanban)
* **Gestión de Comandas en Tiempo Real:** Organizada en 3 columnas: *Pendiente*, *En preparación* y *Listo*.
* **Cambio de Estado con un Clic:** Los cocineros pueden cambiar el estado del pedido, notificando automáticamente al mesero cuando la comanda está lista.

### 1.3 Inventario Automático con Recetas
* **Relación Platillo-Ingrediente:** Asignación de recetas en `app_recetas` que especifican qué cantidad de insumos consumen los platillos.
* **Decremento Automático de Stock:** Al procesar la venta de una orden, el sistema descuenta automáticamente los ingredientes requeridos del almacén.
* **Semáforo de Alertas:** Notificaciones en tiempo real al caer en nivel *Bajo Stock* o *Agotado*.

### 1.4 Sistema de Descuentos y Cupones
* **Gestión de Cupones:** Registro de cupones de descuento (% o monto fijo en `$`).
* **Aplicación en Checkout:** Validación de cupones activos al momento de liquidar la comanda.

### 1.5 División de Cuenta
* **3 Modalidades de División:**
  * *Igual:* Divide el total equitativamente entre N personas.
  * *Porcentaje:* Asigna un porcentaje específico a cada comensal.
  * *Manual:* Permite ingresar montos fijos por persona hasta cubrir el total.

### 1.6 Reportes de Ventas y Exportación CSV
* **Analítica Avanzada:** Gráficas de tendencia de ingresos por fecha, productos más vendidos y desglose por categorías.
* **Exportación a CSV:** Botón para descargar el reporte de ventas en formato hoja de cálculo Excel / CSV.

### 1.7 Plano Interactivo de Mesas
* **Persistencia en Supabase:** Posiciones, dimensiones, rotaciones e identificadores de mesas almacenados en la nube.
* **Modo Edición:** Permite arrastrar, rotar y cambiar la forma de las mesas en la cuadrícula de `900x450`.

### 1.8 Carrito de Compras, Cobros e IVA (16%)
* **Cálculo Automático:** Desglose del Subtotal, Descuento por cupón, IVA del 16% e importe Total.
* **Generación de Ticket Digital:** Emisión de comprobantes con folio único y fecha.

### 1.9 Sistema de Notificaciones Flotante
* **Campanita en Header:** Icono con badge de notificaciones no leídas para alertas de stock bajo y pedidos listos.

---

## 2. Requisitos No Funcionales

* **Usabilidad y Estética:** Interfaz en modo oscuro con acentos dorados (`#D4AF37`) y soporte para cambio a tema claro.
* **Seguridad Directa (RLS):** Políticas de seguridad a nivel de fila por rol en Supabase.
* **Tecnología:** React 18, TypeScript, Tailwind CSS v4, Vite, @supabase/supabase-js y Pytest (Python 3.12).
