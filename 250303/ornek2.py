urun1=int(input("ürün toplam fiyatı"))
urun2=int(input("ürün toplam fiyatı"))
toplam=urun1+urun2
if toplam <=200:
    print("ödenecek",toplam)
else:
    ödeme=toplam*0,75
    print("ödenecek miktar",ödeme)