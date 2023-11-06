from unittest import TestCase, main
from Motorcycle import Motorcycle
from Car import Car


class TransportTest(TestCase):

    def setUp(self):
        self.car = Car('Lada', '2104', 2001)
        self.motorcycle = Motorcycle('Suzuki', '8090', 2002)

    def test_instance(self):
        self.assertTrue(isinstance(self.car, Car))
        self.assertTrue(isinstance(self.motorcycle, Motorcycle))

    def test_count_wheels(self):
        self.assertEqual(self.car.num_wheels, 4)
        self.assertEqual(self.motorcycle.num_wheels, 2)

    def test_test_drive(self):
        self.car.test_drive()
        self.motorcycle.test_drive()
        self.assertEqual(self.car.speed, 60)
        self.assertEqual(self.motorcycle.speed, 75)

    def test_park(self):
        self.car.test_drive()
        self.motorcycle.test_drive()
        self.assertEqual(self.car.speed, 60)
        self.assertEqual(self.motorcycle.speed, 75)


        self.car.park()
        self.motorcycle.park()
        self.assertEqual(self.car.speed, 0)
        self.assertEqual(self.motorcycle.speed, 0)


if __name__ == '__main__':
    main()
