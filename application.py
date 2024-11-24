from pages.dcloud_tech_about_company_page import DcloudTechAboutCompanyPage
from pages.dcloud_tech_corporate_chat_platform_page import DcloudTechCorporateChatPlatformPage
from pages.dcloud_tech_main_page import DcloudTechMainPage


class Application:
    def __init__(self):
        self.dcloud_tech_main_page = DcloudTechMainPage()
        self.dcloud_tech_corporate_chat_platform_page = DcloudTechCorporateChatPlatformPage()
        self.dcloud_tech_about_company_page = DcloudTechAboutCompanyPage()


app = Application()
