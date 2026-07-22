# Manual del Usuario del Producto
## Sistema de Gestión de Restaurante: "El Pulpazo"

---

## 📋 Índice
1. [Introducción y Bienvenida](#1-introducción-y-bienvenida)
2. [Acceso al Sistema y Roles Operativos](#2-acceso-al-sistema-y-roles-operativos)
3. [Guía Paso a Paso de los Módulos](#3-guía-paso-a-paso-de-los-módulos)
   - [3.1 Plano Interactivo de Mesas](#31-plano-interactivo-de-mesas)
   - [3.2 Menú Digital y Tomar Pedido](#32-menú-digital-y-tomar-pedido)
   - [3.3 Carrito, Cobros e IVA (Checkout)](#33-carrito-cobros-e-iva-checkout)
   - [3.4 Control de Inventario e Insumos](#34-control-de-inventario-e-insumos)
   - [3.5 Dashboard Ejecutivo y Métricas](#35-dashboard-ejecutivo-y-métricas)
   - [3.6 Mantenimiento de Platillos (Panel Admin)](#36-mantenimiento-de-platillos-panel-admin)
4. [Herramientas Adicionales](#4-herramientas-adicionales)
5. [Preguntas Frecuentes y Solución de Problemas](#5-preguntas-frecuentes-y-solución-de-problemas)
6. [Guía de Carga y Consulta en OneDrive](#6-guía-de-carga-y-consulta-en-onedrive)

---

## 1. Introducción y Bienvenida

Bienvenido al **Manual del Usuario de El Pulpazo**. Este sistema es una plataforma web moderna para la administración integral de marisquerías y restaurantes. Permite controlar en tiempo real la distribución de comedores, la toma de comandas, el cobro con desglose del IVA del 16%, las existencias en inventario y el análisis ejecutivo de ventas.

### 🌐 Acceso Web Inmediato
Puedes acceder al sistema desde cualquier dispositivo (Computadora, Tablet o Celular) a través de la siguiente dirección:
👉 **[https://santiagopech490-alt.github.io/pescaderia_V3/](https://santiagopech490-alt.github.io/pescaderia_V3/)**

---

## 2. Acceso al Sistema y Roles Operativos

### 🔑 Inicio de Sesión
1. Abre tu navegador de internet e ingresa a la dirección web del sistema.
2. Introduce tu **Correo Electrónico** y **Contraseña** registrada.
3. Haz clic en el botón **`INICIAR SESIÓN`**.

### 👤 Perfiles y Permisos por Rol
El sistema adapta sus opciones según el puesto del empleado:

| Rol | Vistas Disponibles | Descripción de Permisos |
| :--- | :--- | :--- |
| **👑 Administrador** | *Todas las pantallas* | Acceso completo a mesas, edición de mapa, catálogo de platillos, inventario, reportes y finanzas. |
| **💵 Cajera** | *Mesas, Pedidos, Carrito, Inventario* | Gestión de cobros, registro de gastos/abonos, seguimiento de comedores y visualización del stock. |
| **🍽️ Mesero** | *Mesas, Menú de Clientes, Carrito* | Consulta rápida de ocupación de mesas, toma de comanda y envío a cocina. |

#### 🔑 Credenciales de Prueba por Defecto:
- **Administrador:** `admin@elpulpazo.com` / Contraseña: `admin123`
- **Cajera:** `cajero@pulpazo.com` / Contraseña: `cajera123`
- **Mesero:** `mesero@elpulpazo.com` / Contraseña: `mesero123`

---

## 3. Guía Paso a Paso de los Módulos

### 3.1 Plano Interactivo de Mesas
Permite visualizar la distribución física del salón de comedor en tiempo real.

* **Código de Colores de Mesas:**
  - 🟢 **Verde (Libre):** Mesa disponible para asignar nuevos comensales.
  - 🔴 **Rojo (Ocupado):** Mesa con clientes consumiendo y tiempo de apertura transcurrido.
  - 🟠 **Naranja (Reservado):** Mesa apartada para clientes futuros.

* **Acciones Rápidas:**
  1. Haz clic sobre cualquier mesa en el mapa.
  2. En el panel lateral, presiona **"Reservar Mesa"** o **"Liberar Mesa"** para actualizar su estado al instante.

* **Modo Edición del Mapa (Exclusivo Administrador):**
  1. Presiona el botón **`Editar Mesas`** en la barra superior.
  2. **Arrastrar y Soltar:** Haz clic sostenido sobre cualquier mesa y muévela a la posición deseada en la cuadrícula.
  3. **Personalizar:** Ajusta su forma (Rectangular o Circular), ancho, alto o ángulo de rotación.
  4. Haz clic en **`Salir de Edición`**. Las posiciones se guardarán automáticamente en la base de datos de Supabase.

---

### 3.2 Menú Digital y Tomar Pedido
Utilizado por meseros o clientes para seleccionar los platillos a consumir.

1. Entra a la sección **`Tomar Pedido`** (Menú).
2. Filtra la variedad de alimentos utilizando las pestañas superiores:
   - *Entradas* (Ceviches, Tostadas, Cócteles)
   - *Platos Fuertes* (Filetes, Caldos de Mariscos)
   - *Bebidas* (Micheladas, Aguas Frescas)
   - *Postres* (Pay de Limón)
3. Utiliza la **Barra de Búsqueda** para localizar un platillo por su nombre.
4. Para añadir un alimento al pedido, presiona el botón amarillo **`+ AGREGAR`**.

---

### 3.3 Carrito, Cobros e IVA (Checkout)
Punto de venta y liquidación de cuentas.

1. Ve a la sección **`Pedido Actual`** (Carrito).
2. **Seleccionar Mesa:** Es obligatorio elegir la mesa a la cual se le cargará la orden (ej. `Mesa A1`).
3. **Seleccionar Método de Pago:** Elige entre `Efectivo` o `Tarjeta`.
4. **Verificar Desglose Financiero:**
   - **Subtotal:** Suma directa de los precios de los productos.
   - **IVA (16%):** Impuesto retenido calculado automáticamente (`Subtotal * 0.16`).
   - **Total:** Monto definitivo a cobrar (`Subtotal + IVA`).
5. Haz clic en **`Proceder al Pago`** y confirma la transacción.
6. **Ticket Digital:** El sistema desplegará un ticket formal impreso en pantalla con folio único, fecha y desglose. La mesa cambiará automáticamente a color rojo (Ocupada).

---

### 3.4 Control de Inventario e Insumos
Gestión de la materia prima en almacén.

1. Entra a la sección **`Inventario`**.
2. Observa la lista de ingredientes clave (Pulpo, Camarón, Pescado, Limón, Aceite) con sus unidades de medida (`kg`, `L`, `g`, `unidades`).
3. **Semáforo de Stock:**
   - 🟢 **Saludable:** Stock actual por encima del mínimo requerido.
   - 🔴 **Bajo Stock:** El stock actual cayó por debajo del mínimo configurado.
4. **Ajuste Manual:** Selecciona un ingrediente, modifica su cantidad disponible (por ejemplo, al recibir una compra de proveedores) y guarda los cambios.

---

### 3.5 Dashboard Ejecutivo y Métricas
Panel financiero para la toma de decisiones.

1. Ingresa a la sección **`Dashboard Ejecutivo`**.
2. **Indicadores Clave (KPIs):**
   - **Ventas totales del día ($):** Suma del dinero ingresado en cobros.
   - **Comandas Activas:** Número de pedidos pendientes de cobro.
   - **Margen Operativo (%):** Porcentaje de rentabilidad del restaurante.
   - **Ocupación de Mesas (%):** Proporción de mesas ocupadas vs libres.
3. **Gráficas Interactivas:**
   - Gráfica de línea de tendencia de ventas por hora.
   - Gráfica de participación por categoría de productos.
   - Ranking de los platillos más vendidos.

---

### 3.6 Mantenimiento de Platillos (Panel Admin)
1. Ve a la sección **`Panel Admin`**.
2. Haz clic en **`+ Agregar Nuevo Platillo`**.
3. Ingresa nombre, descripción, precio, categoría y la imagen en URL.
4. Puedes activar o desactivar platillos con el interruptor de **Disponibilidad** o marcarlos como **Recomendado**.

---

## 4. Herramientas Adicionales

* **Toggle de Tema Claro / Oscuro:**
  En la esquina superior derecha del menú principal, haz clic en el icono del **Sol / Luna** para cambiar el tema visual de la pantalla. El sistema recordará tu preferencia automáticamente.
* **Respaldo de Datos (JSON):**
  En el menú de administración puedes presionar **`Exportar Datos`** para descargar un archivo comprimido JSON con el respaldo completo del restaurante.

---

## 5. Preguntas Frecuentes y Solución de Problemas

* **¿Qué hago si la página no carga los platillos o mesas?**
  Verifica tu conexión a internet. El sistema se conecta a la nube en Supabase. Si recargas la página (`F5`), los datos se volverán a sincronizar.
* **¿Se borran las mesas al cerrar el navegador?**
  No. En la versión actual V3, las posiciones, tamaños y rotaciones se guardan de forma permanente en la base de datos de Supabase.
* **¿Cómo entrego un ticket al cliente?**
  Al presionar "Proceder al Pago", el sistema muestra el Ticket Digital con su folio. Puedes imprimirlo o mostrarlo en pantalla.

---

## 6. Guía de Carga y Consulta en OneDrive

Para compartir este manual institucionalmente a través de **OneDrive**, sigue estos 3 simples pasos:

1. **Localizar el archivo en Word (`.docx`):**
   Abre la carpeta del proyecto en tu computadora:
   `C:\Users\santi\Downloads\pescaderia (1)\pescaderia_V3\MANUAL_DEL_USUARIO.docx`
2. **Subir a OneDrive:**
   - Abre tu navegador de internet y entra a [onedrive.live.com](https://onedrive.live.com) o al OneDrive de tu institución educativa.
   - Inicia sesión con tu correo.
   - Arrastra el archivo **`MANUAL_DEL_USUARIO.docx`** dentro de la ventana de OneDrive.
3. **Generar Enlace de Consulta Pública:**
   - Una vez subido, haz clic derecho sobre el archivo en OneDrive y selecciona **`Compartir`** (Share).
   - Asegúrate de cambiar los permisos a **"Cualquier persona con el enlace puede ver"** (Anyone with the link can view).
   - Haz clic en **`Copiar enlace`** (Copy link) y pégalo en el documento o tarea de tu asignatura.
