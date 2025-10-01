import random

from selenium.common import TimeoutException
from selenium.webdriver import Keys

from generator.generator import generated_color
from locators.widgets_page_locators import AccodianPageLocators, AutocompletePageLocators
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



