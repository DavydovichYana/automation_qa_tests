import time

import pytest
from pages.alerts_frame_windows_page import BrowserWindowPage, AlertPage


class TestAlertsFrameWindow:

    @pytest.mark.parametrize("window_type", ["tab", "window"])
    def test_new_tab_and_window(self, driver, window_type):  # <-- добавили self
        page = BrowserWindowPage(driver, "https://demoqa.com/browser-windows")
        page.open()
        text_title = page.check_opened_window(window_type)
        assert text_title == "This is a sample page"

    def test_see_alert(self,driver):
        alert_page = AlertPage(driver, "https://demoqa.com/alerts")
        alert_page.open()
        alert_text = alert_page.check_see_alert()
        assert alert_text == "You clicked a button", "Неверный текст алерта"

    def test_check_alert_appear_5_sec(self,driver):
        alert_page = AlertPage(driver, "https://demoqa.com/alerts")
        alert_page.open()
        alert_text = alert_page.check_alert_appear_5_sec()
        assert alert_text == "This alert appeared after 5 seconds", "Неверный текст алерта"

    @pytest.mark.parametrize("confirm_type", ["accept", "dismiss"])
    def test_check_alert_confirm(self,driver,confirm_type):
        alert_page = AlertPage(driver, "https://demoqa.com/alerts")
        alert_page.open()
        text_result = alert_page.check_confirm_alert(confirm_type)
        time.sleep(5)
        if confirm_type == "accept":
            assert text_result == "You selected Ok"
        else:
            assert text_result == "You selected Cancel"

    def test_prompt_alert(self,driver):
        alert_page = AlertPage(driver, "https://demoqa.com/alerts")
        alert_page.open()
        text, alert_text = alert_page.check_prompt_alert()
        assert alert_text == f"You entered {text}", "Неверный текст алерта"