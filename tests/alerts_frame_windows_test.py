import time

import pytest
from pages.alerts_frame_windows_page import BrowserWindowPage, AlertPage, FramesPage, NestedFramesPage


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

    @pytest.mark.parametrize("frame_num", ["frame1", "frame2"])
    def test_frames(self,driver, frame_num):
        frame_page = FramesPage(driver, "https://demoqa.com/frames")
        frame_page.open()
        result = frame_page.check_frame(frame_num)
        print(result)
        if frame_num == "frame1":
            assert result == ['500px','350px','This is a sample page'], 'Размер или текст фрейма не соответствуют ожидаемым'
        else:
            assert result == ['100px','100px','This is a sample page'], 'Размер или текст фрейма не соответствуют ожидаемым'

    def test_nested_frames(self,driver):
        nested_frame_page = NestedFramesPage(driver, "https://demoqa.com/nestedframes")
        nested_frame_page.open()
        parent_text, child_text = nested_frame_page.check_nested_frame()
        assert parent_text == "Parent frame", 'Неверный текст в фрейме родителя'
        assert child_text == "Child Iframe", 'Неверный текст в фрейме ребенка'


