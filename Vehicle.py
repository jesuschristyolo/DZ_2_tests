from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, company: str, model: str,
                 year_release: int, num_wheels: int,
                 speed: int):
        self.__company = company
        self.__model = model
        self.__year_release = year_release
        self.__num_wheels = num_wheels
        self.__speed = speed

    @abstractmethod
    def test_drive(self):
        pass

    @abstractmethod
    def park(self):
        pass

    def __str__(self):
        return f"This car is a company: {self.__company}," \
               f" release_at: {self.__year_release}, wheels:{self.__num_wheels}," \
               f"  speed: {self.__speed}, model: {self.__model}"
