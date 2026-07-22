"""
Pruebas Automatizadas de Software en Python (pytest)
Proyecto: El Pulpazo
"""

import pytest

def calcular_totales(items):
    subtotal = sum(item["precio"] * item["cantidad"] for item in items)
    iva = subtotal * 0.16
    total = subtotal + iva
    cantidad_total = sum(item["cantidad"] for item in items)
    return {
        "subtotal": round(subtotal, 2),
        "iva": round(iva, 2),
        "total": round(total, 2),
        "cantidad_total": cantidad_total
    }

def test_carrito_vacio():
    resultado = calcular_totales([])
    assert resultado["subtotal"] == 0
    assert resultado["iva"] == 0
    assert resultado["total"] == 0
    assert resultado["cantidad_total"] == 0

def test_calculo_iva_16_producto_unico():
    items = [{"id": "1", "nombre": "Ceviche Mixto", "precio": 169.00, "cantidad": 1}]
    resultado = calcular_totales(items)
    
    assert resultado["subtotal"] == 169.00
    assert resultado["iva"] == 27.04
    assert resultado["total"] == 196.04
    assert resultado["cantidad_total"] == 1

def test_calculo_multiples_productos():
    items = [
        {"id": "1", "nombre": "Ceviche Mixto", "precio": 169.00, "cantidad": 2}, # 338.00
        {"id": "7", "nombre": "Agua de Horchata", "precio": 35.00, "cantidad": 3}  # 105.00
    ]
    resultado = calcular_totales(items)
    
    assert resultado["subtotal"] == 443.00
    assert resultado["iva"] == 70.88
    assert resultado["total"] == 513.88
    assert resultado["cantidad_total"] == 5
