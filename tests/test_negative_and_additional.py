from playwright.sync_api import sync_playwright
from Modules_wookie.wookie_modules import WookiePage


def test_registration_page_with_empty_password():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        wookie_page = WookiePage(page)
        wookie_page.goto_registration_page()
        wookie_page.fill_registration_form_with_empty_password("Дар'я Чичкало", "daryachychkalo@gmail.com")
        wookie_page.click_register_button()
        page.wait_for_selector(".form-error-box.errorBox-message")
        browser.close()


def test_registration_page_with_empty_user():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        wookie_page = WookiePage(page)
        wookie_page.goto_registration_page()
        wookie_page.fill_registration_page_with_empty_user("19191993", "daryachychkalo@gmail.com")
        wookie_page.click_register_button()
        page.wait_for_selector(".form-error-box.errorBox-message")
        browser.close()

def test_registration_page_with_empty_email():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        wookie_page = WookiePage(page)
        wookie_page.goto_registration_page()
        wookie_page.fill_registration_page_with_empty_email("Дар'я Чичкало", "19191993")
        wookie_page.click_register_button()
        page.wait_for_selector(".form-error-box.errorBox-message")
        browser.close()


def test_empty_email_authorization():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        wookie_login_page = WookiePage(page)
        wookie_login_page.goto_login_page()
        wookie_login_page.fill_login_form_with_empty_email("210793chychkalo")
        page.get_by_role("button", name="Увійти").click()
        page.wait_for_timeout(1000)
        browser.close()


def test_empty_password_authorization():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        wookie_login_page = WookiePage(page)
        wookie_login_page.goto_login_page()
        wookie_login_page.fill_login_form_with_empty_password("darya.chichkalo@gmail.com")
        page.get_by_role("button", name="Увійти").click()
        page.wait_for_timeout(1000)
        browser.close()


def test_open_mobile_version():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        wookie_mobile_page = WookiePage(page)
        wookie_mobile_page.open_mobile_version()
        browser.close()


def test_return_to_full_site():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        wookie_mobile_page = WookiePage(page)
        wookie_mobile_page.open_mobile_version()
        wookie_mobile_page.return_to_full_site()
        browser.close()
