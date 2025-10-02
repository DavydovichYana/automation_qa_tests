import time

import pytest

from pages.widgets_page import AccodianPage, AutocompletePage, DatePickerPage, SliderPage, ProgressBarPage


class TestWidgets:

    @pytest.mark.parametrize("accordian_num", ["first", "second", "third"])
    def test_accordian(self,driver,accordian_num):
        accordian_page = AccodianPage(driver, 'https://demoqa.com/accordian')
        accordian_page.open()
        section_title, content = accordian_page.check_accordian(accordian_num)
        if accordian_num == "first":
            assert section_title.text == "What is Lorem Ipsum?" and len(content) == 574, 'Ошибка в первом аккордеоне'
        elif accordian_num == "second":
            assert section_title.text == "Where does it come from?" and len(content) == 763, 'Ошибка во втором аккордеоне'
        else:
            assert section_title.text == "Why do we use it?" and len(content) == 613, 'Ошибка в третьем аккордеоне'


    def test_fill_multi_autocomplete(self, driver):
        autocomplit_page = AutocompletePage(driver, 'https://demoqa.com/auto-complete')
        autocomplit_page.open()
        colors = autocomplit_page.fill_input_multi()
        colors_result = autocomplit_page.check_multi_color()
        assert colors == colors_result, "Набор исходных и итоговых цветов не совпадает."
        time.sleep(2)

    def test_remove_multi(self, driver):
        autocomplit_page = AutocompletePage(driver, 'https://demoqa.com/auto-complete')
        autocomplit_page.open()
        color = autocomplit_page.fill_input_multi()
        count_value_before, count_value_after = autocomplit_page.remove_value_from_multi()
        assert count_value_after == count_value_before - 1, "Цвет не удален или удалено более 1 цвета"
        time.sleep(2)

    def test_single_autocomplete(self, driver):
        autocomplit_page = AutocompletePage(driver, 'https://demoqa.com/auto-complete')
        autocomplit_page.open()
        color = autocomplit_page.fill_input_single()
        color_result = autocomplit_page.check_single_color()
        assert color == color_result, "Введенный и итоговый цвет не совпадают"

    def test_change_date(self, driver):
        date_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
        date_page.open()
        value_date_before, value_date_after = date_page.select_date()
        assert value_date_before != value_date_after, "Дата не изменена"

    def test_change_date_and_time(self, driver):
        date_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
        date_page.open()
        value_date_before, value_date_after = date_page.select_date_and_time()
        time.sleep(2)
        print(value_date_before, value_date_after)
        assert value_date_before != value_date_after, "Дата не изменена"

    def test_slider(self, driver):
        slider_page = SliderPage(driver, 'https://demoqa.com/slider')
        slider_page.open()
        before, after = slider_page.check_slider()
        assert before != after, 'Начальное и конечное значение совпадают'


    def test_progress_bar(self, driver):
        progress_bar_page = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
        progress_bar_page.open()
        value = progress_bar_page.check_progress_bar()
        assert value != 0, 'Прогресс-бар не отработал'







