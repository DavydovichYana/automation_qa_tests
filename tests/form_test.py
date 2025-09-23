import time

from pages.form_page import FormPage


class TestFormPage:

    def test_form_page(self,driver):
        form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
        form_page.open()
        name, email, gender, mobile_phone, date_of_birth, current_address, subjects, hobbies, file_name, state_city = form_page.fill_form()
        final_name, final_email, final_gender, final_mobile_phone, final_date_of_birth, final_address, final_subjects, final_hobbies, final_file_name, final_state_city = form_page.save_final_info()
        print(name, email, gender, mobile_phone, date_of_birth, current_address, subjects, hobbies, file_name,
              state_city)
        print(final_name, final_email, final_gender, final_mobile_phone, final_date_of_birth, final_address, final_subjects, final_hobbies, final_file_name, final_state_city)
        assert (name, email, gender, mobile_phone, date_of_birth, current_address, subjects, hobbies, file_name, state_city) == (final_name, final_email, final_gender, final_mobile_phone, final_date_of_birth, final_address, final_subjects, final_hobbies, final_file_name, final_state_city), "Итоговые данные студента не соответствуют введенным данным"