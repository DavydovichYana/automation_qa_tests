from selenium.webdriver.common.by import By


class AccodianPageLocators:
    SECTION_FIRST = (By.ID, 'section1Heading')
    SECTION_CONTENT_FIRST = (By.ID, 'section1Content')
    SECTION_SECOND = (By.ID, 'section2Heading')
    SECTION_CONTENT_SECOND = (By.CSS_SELECTOR, 'div[id="section2Content"] p')
    SECTION_THIRD = (By.ID, 'section3Heading')
    SECTION_CONTENT_THIRD = (By.CSS_SELECTOR, 'div[id="section3Content"] p')

class AutocompletePageLocators:
    MULTIPLE_INPUT = (By.ID, 'autoCompleteMultipleInput')
    MULTIPLE_VALUE = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"]')
    MULTIPLE_REMOVE = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"] svg path')
    SINGLE_CONTAINER = (By.ID, 'autoCompleteSingleContainer')
    SINGLE_INPUT = (By.ID, 'autoCompleteSingleInput')
    SINGLE_VALUE = (By.CSS_SELECTOR, 'div[class="auto-complete__single-value css-1uccc91-singleValue"]')