import time

import pytest

from pages.widgets_page import AccodianPage, AutocompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, \
    ToolTipsPage, MenuPage


class TestWidgets:

    @pytest.mark.parametrize("accordian_num", ["first", "second", "third"])
    def test_accordian(self, driver, accordian_num):
        accordian_page = AccodianPage(driver, 'https://demoqa.com/accordian')
        accordian_page.open()
        section_title, content = accordian_page.check_accordian(accordian_num)
        if accordian_num == "first":
            assert section_title.text == "What is Lorem Ipsum?" and len(content) == 574, 'Ошибка в первом аккордеоне'
        elif accordian_num == "second":
            assert section_title.text == "Where does it come from?" and len(
                content) == 763, 'Ошибка во втором аккордеоне'
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

    @pytest.mark.parametrize("name_tab", ["what", "origin", "use", "more"])
    def test_tabs(self, driver, name_tab):
        tab_titles = {"what": "What", "origin": "Origin", "use": "Use", "more": "More"}
        tabs = TabsPage(driver, 'https://demoqa.com/tabs')
        tabs.open()
        button_text, len_content = tabs.check_tabs(name_tab)
        assert button_text == tab_titles[name_tab] and len_content != 0, f"Вкладка {button_text} работает некорректно."


    def test_tool_tips(self, driver):
        tool_tips_page = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
        tool_tips_page.open()
        text_button, text_input, text_contrary, text_digits = tool_tips_page.check_tool_tips()
        assert text_button == "You hovered over the Button", "Неверный текст тултипа"
        assert text_input == "You hovered over the text field", "Неверный текст тултипа"
        assert text_contrary == "You hovered over the Contrary", "Неверный текст тултипа"
        assert text_digits == "You hovered over the 1.10.32", "Неверный текст тултипа"

    def test_menu(self, driver):
        menu_page = MenuPage(driver, 'https://demoqa.com/menu#')
        menu_page.open()
        data = menu_page.check_menu()
        expected_menu = ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1', 'Sub Sub Item 2', 'Main Item 3']
        assert data == expected_menu
        print(data)
