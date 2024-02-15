length_in_cm = float(input('Введите расстояние в сантиметрах: '))
print(f'{length_in_cm/2.54} дюймов', f'{length_in_cm/(2.54*12)} футов',
      f'{length_in_cm/(2.54*12*3)} ярдов', f'{length_in_cm/(2.54*12*3*1760)} мили', sep='\n')
