import pytest
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login(driver):
    USERNAME = "standard_user"
    PASSWORD = "secret_sauce"
    EXPECTED_TITLE = "Swag Labs"

    login_page = LoginPage(driver)

    login_page.login(USERNAME, PASSWORD)

    assert login_page.is_login_successful(EXPECTED_TITLE), f"O título esperado era '{EXPECTED_TITLE}', e o título encontrado foi '{driver.title}'"

    assert login_page.is_on_products_page(), f"O texto esperado era 'Products', e o texto encontrado foi diferente"

    print(f"Login bem-sucedido. Título da página: {driver.title}")

if __name__ == "__main__":
    pytest.main(["-v"])
