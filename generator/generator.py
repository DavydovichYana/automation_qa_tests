from random import randint, Random
from data.data import Person
from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed(42)
_rng = Random(42)


def generated_person():
    yield Person(
        full_name=f"{faker_ru.first_name()} {faker_ru.last_name()} {faker_ru.middle_name()}",
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=randint(10, 80),
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
    return file.name,path