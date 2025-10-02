import random
import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from generator.generator import generated_color, generated_date
from locators.widgets_page_locators import AccodianPageLocators, AutocompletePageLocators, DatePickerPageLocators
from pages.base_page import BasePage


class AccodianPage(BasePage):
    locators = AccodianPageLocators()

    def check_accordian(self, accordian_num):
        accordian = {'first':
                         {'title': self.locators.SECTION_FIRST,
                          'content': self.locators.SECTION_CONTENT_FIRST},
                     'second':
                         {'title': self.locators.SECTION_SECOND,
                          'content': self.locators.SECTION_CONTENT_SECOND},
                     'third':
                         {'title': self.locators.SECTION_THIRD,
                          'content': self.locators.SECTION_CONTENT_THIRD}}

        section_title = self.element_is_visible(accordian[accordian_num]['title'])
        section_title.click()
        try:
            content = self.element_is_visible(accordian[accordian_num]['content']).text
        except TimeoutException:
            section_title.click()
            content = self.element_is_visible(accordian[accordian_num]['content']).text

        # section_title.click()
        print(section_title, content, len(content))

        return [section_title, content]

class AutocompletePage(BasePage):
    locators = AutocompletePageLocators()

    def fill_input_multi(self):
        colors = random.sample(next(generated_color()).color_name,k=random.randint(1,11))
        for c in colors:
            input_multi = self.element_is_clickable(self.locators.MULTIPLE_INPUT)
            input_multi.send_keys(c)
            input_multi.send_keys(Keys.ENTER)
        return colors

    def remove_value_from_multi(self):
        count_value_before = len(self.elements_are_visible(self.locators.MULTIPLE_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.MULTIPLE_REMOVE)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.elements_are_visible(self.locators.MULTIPLE_VALUE))
        return count_value_before, count_value_after

    def check_multi_color(self):
        colors_in_input = self.elements_are_visible(self.locators.MULTIPLE_VALUE)
        colors = []
        for color in colors_in_input:
            colors.append(color.text)
        return colors

    def fill_input_single(self):
        color = random.sample(next(generated_color()).color_name,k=1)
        input_single = self.element_is_clickable(self.locators.SINGLE_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color[0]

    def check_single_color(self):
        color_in_input = self.element_is_visible(self.locators.SINGLE_VALUE)
        return color_in_input.text

class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    def select_date(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.set_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY, date.day)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after

    def select_date_and_time(self):
        date = next(generated_date())  # Date(year='1980', month='November', day='15', time='12:00')
        inp = self.element_is_visible(self.locators.DATE_TIME_INPUT)
        value_date_before = inp.get_attribute('value')

        # открыть виджет
        inp.click()

        # --- месяц ---
        self.element_is_clickable(self.locators.DATE_TIME_MONTH).click()
        self.set_date_item_from_list(self.locators.DATE_TIME_MONTH_LIST, date.month)

        # --- год ---
        self.element_is_clickable(self.locators.DATE_TIME_YEAR).click()
        self.set_year_for_time_date_picker(self.locators.DATE_TIME_YEAR_LIST, date.year)

        # --- день ---
        # day в генераторе строкой ('15'); если пришёл '05' — нормализуем
        self.set_date_item_from_list(self.locators.DATE_TIME_DAY, str(int(date.day)))

        # --- время ---
        self.set_date_item_from_list(self.locators.DATE_TIME_TIME_LIST, date.time)

        # итоговое значение
        value_date_after = self.element_is_visible(self.locators.DATE_TIME_INPUT).get_attribute('value')
        return value_date_before, value_date_after

    def set_date_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    def set_date_item_from_list(self, elements, value):
        items = self.elements_are_visible(elements)
        for item in items:
            if item.text.strip() == value:
                item.click()
                return
        raise AssertionError(f"Не найден пункт со значением '{value}' для {elements}")

    def set_year_for_time_date_picker(self, element, value: str):
        while True:
            years = self.elements_are_visible(element)
            found = False
            for year in years:
                if year.text.strip() == str(value):
                    self.go_to_element(year)
                    year.click()
                    found = True
                    break
            if found:
                break
            # Если нужного года нет, кликаем на кнопку назад
            self.element_is_clickable(self.locators.TIME_DATE_YEAR_SEARCH_OLD).click()






