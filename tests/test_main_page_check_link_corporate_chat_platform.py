import allure

from application import app


def test_main_page_check_link_corporate_chat_platform():
    with allure.step("Открыть страницу 'https://dcloud.tech/'"):
        app.dcloud_tech_main_page.open_page()

    with allure.step("Нажать на иконку стрелки для открытия страницы корпоративного чата"):
        app.dcloud_tech_main_page.click_link_corporate_chat_platform()

    with allure.step("На странице корпоративного чата отображается текст 'Корпоративная чат платформа'"):
        app.dcloud_tech_corporate_chat_platform_page.corporate_chat_platform_page_should_have_text()
