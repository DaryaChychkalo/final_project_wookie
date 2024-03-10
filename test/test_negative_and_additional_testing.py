from playwright.sync_api import Playwright, sync_playwright, expect


# Registration on the site without entering a password.
def test_registration_page_with_empty_password(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://wookie.com.ua/ua/")
    page.get_by_role("link", name="").click()
    page.get_by_role("link", name="Реєстрація").click()
    page.locator("input[name=\"user\\[title\\]\"]").fill("Дар'я Чичкало")
    page.locator("#signup-form input[name=\"user\\[email\\]\"]").fill("daryachychkalo@gmail.com")
    page.fill("#signup-form input[name=\"user[pass]\"]", "")
    page.get_by_role("button", name="Зареєструватись").click()

    # We expect that an error message about the password length will appear on the page.
    error_message = page.locator("text=Довжина пароля повинна бути не менше 5-ти і не більше 15-ти символів")
    expect(error_message).to_be_visible()

    context.close()
    browser.close()


# Registration on the site without entering a first and last name.
def test_registration_page_with_empty_user(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://wookie.com.ua/ua/")
    page.get_by_role("link", name="").click()
    page.get_by_role("link", name="Реєстрація").click()
    page.fill("#signup-form input[name=\"user[pass]\"]", "")
    page.locator("input[name=\"user\\[title\\]\"]").click()
    page.locator("#signup-form input[name=\"user\\[email\\]\"]").fill("daryachychkalo@gmail.com")
    page.locator("#signup-form input[name=\"user\\[pass\\]\"]").fill("19191993")
    page.get_by_role("button", name="Зареєструватись").click()

    # We expect that an error message about the absence of a first and last name will appear on the page.
    error_message = page.locator("text=Вкажіть ім'я")
    expect(error_message).to_be_visible()

    context.close()
    browser.close()


# Registration on the page without entering an email.
def test_registration_page_with_empty_email(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://wookie.com.ua/ua/")
    page.get_by_role("link", name="").click()
    page.get_by_role("link", name="Реєстрація").click()
    page.locator("input[name=\"user\\[title\\]\"]").fill("Дар'я Чичкало")
    page.fill("#signup-form input[name=\"user\\[email\\]\"]", "")
    page.locator("#signup-form input[name=\"user\\[pass\\]\"]").fill("19191993")
    page.get_by_role("button", name="Зареєструватись").click()

    # We expect that an error message about the absence of an email value will appear on the page.
    error_message = page.locator("text=Некоректна адреса електронної пошти")
    expect(error_message).to_be_visible()

    context.close()
    browser.close()


# Authorization on the page without entering an email.
def test_empty_email_authorization(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://wookie.com.ua/ua/")
    page.get_by_role("link", name="").click()
    page.fill("#login_form_id input[name=\"user\\[email\\]\"]", "")
    page.locator("#login_form_id input[name=\"user\\[pass\\]\"]").click()
    page.locator("#login_form_id input[name=\"user\\[pass\\]\"]").fill("210793chychkalo")
    page.get_by_role("button", name="Увійти").click()

    # We expect that an error message about the absence of entering an email value will appear on the page.
    error_message = page.locator("text=Некоректна адреса електронної пошти")
    expect(error_message).to_be_visible()

    context.close()
    browser.close()


# Authorization on the page without a password.
def test_empty_password_authorization(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://wookie.com.ua/ua/")
    page.get_by_role("link", name="").click()
    page.locator("#login_form_id input[name=\"user\\[email\\]\"]").fill("darya.chichkalo@gmail.com")
    page.fill("#login_form_id input[name=\"user\\[pass\\]\"]", "")
    page.get_by_role("button", name="Увійти").click()

    # We expect that an error message about the absence of a password will appear on the page.
    error_message = page.locator("text=Вкажіть пароль")
    expect(error_message).to_be_visible()

    context.close()
    browser.close()


# Switch to the mobile version of the site.
def test_open_mobile_version(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://wookie.com.ua/ua/")
    page.get_by_role("link", name="Мобільна версія").click()

    context.close()
    browser.close()


# Return to the full version of the site.
def test_return_to_full_site(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://wookie.com.ua/ua/")
    page.get_by_role("link", name="Мобільна версія").click()
    page.get_by_role("link", name="Повна версія сайту").click()

    context.close()
    browser.close()