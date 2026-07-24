# MANUAL DEL USUARIO
## Sistema de Gestión de Restaurante: "El Pulpazo" (Versión 3.1)

---

## 1. Portada y Control de Versiones

| Parámetro | Detalle |
| :--- | :--- |
| **Nombre del Sistema:** | El Pulpazo — Sistema de Gestión de Restaurante y Marisquería |
| **Versión del Manual:** | v3.1 (Versión Mejorada con Cocina, Recetas, Descuentos y Reportes) |
| **Fecha de Actualización:** | 23 de Julio de 2026 |
| **Asignatura:** | Tópicos de calidad para el desarrollo de software (Actividad 5) |
| **Equipo de Desarrollo:** | Lopez Estrella Brandon Oliver, Castro Nuñez Norberto Manuel, Pech Ake Santiago Asahel, May de los Santos Juan Jesus |
| **Público Objetivo:** | Administradores de restaurante, cajeros, meseros, personal de cocina y operaciones. |

---

## 2. Introducción y Objetivo

**El Pulpazo v3.1** es una aplicación web integral diseñada para optimizar la operación diaria de restaurantes y marisquerías. Permite administrar en tiempo real el plano de mesas, la toma de comandas, la preparación en cocina estilo Kanban, el cobro con desglose del IVA del 16%, descuentos por cupón, división de cuentas, inventario automático por recetas y analítica ejecutiva. El objetivo de este manual es guiar de forma clara, sencilla y coloquial a cualquier miembro del personal en el uso correcto de la plataforma.

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
   - [9.3 Carrito, Cobros, IVA y División de Cuenta](#93-carrito-cobros-iva-y-división-de-cuenta)
   - [9.4 Vista de Cocina Kanban](#94-vista-de-cocina-kanban)
   - [9.5 Inventario Automático y Recetas](#95-inventario-automático-y-recetas)
   - [9.6 Cupones y Descuentos](#96-cupones-y-descuentos)
   - [9.7 Reportes de Ventas y Exportación CSV](#97-reportes-de-ventas-y-exportación-csv)
   - [9.8 Dashboard Ejecutivo](#98-dashboard-ejecutivo)
   - [9.9 Administración de Platillos](#99-administración-de-platillos)
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
| **Permisos de Cuenta:** | Credenciales de usuario asignadas por el Administrador según su rol. |

---

## 5. Convenciones e Iconografía

- ⚠️ **Advertencia:** Información crítica para prevenir errores operativos o pérdida de datos.
- 💡 **Tip / Sugerencia:** Consejos útiles para trabajar de forma más rápida y eficiente.
- 🔒 **Requiere Permisos:** Acción restringida únicamente para usuarios con roles autorizados.
- 🟢 **Mesa Libre:** Disponible para asignar a clientes en el comedor.
- 🔴 **Mesa Ocupada:** Comanda activa con tiempo transcurrido.
- 🟠 **Mesa Reservada:** Apartada para comensales futuros.
- 🔔 **Notificación Flotante:** Alerta de stock bajo o comanda lista en cocina.

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

1. **Barra Lateral de Navegación (Sidebar):** Menú desplegable a la izquierda para cambiar entre los módulos autorizados según tu rol.
2. **Encabezado Superior (Header):** Muestra las iniciales del usuario activo, su rol asignado (`Administrador`, `Cajera`, `Mesero`, `Cocina`), la campanita flotante de notificaciones, el selector de Tema (Sol/Luna) y el botón de Cerrar Sesión.
3. **Área de Trabajo Central:** Pantalla dinámica donde se interactúa con los módulos.

![Vista Principal de Mesas](file:///c:/Users/santi/Downloads/pescaderia%20%281%29/pescaderia_V3/evidencias_screenshots/02_plano_de_mesas.png)

---

## 8. Roles y Perfiles de Usuario

El sistema cuenta con **4 roles operativos** estrictamente definidos:

| Rol | Correo de Acceso | Contraseña | Vistas Visibles | Permisos y Capacidades |
| :--- | :--- | :--- | :--- | :--- |
| **👑 Administrador** | `admin@elpulpazo.com` | `admin@elpulpazo` | *Todas las pantallas* | Control total. Edición del mapa de mesas, recetas, platillos, inventario, reportes CSV y finanzas. |
| **💵 Cajera / Cajero** | `Cajero@Pulpazo.com` | `Cajero` | *Mesas, Pedidos, Carrito, Inventario, Corte, Descuentos* | Procesar cobros de comandas, aplicar cupones, corte de caja, gastos, abonos y consultar el stock. |
| **🍽️ Mesero** | *`mesero@elpulpazo.com`* | `mesero123` | *Mesas, Menú, Carrito, Historial* | Consultar disponibilidad de mesas, tomar pedidos en el menú digital y enviar la comanda al carrito. |
| **👨‍🍳 Cocina** | `cocina@elpulpazo.com` | `cocina123` | *Vista Cocina, Historial* | Pantalla Kanban de preparación de platillos (Pendiente, En preparación, Listo). |

---

## 9. Módulos y Operaciones del Usuario

### 9.1 Plano Interactivo de Mesas
**Propósito:** Visualizar y gestionar las mesas del comedor en tiempo real.

![Plano de Mesas](file:///c:/Users/santi/Downloads/pescaderia%20%281%29/pescaderia_V3/evidencias_screenshots/02_plano_de_mesas.png)

**Operación Paso a Paso:**
1. Haz clic sobre cualquier mesa en el mapa.
2. En el panel derecho aparecerá la información de la mesa (Nombre, Tipo, Estado, Tiempo).
3. Presiona **`Reservar Mesa`** para cambiar su estado a Naranja, o **`Liberar Mesa`** para ponerla Verde cuando los clientes se retiren.
4. 🔒 **Modo Edición (Solo Admin):** Haz clic en `Editar Mesas`. Arrastra mesas en la cuadrícula de 900x450, cambia forma (rectángulo/círculo), tamaño o rotación y haz clic en `Salir de Edición`.

---

### 9.2 Menú Digital y Tomar Pedido
**Propósito:** Seleccionar y armar la comanda de los comensales.

![Menú de Clientes](file:///c:/Users/santi/Downloads/pescaderia%20%281%29/pescaderia_V3/evidencias_screenshots/03_menu_platillos.png)

**Operación Paso a Paso:**
1. Entra a la sección **`Tomar Pedido`**.
2. Navega por las pestañas superiores: *Entradas, Platos Fuertes, Bebidas o Postres*.
3. Utiliza la barra de búsqueda para encontrar un platillo por su nombre.
4. Presiona el botón amarillo **`+ AGREGAR`** para mandar el plato al carrito.

---

### 9.3 Carrito, Cobros, IVA y División de Cuenta
**Propósito:** Confirmar comanda, aplicar cupones, calcular impuestos, cobrar y dividir cuentas.

![Carrito de Compras](file:///c:/Users/santi/Downloads/pescaderia%20%281%29/pescaderia_V3/evidencias_screenshots/04_carrito_checkout.png)

**Operación Paso a Paso:**
1. Ve a **`Pedido Actual`** (Carrito).
2. Selecciona la Mesa (ej. `Mesa A1`) y el Método de Pago (`Efectivo` o `Tarjeta`).
3. Opción para ingresar un **Cupón de Descuento** (ej. `MARISCO10`).
4. Revisa Subtotal, Descuento, IVA 16% y Total.
5. Presiona **`Proceder al Pago`**. Generará el Ticket Digital con folio único.
6. **División de Cuenta:** Para cuentas mayores a $100, presiona el botón **`Dividir Cuenta`** para dividir el pago en partes iguales, porcentajes o montos manuales.

---

### 9.4 Vista de Cocina Kanban (NUEVO v3.1)
**Propósito:** Monitorizar y cambiar el estado de preparación de los platillos en cocina.

![Vista de Cocina Kanban](file:///c:/Users/santi/Downloads/pescaderia%20%281%29/pescaderia_V3/evidencias_screenshots/09_vista_cocina_kanban.png)

**Operación Paso a Paso:**
1. Ingresa como rol **Cocina**.
2. Observa los pedidos en las 3 columnas: **`Pendiente`**, **`En Preparación`** y **`Listo`**.
3. Haz clic en **`Iniciar Preparación`** para pasar la comanda a la segunda columna.
4. Cuando el platillo esté cocinado, haz clic en **`Marcar Listo`**. Esto notificará automáticamente al mesero.

---

### 9.5 Inventario Automático y Recetas
**Propósito:** Control de existencias con recetas y descuento automático.

![Control de Inventario](file:///c:/Users/santi/Downloads/pescaderia%20%281%29/pescaderia_V3/evidencias_screenshots/05_inventario_stock.png)

**Operación Paso a Paso:**
1. Entra a **`Inventario`**.
2. Los ingredientes (Pulpo, Camarón, Pescado, Limón) se descuentan **automáticamente al vender un platillo** basándose en la receta registrada.
3. Observa las etiquetas de estado: 🟢 *Saludable*, 🔴 *Bajo Stock* o *Agotado*.

---

### 9.6 Cupones y Descuentos (NUEVO v3.1)
**Propósito:** Administración de promociones y cupones de descuento.

![Cupones y Descuentos](file:///c:/Users/santi/Downloads/pescaderia%20%281%29/pescaderia_V3/evidencias_screenshots/11_cupones_descuentos.png)

**Operación Paso a Paso:**
1. Ve a **`Descuentos`**.
2. Haz clic en **`+ Nuevo Cupón`**, define el código (ej. `MARISCO10`), el tipo (% o monto fijo `$`) y el límite de usos.
3. Activa o desactiva cupones con el switch.

---

### 9.7 Reportes de Ventas y Exportación CSV (NUEVO v3.1)
**Propósito:** Análisis financiero detallado con descarga a Excel.

![Reportes de Ventas](file:///c:/Users/santi/Downloads/pescaderia%20%281%29/pescaderia_V3/evidencias_screenshots/10_reportes_ventas.png)

**Operación Paso a Paso:**
1. Ingresa a **`Reportes`**.
2. Selecciona el rango de fechas (Hoy, Esta semana, Este mes).
3. Haz clic en el botón **`Exportar CSV`** para descargar el informe en formato de hoja de cálculo.

---

### 9.8 Dashboard Ejecutivo
**Propósito:** Métricas en tiempo real.

![Dashboard Ejecutivo](file:///c:/Users/santi/Downloads/pescaderia%20%281%29/pescaderia_V3/evidencias_screenshots/06_dashboard_ejecutivo.png)

**Operación Paso a Paso:**
Revisa las Ventas Totales ($), Comandas Activas, Margen Operativo % y Ocupación de Mesas %.

---

### 9.9 Administración de Platillos
**Propósito:** Catálogo de platillos.

![Panel Admin](file:///c:/Users/santi/Downloads/pescaderia%20%281%29/pescaderia_V3/evidencias_screenshots/07_panel_administracion.png)

Haz clic en `+ Agregar Nuevo Platillo`, completa la información y guarda los cambios.

---

## 10. Validaciones Importantes

| Campo / Módulo | Regla de Negocio | Ejemplo / Resultado |
| :--- | :--- | :--- |
| **Mesa en Checkout** | Obligatorio seleccionar una mesa antes de cobrar. | Si no se elige mesa, no se procesa el pago. |
| **Cantidad en Carrito** | No se permiten cantidades negativas o cero. | El botón `-` elimina el ítem al llegar a 0. |
| **Cálculo de IVA** | Aplica tasa fija del 16% sobre el subtotal neto. | Subtotal = $100.00 → IVA = $16.00 → Total = $116.00. |
| **Cupones** | Se descuenta antes del cálculo de IVA. | Subtotal $200 - Cupón $20 = $180 netos + $28.80 IVA. |
| **Nivel de Stock** | Alerta roja automática al caer el stock. | Stock Actual (1.2 kg) < Stock Mínimo (2.0 kg) → "Bajo Stock". |
| **Acceso a Rutas** | Restringido estrictamente por el rol asignado. | El rol Cocina solo accede a `/cocina` e `/historial`. |

---

## 11. Atajos y Accesos Rápidos

| Acción | Atajo / Acceso Rápido |
| :--- | :--- |
| **Campanita Notificaciones** | Hacer clic en la campanita flotante del header. |
| **Cambiar Tema Visual** | Hacer clic en el icono Sol/Luna en el encabezado. |
| **Colapsar / Abrir Menú** | Hacer clic en el icono de Hamburguesa (≡) junto al logo. |
| **Búsqueda de Platillos** | Usar la barra de búsqueda en 'Tomar Pedido'. |
| **Cerrar Sesión** | Hacer clic en el icono de salir en la esquina superior derecha. |

---

## 12. Solución de Problemas (Troubleshooting)

| Síntoma | Causa Probable | Solución Recomendada |
| :--- | :--- | :--- |
| No puedo iniciar sesión ("Credenciales incorrectas"). | Correo o contraseña mal escritos. | Revisa mayúsculas/minúsculas o contacta al Administrador. |
| Las mesas no guardaron cambios. | No se presionó "Salir de Edición". | Presiona siempre "Salir de Edición" para guardar en Supabase. |
| Los platillos no cargan. | Pérdida temporal de conexión a internet. | Revisa tu red y presiona F5 para recargar. |
| Me aparece "Acceso Restringido". | Intentaste entrar a una vista no permitida por tu rol. | Inicia sesión con la cuenta del rol adecuado (ej. Admin). |

---

## 13. Preguntas Frecuentes (FAQ)

* **¿Cómo divido una cuenta entre varias personas?**
  En la pantalla de pago exitoso del Carrito (para cuentas mayores a $100), presiona "Dividir Cuenta" y elige entre partes iguales, porcentaje o monto manual.
* **¿Los platillos descuentan ingredientes automáticamente?**
  Sí, al confirmar un pedido, el sistema descuenta los gramos/litros configurados en la receta del platillo.
* **¿Puedo exportar reportes a Excel?**
  Sí. En la sección de Reportes, haz clic en "Exportar CSV".

---

## 14. Buenas Prácticas

1. 🔒 **Cierra sesión al retirarte de tu turno.**
2. 💡 **Revisa la campanita de notificaciones** para atender alertas de stock.
3. 👨‍🍳 **Mantén actualizada la pantalla de Cocina** pasando pedidos a "Listo" para avisar a los meseros.
4. ⚠️ **Verifica los cupones** antes de aplicarlos en caja.

---

## 15. Seguridad y Confidencialidad de Datos

La plataforma utiliza Supabase (PostgreSQL en la nube). Las contraseñas están cifradas con bcrypt y las tablas implementan políticas Row Level Security (RLS) por rol para proteger la información sensible.

---

## 16. Canal de Soporte y Contacto

- **Equipo de Soporte:** Lopez Estrella B. O., Castro Nuñez N. M., Pech Ake S. A., May de los Santos J. J.
- **Correo de Contacto:** `soporte@elpulpazo.com`
- **Atención:** Lunes a Domingo de 8:00 AM a 10:00 PM.

---

## 17. Glosario y Conclusiones

### Glosario:
* **RBAC (Role-Based Access Control):** Control de acceso basado en roles de usuario.
* **Kanban:** Sistema visual de columnas (Pendiente, En preparación, Listo) para gestión de tareas/pedidos.
* **Supabase:** Backend as a Service con PostgreSQL en la nube.
* **CSV:** Archivo de texto plano separado por comas compatible con Microsoft Excel.

### Conclusión:
El manual del usuario de **El Pulpazo v3.1** garantiza que todo el personal operativo maneje la plataforma con fluidez, llevando un control impecable del comedor, la cocina, las finanzas y el inventario.
