from dataclasses import dataclass


@dataclass
class Person:
    full_name: str = None
    firstname: str = None
    lastname: str = None
    age: int = None
    salary: int = None
    department: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None
    date_of_birth: str = None
    gender: str = None
    mobile_phone: str = None

@dataclass
class Color:
    color_name: list = None


