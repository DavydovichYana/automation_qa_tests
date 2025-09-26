from selenium.common import TimeoutException

from locators.widgets_page_locators import AccodianPageLocators
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
