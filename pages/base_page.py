from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import BASE_URL, DEFAULT_TIMEOUT


class BasePage:
    """Comportamentos comuns a todas as páginas (Page Object Model)."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)

    def open(self, path: str = "/"):
        self.driver.get(f"{BASE_URL}{path}")
        return self

    def find(self, by: By, value: str):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def find_clickable(self, by: By, value: str):
        return self.wait.until(EC.element_to_be_clickable((by, value)))

    def wait_url_contains(self, fragment: str):
        return self.wait.until(EC.url_contains(fragment))

    @property
    def current_path(self) -> str:
        return self.driver.current_url.replace(BASE_URL, "") or "/"
