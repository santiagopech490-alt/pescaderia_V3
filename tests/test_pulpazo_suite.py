"""
Pruebas de Sistema e Integración de Backend y Lógica de Negocio
Proyecto: El Pulpazo (Pescadería)
Framework: pytest (Python)
"""

import pytest

# ==========================================
# Módulo 1: Autenticación y Roles Operativos
# ==========================================
ROLES_PERMITIDOS = ["administrador", "cajera", "mesero"]

def validar_usuario_rol(email, password, rol_metadata):
    if not email or "@" not in email:
        return {"exito": False, "mensaje": "Correo inválido"}
    if len(password) < 6:
        return {"exito": False, "mensaje": "Contraseña demasiado corta"}
    if rol_metadata not in ROLES_PERMITIDOS:
        return {"exito": False, "mensaje": "Rol no reconocido"}
    return {"exito": True, "token": "jwt_token_valido", "rol": rol_metadata}


class TestAutenticacion:
    def test_login_administrador_exitoso(self):
        res = validar_usuario_rol("admin@elpulpazo.com", "admin123", "administrador")
        assert res["exito"] is True
        assert res["rol"] == "administrador"
        assert "token" in res

    def test_login_cajera_exitoso(self):
        res = validar_usuario_rol("cajero@pulpazo.com", "cajera123", "cajera")
        assert res["exito"] is True
        assert res["rol"] == "cajera"

    def test_login_mesero_exitoso(self):
        res = validar_usuario_rol("mesero@elpulpazo.com", "mesero123", "mesero")
        assert res["exito"] is True
        assert res["rol"] == "mesero"

    def test_login_credenciales_invalidas(self):
        res = validar_usuario_rol("correo_invalido", "123", "administrador")
        assert res["exito"] is False


# ==========================================
# Módulo 2: Carrito, IVA del 16% y Totales
# ==========================================
def procesar_comanda(items, porcentaje_iva=0.16):
    if not items:
        return {"subtotal": 0.0, "iva": 0.0, "total": 0.0, "items_count": 0}
    
    subtotal = sum(item["precio"] * item["cantidad"] for item in items if item["cantidad"] > 0)
    iva = subtotal * porcentaje_iva
    total = subtotal + iva
    items_count = sum(item["cantidad"] for item in items if item["cantidad"] > 0)
    
    return {
        "subtotal": round(subtotal, 2),
        "iva": round(iva, 2),
        "total": round(total, 2),
        "items_count": items_count
    }


class TestCalculosComanda:
    def test_carrito_vacio(self):
        res = procesar_comanda([])
        assert res["total"] == 0.0
        assert res["items_count"] == 0

    def test_calculo_iva_16_ceviche_mixto(self):
        items = [{"id": "1", "nombre": "Ceviche Mixto", "precio": 169.00, "cantidad": 1}]
        res = procesar_comanda(items)
        assert res["subtotal"] == 169.00
        assert res["iva"] == 27.04
        assert res["total"] == 196.04

    def test_calculo_multiples_platillos_y_bebidas(self):
        items = [
            {"id": "1", "nombre": "Ceviche Mixto", "precio": 169.00, "cantidad": 2}, # 338.00
            {"id": "4", "nombre": "Filete al Mojo de Ajo", "precio": 189.00, "cantidad": 1}, # 189.00
            {"id": "7", "nombre": "Agua de Horchata", "precio": 35.00, "cantidad": 4} # 140.00
        ]
        # Subtotal: 338 + 189 + 140 = 667.00
        # IVA (16%): 667 * 0.16 = 106.72
        # Total: 773.72
        res = procesar_comanda(items)
        assert res["subtotal"] == 667.00
        assert res["iva"] == 106.72
        assert res["total"] == 773.72
        assert res["items_count"] == 7


# ==========================================
# Módulo 3: Plano de Mesas y Estados
# ==========================================
ESTADOS_MESA = ["libre", "ocupado", "reservado"]

def cambiar_estado_mesa(mesa_id, estado_actual, nuevo_estado):
    if nuevo_estado not in ESTADOS_MESA:
        raise ValueError(f"Estado {nuevo_estado} no es válido")
    return {"id": mesa_id, "estado": nuevo_estado}


class TestPlanoMesas:
    def test_transicion_mesa_libre_a_ocupado(self):
        mesa = cambiar_estado_mesa("A1", "libre", "ocupado")
        assert mesa["estado"] == "ocupado"

    def test_transicion_mesa_ocupado_a_libre(self):
        mesa = cambiar_estado_mesa("A2", "ocupado", "libre")
        assert mesa["estado"] == "libre"

    def test_estado_mesa_invalido_lanza_excepcion(self):
        with pytest.raises(ValueError):
            cambiar_estado_mesa("B1", "libre", "estado_inexistente")


# ==========================================
# Módulo 4: Inventario y Alertas de Stock
# ==========================================
def evaluar_estado_stock(stock_actual, stock_minimo):
    if stock_actual <= 0:
        return "Agotado"
    elif stock_actual < stock_minimo:
        return "Bajo Stock"
    else:
        return "Saludable"


class TestInventario:
    def test_stock_saludable(self):
        assert evaluar_estado_stock(15.0, 5.0) == "Saludable"

    def test_alerta_bajo_stock(self):
        assert evaluar_estado_stock(1.2, 2.0) == "Bajo Stock"

    def test_stock_agotado(self):
        assert evaluar_estado_stock(0.0, 5.0) == "Agotado"
