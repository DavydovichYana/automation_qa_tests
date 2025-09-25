from selenium.webdriver.common.by import By


class BrowserWindowPageLocators:
    NEW_TAB_BUTTON = (By.ID, 'tabButton')
    NEW_TAB_TITLE = (By.ID, 'sampleHeading')
    NEW_WINDOW_BUTTON = (By.ID, 'windowButton')

class AlertPageLocators:
    ALERT_BUTTON = (By.ID, 'alertButton')
    ALERT_AFTER_5_SEC_BUTTON = (By.ID, 'timerAlertButton')
    ALERT_WITH_CONFIRM_BUTTON = (By.ID, 'confirmButton')
    ALERT_WITH_PROMPT_BUTTON = (By.ID, 'promtButton')
    CONFIRM_RESULT_TEXT = (By.ID, 'confirmResult')
    PROMPT_RESULT_TEXT = (By.ID, 'promptResult')

class FramesPageLocators:
    FIRST_FRAME = (By.ID, 'frame1')
    SECOND_FRAME = (By.ID, 'frame2')
    TITLE_FRAME = (By.ID, 'sampleHeading')

class NestedFramesPageLocators:
    PARENT_FRAME = (By.ID, 'frame1')
    PARENT_TEXT = (By.CSS_SELECTOR, 'body')
    CHILD_FRAME = (By.CSS_SELECTOR, 'body > iframe')
    CHILD_TEXT = (By.CSS_SELECTOR, 'p')
