# MANUAL DEL USUARIO
## Sistema de Gestión de Restaurante: "El Pulpazo"

---

## 1. Portada y Control de Versiones

| Parámetro | Detalle |
| :--- | :--- |
| **Nombre del Sistema:** | El Pulpazo — Sistema de Gestión de Restaurante y Marisquería |
| **Versión del Manual:** | v3.0 (Versión Final con Integración Supabase) |
| **Fecha de Actualización:** | 22 de Julio de 2026 |
| **Asignatura:** | Tópicos de calidad para el desarrollo de software (Actividad 5) |
| **Equipo de Desarrollo:** | Lopez Estrella Brandon Oliver, Castro Nuñez Norberto Manuel, Pech Ake Santiago Asahel, May de los Santos Juan Jesus |
| **Público Objetivo:** | Administradores de restaurante, cajeros, meseros y personal operativo. |

---

## 2. Introducción y Objetivo

**El Pulpazo** es una aplicación web integral diseñada para optimizar la operación diaria de restaurantes y marisquerías. Permite administrar en tiempo real el plano de mesas, la toma de comandas, el cobro con desglose del IVA del 16%, el control de inventario con alertas de stock y la analítica ejecutiva. El objetivo de este manual es guiar de forma clara, sencilla y coloquial a cualquier miembro del personal en el uso correcto de la plataforma.

---

## 3. Índice / Mapa de Contenidos

1. [Portada y Control de Versiones](#1-portada-y-control-de-versiones)
2. [Introducción y Objetivo](#2-introducción-y-objetivo)
3. [Índice / Mapa de Contenidos](#3-índice--mapa-de-contenidos)
4. [Requisitos del Sistema](#4-requisitos-del-sistema)
5. [Convenciones e Iconografía](#5-convenciones-e-iconografía)
6. [Inicio de Sesión](#6-inicio-de-sesión)
7. [Descripción General del Sistema](#7-descripción-general-del-sistema)
8. [Roles y Perfiles de Usuario](#8-roles-y-perfiles-de-usuario)
9. [Módulos y Operaciones del Usuario](#9-módulos-y-operaciones-del-usuario)
   - [9.1 Plano Interactivo de Mesas](#91-plano-interactivo-de-mesas)
   - [9.2 Menú Digital y Tomar Pedido](#92-menú-digital-y-tomar-pedido)
   - [9.3 Carrito, Cobros e IVA (Checkout)](#93-carrito-cobros-e-iva-checkout)
   - [9.4 Control de Inventario e Insumos](#94-control-de-inventario-e-insumos)
   - [9.5 Dashboard Ejecutivo y Métricas](#95-dashboard-ejecutivo-y-métricas)
   - [9.6 Administración de Platillos](#96-administración-de-platillos)
10. [Validaciones Importantes](#10-validaciones-importantes)
11. [Atajos y Accesos Rápidos](#11-atajos-y-accesos-rápidos)
12. [Solución de Problemas (Troubleshooting)](#12-solución-de-problemas-troubleshooting)
13. [Preguntas Frecuentes (FAQ)](#13-preguntas-frecuentes-faq)
14. [Buenas Prácticas](#14-buenas-prácticas)
15. [Seguridad y Confidencialidad de Datos](#15-seguridad-y-confidencialidad-de-datos)
16. [Canal de Soporte y Contacto](#16-canal-de-soporte-y-contacto)
17. [Glosario y Conclusiones](#17-glosario-y-conclusiones)

---

## 4. Requisitos del Sistema

| Componente | Requisito Mínimo Recomendado |
| :--- | :--- |
| **Navegador Web:** | Google Chrome v100+, Microsoft Edge v100+, Safari v15+ o Mozilla Firefox v100+. |
| **Sistema Operativo:** | Windows 10/11, macOS, Linux, Android (Tablet/Celular) o iOS/iPadOS. |
| **Conexión a Internet:** | Estable (Mínimo 2 Mbps) para sincronización en la nube con Supabase. |
| **Permisos de Cuenta:** | Credenciales de usuario asignadas por el Administrador. |

---

## 5. Convenciones e Iconografía

A lo largo de este manual se utilizan los siguientes símbolos para resaltar información clave:

- ⚠️ **Advertencia:** Información crítica para prevenir errores operativos o pérdida de datos.
- 💡 **Tip / Sugerencia:** Consejos útiles para trabajar de forma más rápida y eficiente.
- 🔒 **Requiere Permisos:** Acción restringida únicamente para usuarios con rol de Administrador.
- 🟢 **Mesa Libre:** Disponible para asignar a clientes en el comedor.
- 🔴 **Mesa Ocupada:** Comanda activa con tiempo transcurrido.
- 🟠 **Mesa Reservada:** Apartada para comensales futuros.

---

## 6. Inicio de Sesión

### Pasos para Ingresar:
1. Accede a la URL oficial del sistema: [https://santiagopech490-alt.github.io/pescaderia_V3/](https://santiagopech490-alt.github.io/pescaderia_V3/)
2. Ingresa tu correo electrónico registrado y tu contraseña.
3. Haz clic en el botón amarillo **`INICIAR SESIÓN`**.

![Pantalla de Login](file:///c:/Users/santi/Downloads/pescaderia%20%281%29/pescaderia_V3/evidencias_screenshots/01_login_autenticacion.png)

⚠️ **¿Qué hacer si olvidaste tu contraseña o tu cuenta está bloqueada?**
- Contacta inmediatamente al Administrador del sistema para que restablezca tu acceso desde la consola de Supabase Auth. Por seguridad, la app no permite el autorrestablecimiento directo sin autorización previa.

---

## 7. Descripción General del Sistema

El sistema cuenta con una interfaz limpia en modo oscuro con acentos dorados (`#D4AF37`). Su estructura principal consta de:

1. **Barra Lateral de Navegación (Sidebar):** Menú desplegable a la izquierda para cambiar entre los diferentes módulos (Mesas, Menú, Carrito, Inventario, Dashboard, Admin).
2. **Encabezado Superior (Header):** Muestra las iniciales del usuario activo, su rol asignado (`Administrador`, `Cajera`, `Mesero`), el selector de Tema (Sol/Luna) y el botón de Cerrar Sesión.
3. **Área de Trabajo Central:** Pantalla dinámica donde se interactúa con los módulos.

![Vista Principal de Mesas](file:///c:/Users/santi/Downloads/pescaderia%20%281%29/pescaderia_V3/evidencias_screenshots/02_plano_de_mesas.png)

---

## 8. Roles y Perfiles de Usuario

| Rol | Vistas Visibles | Permisos y Capacidades |
| :--- | :--- | :--- |
| **👑 Administrador** | *Todas las pantallas* | Control total. Puede editar el mapa de mesas (mover/redimensionar), agregar platillos, ajustar inventario, ver métricas financieras y exportar respaldos. |
| **💵 Cajera** | *Mesas, Pedidos, Carrito, Inventario* | Procesar cobros de comandas, calcular cambio/IVA, emitir tickets digitales, registrar gastos/abonos y consultar el stock. |
| **🍽️ Mesero** | *Mesas, Menú, Carrito* | Consultar disponibilidad de mesas, tomar pedidos en el menú digital y enviar la comanda al carrito. |

---

## 9. Módulos y Operaciones del Usuario

### 9.1 Plano Interactivo de Mesas
**Propósito:** Visualizar y gestionar las mesas del comedor en tiempo real.

![Plano de Mesas](file:///c:/Users/santi/Downloads/pescaderia%20%281%29/pescaderia_V3/evidencias_screenshots/02_plano_de_mesas.png)

**Operación Paso a Paso:**
1. Haz clic sobre cualquier mesa en el mapa.
2. En el panel derecho aparecerá la información de la mesa (Nombre, Tipo, Estado, Tiempo).
3. Presiona **`Reservar Mesa`** para cambiar su estado a Naranja, o **`Liberar Mesa`** para ponerla Verde cuando los clientes se retiren.
4. 🔒 **Modo Edición (Solo Admin):** Haz clic en el botón `Editar Mesas`. Puedes arrastrar las mesas con el mouse o dedo, cambiar su forma (rectángulo/círculo), tamaño o rotación. Haz clic en `Salir de Edición` para guardar los cambios en Supabase.

---

### 9.2 Menú Digital y Tomar Pedido
**Propósito:** Seleccionar y armar la comanda de los comensales.

![Menú de Clientes](file:///c:/Users/santi/Downloads/pescaderia%20%281%29/pescaderia_V3/evidencias_screenshots/03_menu_platillos.png)

**Operación Paso a Paso:**
1. Entra a la sección **`Tomar Pedido`**.
2. Navega por las pestañas superiores: *Entradas, Platos Fuertes, Bebidas o Postres*.
3. Utiliza la barra de búsqueda para encontrar un platillo por su nombre (ej. *"Ceviche"*).
4. Presiona el botón amarillo **`+ AGREGAR`** para mandar el plato al carrito.

---

### 9.3 Carrito, Cobros e IVA (Checkout)
**Propósito:** Confirmar la comanda, desglosar el impuesto y cobrar el pedido.

![Carrito de Compras](file:///c:/Users/santi/Downloads/pescaderia%20%281%29/pescaderia_V3/evidencias_screenshots/04_carrito_checkout.png)

**Operación Paso a Paso:**
1. Ve a la sección **`Pedido Actual`** (Carrito).
2. **Selecciona la Mesa:** Elige en la lista desplegable la mesa correspondiente al cliente (ej. `Mesa A1`).
3. **Selecciona el Método de Pago:** `Efectivo` o `Tarjeta`.
4. Revisa los valores financieros:
   - **Subtotal:** Suma de platillos.
   - **IVA (16%):** Impuesto retenido automático.
   - **Total:** Cantidad final a cobrar.
5. Haz clic en **`Proceder al Pago`** y confirma. El sistema cambiará la mesa a color Rojo y desplegará el Ticket Digital con folio único.

---

### 9.4 Control de Inventario e Insumos
**Propósito:** Monitorear las existencias de ingredientes de cocina y almacén.

![Control de Inventario](file:///c:/Users/santi/Downloads/pescaderia%20%281%29/pescaderia_V3/evidencias_screenshots/05_inventario_stock.png)

**Operación Paso a Paso:**
1. Ingresa a la vista **`Inventario`**.
2. Observa la lista de materias primas (Pulpo, Camarón, Pescado, Limón, Aceite) y sus unidades.
3. Si el stock actual es menor al stock mínimo, la etiqueta se tornará roja en estado **`Bajo Stock`**.
4. Haz clic en un insumo para ajustar manualmente la cantidad recibida de proveedores y presiona Guardar.

---

### 9.5 Dashboard Ejecutivo y Métricas
**Propósito:** Consultar la salud financiera y comercial del restaurante.

![Dashboard Ejecutivo](file:///c:/Users/santi/Downloads/pescaderia%20%281%29/pescaderia_V3/evidencias_screenshots/06_dashboard_ejecutivo.png)

**Operación Paso a Paso:**
1. Entra a la sección **`Dashboard Ejecutivo`**.
2. Revisa los KPIs principales: Ventas Totales del Día, Comandas Activas, Margen Operativo % y Ocupación %.
3. Examina las gráficas interactivas de ventas por hora y la lista de platillos más vendidos.

---

### 9.6 Administración de Platillos
**Propósito:** Mantenimiento del catálogo de alimentos.

![Panel Administración](file:///c:/Users/santi/Downloads/pescaderia%20%281%29/pescaderia_V3/evidencias_screenshots/07_panel_administracion.png)

**Operación Paso a Paso:**
1. Ingresa a **`Panel Admin`**.
2. Haz clic en **`+ Agregar Nuevo Platillo`**, completa el nombre, precio, categoría e imagen.
3. Utiliza los switches para marcar si un plato está disponible u ocultarlo del menú.

---

## 10. Validaciones Importantes

| Campo / Módulo | Regla de Negocio | Ejemplo / Resultado |
| :--- | :--- | :--- |
| **Mesa en Checkout** | Obligatorio seleccionar una mesa antes de cobrar. | Si no se elige mesa, el botón "Proceder al Pago" no se procesará. |
| **Cantidad en Carrito** | No se permiten cantidades negativas o cero. | El botón `-` elimina el ítem si llega a 0. |
| **Cálculo de IVA** | Aplica tasa fija del 16% sobre el subtotal. | Subtotal = $100.00 → IVA = $16.00 → Total = $116.00. |
| **Nivel de Stock** | Alerta roja automática al caer el stock. | Stock Actual (1.2 kg) < Stock Mínimo (2.0 kg) → Alerta "Bajo Stock". |
| **Edición de Plano** | Solo accesible con rol de Administrador. | Meseros y Cajeras no ven el botón "Editar Mesas". |

---

## 11. Atajos y Accesos Rápidos

| Acción | Atajo / Acceso Rápido |
| :--- | :--- |
| **Cambiar Tema Visual** | Hacer clic en el icono Sol/Luna en el encabezado superior. |
| **Colapsar / Abrir Menú** | Hacer clic en el icono de Hamburguesa (≡) junto al logo. |
| **Búsqueda Rápida de Menú** | Usar la barra de búsqueda en la pestaña *Tomar Pedido*. |
| **Cerrar Sesión** | Hacer clic en el icono de salir en la esquina superior derecha. |

---

## 12. Solución de Problemas (Troubleshooting)

| Síntoma | Causa Probable | Solución Recomendada |
| :--- | :--- | :--- |
| No puedo iniciar sesión ("Correo o contraseña incorrectos"). | Credenciales mal escritas o usuario no registrado en Supabase Auth. | Verifica mayúsculas o solicita al Administrador revisar tu usuario. |
| Las mesas cambiadas de lugar se regresaron a su sitio. | No se presionó "Salir de Edición" para guardar en la base de datos. | Realiza los cambios en Modo Edición y presiona siempre "Salir de Edición". |
| Los platillos no cargan en el menú. | Pérdida temporal de conexión a internet. | Revisa tu red y presiona `F5` para recargar la página. |
| No veo el botón de Inventario o Dashboard. | Iniciaste sesión con rol de Mesero. | Los meseros tienen acceso limitado. Inicia sesión con cuenta Admin. |

---

## 13. Preguntas Frecuentes (FAQ)

* **¿Puedo exportar un respaldo de la base de datos?**
  Sí. En la vista de administración, haz clic en el botón **`Exportar Datos`** para descargar un archivo comprimido JSON con la copia de seguridad.
* **¿El IVA se calcula automáticamente?**
  Sí, la aplicación calcula la tasa oficial del 16% sobre el subtotal de cada orden y la imprime en el ticket.
* **¿La aplicación funciona en tablets o teléfonos?**
  Sí, el diseño es responsivo y se adapta a pantallas táctiles de iPads, tablets Android o celulares.

---

## 14. Buenas Prácticas

1. 🔒 **Cierra sesión al retirarte:** Siempre haz clic en "Cerrar Sesión" al finalizar tu turno de trabajo para evitar accesos no autorizados.
2. 💡 **Verifica el stock al iniciar el día:** Revisa la pantalla de Inventario al abrir la marisquería para detectar insumos críticos a comprar.
3. ⚠️ **Asigna siempre la mesa correcta:** Asegúrate de vincular la comanda a la mesa exacta para mantener el plano de mesas actualizado.
4. 💡 **Mantén actualizado el catálogo:** Marca como "No Disponible" los platillos cuyos ingredientes se hayan agotado en cocina.

---

## 15. Seguridad y Confidencialidad de Datos

La aplicación utiliza la infraestructura en la nube de **Supabase (PostgreSQL)**. Las contraseñas se almacenan de forma cifrada mediante algoritmos bcrypt. Las tablas de base de datos implementan políticas de seguridad por fila (Row Level Security - RLS), asegurando que cada operación esté protegida y ningún usuario sin autorización modifique datos financieros sensibles.

---

## 16. Canal de Soporte y Contacto

Si experimentas algún fallo técnico que este manual no resuelva, puedes contactar al equipo de desarrollo:

- **Equipo de Soporte:** López Estrella B. O., Castro Nuñez N. M., Pech Ake S. A., May de los Santos J. J.
- **Correo Electrónico de Contacto:** `soporte@elpulpazo.com`
- **Atención:** Lunes a Domingo de 8:00 AM a 10:00 PM.

---

## 17. Glosario y Conclusiones

### Glosario de Términos:
* **Supabase:** Plataforma de base de datos PostgreSQL en la nube y autenticación.
* **KPI (Key Performance Indicator):** Indicador clave de rendimiento financiero o comercial.
* **SVG:** Formato gráfico vectorial utilizado para renderizar el mapa interactivo de mesas.
* **RLS (Row Level Security):** Mecanismo de seguridad a nivel de fila en base de datos.
* **Checkout:** Proceso de confirmación y cobro de un pedido.

### Conclusión:
El manual del usuario de **El Pulpazo** proporciona una guía completa y estructurada para garantizar que todo el personal operativo maneje el sistema con fluidez. La combinación de una interfaz intuitiva, un diseño adaptable y una arquitectura robusta en la nube permite llevar un control impecable del restaurante, mejorando la atención al cliente y la rentabilidad del negocio.
