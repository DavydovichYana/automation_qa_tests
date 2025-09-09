from random import randint

from data.data import Person
from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed()

def generated_person():
    yield Person(
        full_name = faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=randint(10, 80),
        department=faker_ru.job(),
        salary=randint(10000, 800000),
        email = faker_ru.email(),
        current_address = faker_ru.address(),
        permanent_address = faker_ru.address(),
    )