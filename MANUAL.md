# Manual Técnico y Guía de Usuario (OT-5)
## Proyecto: El Pulpazo - Sistema de Gestión de Restaurante

Este manual contiene las especificaciones técnicas para desarrolladores y administradores de sistemas, así como la guía de operación para el personal del restaurante "El Pulpazo".

---

## PARTE 1: Manual Técnico (Desarrolladores y DevOps)

### 1. Requisitos del Entorno
Para ejecutar, modificar y compilar el proyecto localmente se requiere:
* **Node.js:** Versión 18 o superior (Recomendado v20+).
* **Navegador web moderno:** Chrome, Firefox, Safari o Edge.
* **Gestor de paquetes:** `npm` (incluido con Node.js).

### 2. Configuración del Proyecto
Sigue estos pasos en la terminal para iniciar el proyecto en tu entorno local:

1. **Instalar Dependencias:**
   ```bash
   npm install
   ```
2. **Ejecutar Servidor de Desarrollo:**
   ```bash
   npm run dev
   ```
   * *La aplicación estará disponible por defecto en `http://localhost:5173`.*
3. **Compilar para Producción:**
   ```bash
   npm run build
   ```
   * *Genera los archivos optimizados dentro del directorio `/dist`.*

### 3. Estructura del Código Fuente
La estructura de archivos principales bajo el directorio `/src` es la siguiente:
* [main.tsx](file:///c:/Users/santi/Downloads/pescaderia%20%281%29/pescaderia_V3/src/main.tsx): Punto de entrada principal de la aplicación React.
* [app/routes.tsx](file:///c:/Users/santi/Downloads/pescaderia%20%281%29/pescaderia_V3/src/app/routes.tsx): Definición y control de rutas para las diferentes pantallas (Login, Dashboard, Admin, Inventario).
* **[app/context/AppContext.tsx](file:///c:/Users/santi/Downloads/pescaderia%20%281%29/pescaderia_V3/src/app/context/AppContext.tsx):** Manejador del estado global. Provee los datos de las mesas, platos, carrito e insumos, además de simular operaciones de bases de datos.
* **[app/components/](file:///c:/Users/santi/Downloads/pescaderia%20%281%29/pescaderia_V3/src/app/components/):** Directorio de vistas de la aplicación:
  * [Login.tsx](file:///c:/Users/santi/Downloads/pescaderia%20%281%29/pescaderia_V3/src/app/components/Login.tsx): Formulario de ingreso de usuario.
  * [MapaMesas.tsx](file:///c:/Users/santi/Downloads/pescaderia%20%281%29/pescaderia_V3/src/app/components/MapaMesas.tsx): Plano dinámico en SVG con interactividad de movimiento.
  * [ClienteMenu.tsx](file:///c:/Users/santi/Downloads/pescaderia%20%281%29/pescaderia_V3/src/app/components/ClienteMenu.tsx): Catálogo de productos y toma de comandas.
  * [Carrito.tsx](file:///c:/Users/santi/Downloads/pescaderia%20%281%29/pescaderia_V3/src/app/components/Carrito.tsx): Detalle del pedido y pasarela de pago.
  * [Inventario.tsx](file:///c:/Users/santi/Downloads/pescaderia%20%281%29/pescaderia_V3/src/app/components/Inventario.tsx): Gestión del almacén de ingredientes y alertas visuales.
  * [DashboardEjecutivo.tsx](file:///c:/Users/santi/Downloads/pescaderia%20%281%29/pescaderia_V3/src/app/components/DashboardEjecutivo.tsx): Panel gráfico financiero interactivo.
  * [AdminPanel.tsx](file:///c:/Users/santi/Downloads/pescaderia%20%281%29/pescaderia_V3/src/app/components/AdminPanel.tsx): Altas, bajas y disponibilidad del catálogo.

### 4. Flujo de Despliegue (CI/CD)
El proyecto incluye un flujo automatizado mediante GitHub Actions ([deploy.yml](file:///c:/Users/santi/Downloads/pescaderia%20%281%29/pescaderia_V3/.github/workflows/deploy.yml)).
1. Al subir cambios a la rama `main` en GitHub, se dispara el build automáticamente.
2. El pipeline instala paquetes, compila el código frontend y publica el sitio estático en la rama `gh-pages`.
3. Adicionalmente, se puede forzar el despliegue manual desde la consola usando `npm run deploy`.

---

## PARTE 2: Guía de Operación (Personal del Restaurante)

### 1. Acceso al Sistema (Login)
* Ingresa tu correo o nombre de usuario y contraseña en el formulario central.
* Marca "Remember me" si deseas mantener tu sesión iniciada en ese navegador.
* Haz clic en **INICIAR SESIÓN** para acceder al sistema principal.

### 2. Gestión de Mesas
* Al acceder, verás el plano del comedor de "El Pulpazo".
* **Reservar una mesa:** Selecciona una mesa de color verde (Libre) y haz clic en "Reservar Mesa" en el panel derecho. Cambiará a color naranja.
* **Liberar mesa:** Al finalizar la visita de un cliente, selecciona la mesa y haz clic en "Liberar Mesa". Cambiará de nuevo a verde.
* **Reposicionar/Añadir mesas (Solo Administrador):** 
  1. Haz clic en "Activar Edición" en la barra superior.
  2. Arrastra las mesas en pantalla para acomodarlas a la nueva distribución del comedor.
  3. Usa el botón "+ Agregar Mesa" para añadir nuevas mesas al restaurante.
  4. Presiona "Guardar Edición" para congelar las posiciones.

### 3. Registro de Pedidos (Comandas)
1. Ve al módulo de **Menú de Clientes**.
2. Filtra por categoría (Entradas, Platos Fuertes, etc.) o usa el buscador de la barra superior.
3. Haz clic en el botón "+ Agregar" de los platillos que desees pedir.
4. Dirígete a la sección del **Carrito** (en la esquina superior derecha o barra de navegación).
5. Asigna la mesa del pedido, selecciona el método de pago del cliente (Efectivo/Tarjeta) y haz clic en **Confirmar Pedido**.

### 4. Control de Inventario
* En la sección **Inventario**, puedes monitorizar el stock de los insumos (ej. mariscos, condimentos, vegetales).
* Los insumos que muestren una alerta en **color rojo** necesitan reabastecimiento urgente porque están por debajo del límite mínimo.
* Puedes editar las cantidades disponibles haciendo clic sobre el insumo, ajustando el número y guardando.

### 5. Lectura de Estadísticas (Dashboard)
* Diseñado para gerentes y supervisores.
* Permite observar en tiempo real el total de ventas recolectadas del día, el margen estimado y el porcentaje de mesas ocupadas.
* Utiliza las gráficas interactivas para analizar las horas pico de mayor facturación.
