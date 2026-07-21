# Documento de Alcance y Requisitos (OT-1)
## Proyecto: El Pulpazo - Sistema de Gestión de Restaurante

Este documento define formalmente el alcance final y los requisitos del sistema de operación del restaurante "El Pulpazo", integrando el frontend en React y el backend de base de datos en la nube con Supabase.

---

## 1. Módulos y Alcance del Sistema (Frontend + Database)

El sistema está compuesto por las siguientes vistas interactivas conectadas a Supabase:

### 1.1 Autenticación y Control de Roles (Supabase Auth)
* **Inicio de Sesión:** Permite el ingreso seguro de usuarios mediante email y contraseña registrados en Supabase Auth.
* **Perfiles de Usuario:** Vincula cada usuario de autenticación con un perfil operativo (`profiles`) para mostrar su nombre e iniciales en el header.
* **Roles Operativos Reales:** Se implementan 3 roles operativos con vistas personalizadas y permisos específicos en el frontend:
  * 👑 **Administrador:** Acceso completo a todas las pantallas, configuraciones de menú, inventario y finanzas.
  * 💵 **Cajera:** Acceso a control de mesas, cobros, gastos, abonos e historial de pedidos.
  * 🍽️ **Mesero:** Acceso limitado a ver el plano de mesas, tomar pedidos y ver la carta.
* **Seguridad de Rutas:** Protección de vistas mediante componentes de ruta protegida (`ProtectedRoute`) en React Router.

### 1.2 Plano Interactivo de Mesas
* **Persistencia en la Nube:** Las posiciones (`pos_x`, `pos_y`), dimensiones (`ancho`, `alto`, `radio`), rotaciones e identificadores de las mesas se leen y guardan directamente en la tabla `app_mesas` de Supabase.
* **Estados en Tiempo Real:** El color de la mesa representa su estado real almacenado:
  * 🟢 **Libre:** Disponible para asignar clientes.
  * 🔴 **Ocupado:** Con comanda activa y tiempo transcurrido desde la apertura.
  * 🟠 **Reservado:** Mesa apartada para clientes.
* **Modo de Edición (Administrador):**
  * **Agregar Mesa:** Botón para añadir nuevas mesas configurando identificadores automáticos.
  * **Drag and Drop:** Permite arrastrar y reubicar las mesas en la cuadrícula de `900x450` del mapa, guardando la nueva posición inmediatamente en la base de datos.
  * **Eliminar/Modificar:** Opciones de ajuste de forma (circular/rectangular), tamaño y rotación.

### 1.3 Menú Digital del Cliente
* **Categorías de Platillos:** Navegación por pestañas: *Entradas, Platos Fuertes, Bebidas y Postres* alimentado desde la tabla `app_platillos`.
* **Buscador Integrado:** Filtrado de platillos por nombre en tiempo real.
* **Detalle de Producto:** Nombre, descripción, precio, imagen y etiquetas ("Recomendado" o "Disponible").
* **Añadir al Carrito:** Selección rápida de artículos para conformar la comanda.

### 1.4 Carrito de Compras y Cobros (Checkout)
* **Gestión de Comanda:** Incremento, decremento o eliminación de productos del carrito.
* **Asignación de Mesa:** Selector obligatorio de mesa activa para registrar la comanda.
* **Método de Pago:** Selección de método de pago (Efectivo o Tarjeta) correspondiente a los métodos válidos del sistema.
* **Generación de Ticket:** Al confirmar el pedido, el backend calcula automáticamente el IVA del 16%, genera un folio de ticket único y registra la orden en `app_pedidos`.

### 1.5 Panel de Administración de Menú
* **Mantenimiento de Platillos (CRUD):**
  * **Agregar Nuevo Platillo:** Modal para registrar nombre, descripción, precio, categoría y URL de la imagen.
  * **Control de Disponibilidad:** Switch interactivo para marcar si un plato está disponible o agotado en la base de datos.
  * **Recomendaciones:** Botón para marcar platos sugeridos de la casa.
  * **Eliminar:** Opción para remover platillos del catálogo.

### 1.6 Inventario de Insumos (Ingredientes)
* **Control de Stock:** Visualización de ingredientes clave (Camarón, Pulpo, Pescado, Limón, etc.) desde la tabla `app_insumos` con unidades de medida (kg, L, g, ml, unidades, paquetes).
* **Alertas de Nivel Crítico:** Indicadores visuales de advertencia (color rojo) cuando el stock actual está por debajo del stock mínimo configurado.
* **Gestión de Inventario (CRUD):** Opciones para añadir insumos, ajustar cantidades manualmente y eliminarlos.

### 1.7 Historial de Pedidos
* **Registro de Transacciones:** Listado cronológico de órdenes completadas o pendientes desde la base de datos.
* **Detalle del Ticket:** Visualización de los platillos solicitados, cantidad, método de pago, mesa asignada, subtotal, IVA y total cobrado.

### 1.8 Dashboard Ejecutivo (Métricas)
* **Indicadores Clave (KPIs):** Ventas totales del día, número de pedidos activos, margen operativo (%) y porcentaje de ocupación de mesas calculados en tiempo real.
* **Gráfica de Ventas del Día:** Gráfica interactiva de ventas por hora.
* **Gráfica de Distribución de Ventas:** Gráfica de dona por categoría de platillos.
* **Platos Más Vendidos:** Tabla resumen alimentada por la vista `vw_ProductosMasVendidos`.

### 1.9 Módulos Auxiliares de Administración
* **Clientes:** Control de datos de contacto de clientes recurrentes (`app_clientes`).
* **Gastos:** Registro de egresos administrativos de materia prima o insumos (`app_gastos`).
* **Abonos:** Registro de pagos de clientes fiados (`app_abonos`).
* **Respaldo local:** Opción para exportar e importar la base de datos del cliente en formato JSON.

---

## 2. Arquitectura de Base de Datos y Backend (Supabase)

La base de datos PostgreSQL está estructurada en dos capas principales:

1. **Tablas de la aplicación (`app_*`):** Permiten la persistencia directa y ágil de la interfaz frontend.
2. **Esquema Relacional Original (`schema.sql`):** Estructura relacional completa que consta de 17 tablas (Roles, Usuarios, Categorias, Productos, Ingredientes, Recetas, Proveedores, Compras, DetalleCompras, MovimientosInventario, Mesas, Clientes, MetodosPago, Pedidos, DetallePedidos, Pagos y Profiles).

### Triggers y Funciones de Base de Datos:
* **Cálculo de Totales:** triggers automáticos que recalculan los totales al agregar ítems a pedidos o compras.
* **Descuento Automático de Inventario:** El trigger `trg_SalidaInventario` descuenta ingredientes de la tabla de inventario en base a la receta asignada del producto vendido.
* **Liberación de Mesa:** Trigger `trg_LiberarMesa` que cambia el estado de la mesa a "libre" una vez completado y cobrado el pedido.

---

## 3. Requisitos No Funcionales

* **Usabilidad y Estética:** Interfaz con diseño premium en modo oscuro, utilizando contrastes en oro (`#D4AF37`) y tipografía moderna (`Outfit`).
* **Soporte de Tema:** Toggle para cambiar entre modo claro y oscuro con persistencia local.
* **Seguridad Directa (RLS):** Uso de políticas de seguridad a nivel de fila (Row Level Security) para proteger el acceso a las tablas según el rol autenticado.
* **Tecnología:** Desarrollado con **React 18**, **TypeScript**, **Tailwind CSS v4**, **Vite** y **@supabase/supabase-js**.
