from selenium.webdriver.common.by import By


class TextBoxPageLocators:

    # form fields
    FULL_NAME = (By.ID, 'userName')
    EMAIL = (By.ID, 'userEmail')
    CURRENT_ADDRESS = (By.ID, 'currentAddress')
    PERMANENT_ADDRESS = (By.ID, 'permanentAddress')
    SUBMIT = (By.ID, 'submit')


    # created_form
    CREATED_FULL_NAME = (By.CSS_SELECTOR, '#output #name')
    CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    OUTPUT_ITEMS = (By.CSS_SELECTOR, "span[class='text-success']")
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"


class RadioButtonPageLocators:
    YES_RADIOBUTTON = (By.CSS_SELECTOR, "label[class='custom-control-label'][for='yesRadio']")
    IMPRESSIVE_RADIOBUTTON = (By.CSS_SELECTOR, "label[class='custom-control-label'][for='impressiveRadio']")
    NO_RADIOBUTTON = (By.CSS_SELECTOR, "label[class='custom-control-label'][for='noRadio']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")


class WebTablePageLocators:
    #add person form
    ADD_BUTTON = (By.ID, "addNewRecordButton")
    FIRSTNAME_INPUT = (By.ID, "firstName")
    LASTNAME_INPUT = (By.ID, "lastName")
    EMAIL_INPUT = (By.ID, "userEmail")
    AGE_INPUT = (By.ID, "age")
    SALARY_INPUT = (By.ID, "salary")
    DEPARTMENT_INPUT = (By.ID, "department")
    SUBMIT_BUTTON = (By.ID, "submit")

    #tables
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    DELETE_PERSON_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[class='form-control']")
    ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"
    EDIT_BUTTON = (By.CSS_SELECTOR, "span[title='Edit']")
    NO_ROWS_FOUND = (By.CSS_SELECTOR, "div[class='rt-noData']")
    COUNT_ROW_LIST_BUTTON = (By.CSS_SELECTOR, "select[aria-label='rows per page']")


class ButtonsPageLocators:
    DOUBLE_BUTTON = (By.ID, "doubleClickBtn")
    RIGHT_CLICK_BUTTON = (By.ID, "rightClickBtn")
    CLICK_ME_BUTTON = (By.XPATH, '//button[text()="Click Me"]')

    #result
    SUCCESS_DOUBLE = (By.ID, "doubleClickMessage")
    SUCCESS_RIGHT_CLICK = (By.ID, "rightClickMessage")
    SUCCESS_CLICK_ME = (By.ID, "dynamicClickMessage")

class LinksPageLocators:
    SIMPLE_LINK = (By.ID, "simpleLink")
    BAD_REQUEST_LINK = (By.ID, "bad-request")

class UploadDownloadLocators:
    UPLOAD_FILE = (By.ID, "uploadFile")
    SUCCESS_UPLOAD_FILE = (By.ID, "uploadedFilePath")

    DOWNLOAD_FILE = (By.ID, "downloadButton")

class DynamicPropertiesPageLocators:
    COLOR_CHANGE_BUTTON = (By.ID, "colorChange")
    VISIBLE_AFTER_5S_BUTTON = (By.ID, "visibleAfter")
    TIME_INFO_BUTTON = (By.ID, "enableAfter")

