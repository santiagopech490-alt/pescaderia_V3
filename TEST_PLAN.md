# Plan de Pruebas y Estrategia de QA (OT-3)
## Proyecto: El Pulpazo - Sistema de Gestión de Restaurante

Este documento establece la estrategia, el alcance y los casos de prueba para garantizar la calidad y correcto funcionamiento del sistema de "El Pulpazo".

---

## 1. Alcance de las Pruebas

El objetivo es validar la funcionalidad, usabilidad y responsividad de todos los módulos del frontend interactivo de la aplicación.

### Ambientes de Prueba
* **Localhost:** `http://localhost:5173` (Desarrollo).
* **Producción (Simulado):** GitHub Pages (Rama `gh-pages` / GitHub Actions).
* **Dispositivos objetivo:** Computadoras de escritorio (Chrome, Firefox, Edge) y Tablets en modo horizontal.

---

## 2. Casos de Prueba (Checklist)

### 2.1 Caso de Prueba 01: Módulo de Acceso (Login)
* **Precondición:** El usuario se encuentra en la pantalla de inicio de sesión (`/`).
* **Pasos de ejecución:**
  1. Intentar hacer clic en "INICIAR SESIÓN" con los campos vacíos. (Esperado: Evitar el avance o solicitar datos).
  2. Ingresar usuario `manager@elpulpazo.com` y contraseña `admin123`.
  3. Activar la opción "Remember me" (Recordar contraseña).
  4. Presionar el botón de visualización de contraseña (ojo) para revelar el texto.
  5. Hacer clic en "INICIAR SESIÓN".
* **Resultado Esperado:** Redirección automática a la vista del mapa de mesas (`/dashboard/mapa-mesas`).

### 2.2 Caso de Prueba 02: Plano de Mesas y Reservas
* **Precondición:** El usuario ha iniciado sesión y se encuentra en `/dashboard/mapa-mesas`.
* **Pasos de ejecución:**
  1. Seleccionar la mesa `A1` (Libre). (Esperado: Se abre el panel lateral de detalles de mesa).
  2. Hacer clic en "Reservar Mesa". (Esperado: El estado e indicador de color de la mesa cambia a Naranja/Reservado).
  3. Seleccionar la mesa `A2` (Ocupada). (Esperado: El panel muestra la comanda activa y el tiempo transcurrido).
  4. Activar el **Modo Edición** mediante el botón de la barra superior.
  5. Intentar arrastrar la mesa `B1` a otra posición. (Esperado: La mesa se desplaza suavemente al arrastrarla).
  6. Hacer clic en "+ Agregar Mesa". (Esperado: Se crea una nueva mesa circular en el mapa con identificador secuencial).
  7. Desactivar el Modo Edición. (Esperado: Se guardan las posiciones y ya no se pueden mover al arrastrarlas).

### 2.3 Caso de Prueba 03: Toma de Pedidos (Menú y Carrito)
* **Precondición:** Estar en la vista de menú de cliente (`/dashboard/cliente-menu`).
* **Pasos de ejecución:**
  1. Filtrar el menú seleccionando la categoría "Bebidas". (Esperado: Solo se muestran bebidas en pantalla).
  2. Escribir "Ceviche" en la barra de búsqueda superior. (Esperado: Se filtra y solo se visualizan los platillos que contengan "Ceviche").
  3. Presionar "+ Agregar" en "Ceviche Mixto" dos veces.
  4. Ir a la vista del carrito (`/dashboard/carrito`).
  5. Aumentar la cantidad del plato a 3. (Esperado: El total se recalcula correctamente).
  6. Seleccionar la mesa `A1` en el dropdown de mesa.
  7. Seleccionar método de pago "Efectivo".
  8. Hacer clic en "Confirmar Pedido".
* **Resultado Esperado:** Mensaje de confirmación (toast o alerta de éxito), carrito vacío y redirección o actualización de la mesa asignada a estado "Ocupada".

### 2.4 Caso de Prueba 04: Administración del Menú (CRUD)
* **Precondición:** Estar en `/dashboard/admin` (Panel de Administración).
* **Pasos de ejecución:**
  1. Desactivar el interruptor de "Disponible" para el platillo "Pay de Limón". (Esperado: El platillo debe aparecer como "Agotado" en la vista del cliente).
  2. Activar la opción "Recomendado" para "Cóctel de Camarón". (Esperado: Se muestra con estrella o destaque visual).
  3. Hacer clic en "Nuevo Platillo".
  4. Llenar el formulario con datos de prueba (Nombre: "Tacos Gobernador", Precio: 120, Categoría: Platos Fuertes).
  5. Hacer clic en "Guardar".
* **Resultado Esperado:** El nuevo platillo se muestra al final de la lista del panel y está disponible en la vista de cliente.

### 2.5 Caso de Prueba 05: Inventario de Insumos
* **Precondición:** Estar en `/dashboard/inventario`.
* **Pasos de ejecución:**
  1. Buscar el ingrediente "Camarón". (Esperado: Muestra stock actual de 15 kg y mínimo de 20 kg en color rojo de alerta).
  2. Editar el insumo para aumentar el stock a 25 kg.
* **Resultado Esperado:** Al guardar, la alerta roja desaparece porque el stock actual supera el mínimo configurado.

### 2.6 Caso de Prueba 06: Dashboard y Analítica
* **Precondición:** Estar en `/dashboard/dashboard-ejecutivo`.
* **Pasos de ejecución:**
  1. Visualizar las tarjetas superiores de KPI (Ventas, Pedidos, Margen, Ocupación).
  2. Posicionar el cursor sobre la gráfica de línea de "Ventas por hora".
* **Resultado Esperado:** Se despliega un *tooltip* interactivo con la hora y el monto de venta exacto.

---

## 3. Criterios de Aceptación para Liberación

1. **Compilación sin errores:** `npm run build` debe completarse de forma exitosa en el pipeline de CI/CD.
2. **Pruebas Críticas Aprobadas:** 100% de éxito en los flujos de Login, Creación de pedidos y Mapa de mesas.
3. **Cero errores en consola:** No deben registrarse warnings críticos o errores de React en la consola del desarrollador.
4. **Diseño Adaptable:** El diseño debe mantener su integridad estética sin desbordamientos de texto en resoluciones de Tablet (1024x768) y Desktop (1920x1080).
