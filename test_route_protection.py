from config import BASE_URL, USERS
from pages.login_page import LoginPage


def test_unauthenticated_user_redirected_from_admin_area(driver):
    driver.get(f"{BASE_URL}/admin/home")
    LoginPage(driver).wait_url_contains("/login")

    assert "/login" in driver.current_url
    assert "redirect=" in driver.current_url


def test_unauthenticated_user_redirected_from_aluno_area(driver):
    driver.get(f"{BASE_URL}/aluno/home")
    LoginPage(driver).wait_url_contains("/login")

    assert "/login" in driver.current_url
    assert "redirect=" in driver.current_url


def test_logged_in_admin_visiting_login_page_is_redirected_home(driver):
    """Middleware redireciona quem já está autenticado para longe de /login."""
    page = LoginPage(driver)
    user = USERS["admin"]
    page.login(user["identifier"], user["password"], mode=user["mode"])
    page.wait_url_contains(user["home"])

    driver.get(f"{BASE_URL}/login")
    page.wait_url_contains(user["home"])

    assert user["home"] in driver.current_url


def test_admin_cannot_stay_on_aluno_only_route(driver):
    """Papel ADMINISTRADOR acessando /aluno/* deve ser barrado pelo middleware."""
    page = LoginPage(driver)
    user = USERS["admin"]
    page.login(user["identifier"], user["password"], mode=user["mode"])
    page.wait_url_contains(user["home"])

    driver.get(f"{BASE_URL}/aluno/home")
    page.wait_url_contains("/admin/home")

    assert "/admin/home" in driver.current_url
