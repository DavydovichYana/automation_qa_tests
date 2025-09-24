from locators.alerts_frame_windows_locators import BrowserWindowPageLocators
from pages.base_page import BasePage


class BrowserWindowPage(BasePage):
    locators = BrowserWindowPageLocators()

    def check_opened_window(self, window_type: str):
        button_map = {
            "tab": self.locators.NEW_TAB_BUTTON,
            "window": self.locators.NEW_WINDOW_BUTTON,
        }
        if window_type not in button_map:
            raise ValueError(f"Unknown window type: {window_type}")

        self.element_is_visible(button_map[window_type]).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        return self.element_is_present(self.locators.NEW_TAB_TITLE).text