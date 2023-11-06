from Vehicle import Vehicle

class Car(Vehicle):

    def __init__(self, company: str, model: str, year_release: int, num_wheels: int = 4, speed: int = 0):
        super().__init__(company, model, year_release, num_wheels, speed)
        self.__company = company
        self.__model = model
        self.__year_release = year_release
        self.__num_wheels = num_wheels
        self.__speed = speed

    def test_drive(self):
        self.__speed = 60

    def park(self):
        self.__speed = 0

    @property
    def company(self):
        return self.__company

    @property
    def model(self):
        return self.__model

    @property
    def year_release(self):
        return self.__year_release

    @property
    def num_wheels(self):
        return self.__num_wheels

    @property
    def speed(self):
        return self.__speed

