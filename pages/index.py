"""
This module contains index page
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class IndexPage:
  # URL
  URL = 'hhttps://metodologias-agiles-juego-ahorcado.onrender.com/'
  # Locators
  SEARCH_BOTTON = (By.XPATH, "//button[contains(text(), 'Continuar')]")

  # Initializer

  def __init__(self, browser):
    self.browser = browser

  # Interaction Methods

  def load(self):
    self.browser.get(self.URL)

  def click_en_continuar(self):
    search_input = self.browser.find_element(*self.SEARCH_BOTTON)
    search_input.click()
