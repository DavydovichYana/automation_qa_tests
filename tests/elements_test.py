import time

from pages.base_page import BasePage
from pages.elements_page import TextBoxPage


class TestElements:

    def test_text_box(self,driver):
        text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
        text_box_page.open()
        full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
        output_name, output_email, output_cur_address, output_per_address = text_box_page.check_filled_form()
        assert full_name == output_name, 'Имя не совпадает'
        assert email == output_email, 'Email не совпадает'
        assert current_address == output_cur_address, 'Текущий адрес не совпадает'
        assert permanent_address == output_per_address, 'Постоянный адрес не совпадает'


