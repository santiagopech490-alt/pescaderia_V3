# Reporte de Evidencias de Pruebas (Actividad 4)
## Proyecto: El Pulpazo (Pescadería)

Este documento sirve como evidencia física y técnica de la ejecución del plan de pruebas del sistema, utilizando las herramientas requeridas por la asignatura.

---

## 1. Resumen de Pruebas Ejecutadas

| Tipo de Testeo | Herramienta Usada | Estatus | Descripción / Cobertura |
| :--- | :---: | :---: | :--- |
| **Pruebas Unitarias** | Vitest (Jest) | ✅ Exitoso | Validó cálculos matemáticos del carrito (subtotal, desglose de IVA del 16% y totales acumulados). |
| **Pruebas de Sistema (E2E)** | Playwright | ✅ Exitoso | Simuló el flujo completo de inicio de sesión de Administrador y la redirección exitosa al panel. |
| **Pruebas de Accesibilidad** | Axe-Core | ✅ Exitoso | Escaneo automatizado de la norma WCAG 2.2 sobre los componentes de la interfaz. |
| **Pruebas de API** | Postman | ✅ Diseñado | Colección JSON estructurada lista para importar y ejecutar pruebas de endpoints. |

---

## 2. Evidencia de Ejecución de Pruebas Unitarias (Vitest)

Las pruebas unitarias se ejecutaron enfocándose en la lógica matemática del carrito de compras:

```text
 RUN  v4.1.10 C:/Users/santi/Downloads/pescaderia (1)/pescaderia_V3

 ✓ src/app/context/__tests__/AppContext.test.ts (4 tests) 3ms

 Test Files  1 passed (1)
      Tests  4 passed (4)
   Start at  08:10:01
   Duration  191ms (transform 22ms, setup 0ms, import 34ms, tests 3ms, environment 0ms)
```

**Casos validados:**
1. Inicialización en cero de totales para carritos vacíos.
2. Cálculo de subtotal e IVA del 16% para un solo producto.
3. Suma correcta de múltiples alimentos con diferentes cantidades.
4. Prevención de valores incorrectos.

---

## 3. Evidencia de Pruebas de Sistema y Accesibilidad (Playwright + Axe-Core)

Las pruebas end-to-end de sistema y accesibilidad transversal WCAG 2.2 se ejecutaron simulando navegación real:

```text
Running 3 tests using 2 workers

  ok 1 tests\e2e\auth-flow.spec.ts:4:3 › Pruebas de Sistema - Flujo de Autenticación (Login) › Debería cargar la página de login correctamente (526ms)
  ok 2 tests\e2e\auth-flow.spec.ts:16:3 › Pruebas de Sistema - Flujo de Autenticación (Login) › Debería iniciar sesión con el rol de Administrador y redirigir al Dashboard (593ms)
  ok 3 tests\e2e\accessibility.spec.ts:5:3 › Pruebas de Accesibilidad - Dimensión Transversal (Axe-Core) › La página de inicio de sesión no debería presentar violaciones críticas de accesibilidad (1.2s)

  3 passed (2.6s)
```

---

## 4. Hallazgos y Bugs Detectados (QA)

Durante la ejecución inicial del escáner de accesibilidad Axe-Core se detectó un **bug crítico de accesibilidad** en la pantalla de Login:

* **Error detectado:** `button-name (critical): Ensure buttons have discernible text`
* **Causa:** El botón interactivo para mostrar/ocultar contraseña (ojo) contenía únicamente un icono de Lucide React y carecía de texto descriptivo o atributo `aria-label` para lectores de pantalla.
* **Solución aplicada:** Se modificó [Login.tsx](file:///c:/Users/santi/Downloads/pescaderia%20%281%29/pescaderia_V3/src/app/components/Login.tsx) para asignarle un atributo accesible dinámico:
  ```html
  aria-label={showPassword ? "Ocultar contraseña" : "Mostrar contraseña"}
  ```
  *Tras aplicar este cambio, la prueba de accesibilidad pasó con 0 violaciones.*

---

## 5. Colección de Postman de la API

Se adjunta al proyecto el archivo [El-Pulpazo-API.postman_collection.json](file:///c:/Users/santi/Downloads/pescaderia%20%281%29/pescaderia_V3/El-Pulpazo-API.postman_collection.json) con los siguientes endpoints modelados:
1. **Autenticación:** `POST {{SUPABASE_URL}}/auth/v1/token?grant_type=password` (con payloads de prueba).
2. **Mesas:** `GET {{SUPABASE_URL}}/rest/v1/app_mesas?select=*`
3. **Platillos:** `GET {{SUPABASE_URL}}/rest/v1/app_platillos?select=*`
4. **Inventario:** `GET {{SUPABASE_URL}}/rest/v1/app_insumos?select=*`
