import pytest
from playwright.sync_api import sync_playwright, Playwright, expect

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

# Е2E_testing
# def test_buy_products(browser, login_data):
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://wookie.com.ua/ua/")
#     page.get_by_role("link", name="").click()
#     page.locator("#login_form_id input[name=\"user\\[email\\]\"]").fill(login_data['email'])
#     page.locator("#login_form_id input[name=\"user\\[pass\\]\"]").fill(login_data['password'])
#     page.get_by_role("button", name="Увійти").click()
#     page.once("dialog", lambda dialog: dialog.accept())
#     page.get_by_placeholder("пошук товарів").click()
#     page.locator("[id=\"q\"]").fill("Бездротові навушники Xiaomi Buds 3")
#     page.get_by_role("link", name="Бездротові навушники Xiaomi Buds 3 (BHR5526GL) - White").click()
#     page.get_by_role("link", name="Купити").click()
#     page.get_by_role("link", name="Повернутись до покупок").click()
#     page.get_by_role("link", name="Каталог товарів").click()
#     page.get_by_role("link", name="Samsung - купити на Wookie.UA").click()
#     page.get_by_role("link", name="Серія Samsung Galaxy A").click()
#     page.get_by_role("link", name="Samsung Galaxy A73").click()
#     page.get_by_role("link", name="Захисний чохол IMAK UC-2 Series "
#                                       "для Samsung Galaxy A73 (A736) - Red: фото 1 з").click()
#     page.locator("#j-buy-button-widget-112479").click()
#     page.get_by_role("link", name="Повернутись до покупок").click()
#     page.get_by_role("link", name="Каталог товарів").click()
#     page.get_by_role("link", name="Samsung - купити на Wookie.UA").click()
#     page.get_by_role("link", name="Годинники Samsung Galaxy").click()
#     page.get_by_role("link", name="Samsung Galaxy Watch 5 40mm").click()
#     page.get_by_role("link", name="Оригінальний ремінець Sport Band (S/M) "
#                                       "для Samsung Galaxy Watch 4 / 4 Classic / 5 / 5 Pro / 6 / 6 Classic "
#                                       "(ET-SFR93SOEGEU) - Apricot: фото 1 з").click()
#     page.get_by_role("link", name="Додати товар у вибране").click()
#     page.locator("span").filter(has_text="Оплата і доставка").get_by_role("link").click()
#     page.locator("#main").get_by_role("link", name="Обмін і повернення").click()
#     page.locator("#main").get_by_role("link", name="Відгуки").click()
#     page.get_by_role("link", name="1", exact=True).click()
#     page.get_by_role("link", name="Оригінальний ремінець Sport Band (S/M) "
#                                       "для Samsung Galaxy Watch 4 / 4 Classic / 5 / 5 Pro / 6 / 6 Classic "
#                                       "(ET-SFR93SOEGEU) - Apricot: фото 1 з").click()
#     page.get_by_role("link", name="Купити").click()
#     page.get_by_role("link", name="Повернутись до покупок").click()
#     page.get_by_role("link", name="Товар у вибраному").click()
#     page.get_by_role("link", name="3 977 грн").click()
#     page.get_by_role("link", name="Оформити замовлення").click()
#     page.once("dialog", lambda dialog: dialog.accept())
#     page.get_by_role("link", name="").first.click()
#     page.reload()
#     page.wait_for_timeout(1000)
#     page.once("dialog", lambda dialog: dialog.accept())
#     page.get_by_role("link", name="").first.click()
#     page.reload()
#     page.wait_for_timeout(1000)
#     page.once("dialog", lambda dialog: dialog.accept())
#     page.get_by_role("link", name="").first.click()
#     page.reload()
#     page.wait_for_timeout(1000)
#     context.close()

def login(page, login_data):
    page.goto("https://wookie.com.ua/ua/")
    page.get_by_role("link", name="").click()
    page.locator("#login_form_id input[name=\"user\\[email\\]\"]").fill(login_data['email'])
    page.locator("#login_form_id input[name=\"user\\[pass\\]\"]").fill(login_data['password'])
    page.get_by_role("button", name="Увійти").click()
    page.once("dialog", lambda dialog: dialog.accept())


def search_and_buy_products(page):
    page.get_by_placeholder("пошук товарів").click()
    page.locator("[id=\"q\"]").fill("Бездротові навушники Xiaomi Buds 3")
    page.get_by_role("link", name="Бездротові навушники Xiaomi Buds 3 (BHR5526GL) - White").click()
    page.get_by_role("link", name="Купити").click()
    page.get_by_role("link", name="Повернутись до покупок").click()
    page.get_by_role("link", name="Каталог товарів").click()
    page.get_by_role("link", name="Samsung - купити на Wookie.UA").click()
    page.get_by_role("link", name="Серія Samsung Galaxy A").click()
    page.get_by_role("link", name="Samsung Galaxy A73").click()
    page.get_by_role("link", name="Захисний чохол IMAK UC-2 Series "
                                  "для Samsung Galaxy A73 (A736) - Red: фото 1 з").click()
    page.locator("#j-buy-button-widget-112479").click()
    page.get_by_role("link", name="Повернутись до покупок").click()
    page.get_by_role("link", name="Каталог товарів").click()
    page.get_by_role("link", name="Samsung - купити на Wookie.UA").click()
    page.get_by_role("link", name="Годинники Samsung Galaxy").click()
    page.get_by_role("link", name="Samsung Galaxy Watch 5 40mm").click()
    page.get_by_role("link", name="Оригінальний ремінець Sport Band (S/M) "
                                  "для Samsung Galaxy Watch 4 / 4 Classic / 5 / 5 Pro / 6 / 6 Classic "
                                  "(ET-SFR93SOEGEU) - Apricot: фото 1 з").click()
    page.get_by_role("link", name="Додати товар у вибране").click()


def navigate_and_buy(page):
    page.locator("span").filter(has_text="Оплата і доставка").get_by_role("link").click()
    page.locator("#main").get_by_role("link", name="Обмін і повернення").click()
    page.locator("#main").get_by_role("link", name="Відгуки").click()
    page.get_by_role("link", name="1", exact=True).click()
    page.get_by_role("link", name="Оригінальний ремінець Sport Band (S/M) "
                                  "для Samsung Galaxy Watch 4 / 4 Classic / 5 / 5 Pro / 6 / 6 Classic "
                                  "(ET-SFR93SOEGEU) - Apricot: фото 1 з").click()
    page.get_by_role("link", name="Купити").click()
    page.get_by_role("link", name="Повернутись до покупок").click()
    page.get_by_role("link", name="Товар у вибраному").click()
    page.get_by_role("link", name="3 977 грн").click()
    page.get_by_role("link", name="Оформити замовлення").click()
    page.once("dialog", lambda dialog: dialog.accept())
    page.get_by_role("link", name="").first.click()


def refresh_page(page):
    page.reload()
    page.wait_for_timeout(1000)
    page.once("dialog", lambda dialog: dialog.accept())
    page.get_by_role("link", name="").first.click()
    page.reload()
    page.wait_for_timeout(1000)
    page.once("dialog", lambda dialog: dialog.accept())
    page.get_by_role("link", name="").first.click()
    page.reload()
    page.wait_for_timeout(1000)


def test_buy_products(browser, login_data):
    context = browser.new_context()
    page = context.new_page()

    login(page, login_data)
    search_and_buy_products(page)
    navigate_and_buy(page)
    refresh_page(page)

    context.close()


if __name__ == "__main__":
    pytest.main([__file__])