import random
import allure
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    UploadDownloadPage, DynamicPropertiesPage

@allure.suite("Elements")
class TestElements:

    @allure.feature("TextBox")
    class TestTextBox:
        @allure.title("Check TextBox")
        def test_text_box(self,driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_address, output_per_address = text_box_page.check_filled_form()
            assert full_name == output_name, 'Имя не совпадает'
            assert email == output_email, 'Email не совпадает'
            assert current_address == output_cur_address, 'Текущий адрес не совпадает'
            assert permanent_address == output_per_address, 'Постоянный адрес не совпадает'

    @allure.feature("CheckBox")
    class TestCheckBox:
        @allure.title("Check CheckBox")
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            checked_checkboxes = check_box_page.get_checked_checkboxes()
            final_checked_checkboxes = check_box_page.get_output_result()
            assert checked_checkboxes == final_checked_checkboxes, "Чек-боксы не выбраны"

    @allure.feature("RadioButton")
    class TestRadioButton:
        @allure.title("Check RadioButton")
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_radio_button('no')
            output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes', "Yes не выбран"
            assert output_impressive == 'Impressive', "Impressive не выбран"
            assert output_no == 'No', "No не выбран"

    @allure.feature("WebTables")
    class TestWebTables:
        @allure.title("Check Adding a person")
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            added_people_list = web_table_page.add_new_person()
            table_result = web_table_page.check_new_added_person()
            print(added_people_list)
            print(table_result)
            for new_person in added_people_list:
                assert new_person in table_result

    @allure.title("Check Searching a person")
    def test_web_page_search_person(self, driver):
        #реализован полный поиск, а еще можно сделать по частичному совпадению
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        added_people_list = web_table_page.add_new_person()
        random_added_person = random.choice(added_people_list)
        keyword = random_added_person[random.randint(0, len(random_added_person) - 1)]
        web_table_page.search_some_person(keyword)
        searched_person = web_table_page.check_searched_person()
        assert keyword in searched_person, "Персона не найдена в таблице"

    @allure.title("Check Updating a person")
    def test_web_page_update_person_info(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        added_people_list = web_table_page.add_new_person()
        random_added_person = random.choice(added_people_list)
        lastname = random_added_person[1]
        web_table_page.search_some_person(lastname)
        age = web_table_page.update_person_info()
        row = web_table_page.check_searched_person()
        print(age, row)
        assert age in row, 'Информация о персоне не изменена'

    @allure.title("Check Deleting a person")
    def test_web_page_delete_person(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        added_people_list = web_table_page.add_new_person()
        random_added_person = random.choice(added_people_list)
        email = random_added_person[3]
        web_table_page.search_some_person(email)
        web_table_page.delete_person()
        text = web_table_page.check_deteted_person()
        assert text == "No rows found", "Персона не удалена"

    @allure.title("Check Changing Count of rows")
    def test_web_table_change_count_rows(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        count = web_table_page.select_count_of_rows()
        assert count==[5,10,20,25,50,100], "Невозможно выбрать количество строк"

    @allure.feature("Buttons")
    class TestButtons:
        @allure.title("Check clicking buttons")
        def test_different_click_on_the_button(self, driver):
            button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            double = button_page.click_on_different_button('double')
            right = button_page.click_on_different_button('right')
            click = button_page.click_on_different_button('click')
            assert double == "You have done a double click", "Двойной клик не сработал"
            assert right == "You have done a right click", "Правый клик не сработал"
            assert click == "You have done a dynamic click", "Обычный клик не сработал"

    @allure.feature("Links")
    class TestButtons:
        @allure.title("Check links")
        def test_check_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_new_tab_simple_link()
            assert href_link == current_url, 'Ссылка сломана или некорректна'

    @allure.feature("BrokenLinks")
    class TestBrokenLinks:
        @allure.title("Check broken links")
        def test_broken_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_broken_link('https://demoqa.com/bad-request')
            assert response_code == 400, "Статус-код не равен ожидаемому"

    @allure.feature("UploadAndDownload")
    class TestBrokenLinks:
        @allure.title("Check upload a file")
        def test_upload_file(self, driver):
            upload_download_page = UploadDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            file_name, result_text = upload_download_page.upload_file()
            assert file_name == result_text, "Ошибка при загрузке файла"

        @allure.title("Check download a file")
        def test_download_file(self,driver):
            upload_download_page = UploadDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            check = upload_download_page.download_file()
            assert check is True, "Ошибка при выгрузке файла"

    @allure.feature("DynamicProperties")
    class TestBrokenLinks:
        @allure.title("Check changing colour of buttons")
        def test_change_color_of_buttons(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            color_button_before, color_button_after = dynamic_properties_page.check_changed_colors()
            assert color_button_before != color_button_after

        @allure.title("Check appearing of buttons")
        def test_check_appear_of_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            invisible_button_result = dynamic_properties_page.check_appear_of_button()
            assert invisible_button_result is True, "Кнопка не появилась"

        @allure.title("Check enable buttons")
        def test_check_enable_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            enable = dynamic_properties_page.check_enable_button()
            assert enable is True, "Кнопка осталась задизейбленной"






