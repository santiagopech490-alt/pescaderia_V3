import { test, expect } from "@playwright/test";
import AxeBuilder from "@axe-core/playwright";

test.describe("Pruebas de Accesibilidad - Dimensión Transversal (Axe-Core)", () => {
  test("La página de inicio de sesión no debería presentar violaciones críticas de accesibilidad", async ({ page }) => {
    await page.goto("http://localhost:5173/pescaderia_V3/");

    // Esperar a que la tarjeta de login se renderice completamente
    await page.waitForSelector("h1:has-text('EL PULPAZO')");

    // Ejecutar el motor de análisis de accesibilidad de axe-core
    const accessibilityResults = await new AxeBuilder({ page })
      .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"]) // Filtrar por normas estándar de la W3C
      .analyze();

    // Guardar los fallos para ver detalles si existen
    const violations = accessibilityResults.violations;
    if (violations.length > 0) {
      console.log(`[WCAG Alert] Se encontraron ${violations.length} violaciones de accesibilidad:`);
      violations.forEach((violation) => {
        console.log(`- ID: ${violation.id} (${violation.impact}): ${violation.description}`);
      });
    }

    // Aseveración de que no hay fallos críticos de accesibilidad
    // Nota: permitimos violaciones menores o moderadas ya que es un prototipo, pero validamos que la estructura general sea robusta.
    const criticalViolations = violations.filter(v => v.impact === "critical" || v.impact === "serious");
    expect(criticalViolations.length).toBe(0);
  });
});
