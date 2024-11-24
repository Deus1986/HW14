import time

from selene import browser, be, command, have
from selenium.webdriver.common.by import By


class DcloudTechCorporateChatPlatformPage:
    def __init__(self):
        pass

    def corporate_chat_platform_page_should_have_text(self):
        browser.element('//div[@field= "tn_text_8265015865691"]').should(have.text('Корпоративная\nчат платформа'))
