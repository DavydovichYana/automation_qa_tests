from random import randint, Random, random, sample, choice
from data.data import Person
from faker import Faker

from data.mappings import Gender

faker_ru = Faker('ru_RU')
# Faker.seed(42)
_rng = Random(21)


def generated_person():
    yield Person(
        full_name=f"{faker_ru.first_name()} {faker_ru.last_name()} {faker_ru.middle_name()}",
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=randint(10, 80),
        date_of_birth=faker_ru.date_of_birth(),
        gender=_rng.choice(list(Gender)),
        mobile_phone=faker_ru.msisdn()[-10:],
        department=faker_ru.job(),
        salary=_rng.randint(100000, 800000),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
    )


def generated_file():
    path = rf'C:\Users\lucky\PycharmProjects\automation_qa_tests\test_file_{_rng.randint(0, 999)}.txt'
    file = open(path, "w+")
    file.write(f"Hello World{_rng.randint(0, 999)}")
    file.close()
    return file.name, path


def generate_subjects(min_count=0, max_count=3):
    STUDENT_SUBJECTS = [
        "Hindi",
        "English",
        "Maths",
        "Physics",
        "Chemistry",
        "Biology",
        "Computer Science",
        "Commerce",
        "Accounting",
        "Economics",
        "Arts",
        "Social Studies",
        "History",
        "Civics",
    ]

    """Генерирует случайный список предметов студента"""
    count = randint(min_count, max_count)
    return sample(STUDENT_SUBJECTS, count)

def generate_hobbies(min_count=0, max_count=3):
    HOBBIES = ["Sports", "Reading", "Music"]
    count = randint(min_count, max_count)
    return sample(HOBBIES, count)


def generate_state_city():
    STATE_CITIES = {
        "NCR": ["Delhi", "Gurgaon", "Noida"],
        "Uttar Pradesh": ["Agra", "Lucknow", "Merrut"],
        "Haryana": ["Karnal", "Panipat"],
        "Rajasthan": ["Jaipur", "Jaiselmer"],
    }
    state = choice(list(STATE_CITIES.keys()))
    city = choice(STATE_CITIES[state])
    return state, city
