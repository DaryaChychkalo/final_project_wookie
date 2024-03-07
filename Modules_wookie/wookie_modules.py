from playwright.sync_api import Page, expect

class WookiePage:
    def __init__(self, page: Page):
        self.page = page

    def open_homepage(self):
        self.page.goto("https://wookie.com.ua/ua/")

    def login(self, email, password):
        self.page.get_by_role("link", name="").click()
        self.page.locator("#login_form_id input[name=\"user\\[email\\]\"]").fill(email)
        self.page.locator("#login_form_id input[name=\"user\\[pass\\]\"]").fill(password)
        self.page.get_by_role("button", name="Увійти").click()
        self.page.once("dialog", lambda dialog: dialog.accept())

    def search_for_product(self, product_name):
        self.page.get_by_placeholder("пошук товарів").click()
        self.page.locator("[id=\"q\"]").fill(product_name)

    def add_product_to_cart(self, product_name):
        self.page.get_by_role("link", name=product_name).click()
        self.page.get_by_role("link", name="Купити").click()

    def add_to_cart_multi(self, product_name):
        self.page.get_by_role("link", name=product_name).click()
        self.page.locator("#j-buy-button-widget-112479").click()

    def go_to_catalog(self):
        self.page.get_by_role("link", name="Повернутись до покупок").click()
        self.page.get_by_role("link", name="Каталог товарів").click()

    def select_category(self, category_name):
        self.page.get_by_role("link", name=category_name).click()

    def select_product(self, product_name):
        self.page.get_by_role("link", name=product_name).click()

    def add_product_to_favorites(self):
        self.page.get_by_role("link", name="Оригінальний ремінець Sport Band (S/M) "
                                  "для Samsung Galaxy Watch 4 / 4 Classic / 5 / 5 Pro / 6 / 6 Classic "
                                  "(ET-SFR93SOEGEU) - Apricot: фото 1 з").click()
        self.page.get_by_role("link", name="Додати товар у вибране").click()

    def navigate_and_buy(self):
        self.page.locator("span").filter(has_text="Оплата і доставка").get_by_role("link").click()
        self.page.locator("#main").get_by_role("link", name="Обмін і повернення").click()
        self.page.locator("#main").get_by_role("link", name="Відгуки").click()

    def go_to_checkout(self):
        self.page.get_by_role("link", name="1", exact=True).click()
        self.page.get_by_role("link", name="Оригінальний ремінець Sport Band (S/M) "
                                      "для Samsung Galaxy Watch 4 / 4 Classic / 5 / 5 Pro / 6 / 6 Classic "
                                      "(ET-SFR93SOEGEU) - Apricot: фото 1 з").click()
        self.page.get_by_role("link", name="Купити").click()
        self.page.get_by_role("link", name="Повернутись до покупок").click()
        self.page.get_by_role("link", name="Товар у вибраному").click()
        self.page.get_by_role("link", name="3 977 грн").click()

    def proceed_to_checkout(self):
        self.page.get_by_role("link", name="Оформити замовлення").click()

    def refresh_page(self):
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.page.get_by_role("link", name="").first.click()
        self.page.reload()
        self.page.wait_for_timeout(1000)
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.page.get_by_role("link", name="").first.click()
        self.page.reload()
        self.page.wait_for_timeout(1000)
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.page.get_by_role("link", name="").first.click()
        self.page.reload()
        self.page.wait_for_timeout(1000)

    # Negative_and_additional_testing
    def goto_registration_page(self):
        self.page.goto("https://wookie.com.ua/ua/")
        self.page.get_by_role("link", name="").click()
        self.page.get_by_role("link", name="Реєстрація").click()

    def fill_registration_form_with_empty_password(self, name, email):
        self.page.locator("input[name=\"user\\[title\\]\"]").fill(name)
        self.page.locator("#signup-form input[name=\"user\\[email\\]\"]").fill(email)
        self.page.fill("#signup-form input[name=\"user[pass]\"]", "")

    def click_register_button(self):
        self.page.get_by_role("button", name="Зареєструватись").click()

    def expect_error_message_password_length(self):
        return self.page.locator("text=Довжина пароля повинна бути не менше 5-ти і не більше 15-ти символів")

    def fill_registration_page_with_empty_user(self, password, email):
        self.page.fill("#signup-form input[name=\"user[pass]\"]", "")
        self.page.locator("#signup-form input[name=\"user\\[email\\]\"]").fill(email)
        self.page.locator("#signup-form input[name=\"user\\[pass\\]\"]").fill(password)

    def expect_error_message_empty_name(self):
        return self.page.locator("text=Вкажіть ім'я")

    def fill_registration_page_with_empty_email(self, email, password):
        self.page.locator("input[name=\"user\\[title\\]\"]").fill(email)
        self.page.fill("#signup-form input[name=\"user\\[email\\]\"]", "")
        self.page.locator("#signup-form input[name=\"user\\[pass\\]\"]").fill(password)

    def expect_error_message_empty_email(self):
        return self.page.locator("text=Некоректна адреса електронної пошти")

    def goto_login_page(self):
        self.page.goto("https://wookie.com.ua/ua/")
        self.page.get_by_role("link", name="").click()

    def fill_login_form_with_empty_email(self, password):
        self.page.fill("#login_form_id input[name=\"user[pass]\"]", password)

    def fill_login_form_with_empty_password(self, email):
        self.page.locator("#login_form_id input[name=\"user\\[email\\]\"]").fill(email)

    def expect_error_message_empty_password(self):
        return self.page.locator("text=Вкажіть пароль")

    def open_mobile_version(self):
        self.page.goto("https://wookie.com.ua/ua/")
        self.page.get_by_role("link", name="Мобільна версія").click()

    def return_to_full_site(self):
        self.page.get_by_role("link", name="Повна версія сайту").click()
