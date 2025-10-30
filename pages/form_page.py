import os
import time

from selenium.webdriver import Keys

from data.mappings import GENDER_LOCATORS
from generator.generator import generated_person, generate_subjects, generate_hobbies, generated_file, \
    generate_state_city
from locators.form_page_locators import FormPageLocators
from pages.base_page import BasePage


class FormPage(BasePage):
    L = FormPageLocators()

    def fill_form(self):
        person_info = next(generated_person())
        first_name = person_info.firstname
        last_name = person_info.lastname
        email = person_info.email
        gender = person_info.gender
        mobile_phone = person_info.mobile_phone
        date_of_birth = person_info.date_of_birth
        print(date_of_birth)
        current_address = person_info.current_address

        self.element_is_visible(self.L.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.L.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.L.EMAIL).send_keys(email)
        self.choose_gender(gender)
        self.element_is_visible(self.L.MOBILE).send_keys(mobile_phone)
        self.set_date_of_birth(date_of_birth.year, date_of_birth.strftime("%B"), date_of_birth.day)
        subjects = self.choose_subjects()
        hobbies = self.choose_hobbies()
        file_name = self.upload_file()
        self.element_is_visible(self.L.CURRENT_ADDRESS).send_keys(current_address)
        state, city = self.set_state_and_city()
        self.element_is_visible(self.L.SUBMIT).click()
        return str(
            first_name + ' ' + last_name), email, gender.value, mobile_phone, date_of_birth.strftime("%d %B,%Y"), current_address, ", ".join(subjects), ", ".join(hobbies), file_name, str(
            state + ' ' + city)

    def set_date_of_birth(self, year: str, month: str, day: int):
        # Открыть календарь
        self.element_is_visible(self.L.DATE_OF_BIRTH).click()

        # Выбрать год
        year_dropdown = self.element_is_visible(self.L.YEAR_SELECT)
        year_dropdown.send_keys(year)

        # Выбрать месяц
        month_dropdown = self.element_is_visible(self.L.MONTH_SELECT)
        print(month)
        month_dropdown.send_keys(month)

        # Выбрать день
        day_locator = self.L.day(day)
        self.element_is_visible(day_locator).click()

    def choose_gender(self, gender: str) -> None:
        self.element_is_visible(GENDER_LOCATORS.get(gender)).click()

    def choose_subjects(self):
        subjects = generate_subjects()
        for s in subjects:
            input_field = (self.element_is_visible(self.L.SUBJECTS_INPUT))
            input_field.send_keys(s)
            input_field.send_keys(Keys.ENTER)
        return subjects

    def choose_hobbies(self):
        hobbies = generate_hobbies()
        for h in hobbies:
            if h == "Sports":
                self.element_is_visible(self.L.HOBBY_SPORTS).click()
            elif h == "Reading":
                self.element_is_visible(self.L.HOBBY_READING).click()
            elif h == "Music":
                self.element_is_visible(self.L.HOBBY_MUSIC).click()
        return hobbies

    def upload_file(self):
        file_name, path = generated_file()
        self.element_is_present(self.L.UPLOAD_PICTURE).send_keys(file_name)
        os.remove(path)
        file_name = file_name.split("\\")[-1]
        return file_name

    def set_state_and_city(self):
        state, city = generate_state_city()
        # State
        self.element_is_visible(self.L.STATE_DROPDOWN).click()
        state_input = self.element_is_visible(self.L.STATE_INPUT)
        state_input.send_keys(state)
        state_input.send_keys(Keys.ENTER)

        # City (список зависит от выбранного штата)
        self.element_is_visible(self.L.CITY_DROPDOWN).click()
        city_input = self.element_is_visible(self.L.CITY_INPUT)
        city_input.send_keys(city)
        city_input.send_keys(Keys.ENTER)

        return state, city

    def save_final_info(self):
        name = self.element_is_visible(self.L.STUDENT_NAME_RESULT).text
        email = self.element_is_visible(self.L.STUDENT_EMAIL_RESULT).text
        gender = self.element_is_visible(self.L.GENDER_RESULT).text
        mobile_phone = self.element_is_visible(self.L.MOBILE_RESULT).text
        date_of_birth = self.element_is_visible(self.L.DATE_OF_BIRTH_RESULT).text
        current_address = self.element_is_visible(self.L.ADDRESS_RESULT).text
        subjects = self.element_is_visible(self.L.SUBJECTS_RESULT).text
        hobbies = self.element_is_visible(self.L.HOBBIES_RESULT).text
        file_name = self.element_is_visible(self.L.PICTURE_RESULT).text
        state_city = self.element_is_visible(self.L.STATE_AND_CITY_RESULT).text

        return name, email, gender, mobile_phone, date_of_birth, current_address, subjects, hobbies, file_name, state_city
