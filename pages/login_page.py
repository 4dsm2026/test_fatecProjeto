from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    PATH = "/login"

    IDENTIFIER_INPUT = (By.ID, "identifier")
    PASSWORD_INPUT = (By.ID, "password")
    IDENTIFIER_LABEL = (By.CSS_SELECTOR, "label[for='identifier']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_BOX = (By.CSS_SELECTOR, ".text-destructive")
    MODE_EMAIL_BUTTON = (By.XPATH, "//button[contains(., 'Funcionário')]")
    MODE_RA_BUTTON = (By.XPATH, "//button[contains(., 'Aluno (RA)')]")
    TOGGLE_PASSWORD_BUTTON = (
        By.CSS_SELECTOR,
        "button[aria-label='Mostrar senha'], button[aria-label='Ocultar senha']",
    )

    def open_login(self):
        self.open(self.PATH)
        self.find(*self.IDENTIFIER_INPUT)
        return self

    def switch_to_email_mode(self):
        self.find_clickable(*self.MODE_EMAIL_BUTTON).click()
        return self

    def switch_to_ra_mode(self):
        self.find_clickable(*self.MODE_RA_BUTTON).click()
        return self

    def fill_identifier(self, value: str):
        field = self.find(*self.IDENTIFIER_INPUT)
        field.clear()
        field.send_keys(value)
        return self

    def fill_password(self, value: str):
        field = self.find(*self.PASSWORD_INPUT)
        field.clear()
        field.send_keys(value)
        return self

    def submit(self):
        self.find_clickable(*self.SUBMIT_BUTTON).click()
        return self

    def is_submit_enabled(self) -> bool:
        return self.find(*self.SUBMIT_BUTTON).is_enabled()

    def toggle_password_visibility(self):
        self.find_clickable(*self.TOGGLE_PASSWORD_BUTTON).click()
        return self

    def password_field_type(self) -> str:
        return self.find(*self.PASSWORD_INPUT).get_attribute("type")

    def get_error_text(self) -> str:
        return self.find(*self.ERROR_BOX).text

    def identifier_label_text(self) -> str:
        return self.find(*self.IDENTIFIER_LABEL).text

    def login(self, identifier: str, password: str, mode: str = "email"):
        """Fluxo completo: abre /login, escolhe o modo, preenche e envia."""
        self.open_login()
        if mode == "ra":
            self.switch_to_ra_mode()
        else:
            self.switch_to_email_mode()
        self.fill_identifier(identifier)
        self.fill_password(password)
        self.submit()
        return self
