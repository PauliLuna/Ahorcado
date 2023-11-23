from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

INDEX_URL = "https://metodologias-agiles-juego-ahorcado.onrender.com/"
ELEGIR_URL = "https://metodologias-agiles-juego-ahorcado.onrender.com/elegir_opcion"
JUGAR_URL = "https://metodologias-agiles-juego-ahorcado.onrender.com/jugar"

def esperar_elemento(context, by, value):
    return WebDriverWait(context.driver, 50).until(
        EC.presence_of_element_located((by, value))
    )

def obtener_opciones_dropdown(context, dropdown_id):
    dropdown = esperar_elemento(context, By.ID, dropdown_id)
    select = Select(dropdown)
    return [option.text for option in select.options]

# features/steps/ahorcado_steps.py
@given('Que estoy en la página del Juego del Ahorcado')
def step_given(context):
    context.driver = webdriver.Chrome()
    context.driver.get(INDEX_URL)

@when('Eligo "{opcion}"')
def step_when(context, opcion):
    dropdown = esperar_elemento(context, By.ID, "opcion")
    select = Select(dropdown)
    select.select_by_visible_text(opcion)

@when('Hago clic en el boton Continuar')
def step_impl(context) :
    boton = esperar_elemento(context, By.XPATH, "//button[contains(text(), 'Continuar')]")
    boton.click()

@then('Deberia ser redirigido a la proxima pagina')
def step_then(context):
    assert ELEGIR_URL in context.driver.current_url

@then('Deberia ver el label "{texto_label}"')
def step_then(context, texto_label) :
    esperar_elemento(context, By.XPATH, f"//*[contains(text(), '{texto_label}')]")
    label = context.driver.find_element(By.XPATH, f"//*[contains(text(), '{texto_label}')]")
    assert label.is_displayed()

@then('Deberia ver la opcion "{seleccion}"')
def step_then(context, seleccion):
    opciones = obtener_opciones_dropdown(context, "seleccion")
    assert seleccion in opciones
#-----

@when('Eligo {string}')
def step_when(context, opcion):
    dropdown = esperar_elemento(context, By.ID, "Jugar por temáticas")
    select = Select(dropdown)
    select.select_by_visible_text(opcion)

@when('Hago clic en el botón Continuar')
def step_impl(context) :
    boton = esperar_elemento(context, By.XPATH, "//button[contains(text(), 'Continuar')]")
    boton.click()

@then('Debería ser redirigido a la próxima página')
def step_then(context):
    assert ELEGIR_URL in context.driver.current_url

@then('Debería ver el label {string}')
def step_then(context, string):
    esperar_elemento(context, By.XPATH, f"//*[contains(text(), '{string}')]")
    label = context.driver.find_element(By.XPATH, f"//*[contains(text(), '{string}')]")
    assert label.is_displayed()


@given('Que estoy en la página Elegir opcion')
def step_given(context):
    context.driver = webdriver.Chrome()
    context.driver.get(ELEGIR_URL)

@when('Selecciono la temática {string}')
def step_seleccionar_tematica(context, string):
    dropdown_tematica = esperar_elemento(context, By.ID, "Animales")
    select_tematica = Select(dropdown_tematica)
    select_tematica.select_by_visible_text(string)

@when('Hago clic en el botón Comenzar Juego')
def step_comenzar_juego(context):
    boton_comenzar = esperar_elemento(context, By.XPATH, "//button[contains(text(), 'Comenzar Juego')]")
    boton_comenzar.click()

@then('Debería ser redirigido a la próxima página de juego')
def step_then(context):
    assert JUGAR_URL in context.driver.current_url


@given('Que estoy en la página Jugar')
def step_given(context):
    context.driver = webdriver.Chrome()
    context.driver.get(JUGAR_URL)

@when('Ingreso la letra {string}')
def step_ingresar_letra(context, letra):
    input_letra = esperar_elemento(context, By.ID, "entrada-letra")
    input_letra.send_keys(letra)

@when('Hago clic en el botón Adivinar')
def step_adivinar(context):
    boton_adivinar = esperar_elemento(context, By.XPATH, "//button[contains(text(), 'Adivinar')]")
    boton_adivinar.click()

@then('Debería ver el mensaje de letra incorrecta')
def step_ver_mensaje_letra_incorrecta(context):
    mensaje_letra_incorrecta = esperar_elemento(context, By.CLASS_NAME, "mensaje-advertencia")
    assert "La letra X es incorrecta." in mensaje_letra_incorrecta.text  # Ajusta según tu mensaje específico

@then('Debería ver que las vidas disminuyen en 1')
def step_ver_vidas_disminuyen(context):
    vidas_restantes = esperar_elemento(context, By.ID, "vidas-restantes")
    assert int(vidas_restantes.text) == context.vidas_restantes - 1  # Ajusta según la lógica de tu aplicación



