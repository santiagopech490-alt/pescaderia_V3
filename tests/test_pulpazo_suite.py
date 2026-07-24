"""
Pruebas de Sistema, Integración y Lógica de Negocio en Python (pytest)
Proyecto: El Pulpazo (Pescadería) - Versión 3.1
"""

import pytest
import math

# ==============================================================================
# Módulo 1: Autenticación y Control de Acceso por Roles (RBAC 4 Roles)
# ==============================================================================
ROLES_PERMITIDOS = {
    "administrador": ["/dashboard/mapa-mesas", "/dashboard/admin", "/dashboard/dashboard-ejecutivo", "/dashboard/cocina", "/dashboard/reportes", "/dashboard/descuentos", "/dashboard/inventario"],
    "cajera": ["/dashboard/mapa-mesas", "/dashboard/corte-caja", "/dashboard/clientes", "/dashboard/reportes", "/dashboard/descuentos", "/dashboard/historial"],
    "mesero": ["/dashboard/mapa-mesas", "/dashboard/cliente-menu", "/dashboard/carrito", "/dashboard/historial"],
    "cocina": ["/dashboard/cocina", "/dashboard/historial"]
}

def autenticar_usuario(email, password):
    usuarios_db = {
        "admin@elpulpazo.com": {"pass": "admin@elpulpazo", "rol": "administrador", "nombre": "Administrador"},
        "cajero@pulpazo.com": {"pass": "Cajero", "rol": "cajera", "nombre": "Cajera Principal"},
        "mesero@elpulpazo.com": {"pass": "mesero123", "rol": "mesero", "nombre": "Mesero Turno"},
        "cocina@elpulpazo.com": {"pass": "cocina123", "rol": "cocina", "nombre": "Jefe de Cocina"}
    }
    
    user = usuarios_db.get(email.lower())
    if not user or user["pass"] != password:
        return {"exito": False, "error": "Credenciales inválidas"}
    
    return {"exito": True, "token": "jwt_supabase_valid", "rol": user["rol"], "nombre": user["nombre"]}

def verificar_acceso_ruta(rol, ruta):
    rutas_permitidas = ROLES_PERMITIDOS.get(rol, [])
    return ruta in rutas_permitidas


class TestRBACAutenticacion:
    def test_login_4_roles_exitoso(self):
        assert autenticar_usuario("admin@elpulpazo.com", "admin@elpulpazo")["rol"] == "administrador"
        assert autenticar_usuario("cajero@pulpazo.com", "Cajero")["rol"] == "cajera"
        assert autenticar_usuario("mesero@elpulpazo.com", "mesero123")["rol"] == "mesero"
        assert autenticar_usuario("cocina@elpulpazo.com", "cocina123")["rol"] == "cocina"

    def test_login_fallido(self):
        assert autenticar_usuario("admin@elpulpazo.com", "wrongpass")["exito"] is False

    def test_permisos_rutas_por_rol(self):
        # Admin accede a todo
        assert verificar_acceso_ruta("administrador", "/dashboard/admin") is True
        # Mesero no accede a panel admin
        assert verificar_acceso_ruta("mesero", "/dashboard/admin") is False
        # Cocina accede a vista Kanban de cocina
        assert verificar_acceso_ruta("cocina", "/dashboard/cocina") is True
        # Cajera accede a corte de caja
        assert verificar_acceso_ruta("cajera", "/dashboard/corte-caja") is True


# ==============================================================================
# Módulo 2: Carrito, Cálculo de IVA 16% y Sistema de Descuentos / Cupones
# ==============================================================================
CUPONES_VALIDOS = {
    "MARISCO10": {"tipo": "porcentaje", "valor": 10.0}, # 10% de descuento
    "PULPAZO50": {"tipo": "fijo", "valor": 50.0}        # $50 de descuento fijo
}

def calcular_checkout(items, cupon_codigo=None, porcentaje_iva=0.16):
    if not items:
        return {"subtotal": 0.0, "descuento": 0.0, "iva": 0.0, "total": 0.0}

    subtotal = sum(item["precio"] * item["cantidad"] for item in items)
    descuento = 0.0

    if cupon_codigo and cupon_codigo in CUPONES_VALIDOS:
        cup = CUPONES_VALIDOS[cupon_codigo]
        if cup["tipo"] == "porcentaje":
            descuento = subtotal * (cup["valor"] / 100.0)
        elif cup["tipo"] == "fijo":
            descuento = min(subtotal, cup["valor"])

    subtotal_con_descuento = max(0.0, subtotal - descuento)
    iva = subtotal_con_descuento * porcentaje_iva
    total = subtotal_con_descuento + iva

    return {
        "subtotal": round(subtotal, 2),
        "descuento": round(descuento, 2),
        "subtotal_con_descuento": round(subtotal_con_descuento, 2),
        "iva": round(iva, 2),
        "total": round(total, 2)
    }


class TestCalculosYDescuentos:
    def test_compra_sin_cupon(self):
        items = [{"id": "1", "nombre": "Ceviche Mixto", "precio": 169.00, "cantidad": 2}] # 338.00
        res = calcular_checkout(items)
        assert res["subtotal"] == 338.00
        assert res["descuento"] == 0.0
        assert res["iva"] == 54.08 # 338 * 0.16
        assert res["total"] == 392.08

    def test_cupon_porcentaje(self):
        items = [{"id": "1", "nombre": "Ceviche", "precio": 200.00, "cantidad": 1}]
        res = calcular_checkout(items, "MARISCO10")
        assert res["subtotal"] == 200.00
        assert res["descuento"] == 20.00 # 10%
        assert res["subtotal_con_descuento"] == 180.00
        assert res["iva"] == 28.80 # 180 * 0.16
        assert res["total"] == 208.80

    def test_cupon_monto_fijo(self):
        items = [{"id": "4", "nombre": "Filete al Mojo de Ajo", "precio": 189.00, "cantidad": 1}]
        res = calcular_checkout(items, "PULPAZO50")
        assert res["subtotal"] == 189.00
        assert res["descuento"] == 50.00
        assert res["subtotal_con_descuento"] == 139.00
        assert res["iva"] == 22.24
        assert res["total"] == 161.24


# ==============================================================================
# Módulo 3: División de Cuenta (Igual, Porcentaje, Manual)
# ==============================================================================
def dividir_cuenta(total_orden, num_personas, modo, parametros=None):
    if num_personas <= 0 or total_orden <= 0:
        raise ValueError("Total y personas deben ser mayores a 0")

    if modo == "igual":
        monto_individual = round(total_orden / num_personas, 2)
        return [monto_individual] * num_personas

    elif modo == "porcentaje":
        # parametros: lista de porcentajes ej. [50, 50]
        if not parametros or sum(parametros) != 100:
            raise ValueError("Los porcentajes deben sumar 100%")
        return [round(total_orden * (p / 100.0), 2) for p in parametros]

    elif modo == "manual":
        # parametros: lista de montos manuales
        if not parametros or sum(parametros) != total_orden:
            raise ValueError("La suma de montos manuales debe ser igual al total")
        return parametros

    raise ValueError("Modo de división no soportado")


class TestDividirCuenta:
    def test_division_igual(self):
        partes = dividir_cuenta(300.00, 3, "igual")
        assert partes == [100.00, 100.00, 100.00]

    def test_division_porcentaje(self):
        partes = dividir_cuenta(500.00, 2, "porcentaje", [60, 40])
        assert partes == [300.00, 200.00]

    def test_division_manual(self):
        partes = dividir_cuenta(450.00, 3, "manual", [200.00, 150.00, 100.00])
        assert partes == [200.00, 150.00, 100.00]
        assert sum(partes) == 450.00


# ==============================================================================
# Módulo 4: Vista de Cocina Kanban (Estados de Comanda)
# ==============================================================================
ESTADOS_COCINA = ["pendiente", "preparando", "listo"]

def cambiar_estado_cocina(comanda_id, estado_actual, nuevo_estado):
    if nuevo_estado not in ESTADOS_COCINA:
        raise ValueError("Estado de cocina inválido")
    return {"id": comanda_id, "estado": nuevo_estado}


class TestCocinaKanban:
    def test_flujo_preparacion_cocina(self):
        c = cambiar_estado_cocina("ORD-001", "pendiente", "preparando")
        assert c["estado"] == "preparando"
        
        c = cambiar_estado_cocina("ORD-001", "preparando", "listo")
        assert c["estado"] == "listo"


# ==============================================================================
# Módulo 5: Inventario Automático con Recetas y Decremento de Stock
# ==============================================================================
RECETAS_PLATILLOS = {
    "1": [{"insumo_id": "i1", "nombre": "Pulpo Fresco", "cantidad": 0.200}], # 200g por Ceviche
    "4": [{"insumo_id": "i2", "nombre": "Aceite de Oliva", "cantidad": 0.050}]
}

def descontar_inventario_por_receta(inventario_actual, platillo_id, cantidad_vendida):
    receta = RECETAS_PLATILLOS.get(platillo_id, [])
    inventario_actualizado = {k: v.copy() for k, v in inventario_actual.items()}

    for ing in receta:
        ins_id = ing["insumo_id"]
        cant_requerida = ing["cantidad"] * cantidad_vendida
        if ins_id in inventario_actualizado:
            inventario_actualizado[ins_id]["stock_actual"] -= cant_requerida
            inventario_actualizado[ins_id]["stock_actual"] = round(inventario_actualizado[ins_id]["stock_actual"], 3)

    return inventario_actualizado


class TestInventarioRecetas:
    def test_descuento_automatico_receta(self):
        inventario_inicial = {
            "i1": {"nombre": "Pulpo Fresco", "stock_actual": 10.000, "stock_minimo": 2.000}
        }
        # Vender 3 ceviches -> Descuento: 3 * 0.200 = 0.600 kg
        inv_final = descontar_inventario_por_receta(inventario_inicial, "1", 3)
        assert inv_final["i1"]["stock_actual"] == 9.400


# ==============================================================================
# Módulo 6: Notificaciones de Sistema y Alertas de Stock
# ==============================================================================
def generar_notificaciones_stock(inventario):
    notificaciones = []
    for item_id, data in inventario.items():
        if data["stock_actual"] <= 0:
            notificaciones.append({"tipo": "stock_agotado", "mensaje": f"El insumo {data['nombre']} está agotado."})
        elif data["stock_actual"] < data["stock_minimo"]:
            notificaciones.append({"tipo": "stock_bajo", "mensaje": f"Alerta: {data['nombre']} está en nivel crítico."})
    return notificaciones


class TestNotificaciones:
    def test_generacion_alertas_stock(self):
        inv = {
            "i1": {"nombre": "Pulpo", "stock_actual": 5.0, "stock_minimo": 2.0},
            "i2": {"nombre": "Limón", "stock_actual": 1.0, "stock_minimo": 3.0}, # Bajo
            "i3": {"nombre": "Camarón", "stock_actual": 0.0, "stock_minimo": 5.0} # Agotado
        }
        notifs = generar_notificaciones_stock(inv)
        assert len(notifs) == 2
        assert notifs[0]["tipo"] == "stock_bajo"
        assert notifs[1]["tipo"] == "stock_agotado"
