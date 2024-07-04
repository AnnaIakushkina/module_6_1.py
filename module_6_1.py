class Car:
    price = 1000000

    def horse_powers(self):
        return 100


class Nissan(Car):
    price = 2000000

    def horse_powers(self):
        return 120


class Kia(Car):
    price = 3000000

    def horse_powers(self):
        return 150


car_ = Car()
print(f'Мощность автомобиля {car_.__class__.__name__} {car_.horse_powers()} л.с.')

nissan_ = Nissan()
print(f'Мощность автомобиля {nissan_.__class__.__name__} {nissan_.horse_powers()} л.с.')

kia_ = Kia()
print(f'Мощность автомобиля {kia_.__class__.__name__} {kia_.horse_powers()} л.с.')