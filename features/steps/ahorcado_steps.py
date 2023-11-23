from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

INDEX_URL = "https://metodologias-agiles-juego-ahorcado.onrender.com/"
ELEGIR_URL = "https://metodologias-agiles-juego-ahorcado.onrender.com/elegir_opcion"

def esperar_elemento(context, by, value):
    return WebDriverWait(context.driver, 30).until(
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