import allure

from application import app


def test_main_page_check_link_about_company():
    with allure.step("Открыть страницу 'https://dcloud.tech/'"):
        app.dcloud_tech_main_page.open_page()

    with allure.step("Нажать в хэдере 'О компании'"):
        app.dcloud_tech_main_page.click_link_about_company()

    with allure.step("На странице 'О компании' отображается текст 'Dcloud — это команда независимых разработчиков'"):
        app.dcloud_tech_about_company_page.about_company_page_should_have_text()
