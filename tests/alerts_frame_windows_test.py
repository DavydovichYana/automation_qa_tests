import pytest
from pages.alerts_frame_windows_page import BrowserWindowPage

class TestAlertsFrameWindow:

    @pytest.mark.parametrize("window_type", ["tab", "window"])
    def test_new_tab_and_window(self, driver, window_type):  # <-- добавили self
        page = BrowserWindowPage(driver, "https://demoqa.com/browser-windows")
        page.open()
        text_title = page.check_opened_window(window_type)
        assert text_title == "This is a sample page"