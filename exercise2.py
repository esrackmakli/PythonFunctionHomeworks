# odev2

birler = ["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
onlar = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]
sayi = 56

def sayiAtama(sayi):
    x = sayi
    return sayiOkunusu(x)


def sayiOkunusu(sayi):
    birinci = sayi % 10
    ikinci = sayi // 10
    return print("okunuus: " + str(onlar[ikinci] + " " + birler[birinci]))


if sayi < 100 and sayi > 9:
    sayiAtama(sayi)
else:
    print("please enter two digits number!")
