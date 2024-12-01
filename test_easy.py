from playwright.sync_api import Playwright, sync_playwright, expect


def test_easy(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://web.telegram.org/k/#@EmojiRy_Bot")
    page.get_by_role("button", name="START").click()
    expect(page.locator("section")).to_contain_text("Откуда ты ?")
    page.get_by_role("link", name=" 🇷🇺 РОССИЯ").click()
    page.get_by_role("button", name="").click()
    expect(page.locator("section")).to_contain_text("Я самый уникальный каталог в Telegram! Выбери действие в меню")
    expect(page.locator("section")).to_contain_text("Так же я умею работать в чатах!")

    # ---------------------
    context.close()
    browser.close()


