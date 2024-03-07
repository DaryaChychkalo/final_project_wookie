import pytest
from playwright.sync_api import sync_playwright
from Modules_wookie.wookie_modules import WookiePage

@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def login_data():
    return {
        'email': 'darya.chichkalo@gmail.com',
        'password': '210793chychkalo'
    }

def test_buy_products(browser, login_data):
    with browser as browser:
        page = browser.new_context().new_page()
        wookie_page = WookiePage(page)
        wookie_page.open_homepage()

        wookie_page.login(login_data['email'], login_data['password'])
        page.pause()
        wookie_page.search_for_product("Бездротові навушники Xiaomi Buds 3")
        wookie_page.add_product_to_cart("Бездротові навушники Xiaomi Buds 3 (BHR5526GL) - White")
        wookie_page.go_to_catalog()
        wookie_page.select_category("Samsung - купити на Wookie.UA")
        wookie_page.select_category("Серія Samsung Galaxy A")

        wookie_page.select_product("Samsung Galaxy A73")
        wookie_page.add_to_cart_multi("Захисний чохол IMAK UC-2 Series для Samsung Galaxy A73 (A736) - Red: фото 1 з")
        wookie_page.go_to_catalog()
        wookie_page.select_category("Samsung - купити на Wookie.UA")
        wookie_page.select_category("Годинники Samsung Galaxy")
        wookie_page.select_product("Samsung Galaxy Watch 5 40mm")
        wookie_page.add_product_to_favorites()
        wookie_page.navigate_and_buy()
        wookie_page.go_to_checkout()
        wookie_page.proceed_to_checkout()
        wookie_page.refresh_page()
        page.context.close()











