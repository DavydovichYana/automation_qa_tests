from selenium.webdriver.common.by import By

from pages.base_page import BasePage


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

class DatePickerPageLocators:
    DATE_INPUT = (By.ID, 'datePickerMonthYearInput')
    DATE_SELECT_MONTH = (By.CLASS_NAME, 'react-datepicker__month-select')
    DATE_SELECT_YEAR = (By.CLASS_NAME, 'react-datepicker__year-select')
    DATE_SELECT_DAY = (By.CSS_SELECTOR, 'div[class^="react-datepicker__day react-datepicker__day"]')

    DATE_TIME_INPUT = (By.ID, 'dateAndTimePickerInput')
    DATE_TIME_MONTH = (By.CLASS_NAME, 'react-datepicker__month-read-view--down-arrow')
    DATE_TIME_MONTH_LIST = (By.CLASS_NAME, 'react-datepicker__month-option')
    DATE_TIME_YEAR = (By.CLASS_NAME, 'react-datepicker__year-read-view--down-arrow')
    DATE_TIME_YEAR_LIST = (By.CLASS_NAME, 'react-datepicker__year-option')
    DATE_TIME_DAY = (By.CSS_SELECTOR, 'div[class^="react-datepicker__day react-datepicker__day"]')
    DATE_TIME_TIME_LIST = (By.CLASS_NAME, 'react-datepicker__time-list-item')

    TIME_DATE_YEAR_SEARCH_OLD = (By.CSS_SELECTOR, '.react-datepicker__navigation--years-previous')
    TIME_DATE_YEAR_SEARCH_NEW = (By.CSS_SELECTOR, '.react-datepicker__navigation--years-upcoming')

class SliderPageLocators:
    INPUT_SLIDER = (By.CSS_SELECTOR, 'input[class="range-slider range-slider--primary"]')
    SLIDER_VALUE = (By.ID, 'sliderValue')

class ProgressBarPageLocators():
    PROGRESS_BAR_BUTTON = (By.ID, 'startStopButton')
    PROGRESS_BAR_VALUE = (By.CSS_SELECTOR, 'div[role="progressbar"]')