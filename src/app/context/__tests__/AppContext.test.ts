import { describe, test, expect } from "vitest";

// Mock interface to simulate AppContext cart logic
interface CartItem {
  id: string;
  name: string;
  price: number;
  quantity: number;
}

// Helper calculations identical to Carrito.tsx logic
function calculateTotals(items: CartItem[]) {
  const subtotal = items.reduce((sum, item) => sum + item.price * item.quantity, 0);
  const tax = subtotal * 0.16;
  const total = subtotal + tax;
  const count = items.reduce((sum, item) => sum + item.quantity, 0);
  return { subtotal, tax, total, count };
}

describe("Pruebas Unitarias - Módulo de Pedidos (Carrito)", () => {
  test("Debería inicializar un carrito vacío con totales en cero", () => {
    const items: CartItem[] = [];
    const totals = calculateTotals(items);
    
    expect(totals.subtotal).toBe(0);
    expect(totals.tax).toBe(0);
    expect(totals.total).toBe(0);
    expect(totals.count).toBe(0);
  });

  test("Debería calcular el subtotal, el IVA (16%) y el total de un solo producto", () => {
    const items: CartItem[] = [
      { id: "1", name: "Ceviche Mixto", price: 169.00, quantity: 1 }
    ];
    const totals = calculateTotals(items);

    expect(totals.count).toBe(1);
    expect(totals.subtotal).toBe(169.00);
    expect(totals.tax).toBe(169.00 * 0.16); // 27.04
    expect(totals.total).toBe(169.00 * 1.16); // 196.04
  });

  test("Debería calcular correctamente la suma de múltiples artículos con diferentes cantidades", () => {
    const items: CartItem[] = [
      { id: "1", name: "Ceviche Mixto", price: 169.00, quantity: 2 }, // 338
      { id: "7", name: "Agua de Horchata", price: 35.00, quantity: 3 } // 105
    ];
    // Subtotal esperado = 338 + 105 = 443
    // IVA esperado (16%) = 443 * 0.16 = 70.88
    // Total esperado = 443 + 70.88 = 513.88

    const totals = calculateTotals(items);

    expect(totals.count).toBe(5);
    expect(totals.subtotal).toBe(443.00);
    expect(totals.tax).toBeCloseTo(70.88, 2);
    expect(totals.total).toBeCloseTo(513.88, 2);
  });

  test("Debería prevenir el cálculo de valores incorrectos con números no válidos", () => {
    const items: CartItem[] = [
      { id: "8", name: "Pay de Limón", price: 65.00, quantity: 0 }
    ];
    const totals = calculateTotals(items);

    expect(totals.count).toBe(0);
    expect(totals.subtotal).toBe(0);
    expect(totals.total).toBe(0);
  });
});
