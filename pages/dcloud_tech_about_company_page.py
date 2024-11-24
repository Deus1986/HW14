import time

from selene import browser, be, command, have
from selenium.webdriver.common.by import By


class DcloudTechAboutCompanyPage:
    def __init__(self):
        pass

    def open_about_company_page(self):
        browser.open('/ru/about/')

    def about_company_page_should_have_text(self):
        browser.element('//div[@field="tn_text_1436365156641"]').should(have.text('Dcloud — это команда независимых '
                                                                                  'разработчиков'))