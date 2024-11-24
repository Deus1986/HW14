import allure

from application import app


def test_main_page_check_leave_a_request():
    with allure.step("Открыть страницу 'https://dcloud.tech/'"):
        app.dcloud_tech_main_page.open_page()

    with allure.step("Проскроллить страницу до 'Начнем работу?'"):
        app.dcloud_tech_main_page.scroll_to_element('//div[text()="Начнем работу?"]')

    with allure.step("Заполнить поле 'Имя', 'Фамилия'"):
        app.dcloud_tech_main_page.fill_name_and_surname()

    with allure.step("Заполнить поле 'Компания и должность'"):
        app.dcloud_tech_main_page.fill_company_and_position()

    with allure.step("Заполнить поле 'Рабочая почта'"):
        app.dcloud_tech_main_page.fill_working_email()

    with allure.step("Заполнить поле 'Телефон'"):
        app.dcloud_tech_main_page.fill_phone()

    with allure.step("Заполнить поле 'Ваше сообщение'"):
        app.dcloud_tech_main_page.fill_message()

    with allure.step("Нажать 'Отправить'"):
        app.dcloud_tech_main_page.click_submit()

    with allure.step("В окне отображается текст 'Спасибо! Данные успешно отправлены.'"):
        app.dcloud_tech_main_page.success_form_shuold_have_text()
