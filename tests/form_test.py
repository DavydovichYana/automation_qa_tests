from pages.form_page import FormPage


class TestFormPage:

    def test_form_page(self,driver):
        form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
        form_page.open()
        form_page.fill_form()