import allure

from application import app
from pages.dcloud_tech_main_page import menu_items_dict


def test_main_page_check_link_about_company():
    with allure.step("Открыть страницу 'https://dcloud.tech/'"):
        app.dcloud_tech_main_page.open_page()

    with allure.step("В футере отображается текст 'Главная', 'О компании', 'Проекты', 'Карьера', 'Контакты'"):
        app.dcloud_tech_main_page.header_or_header_should_have_text('.t389__list_item', menu_items_dict)
