# Manual Técnico y Guía de Usuario (OT-5)
## Proyecto: El Pulpazo - Sistema de Gestión de Restaurante

Este manual contiene las especificaciones técnicas para configurar el backend de base de datos en la nube (Supabase), así como la guía de operación para el personal del restaurante "El Pulpazo".

---

## PARTE 1: Manual Técnico (Desarrolladores y Administradores)

### 1. Requisitos del Entorno
* **Node.js:** Versión 18 o superior (Recomendado v20+).
* **Gestor de paquetes:** `npm` (incluido con Node.js).
* **Base de datos:** Cuenta gratuita en **Supabase** (`supabase.com`).

### 2. Configuración de la Base de Datos en Supabase

Sigue estos pasos para levantar la base de datos PostgreSQL en la nube:

1. **Crear Proyecto:**
   * Entra a [supabase.com](https://supabase.com) y crea un nuevo proyecto llamado `el-pulpazo`.
2. **Ejecutar el Esquema e Inicializar Datos:**
   * Ve a la sección **SQL Editor** en el panel izquierdo de Supabase y haz clic en **New Query**.
   * Abre y copia el contenido del archivo [app_tables.sql](file:///c:/Users/santi/Downloads/pescaderia%20%281%29/pescaderia_V3/supabase/app_tables.sql). Pégalo en el editor de Supabase y presiona **Run**. (Esto creará las tablas `app_*` y cargará los registros iniciales de mesas, platillos, clientes e insumos).
   * *(Opcional)* Si deseas implementar el esquema robusto relacional completo original (de 17 tablas), puedes ejecutar de la misma manera el script [schema.sql](file:///c:/Users/santi/Downloads/pescaderia%20%281%29/pescaderia_V3/supabase/schema.sql).
3. **Deshabilitar RLS para Pruebas Rápidas:**
   * Ejecuta el script [fix_rls.sql](file:///c:/Users/santi/Downloads/pescaderia%20%281%29/pescaderia_V3/supabase/fix_rls.sql) en el SQL Editor para deshabilitar las políticas de seguridad por fila si deseas interactuar sin restricciones de sesión durante tus pruebas de desarrollo local.

### 3. Configuración de Usuarios y Roles

La aplicación de React valida los roles leyendo los metadatos del usuario autenticado de Supabase Auth:

1. Ve a la sección **Authentication** → **Users** → **Add user** → **Create user**.
2. Registra los siguientes usuarios con sus respectivas contraseñas:
   * **Administrador:** `admin@elpulpazo.com` / `admin123`
   * **Cajera:** `cajero@pulpazo.com` / `cajera123`
   * **Mesero:** `mesero@elpulpazo.com` / `mesero123`
3. En la configuración de cada usuario (o mediante el script [fix_user_metadata.sql](file:///c:/Users/santi/Downloads/pescaderia%20%281%29/pescaderia_V3/supabase/fix_user_metadata.sql)), define los metadatos correspondientes de esta manera:
   ```json
   {
     "full_name": "Nombre de Usuario",
     "role": "administrador"  // O "cajera" / "mesero"
   }
   ```

### 4. Variables de Entorno y Configuración Local
1. En la raíz de tu proyecto local, crea un archivo llamado `.env` copiando el contenido de `.env.example`:
   ```env
   VITE_SUPABASE_URL=https://TU-PROYECTO.supabase.co
   VITE_SUPABASE_ANON_KEY=tu-anon-key
   ```
2. Reemplaza los valores con la URL de tu proyecto y la Anon Key de API (disponibles en Supabase en **Project Settings** → **API**).
3. En tu terminal local, instala las dependencias y ejecuta el proyecto:
   ```bash
   npm install
   npm run dev
   ```
   * *La aplicación estará disponible localmente en `http://localhost:5173/pescaderia_V3/`.*

---

## PARTE 2: Guía de Operación (Personal del Restaurante)

### 1. Acceso al Sistema (Login)
* Ingresa con tu correo registrado y tu contraseña operativa.
* El sistema te asignará automáticamente tu perfil (Administrador, Cajera o Mesero) y personalizará el menú lateral de acuerdo con tus permisos.

### 2. Gestión de Mesas
* **Reservas:** Selecciona una mesa de color verde (Libre) y haz clic en "Reservar Mesa" en el panel lateral. Cambiará a color naranja.
* **Cobro y Liberación:** Cuando la comanda de una mesa de color rojo (Ocupado) se pague, haz clic en "Liberar Mesa". Cambiará automáticamente a color verde y estará disponible para nuevos comensales.
* **Mover y Editar Mesas (Administrador):**
  * Activa el interruptor "Editar Mesas" en la barra superior.
  * Arrastra las mesas en pantalla para acomodarlas a la distribución del comedor.
  * Ajusta su forma (rectangular/circular), tamaño o rotación desde el panel derecho.
  * Al hacer clic en "Salir de Edición", las ubicaciones y rotaciones se guardarán de forma permanente en la base de datos de Supabase.

### 3. Registro de Comandas y Checkout
1. Entra al módulo de **Menú de Clientes**.
2. Filtra por categoría o usa el buscador para localizar platillos (ej. Ceviche).
3. Presiona "+ Agregar" para añadir alimentos al carrito de pedidos.
4. Ve al **Carrito**, selecciona la mesa de los comensales y el método de pago (Efectivo/Tarjeta).
5. Haz clic en **Proceder al Pago** y confirma el cobro.
6. El sistema te mostrará el Ticket de Compra digital con su folio único, IVA del 16% calculado y total. Presiona "Entregar Ticket" para finalizar y vaciar el carrito.

### 4. Control de Inventario
* En la sección **Inventario**, puedes monitorizar la materia prima.
* Si el stock de un ingrediente (ej. Pulpo Fresco) cae por debajo del stock mínimo configurado, se mostrará en color rojo de alerta ("Bajo Stock").
* Puedes aumentar o ajustar manualmente las cantidades del stock haciendo clic sobre el insumo e ingresando la cantidad recibida por los proveedores.

### 5. Respaldo Local (Administrador)
* El administrador puede realizar un respaldo manual de los datos y configuraciones del restaurante desde el menú administrativo haciendo clic en **"Exportar Datos"**. Esto descargará un archivo de datos en formato JSON para mayor seguridad.
