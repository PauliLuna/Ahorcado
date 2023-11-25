from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

INDEX_URL = "https://metodologias-agiles-juego-ahorcado.onrender.com/"
ELEGIR_URL = "https://metodologias-agiles-juego-ahorcado.onrender.com/elegir_opcion"
JUGAR_URL = "https://metodologias-agiles-juego-ahorcado.onrender.com/jugar"

def esperar_elemento(context, by, value):
    return WebDriverWait(context.driver, 30).until(
        EC.presence_of_element_located((by, value))
    )

def obtener_opciones_dropdown(context, dropdown_id):
    dropdown = esperar_elemento(context, By.ID, dropdown_id)
    select = Select(dropdown)
    return [option.text for option in select.options]

def obtener_numero_vidas(context):
    vidas_elemento = WebDriverWait(context.driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Vidas restantes')]"))
)
    vidas_texto = vidas_elemento.text
    return int(''.join(filter(str.isdigit, vidas_texto)))

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

@given('Que estoy en la pagina Elegir opcion')
def step_given(context):
    assert ELEGIR_URL in context.driver.current_url

@when('Selecciono la tematica "{string}"')
def step_seleccionar_tematica(context, string):
    dropdown_tematica = esperar_elemento(context, By.ID, "seleccion")
    select_tematica = Select(dropdown_tematica)
    select_tematica.select_by_visible_text(string)

@when('Hago clic en el boton Comenzar Juego')
def step_comenzar_juego(context):
    boton_comenzar = esperar_elemento(context, By.XPATH, "//button[contains(text(), 'Comenzar Juego')]")
    boton_comenzar.click()

@then('Deberia ser redirigido a la proxima pagina de juego')
def step_then(context):
    assert JUGAR_URL in context.driver.current_url


@given('Que estoy en la pagina Jugar')
def step_given(context):
    assert JUGAR_URL in context.driver.current_url

@when('Ingreso la letra "{letra}"')
def step_ingresar_letra(context, letra):
    input_letra = esperar_elemento(context, By.NAME, "entrada")
    input_letra.send_keys(letra)

@when('Hago clic en el boton Adivinar')
def step_adivinar(context):
    boton_adivinar = esperar_elemento(context, By.XPATH, "//button[contains(text(), 'Adivinar')]")
    boton_adivinar.click()

@then('Deberia ver el mensaje de letra incorrecta')
def step_ver_mensaje_letra_incorrecta(context):
    mensaje_letra_incorrecta = esperar_elemento(context, By.CLASS_NAME, "mensaje-advertencia")
    assert "La letra x es incorrecta. Perdiste 1 vida." in mensaje_letra_incorrecta.text  # Ajusta según tu mensaje específico

@then('Deberia ver el mensaje de letra repetida')
def step_ver_mensaje_letra_incorrecta(context):
    mensaje_letra_incorrecta = esperar_elemento(context, By.CLASS_NAME, "mensaje-repetida")
    assert "La letra x ya fue ingresada anteriormente." in mensaje_letra_incorrecta.text

@then('Deberia ver que las vidas es 6')
def step_ver_vidas_disminuyen(context):
    vidas_restantes =  obtener_numero_vidas(context)
    print(vidas_restantes)
    assert vidas_restantes == 6