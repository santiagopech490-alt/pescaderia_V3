# Plan de Pruebas y Estrategia de QA (OT-3)
## Proyecto: El Pulpazo - Sistema de Gestión de Restaurante

Este documento establece la estrategia y los casos de prueba para validar el funcionamiento integrado del sistema de "El Pulpazo" con el backend en la nube de Supabase.

---

## 1. Alcance de las Pruebas

El objetivo es validar que la interfaz en React consuma, modifique y persista los datos de forma consistente en la base de datos de Supabase, respetando los roles del personal.

### Ambientes de Prueba
* **Desarrollo Local:** `http://localhost:5173/pescaderia_V3/`
* **Base de datos:** Proyecto Supabase en la nube (`https://supabase.com`).
* **Usuarios de Prueba:**
  * **Administrador:** `admin@elpulpazo.com` (Contraseña: `admin@elpulpazo`)
  * **Cajera / Cajero:** `Cajero@Pulpazo.com` (Contraseña: `Cajero`)
  * **Mesero:** `mesero@elpulpazo.com` (Contraseña: `mesero123`)

---

## 2. Casos de Prueba (Checklist de Integración)

### 2.1 Caso de Prueba 01: Autenticación y Roles Reales (Supabase Auth)
* **Precondición:** El usuario se encuentra en la pantalla de inicio de sesión.
* **Pasos de ejecución:**
  1. Ingresar las credenciales de Mesero: `mesero@elpulpazo.com` / `mesero123`.
  2. Presionar el botón "INICIAR SESIÓN".
  3. Verificar el Header superior. (Esperado: Se visualiza el nombre del mesero y sus iniciales, y no aparece la opción de "Inventario" o "Dashboard Ejecutivo" en el menú).
  4. Cerrar sesión y repetir los pasos con la cuenta de Administrador: `admin@elpulpazo.com` / `admin123`.
* **Resultado Esperado:** Redirección exitosa, despliegue del nombre de usuario real leído desde la base de datos y ocultamiento/activación de vistas según los permisos del rol.

### 2.2 Caso de Prueba 02: Persistencia del Plano de Mesas
* **Precondición:** Iniciar sesión como Administrador. Ir a `/dashboard/mapa-mesas`.
* **Pasos de ejecución:**
  1. Activar el **Modo Edición** mediante el botón superior "Editar Mesas".
  2. Agregar una mesa nueva haciendo clic en "+ Agregar Mesa".
  3. Arrastrar la nueva mesa a la posición central `(X: 450, Y: 220)`.
  4. Seleccionar la mesa en el panel lateral y cambiar su rotación a `45°`.
  5. Desactivar el Modo Edición ("Salir de Edición").
  6. Recargar la página en el navegador (`F5`).
* **Resultado Esperado:** Al recargar la página, la mesa agregada debe seguir apareciendo en el mapa en la misma posición y rotación configuradas, demostrando la persistencia exitosa en la tabla `app_mesas` de Supabase.

### 2.3 Caso de Prueba 03: Flujo de Pedidos y Ticket con IVA (Checkout)
* **Precondición:** Iniciar sesión y agregar platillos al carrito. Ir a `/dashboard/carrito`.
* **Pasos de ejecución:**
  1. Seleccionar la Mesa `A1` y establecer el método de pago (Efectivo o Tarjeta).
  2. Verificar los cálculos numéricos. (Esperado: Se muestra el desglose del Subtotal, el cálculo del IVA del 16% sobre el subtotal, y el Total sumado correctamente).
  3. Hacer clic en "Proceder al Pago" y confirmar el pedido.
  4. Revisar la pantalla "Esperando Ticket de Compra". (Esperado: Se muestra el folio único autogenerado y el ticket detallado).
  5. Hacer clic en "Entregar Ticket y Regresar".
  6. Ir al módulo de **Historial** y verificar la orden.
* **Resultado Esperado:** La comanda se guarda en la tabla `app_pedidos` y limpia el carrito al regresar. La mesa `A1` cambia automáticamente a color rojo (Ocupado).

### 2.4 Caso de Prueba 04: Inventario y Alertas de Stock
* **Precondición:** Ir a la vista de `/dashboard/inventario`.
* **Pasos de ejecución:**
  1. Buscar el ingrediente "Sal de Grano". (Esperado: Muestra stock actual inferior al mínimo y una alerta roja de "Bajo Stock").
  2. Hacer clic en editar el insumo y modificar el stock actual a un valor superior al mínimo. Guardar cambios.
  3. Verificar que la alerta roja cambie a verde ("Saludable").
  4. Recargar la página.
* **Resultado Esperado:** Los valores actualizados del inventario se leen de forma persistente desde Supabase.

### 2.5 Caso de Prueba 05: Tema y Respaldo Local (JSON)
* **Precondición:** Ir a cualquier sección del Dashboard.
* **Pasos de ejecución:**
  1. Hacer clic en el interruptor de Tema en el Header. (Esperado: La aplicación cambia a tema claro con colores claros legibles).
  2. Recargar la página. (Esperado: El navegador recuerda y aplica el tema claro desde `localStorage`).
  3. Ir a la administración e interactuar con el módulo de Respaldo Local.
  4. Hacer clic en "Exportar Datos". (Esperado: Se descarga un archivo `.json` con el volcado actual de las tablas).
* **Resultado Esperado:** Persistencia del tema clara/oscura y correcto funcionamiento de la descarga del JSON de respaldo.

---

## 3. Criterios de Aceptación para Liberación

1. **Conexión Exitosa con Supabase:** La aplicación debe leer y escribir información en la base de datos sin errores de CORS o conexión.
2. **Control de Acceso (Auth):** Ningún usuario no autenticado puede entrar a las vistas protegidas (`/dashboard/*`).
3. **Cálculo de IVA Exacto:** La suma matemática en el checkout y ticket digital debe ser exacta: `Total = Subtotal * 1.16`.
4. **Persistencia Total:** Los cambios en las mesas (posición, tamaño), platillos e inventario deben sobrevivir a una recarga de la página (`F5`).
