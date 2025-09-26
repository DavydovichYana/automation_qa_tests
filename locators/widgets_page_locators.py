from selenium.webdriver.common.by import By


class AccodianPageLocators:
    SECTION_FIRST = (By.ID, 'section1Heading')
    SECTION_CONTENT_FIRST = (By.ID, 'section1Content')
    SECTION_SECOND = (By.ID, 'section2Heading')
    SECTION_CONTENT_SECOND = (By.CSS_SELECTOR, 'div[id="section2Content"] p')
    SECTION_THIRD = (By.ID, 'section3Heading')
    SECTION_CONTENT_THIRD = (By.CSS_SELECTOR, 'div[id="section3Content"] p')