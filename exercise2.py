# odev2

birler = ["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
onlar = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]


def sayiAtama(sayi):
    x = sayi
    return print('okunus: ', sayiOkunusu(x))


def sayiOkunusu(sayi):
    birinci = sayi % 10
    ikinci = sayi // 10
    return str(onlar[ikinci] + " " + birler[birinci])


digits = 0
sayi = 49

while sayi > 0:
    digits += 1
    sayi //= 10

if digits == 2:
    sayiAtama(sayi)
else:
    print("please enter two digits number!")
