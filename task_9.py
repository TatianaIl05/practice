songs = []
print('Введите плей-лист папы:')
for i in range(5):
    song = input()
    songs.append(song)
print('Плей-лист мамы:')
for j in range(5):
    print(songs[::-1][j])
