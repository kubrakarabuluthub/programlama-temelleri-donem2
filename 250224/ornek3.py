not1=int(input("1.sınav notunu girin"))
not2=int(input("2.sınav notunu girin"))
perf=int(input("performans notunu girin"))
ortalama=(not1+not2+perf)/3
if ortalama>=50:
    print("başarılı")
    else:
        print("başarısız")