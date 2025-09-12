from enum import Enum
from locators.form_page_locators import FormPageLocators as L

class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"

# для клика по радио-кнопкам
GENDER_LOCATORS = {
    Gender.MALE: L.GENDER_MALE,
    Gender.FEMALE: L.GENDER_FEMALE,
    Gender.OTHER: L.GENDER_OTHER,
}