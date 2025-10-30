from selenium.webdriver.common.by import By

class FormPageLocators:
    # --- Поля ввода ---
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    MOBILE = (By.ID, "userNumber")
    DATE_OF_BIRTH = (By.ID, "dateOfBirthInput")
    SUBJECTS_INPUT = (By.ID, "subjectsInput")
    CURRENT_ADDRESS = (By.ID, "currentAddress")

    # --- Радио-кнопки Gender ---
    GENDER_MALE = (By.XPATH, "//label[@for='gender-radio-1']")
    GENDER_FEMALE = (By.XPATH, "//label[@for='gender-radio-2']")
    GENDER_OTHER = (By.XPATH, "//label[@for='gender-radio-3']")

    # --- Чекбоксы Hobbies ---
    HOBBY_SPORTS = (By.XPATH, "//label[@for='hobbies-checkbox-1']")
    HOBBY_READING = (By.XPATH, "//label[@for='hobbies-checkbox-2']")
    HOBBY_MUSIC = (By.XPATH, "//label[@for='hobbies-checkbox-3']")

    # --- Загрузка файла ---
    UPLOAD_PICTURE = (By.ID, "uploadPicture")

    # --- State & City (React-dropdowns) ---
    STATE_DROPDOWN = (By.ID, "state")
    STATE_INPUT = (By.ID, "react-select-3-input")
    CITY_DROPDOWN = (By.ID, "city")
    CITY_INPUT = (By.ID, "react-select-4-input")

    # --- Кнопка отправки ---
    SUBMIT = (By.ID, "submit")

    # --- Итоговая таблица ---
    STUDENT_NAME_RESULT = (By.XPATH, "//td[text()='Student Name']/following-sibling::td")
    STUDENT_EMAIL_RESULT = (By.XPATH, "//td[text()='Student Email']/following-sibling::td")
    GENDER_RESULT = (By.XPATH, "//td[text()='Gender']/following-sibling::td")
    MOBILE_RESULT = (By.XPATH, "//td[text()='Mobile']/following-sibling::td")
    DATE_OF_BIRTH_RESULT = (By.XPATH, "//td[text()='Date of Birth']/following-sibling::td")
    SUBJECTS_RESULT = (By.XPATH, "//td[text()='Subjects']/following-sibling::td")
    HOBBIES_RESULT = (By.XPATH, "//td[text()='Hobbies']/following-sibling::td")
    PICTURE_RESULT = (By.XPATH, "//td[text()='Picture']/following-sibling::td")
    ADDRESS_RESULT = (By.XPATH, "//td[text()='Address']/following-sibling::td")
    STATE_AND_CITY_RESULT = (By.XPATH, "//td[text()='State and City']/following-sibling::td")


    # Поле ввода даты рождения
    DATE_OF_BIRTH_INPUT = (By.ID, "dateOfBirthInput")

    # Выпадающие списки выбора года и месяца
    YEAR_SELECT = (By.CLASS_NAME, "react-datepicker__year-select")
    MONTH_SELECT = (By.CLASS_NAME, "react-datepicker__month-select")

    # День месяца (локатор будет формироваться динамически)
    @staticmethod
    def day(day_number: int):
        # day_number — число месяца (1–31)
        return (
            By.XPATH,
            f"//div[contains(@class,'react-datepicker__day') "
            f"and not(contains(@class,'react-datepicker__day--outside-month')) "
            f"and normalize-space(text())='{day_number}']"
        )