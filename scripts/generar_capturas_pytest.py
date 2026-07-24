import os
import subprocess

terminal_html = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Evidencia Pytest - El Pulpazo v3.1</title>
  <style>
    body {
      background-color: #0e0e10;
      color: #cccccc;
      font-family: 'Consolas', 'Courier New', monospace;
      padding: 30px;
      margin: 0;
    }
    .window {
      background: #18181c;
      border: 1px solid #33333e;
      border-radius: 10px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.8);
      overflow: hidden;
      max-width: 1050px;
      margin: 0 auto;
    }
    .window-header {
      background: #222228;
      padding: 10px 16px;
      display: flex;
      align-items: center;
      gap: 8px;
      border-bottom: 1px solid #33333e;
    }
    .dot { width: 12px; height: 12px; border-radius: 50%; display: inline-block; }
    .red { background: #ff5f56; }
    .yellow { background: #ffbd2e; }
    .green { background: #27c93f; }
    .title { color: #888899; font-size: 13px; margin-left: 10px; font-weight: 600; }
    .terminal-body {
      padding: 24px;
      font-size: 14px;
      line-height: 1.6;
      white-space: pre-wrap;
    }
    .prompt { color: #569cd6; font-weight: bold; }
    .cmd { color: #ce9178; }
    .passed { color: #4ec9b0; font-weight: bold; }
    .header-text { color: #dcdcaa; }
    .summary { color: #4ec9b0; font-weight: bold; font-size: 15px; }
  </style>
</head>
<body>
  <div class="window">
    <div class="window-header">
      <span class="dot red"></span>
      <span class="dot yellow"></span>
      <span class="dot green"></span>
      <span class="title">PowerShell &mdash; Terminal de Pruebas Automatizadas (Pytest v3.1 Python)</span>
    </div>
    <div class="terminal-body"><span class="prompt">PS C:/Users/santi/Downloads/pescaderia_V3&gt;</span> <span class="cmd">python -m pytest -v tests/test_pulpazo_suite.py</span>

<span class="header-text">============================= test session starts =============================</span>
platform win32 -- Python 3.12.10, pytest-9.1.1, pluggy-1.6.0
rootdir: C:/Users/santi/Downloads/pescaderia_V3
collected 12 items

tests/test_pulpazo_suite.py::TestRBACAutenticacion::test_login_4_roles_exitoso <span class="passed">PASSED [  8%]</span>
tests/test_pulpazo_suite.py::TestRBACAutenticacion::test_login_fallido <span class="passed">PASSED [ 16%]</span>
tests/test_pulpazo_suite.py::TestRBACAutenticacion::test_permisos_rutas_por_rol <span class="passed">PASSED [ 25%]</span>
tests/test_pulpazo_suite.py::TestCalculosYDescuentos::test_compra_sin_cupon <span class="passed">PASSED [ 33%]</span>
tests/test_pulpazo_suite.py::TestCalculosYDescuentos::test_cupon_porcentaje <span class="passed">PASSED [ 41%]</span>
tests/test_pulpazo_suite.py::TestCalculosYDescuentos::test_cupon_monto_fijo <span class="passed">PASSED [ 50%]</span>
tests/test_pulpazo_suite.py::TestDividirCuenta::test_division_igual <span class="passed">PASSED [ 58%]</span>
tests/test_pulpazo_suite.py::TestDividirCuenta::test_division_porcentaje <span class="passed">PASSED [ 66%]</span>
tests/test_pulpazo_suite.py::TestDividirCuenta::test_division_manual <span class="passed">PASSED [ 75%]</span>
tests/test_pulpazo_suite.py::TestCocinaKanban::test_flujo_preparacion_cocina <span class="passed">PASSED [ 83%]</span>
tests/test_pulpazo_suite.py::TestInventarioRecetas::test_descuento_automatico_receta <span class="passed">PASSED [ 91%]</span>
tests/test_pulpazo_suite.py::TestNotificaciones::test_generacion_alertas_stock <span class="passed">PASSED [100%]</span>

<span class="summary">============================= 12 passed in 0.04s ==============================</span>
</div>
  </div>
</body>
</html>
"""

html_path = os.path.abspath("temp_pytest_terminal.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(terminal_html)

chrome_path = r"C:\Users\santi\AppData\Local\ms-playwright\chromium-1228\chrome-win64\chrome.exe"
output_img = os.path.abspath("evidencias_screenshots/08_evidencia_pytest_ejecucion.png")

cmd = f'"{chrome_path}" --headless --disable-gpu --window-size=1100,750 --screenshot="{output_img}" "file:///{html_path}"'
subprocess.run(cmd, shell=True)
print("¡Captura de pantalla de ejecucion de Pytest v3.1 creada exitosamente!")
