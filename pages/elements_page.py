import base64
import os
import re
import time
from random import randint

import allure
import requests
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from generator.generator import generated_person, generated_file
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators, ButtonsPageLocators, LinksPageLocators, UploadDownloadLocators, DynamicPropertiesPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    @allure.step("Fill in all fields")
    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address

        with allure.step('filling fields with person`s info'):
            self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
            self.element_is_visible(self.locators.EMAIL).send_keys(email)
            self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
            self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        with allure.step('filling fields with person`s info'):
            self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    @allure.step("checking filled form")
    def check_filled_form(self):
        full_name = self.element_is_visible(self.locators.CREATED_FULL_NAME).text.split(":")[1]
        email = self.element_is_visible(self.locators.CREATED_EMAIL).text.split(":")[1]
        current_address = self.element_is_visible(self.locators.CREATED_CURRENT_ADDRESS).text.split(":")[1]
        permanent_address = self.element_is_visible(self.locators.CREATED_PERMANENT_ADDRESS).text.split(":")[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    @allure.step("clicking random checkboxes")
    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count > 0:
            item = item_list[randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    @allure.step("getting clicked checkboxes")
    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element("xpath", self.locators.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(" ", "").replace(".doc", "").lower()

    @allure.step("getting output result")
    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_ITEMS)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(" ", "").lower()


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    @allure.step("clicking radio button")
    def click_radio_button(self, choice):
        choices = {
            'yes': self.locators.YES_RADIOBUTTON,
            'impressive': self.locators.IMPRESSIVE_RADIOBUTTON,
            'no': self.locators.NO_RADIOBUTTON}

        self.element_is_visible(choices[choice]).click()

    @allure.step("getting output result")
    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    @allure.step("adding a new person")
    def add_new_person(self):
        count = randint(1, 2)
        added_people_list = []
        while count != 0:
            person_info = next(generated_person())
            firstname = person_info.firstname
            lastname = person_info.lastname
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department

            self.element_is_visible(self.locators.ADD_BUTTON).click()

            with allure.step("filling person`s info"):
                self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(firstname)
                self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(lastname)
                self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
                self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
                self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
                self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)

            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
            added_people_list.append([firstname, lastname, str(age), email, str(salary), department])
            count -= 1
        return added_people_list

    @allure.step("cheking new added person")
    def check_new_added_person(self):
        people_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for item in people_list:
            data.append(item.text.splitlines())
        return data

    @allure.step("searching a person")
    def search_some_person(self, keyword):
        self.element_is_visible(self.locators.SEARCH_INPUT).click()
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(keyword)

    @allure.step("checking a searched person")
    def check_searched_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_PERSON_BUTTON)
        row = delete_button.find_element(By.XPATH, self.locators.ROW_PARENT)
        return row.text.splitlines()

    @allure.step("updating person   s info")
    def update_person_info(self):
        # todo сделать метод универсальным для разных полей
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visible(self.locators.EDIT_BUTTON).click()
        self.element_is_visible(self.locators.AGE_INPUT).clear()
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return str(age)

    @allure.step("deleting a person")
    def delete_person(self):
        self.element_is_present(self.locators.DELETE_PERSON_BUTTON).click()

    @allure.step("cheking a deleted person")
    def check_deteted_person(self):
        return self.element_is_present(self.locators.NO_ROWS_FOUND).text

    @allure.step("selecting rows")
    def select_count_of_rows(self):
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for x in count:
            count_row_button = self.element_is_visible(self.locators.COUNT_ROW_LIST_BUTTON)
            self.go_to_element(count_row_button)
            count_row_button.click()

            self.element_is_visible((By.CSS_SELECTOR, f"option[value='{x}']")).click()
            list_rows = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)

            data.append(len(list_rows))
        return data


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    @allure.step("click on a button")
    def click_on_different_button(self, type_click):
        if type_click == "double":
            self.action_double_click(self.element_is_visible(self.locators.DOUBLE_BUTTON))
            return self.check_clicked_button(self.locators.SUCCESS_DOUBLE)

        if type_click == "right":
            self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON))
            return self.check_clicked_button(self.locators.SUCCESS_RIGHT_CLICK)

        if type_click == "click":
            self.element_is_visible(self.locators.CLICK_ME_BUTTON).click()
            return self.check_clicked_button(self.locators.SUCCESS_CLICK_ME)

    def check_clicked_button(self, element):
        return self.element_is_present(element).text


class LinksPage(BasePage):
    # TODO сделать для всех ссылок
    locators = LinksPageLocators()

    @allure.step("checking a link")
    def check_new_tab_simple_link(self):
        simple_link = self.element_is_visible(self.locators.SIMPLE_LINK)
        link_href = simple_link.get_attribute("href")
        request = requests.get(link_href)
        if request.status_code == 200:
            simple_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return link_href, url
        else:
            return request.status_code

    @allure.step("checking a broken link")
    def check_broken_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_present(self.locators.BAD_REQUEST_LINK).click()
        else:
            return request.status_code


class UploadDownloadPage(BasePage):
    locators = UploadDownloadLocators()

    @allure.step("uploading a file")
    def upload_file(self):
        file_name, path = generated_file()
        self.element_is_present(self.locators.UPLOAD_FILE).send_keys(file_name)
        os.remove(path)

        file_name = file_name.split("\\")[-1]
        result_text = self.element_is_present(self.locators.SUCCESS_UPLOAD_FILE).text.split("\\")[-1]

        return file_name, result_text

    @allure.step("downloading a file")
    def download_file(self):
        link = self.element_is_present(self.locators.DOWNLOAD_FILE).get_attribute("href")
        link_b = base64.b64decode(link)
        path_name_file = r'C:\Users\lucky\PycharmProjects\automation_qa_tests\test_file_image.jpg'
        with open(path_name_file, "wb+") as f:
            offset = link_b.find(b"\xff\xd8")
            f.write(link_b[offset:])
            check_file = os.path.exists(path_name_file)
            f.close()
        os.remove(path_name_file)
        return check_file

class DynamicPropertiesPage(BasePage):
    locators = DynamicPropertiesPageLocators()

    @allure.step("checking changed colours")
    def check_changed_colors(self):
        color_button = self.element_is_present(self.locators.COLOR_CHANGE_BUTTON)
        color_button_before = color_button.value_of_css_property("color")

        time_info = self.find_time_info()

        time.sleep(time_info)
        color_button_after = color_button.value_of_css_property("color")
        return color_button_before, color_button_after

    @allure.step("checking appearing of a button")
    def check_appear_of_button(self):
        try:
            self.element_is_visible(self.locators.VISIBLE_AFTER_5S_BUTTON)
        except TimeoutException:
            return False
        return True

    @allure.step("checking enable button")
    def check_enable_button(self):
        try:
            enable_button = self.element_is_clickable(self.locators.TIME_INFO_BUTTON)
        except TimeoutException:
            return False
        return True

    @allure.step("finding time information")
    def find_time_info(self):
        time_info_button = self.element_is_visible(self.locators.TIME_INFO_BUTTON).text
        time_info = int(re.findall(r'\d+', time_info_button)[0])
        return time_info





