import time
from random import randint

from locators.alerts_frame_windows_locators import BrowserWindowPageLocators, AlertPageLocators, FramesPageLocators, \
    NestedFramesPageLocators, ModalDialogPageLocators
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


class AlertPage(BasePage):
    locators = AlertPageLocators()

    def check_see_alert(self):
        self.element_is_visible(self.locators.ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_alert_appear_5_sec(self):
        self.element_is_visible(self.locators.ALERT_AFTER_5_SEC_BUTTON).click()
        time.sleep(5.1)
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_confirm_alert(self, confirm_type):
        self.element_is_visible(self.locators.ALERT_WITH_CONFIRM_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept() if confirm_type == "accept" else alert_window.dismiss()
        text_result = self.element_is_visible(self.locators.CONFIRM_RESULT_TEXT).text
        return text_result

    def check_prompt_alert(self):
        text = f'Autotest text {randint(0,999)}'
        self.element_is_visible(self.locators.ALERT_WITH_PROMPT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self.element_is_visible(self.locators.PROMPT_RESULT_TEXT).text
        return text, text_result

class FramesPage(BasePage):

    locators = FramesPageLocators()

    def check_frame(self, frame_num):
        frame_map = {
            "frame1": self.locators.FIRST_FRAME,
            "frame2": self.locators.SECOND_FRAME,
        }
        if frame_num not in frame_map:
            raise ValueError(f"Unknown frame: {frame_num}")

        frame = self.element_is_present(frame_map[frame_num])
        width = frame.get_attribute("width")
        height = frame.get_attribute("height")
        self.driver.switch_to.frame(frame)
        text = self.element_is_present(self.locators.TITLE_FRAME).text
        self.driver.switch_to.default_content()
        return [width, height, text]

class NestedFramesPage(BasePage):
    locators = NestedFramesPageLocators()

    def check_nested_frame(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.driver.switch_to.frame(parent_frame)
        parent_text = self.element_is_present(self.locators.PARENT_TEXT).text

        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)
        child_text = self.element_is_present(self.locators.CHILD_TEXT).text

        return parent_text, child_text

class ModalDialogPage(BasePage):
    locators = ModalDialogPageLocators()

    def check_modal_dialog(self):
        self.element_is_visible(self.locators.SMALL_MODAL).click()
        title_small = self.element_is_visible(self.locators.TITLE_SMALL_MODAL).text
        body_small = self.element_is_visible(self.locators.BODY_SMALL_MODAL).text
        self.element_is_visible(self.locators.SMALL_MODAL_CLOSE_BUTTON).click()

        self.element_is_visible(self.locators.LARGE_MODAL).click()
        title_large = self.element_is_visible(self.locators.TITLE_LARGE_MODAL).text
        body_large = self.element_is_visible(self.locators.BODY_LARGE_MODAL).text
        self.element_is_visible(self.locators.LARGE_MODAL_CLOSE_BUTTON).click()

        return [title_small, len(body_small)], [title_large, len(body_large)]








