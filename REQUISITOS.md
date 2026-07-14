# Documento de Alcance y Requisitos (OT-1)
## Proyecto: El Pulpazo - Sistema de Gestión de Restaurante

Este documento define formalmente el alcance de la versión actual del frontend y los requisitos acordados para el sistema de operación del restaurante "El Pulpazo".

---

## 1. Módulos y Alcance del Frontend

El sistema está compuesto por las siguientes vistas y componentes clave:

### 1.1 Módulo de Acceso (Login)
* **Pantalla de Inicio de Sesión:** Permite el ingreso de usuarios mediante nombre de usuario/correo y contraseña.
* **Roles Operativos Simulados:** Soporta acceso administrativo y operativo.
* **Seguridad Visual:** Opción para mostrar/ocultar la contraseña y recordar credenciales.
* **Accesos Alternativos:** Botones simulados para inicio de sesión alternativo (Facebook/Instagram).

### 1.2 Plano Interactivo de Mesas (Mapa de Mesas)
* **Visualización en Tiempo Real:** Renderizado en formato SVG de mesas circulares y rectangulares con sus respectivos identificadores.
* **Control de Estados:** Identificación por colores del estado de la mesa:
  * 🟢 **Libre:** Disponible para asignar clientes.
  * 🔴 **Ocupado:** Con comanda activa y tiempo transcurrido desde la apertura.
  * 🟠 **Reservado:** Mesa apartada para clientes futuros.
* **Modo de Edición (Administrador):**
  * **Agregar Mesa:** Botón para añadir nuevas mesas configurando identificadores automáticos.
  * **Drag and Drop:** Permite arrastrar y reubicar las mesas en la cuadrícula del mapa mediante eventos de mouse o táctiles.
  * **Eliminar/Modificar:** Opciones de ajuste de forma y tamaño.

### 1.3 Menú Digital del Cliente
* **Categorías de Platillos:** Navegación filtrada por: *Entradas, Platos Fuertes, Bebidas y Postres*.
* **Buscador Integrado:** Filtrado de platillos por nombre en tiempo real.
* **Detalle de Producto:** Nombre, descripción, precio, imagen y etiquetas ("Recomendado" o "Disponible").
* **Añadir al Carrito:** Selección rápida de artículos para conformar la comanda.

### 1.4 Carrito de Compras y Cobros (Checkout)
* **Gestión de Comanda:** Incremento, decremento o eliminación de productos del carrito.
* **Asignación de Mesa:** Selector obligatorio de mesa activa para registrar la comanda.
* **Método de Pago:** Selección de método de pago (Efectivo, Tarjeta de Crédito, Transferencia).
* **Confirmación de Orden:** Botón para enviar la orden y actualizar el estado de la mesa a "Ocupado".

### 1.5 Panel de Administración de Menú
* **Mantenimiento de Platillos (CRUD):**
  * **Agregar Nuevo Platillo:** Modal para registrar nombre, descripción, precio, categoría y URL de la imagen.
  * **Control de Disponibilidad:** Switch interactivo para marcar si un plato está disponible o agotado.
  * **Recomendaciones:** Botón para marcar platos sugeridos de la casa.
  * **Eliminar:** Opción para remover platillos del catálogo.

### 1.6 Inventario de Insumos (Ingredientes)
* **Control de Stock:** Visualización detallada de ingredientes clave (Camarón, Pulpo, Pescado, Limón, etc.) con sus unidades de medida (kg, unidades).
* **Alertas de Nivel Crítico:** Indicadores visuales de advertencia (color rojo) cuando el stock actual está por debajo del stock mínimo configurado.
* **Gestión de Inventario (CRUD):** Opciones para añadir insumos, ajustar cantidades y eliminarlos.

### 1.7 Historial de Pedidos
* **Registro de Transacciones:** Listado cronológico de órdenes completadas o pendientes.
* **Detalle del Ticket:** Visualización de los platillos solicitados, cantidad, método de pago, mesa asignada y total cobrado.

### 1.8 Dashboard Ejecutivo (Métricas)
* **Indicadores Clave (KPIs):** Ventas totales del día, número de pedidos activos, margen operativo (%) y porcentaje de ocupación de mesas.
* **Gráfica de Ventas del Día:** Gráfica de línea interactiva que muestra la evolución de las ventas por hora.
* **Gráfica de Distribución de Ventas:** Gráfica de dona que muestra la participación por categoría de platillos (Entradas vs Bebidas, etc.).
* **Platos Más Vendidos:** Tabla resumen de los platos con mayor volumen de venta.

---

## 2. Requisitos No Funcionales

* **Usabilidad y Estética:** Interfaz con diseño premium en modo oscuro, utilizando contrastes en oro (`#D4AF37`) y tipografía moderna (`Outfit`).
* **Diseño Responsivo:** Adaptabilidad de los componentes para funcionar correctamente en tablets y pantallas de escritorio.
* **Rendimiento:** Tiempos de respuesta óptimos en el filtrado y renderizado del mapa.
* **Tecnología:** Desarrollado con **React 18**, **TypeScript**, **Tailwind CSS v4** y **Vite**.
