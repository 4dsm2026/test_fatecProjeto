import pytest

from config import USERS
from pages.login_page import LoginPage


def test_admin_login_direct_access(driver):
    """Admin não passa por 'primeiro acesso' e entra direto na home admin."""
    page = LoginPage(driver)
    user = USERS["admin"]

    page.login(user["identifier"], user["password"], mode=user["mode"])
    page.wait_url_contains(user["home"])

    assert user["home"] in driver.current_url
    token = driver.execute_script("return window.localStorage.getItem('accessToken');")
    assert token, "accessToken deveria estar salvo no localStorage após login"


@pytest.mark.parametrize("user_key", ["backoffice", "aluno_1", "aluno_2", "aluno_3"])
def test_first_access_users_are_redirected_to_password_change(driver, user_key):
    """Backoffice e alunos (seed) exigem troca de senha no 1º acesso (HTTP 428)."""
    page = LoginPage(driver)
    user = USERS[user_key]

    page.login(user["identifier"], user["password"], mode=user["mode"])
    page.wait_url_contains("/primeiro-acesso")

    assert "/primeiro-acesso" in driver.current_url


def test_login_with_wrong_password_shows_inline_error(driver):
    """Credenciais inválidas devem exibir erro e manter o usuário em /login."""
    page = LoginPage(driver)
    user = USERS["admin"]

    page.login(user["identifier"], "senha-errada-123", mode=user["mode"])

    error_text = page.get_error_text()
    assert error_text
    assert "/login" in driver.current_url


def test_mode_switches_automatically_when_typing_ra(driver):
    """Digitar algo sem '@' no campo identificador troca o modo para RA."""
    page = LoginPage(driver).open_login()
    assert "Email institucional" in page.identifier_label_text()

    page.fill_identifier("123456789")
    assert "Registro de Aluno" in page.identifier_label_text()


def test_submit_disabled_with_short_password(driver):
    """Botão 'Entrar' deve ficar desabilitado com senha menor que 8 caracteres."""
    page = LoginPage(driver).open_login()
    page.switch_to_email_mode()
    page.fill_identifier("admin@example.com")
    page.fill_password("123")

    assert page.is_submit_enabled() is False


def test_password_visibility_toggle(driver):
    """O botão de olho deve alternar o campo de senha entre texto e password."""
    page = LoginPage(driver).open_login()
    page.fill_password("qualquer-senha")

    assert page.password_field_type() == "password"
    page.toggle_password_visibility()
    assert page.password_field_type() == "text"
