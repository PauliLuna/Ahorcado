from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('Que estoy en la página del Juego del Ahorcado')
def step_given(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://metodologias-agiles-juego-ahorcado.onrender.com/")

@when('Hago clic en el boton {string}')
def step_when(context, string):
    boton = context.driver.find_element(By.XPATH, "//button[contains(text(), '{}')]".format(string))
    boton.click()

@then('Deberia ser redirigido a la proxima pagina')
def step_then(context):
    # Espera hasta que se cargue la próxima página (puedes ajustar según tu aplicación)
    WebDriverWait(context.driver, 30).until(EC.url_changes(context.driver.current_url))
    assert "https://metodologias-agiles-juego-ahorcado.onrender.com/elegir_opcion" in context.driver.current_url

@then('Deberia ver el label {texto_label}')
def step_then(context, texto_label) :
    # Espera hasta que el elemento con el texto del label esté presente
    print("Esperando la visibilidad del elemento...")
    WebDriverWait(context.driver, 30).until(EC.visibility_of_element_located((By.XPATH, f"//*[contains(text(), '{texto_label}')]")))
    print("Elemento visible. Verificando...")
    # Verifica que el label con el texto esperado está presente en la página
    label = context.driver.find_element(By.XPATH, f"//*[contains(text(), '{texto_label}')]")
    assert label.is_displayed()