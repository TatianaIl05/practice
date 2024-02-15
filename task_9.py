j = ['Номер рейса: ', 'Название авиакомании(на русском): ', 'Название авиакомпании(на английском): ',
     'Город прилёта(на русском): ', 'Город прилёта(на английском): ']
all_infrmation = []
for i in j:
    infrmation = input(i)
    all_infrmation.append(infrmation)
print(f'Заканчивается посадка на рейс {all_infrmation[0]} {all_infrmation[1]} до {all_infrmation[3]}')
print(f'This is the final boarding call for {all_infrmation[2]} flight {all_infrmation[0]} to {all_infrmation[4]}')
