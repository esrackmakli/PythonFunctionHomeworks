# odev3

vize1 = int(input("vize1 sınav notu girin: "))
vize2 = int(input("vize2 sınav notu girin: "))
final = int(input("final sınav notu girin: "))

if 0 < vize1 < 100 and 0 < vize2 < 100 and 0 < final < 100:

    toplam_not = (vize1 * 0.3) + (vize2 * 0.3) + (final * 0.140)
    if toplam_not >= 90:
        print("harf notunuz: AA")
    if toplam_not >= 85 and toplam_not < 90:
        print("harf notunuz: BA")
    if toplam_not >= 80 and toplam_not < 85:
        print("harf notunuz: BB")
    if toplam_not >= 75 and toplam_not < 80:
        print("harf notunuz: CB")
    if toplam_not >= 70 and toplam_not < 75:
        print("harf notunuz: CC")
    if toplam_not >= 65 and toplam_not < 70:
        print("harf notunuz: DC")
    if toplam_not >= 60 and toplam_not < 65:
        print("harf notunuz: DD")
    if toplam_not >= 55 and toplam_not < 60:
        print("harf notunuz: FD")
    if toplam_not < 55:
        print("harf notunuz: FF")
else:
    print("Harf notunuz FF KALDINIZ ")
