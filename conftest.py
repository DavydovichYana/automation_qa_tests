#файл для фикстур - делает экземпляр вебдрайвера и в конце закрывает его
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
#
# @pytest.fixture(scope="function") #сетап и теардаун вебдрайвера в рамках одного теста
# def driver():
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     driver.maximize_window()
#     yield driver
#     driver.quit()

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
# import random
# from faker import Faker


# @pytest.fixture(scope="session", autouse=True)
# def _seed_everything():
#     random.seed(42)
#     Faker.seed(42)


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--start-maximized")  # чтобы сразу разворачивалось
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options,
    )
    driver.implicitly_wait(0)
    yield driver
    driver.quit()



