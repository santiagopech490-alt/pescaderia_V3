const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  const outputDir = path.join(__dirname, '..', 'evidencias_screenshots');
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }

  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({ viewport: { width: 1280, height: 800 } });
  const page = await context.newPage();

  console.log("Capturando Evidencia 1: Pantalla de Login...");
  await page.goto('http://localhost:5173/pescaderia_V3/');
  await page.waitForTimeout(1500);
  await page.screenshot({ path: path.join(outputDir, '01_login_autenticacion.png'), fullPage: true });

  console.log("Capturando Evidencia 2: Iniciar sesión y Plano de Mesas...");
  await page.locator("input[placeholder='admin@elpulpazo.com']").fill("admin@elpulpazo.com");
  await page.locator("input[placeholder='••••••••••']").fill("admin123");
  await page.locator("button:has-text('INICIAR SESIÓN')").click();
  await page.waitForTimeout(2000);
  await page.screenshot({ path: path.join(outputDir, '02_plano_de_mesas.png'), fullPage: true });

  console.log("Capturando Evidencia 3: Menú de Clientes...");
  await page.goto('http://localhost:5173/pescaderia_V3/#/dashboard/menu');
  await page.waitForTimeout(1500);
  await page.screenshot({ path: path.join(outputDir, '03_menu_platillos.png'), fullPage: true });

  console.log("Capturando Evidencia 4: Carrito y Cobro con IVA...");
  await page.goto('http://localhost:5173/pescaderia_V3/#/dashboard/carrito');
  await page.waitForTimeout(1500);
  await page.screenshot({ path: path.join(outputDir, '04_carrito_checkout.png'), fullPage: true });

  console.log("Capturando Evidencia 5: Inventario e Insumos...");
  await page.goto('http://localhost:5173/pescaderia_V3/#/dashboard/inventario');
  await page.waitForTimeout(1500);
  await page.screenshot({ path: path.join(outputDir, '05_inventario_stock.png'), fullPage: true });

  await browser.close();
  console.log("¡Todas las capturas de pantalla de evidencia se guardaron exitosamente en evidencias_screenshots!");
})();
