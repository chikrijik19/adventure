sek = int(input('сколько секунд? '))
min = sek // 60
hours = min // 60
sek %= 60
min %= 60
print(hours, 'часов', min, 'минут', sek, 'секунд')