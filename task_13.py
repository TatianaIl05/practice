import math
radius_of_blind_zone = float(input('Введите радиус слепой зоны: '))
radius_of_reception = float(input('Введите радиус дальности приёма: '))
print('Площадь покрываемой территории = ', abs(math.pi*(radius_of_reception**2-radius_of_blind_zone**2)))
