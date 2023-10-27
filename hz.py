rub = int(input('сколько рублей стоит батарейка? '))
kop = int(input('сколько копеек стоит батарейка? '))
tov = int(input('сколько ты купишь батареек? '))

rub *= tov
kop *= tov
while kop > 99:
    kop -= 100
    rub += 1

else:
    print('с тебя', rub, 'рублей', 'и', kop, 'копеек')
