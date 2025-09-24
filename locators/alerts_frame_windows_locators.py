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