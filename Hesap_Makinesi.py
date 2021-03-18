print()
print("Hosgeldiniz!!! Yapmak Istediginiz Islemi Menuden Seciniz Lutfen.....")


while True:
    while True:

        secim= input("""
        Menu:
    
        1: Toplama 
        2: Cikarma
        3: Carpma
        4: Bolme
        5: Mod Alma
        6: Karekok Hesaplama
        7: Karesini Hesaplama
        8: Cikis Yapma
        """)




        if secim== '1':
            sayi1 = float(input("Birinci Sayiyi Giriniz: "))
            sayi2 = float(input("Ikinci sayiyi Giriniz: "))
            toplam=sayi1+sayi2
            print("Sayilarin Toplami: {} ".format(toplam))
            break


        elif secim=='2':
             sayi1 = float(input("Birinci Sayiyi Giriniz: "))
             sayi2 = float(input("Ikinci sayiyi Giriniz: "))
             cikarma=sayi1-sayi2
             print("Sayilarin Farki: {}".format(cikarma))
             break


        elif secim== '3':
            sayi1 = float(input("Birinci Sayiyi Giriniz: "))
            sayi2 = float(input("Ikinci sayiyi Giriniz: "))
            carpma=sayi1*sayi2
            print("Sayilarin Carpimi: {}".format(carpma))
            break



        elif secim=='4':
            sayi1 = float(input("Birinci Sayiyi Giriniz: "))
            sayi2 = float(input("Ikinci sayiyi Giriniz: "))
            bolme= sayi1/sayi2
            print("Sayilarin Bolumu: {}".format(bolme))
            break



        elif secim=='5':
            sayi1 = float(input("Birinci Sayiyi Giriniz: "))
            sayi2 = float(input("Ikinci sayiyi Giriniz: "))
            mod=sayi1%sayi2
            print("Birinci Sayinin Ikinci Sayiya Bolumunden Kalan: {}".format(mod))
            break



        elif secim== '6':
            sayi1 = float(input("Birinci Sayiyi Giriniz: "))
            karekok= sayi1*0.5
            print("Sayinin Karekok Degeri: {}".format(karekok))
            break



        elif secim=='7':
            sayi1 = float(input("Birinci Sayiyi Giriniz: "))
            kare= sayi1*sayi1
            print("Sayinin Karesi: {}".format(kare))
            break



        elif secim== '8':
            quit("Programdan Cikis Yapildi...... Gorusmek uzere...")
            break


        else:
            print("Yalnis Tuslama Yaptiniz: ")
            break



    print()
    input("Tekrar Menuye Donmek Icin Onaylayiniz: ")
    continue

    



