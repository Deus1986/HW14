from selene import browser, be, command, have
from selenium.webdriver.common.by import By

menu_items_dict = {1: "Главная", 2: "О компании", 3: "Проекты", 4: "Карьера", 5: "Контакты"}


class DcloudTechMainPage:
    def __init__(self):
        pass

    def open_page(self):
        browser.open('/')

    def header_or_header_should_have_text(self, locator, menu_items_dict):
        for i in range(len(menu_items_dict)):
            browser.all(locator)[i].should(have.text(menu_items_dict[i + 1]))

    def click_link_corporate_chat_platform(self):
        browser.element('//div[@data-elem-id="6593130373366"]').click()

    def click_link_about_company(self):
        browser.element('//a[text()="О компании"]').click()

    def scroll_to_element(self, locator):
        browser.element(locator).perform(command.js.scroll_into_view)

    def fill_name_and_surname(self):
        browser.element('//input[@name="Name"]').should(be.blank).type("Joe Literman")

    def fill_company_and_position(self):
        browser.element('//input[@name="Input"]').should(be.blank).type("Parmalat, milkman")

    def fill_working_email(self):
        browser.element('//input[@name="Email"]').should(be.blank).type("milkman1976@gmail.ru")

    def fill_phone(self):
        browser.element('//input[@name="Phone"]').should(be.blank).type("+39 333 3333333")

    def fill_message(self):
        browser.element('//textarea[@name="Textarea"]').should(be.blank).type("Hi, i am glad to meet you)")

    def click_submit(self):
        browser.element('//button[@type="submit"]').click()

    def success_form_shuold_have_text(self):
        browser.element('//div[@id="tildaformsuccesspopuptext"]').should(
            have.text("Thank you! Your data has been submitted."))
