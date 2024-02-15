import math
radius_of_blind_zone, radius_of_reception = map(int, input('Введите радиус слепой зоны и дальность приёма: ').split())
if radius_of_blind_zone <= radius_of_reception:
    print('Площадь покрываемой территории = ', math.pi*(radius_of_reception**2-radius_of_blind_zone**2))
