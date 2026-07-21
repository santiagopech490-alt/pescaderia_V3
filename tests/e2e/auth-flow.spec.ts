import { test, expect } from "@playwright/test";

test.describe("Pruebas de Sistema - Flujo de Autenticación (Login)", () => {
  test("Debería cargar la página de login correctamente", async ({ page }) => {
    // Ir a la página local del servidor de desarrollo
    await page.goto("http://localhost:5173/pescaderia_V3/");

    // Verificar que el título de la página sea el esperado
    await expect(page).toHaveTitle("Prototipo de gestión de restaurante");

    // Verificar presencia del logo o título corporativo
    const logoTitle = page.locator("h1", { hasText: "EL PULPAZO" });
    await expect(logoTitle).toBeVisible();
  });

  test("Debería iniciar sesión con el rol de Administrador y redirigir al Dashboard", async ({ page }) => {
    // Interceptar la llamada de login de Supabase y simular éxito
    await page.route("**/auth/v1/token*", async (route) => {
      await route.fulfill({
        status: 200,
        contentType: "application/json",
        body: JSON.stringify({
          access_token: "fake-jwt-token",
          token_type: "bearer",
          expires_in: 3600,
          refresh_token: "fake-refresh-token",
          user: {
            id: "fake-user-uuid",
            email: "admin@elpulpazo.com",
            user_metadata: {
              full_name: "Administrador",
              role: "administrador"
            }
          }
        })
      });
    });

    // Interceptar llamadas de base de datos REST para devolver datos vacíos y usar el fallback local
    await page.route("**/rest/v1/*", async (route) => {
      await route.fulfill({
        status: 200,
        contentType: "application/json",
        body: JSON.stringify([])
      });
    });

    await page.goto("http://localhost:5173/pescaderia_V3/");

    // Ingresar credenciales
    await page.locator("input[placeholder='admin@elpulpazo.com']").fill("admin@elpulpazo.com");
    await page.locator("input[placeholder='••••••••••']").fill("admin123");

    // Enviar formulario
    await page.locator("button:has-text('INICIAR SESIÓN')").click();

    // Esperar redirección al plano de mesas
    await page.waitForURL("**/dashboard/mapa-mesas");

    // Verificar que estamos en la vista de mesas
    const headerTitle = page.locator("h2", { hasText: "Plano de Mesas" });
    await expect(headerTitle).toBeVisible();

    // Verificar que se muestre el rol del usuario en la parte superior
    const userRoleText = page.locator("span", { hasText: "Administrador" }).first();
    await expect(userRoleText).toBeVisible();
  });
});
