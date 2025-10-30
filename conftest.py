#файл для фикстур - делает экземпляр вебдрайвера и в конце закрывает его
import datetime

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session") #сетап и теардаун вебдрайвера в рамках одного теста
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f"Screenshot {datetime.date.today()}", attachment_type=allure.attachment_type.PNG)
    driver.quit()

