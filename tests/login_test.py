import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    # Inicializa o driver
    driver = webdriver.Chrome()
    yield driver
    # Fecha o navegador após o teste
    driver.quit()

def test_login(driver):
    # Constantes
    URL = "https://www.saucedemo.com"
    USERNAME = "standard_user"
    PASSWORD = "secret_sauce"
    EXPECTED_TITLE = "Swag Labs"

    # Navega para a página
    driver.get(URL)

    # Preenche o formulário de login
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_field.send_keys(USERNAME)
    password_field.send_keys(PASSWORD)
    login_button.click()

    # Espera até que o título da página mude (indicando login bem-sucedido)
    WebDriverWait(driver, 10).until(EC.title_is(EXPECTED_TITLE))

    # Verifica se o login foi bem-sucedido
    assert driver.title == EXPECTED_TITLE, f"O título esperado era '{EXPECTED_TITLE}', e o título encontrado foi '{driver.title}'"

    # Verifica se estamos na página de produtos
    products_title = driver.find_element(By.CLASS_NAME, "title")
    assert products_title.text == "Products", f"O texto esperado era 'Products', e o texto encontrado foi '{products_title.text}'"

    print(f"Login bem-sucedido. Título da página: {driver.title}")

if __name__ == "__main__":
    pytest.main(["-v"])