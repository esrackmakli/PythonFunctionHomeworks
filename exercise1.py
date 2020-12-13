# odev1

dizi = []
min_sayi = int(input("please enter the min_sayi: "))
max_sayi = int(input("please enter the max_sayi: "))
bolunecek_sayi = int(input("please enter the bolunecek_sayi: "))


def bolunenSayiBulma(min_sayi, max_sayi, bolunecek_sayi):
    for sayilar in range(min_sayi, max_sayi):
        if sayilar % bolunecek_sayi == 0:
            dizi.append(sayilar)

    print(dizi)
    toplam_sayi = str(len(dizi))
    return toplam_sayi


print("toplam sayi: ", bolunenSayiBulma(min_sayi, max_sayi, bolunecek_sayi))
