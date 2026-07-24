import { test } from '@playwright/test';
import fs from 'fs';
import path from 'path';

test('Generar capturas de pantalla reales v3.1', async ({ page }) => {
  const outputDir = path.join(process.cwd(), 'evidencias_screenshots');
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }

  // Interceptar la autenticación de Supabase para simular sesión iniciada
  await page.route('**/auth/v1/token*', async (route) => {
    await route.fulfill({
      status: 200,
      contentType: 'application/json',
      body: JSON.stringify({
        access_token: 'fake-token',
        token_type: 'bearer',
        expires_in: 3600,
        refresh_token: 'fake-refresh',
        user: {
          id: 'fake-uuid',
          email: 'admin@elpulpazo.com',
          user_metadata: { full_name: 'Administrador', role: 'administrador' }
        }
      })
    });
  });

  await page.route('**/rest/v1/*', async (route) => {
    await route.fulfill({
      status: 200,
      contentType: 'application/json',
      body: JSON.stringify([])
    });
  });

  // 1. Login
  await page.goto('http://localhost:5173/pescaderia_V3/');
  await page.waitForTimeout(1000);
  await page.screenshot({ path: path.join(outputDir, '01_login_autenticacion.png') });

  // Iniciar sesión
  await page.locator('input[type="email"]').fill('admin@elpulpazo.com');
  await page.locator('input[type="password"]').fill('admin@elpulpazo');
  await page.locator("button:has-text('INICIAR SESIÓN')").click();
  await page.waitForURL('**/dashboard/mapa-mesas');
  await page.waitForTimeout(1500);

  // 2. Mapa de Mesas
  await page.screenshot({ path: path.join(outputDir, '02_plano_de_mesas.png') });

  // 3. Tomar Pedido (Menú)
  await page.goto('http://localhost:5173/pescaderia_V3/#/dashboard/cliente-menu');
  await page.waitForTimeout(1500);
  await page.screenshot({ path: path.join(outputDir, '03_menu_platillos.png') });

  // 4. Carrito
  await page.goto('http://localhost:5173/pescaderia_V3/#/dashboard/carrito');
  await page.waitForTimeout(1500);
  await page.screenshot({ path: path.join(outputDir, '04_carrito_checkout.png') });

  // 5. Inventario
  await page.goto('http://localhost:5173/pescaderia_V3/#/dashboard/inventario');
  await page.waitForTimeout(1500);
  await page.screenshot({ path: path.join(outputDir, '05_inventario_stock.png') });

  // 6. Dashboard Ejecutivo
  await page.goto('http://localhost:5173/pescaderia_V3/#/dashboard/dashboard-ejecutivo');
  await page.waitForTimeout(1500);
  await page.screenshot({ path: path.join(outputDir, '06_dashboard_ejecutivo.png') });

  // 7. Panel Admin
  await page.goto('http://localhost:5173/pescaderia_V3/#/dashboard/admin');
  await page.waitForTimeout(1500);
  await page.screenshot({ path: path.join(outputDir, '07_panel_administracion.png') });

  // 8. Vista de Cocina Kanban (NUEVO v3.1)
  await page.goto('http://localhost:5173/pescaderia_V3/#/dashboard/cocina');
  await page.waitForTimeout(1500);
  await page.screenshot({ path: path.join(outputDir, '09_vista_cocina_kanban.png') });

  // 9. Reportes de Ventas (NUEVO v3.1)
  await page.goto('http://localhost:5173/pescaderia_V3/#/dashboard/reportes');
  await page.waitForTimeout(1500);
  await page.screenshot({ path: path.join(outputDir, '10_reportes_ventas.png') });

  // 10. Descuentos y Cupones (NUEVO v3.1)
  await page.goto('http://localhost:5173/pescaderia_V3/#/dashboard/descuentos');
  await page.waitForTimeout(1500);
  await page.screenshot({ path: path.join(outputDir, '11_cupones_descuentos.png') });

  // 11. División de Cuenta (NUEVO v3.1)
  await page.goto('http://localhost:5173/pescaderia_V3/#/dashboard/dividir-cuenta');
  await page.waitForTimeout(1500);
  await page.screenshot({ path: path.join(outputDir, '12_dividir_cuenta.png') });
});
