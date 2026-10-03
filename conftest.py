import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config import HEADLESS


@pytest.fixture
def driver():
    """Instância do Chrome usada por cada teste (isolada e descartada ao fim)."""
    options = Options()
    if HEADLESS:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1366,900")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    # Selenium 4.6+ resolve o chromedriver sozinho (Selenium Manager),
    # não é necessário baixar o driver manualmente.
    drv = webdriver.Chrome(options=options)
    yield drv
    drv.quit()
