#20010011091/Hasan/Ceyhan
import random

def oyunAlaniDoldurma(liste):           #oyun alananını oluşturma fonksiyonu
    for i in range(10):                 #i 10 olana kadar dön
        satir = []                      #satırları eklemek için liste
        for k in range(10):             #k 10 olana kadar dön
            satir.append("?")           #satır listesine soru işareti ekle
        liste.append(satir)             #listeye satırı ekle
    return liste                        #fonksiyondan liste olarak dön

def yazdirma(liste1):                   #ekrana listeyi yazdırmak için fonkiyon
    satir = list(range(1,11))           #üst taraftaki 1'den 10'a kadar olan sayıları yazdırmak için liste
    satir = list(map(str,satir))        #listenin içindeki sayıları str'ye çevir
    print("   "," ".join(satir))        #virgül veya parantez olmadan ekrana yazdır
    for i in range(10):                 #i 10 olana kadar dön
        liste2 = " ".join(liste1[i])    #gelen listedeki satırları boşluk ile ayır
        if i >= 9:                      #satır sayısıyla beraber satırları yazdır ama 10'dan büyükse satır numarası boşluk bırakmaki başında 2 haneli olduğu için kayma olmasın
            print((i+1),"", liste2)
        else:
            print((i+1)," ",liste2)

def gemi_yapma(boy):                        #gemilerin konumunu ve pozisyonunu seçmek için fonksiyon
    x = ["dikey","yatay"]                   #geminon pozisyonunu seçeceğim liste
    gemi = [boy]                            # [boyu,pozisyon,satir,sutun] gemi değişkeninin içine bunlar eklenecek
    gemi.append(random.choice(x))           #random dikey yatay seçiliyor
    gemi.append(random.randint(1,10))
    gemi.append(random.randint(1, 10))
    a =[]                                   #en sonunda konumlar girilecek liste
    if gemi[1] == "yatay":                  #eğer yataysa buraya girecek dikeyse alttakine köşeye yakınsa geriye doğru yerleştirecek gemiyi yakın değilse ileri doğru
        if gemi[3] < 7:
            for j in range(gemi[0]):
                a.append([gemi[2],gemi[3]+j])
        else:
            for j in range(gemi[0]):
                a.append([gemi[2],gemi[3]-j])
    if gemi[1] == "dikey":
        if gemi[2] < 7:
            for j in range(gemi[0]):
                a.append([gemi[2]+j,gemi[3]])
        else:
            for j in range(gemi[0]):
                a.append([gemi[2]-j,gemi[3]])
    return  a                               #gemi konumları döndürülüyor

def koordinat_alma(atis1,atis2,atislar):    #kullanıcıdan konumları almak ve daha önce girilmiş mi veya listenin dışına çıkıyor mu girilen veriler kontrolü
    while True:
        atis1 = int(input("Satır giriniz: "))
        atis2 = int(input("Sütun giriniz: "))
        if (atis1 >= 1 and atis1 <=10) and (atis2 >= 1 and atis2 <=10):
            break
        else:
            print("Satır ve sütun sayıları 0 ile 11 arasında olmalıdır.")

    if [atis1, atis2] in atislar:
        while True:
            print("Daha önce oraya atış yaptınız, yeniden yer seçiniz.")
            atis1 = int(input("Satır giriniz: "))
            atis2 = int(input("Sütun giriniz: "))
            if [atis1, atis2] not in atislar:
                break
    return atis1,atis2,atislar

def gemiKontrol(gemi1,gemi2,gemi3,gemi4):       #gemilerin koordinatları üst üste geliyor mu kontrolü
    gemitop =[]                                 #tüm koordinatları bir listeye topluyor
    gemitop.append(gemi1)
    gemitop.append(gemi2)
    gemitop.append(gemi3)
    gemitop.append(gemi4)
    for i in gemitop:                           #sırayla listedeki elemanları alıyor
        if gemitop.count(i) >= 2:               #eğer o elemandan iki tane veya daha fazla varsa oyun fonksiyonunu yeniden başlatıyor böylelikle yeni koordinatlar alınıyor
            oyun()

def yeniden_baslama():                          #oyun bitince yeniden başlatmayı soruyor ve seçim değişkenini döndürüyor
    while True:
        secim = input("Yeniden oynamak ister misiniz? Evetse 1'i, hayırsa 2'yi tuşlayın: ")
        if secim == "1":
            print("Oyuna baştan başlıyorsunuz.")
            break
        if secim == "2":
            print("Oyun kapatılıyor.")
            break
    return secim

def mod1(gemi,oyunalani):                           #gemiler gözükecekse mod 1'e geçiyor ve gemilerin olduğu yere + işareti koyuyor
    for i in range(len(gemi)):
        oyunalani[gemi[i][0]-1][gemi[i][1]-1] = "+"
    return oyunalani

def oyun(mod):                                      #oyunun asıl oynandığı fonksiyon yeniden oyuna girebilmek için fonksiyonda oynattım oyunu
    g1 = 0                                          #gemilerin kaç parçası vurulduğunun kontrol değişkeni
    g2 = 0
    g3 = 0
    g4 = 0
    atis1 = 0                                       #kullanıcıdan alınacak atış yerleri
    atis2 =0
    kalan_hak = 33                                  #kalan hak
    oyun_alani = []                                 #oyun alanını atışları tutacak değişken
    atislar = []
    oyun_alani = oyunAlaniDoldurma(oyun_alani)      #oyun alanını doldurma fonksiyonuna gönderme
    gemi1 = gemi_yapma(1)                           #gemileri oluşturmak için gemi oluşturma fonksiyonuna kaç birimlik olacağını belirterek gönderme
    gemi2 = gemi_yapma(2)
    gemi3 = gemi_yapma(3)
    gemi4 = gemi_yapma(4)
    gemiKontrol(gemi1,gemi2,gemi3,gemi4)
    if mod == "1":                                  #mod 1 ise buraya gir mod 1'de olduğunu yazdır ve tek tek oyun alanını güncellemek için gemi konumlarını mod1 fonksiyonuna gönder
        print("Gemiler '+' işareti ile görünüyor.")
        oyun_alani = mod1(gemi1,oyun_alani)
        oyun_alani = mod1(gemi2, oyun_alani)
        oyun_alani = mod1(gemi3, oyun_alani)
        oyun_alani = mod1(gemi4, oyun_alani)
    while True:                                                         #atışlar yapıldıkça başa dönecek döngü
        yazdirma(oyun_alani)                                            #listeyi virgülsüz parantezsiz yazabilmek için fonksiyona gönderiyorum
        print("Kalan atış hakkınız: ", kalan_hak)
        atis1, atis2, atislar = koordinat_alma(atis1,atis2,atislar)     #koordinat alma kalabalık yapmasın diye fonksiyona gönderiyorum
        kalan_hak = kalan_hak - 1                                       #koordinatlar alınınca kalan haktan düşüyorum
        atislar.append([atis1, atis2])                                  #atılan koordinatları tutmak için listeye ekliyorum
        oyun_alani[atis1 - 1][atis2 - 1] = '*'                          #atış yapılan yerleri belirtmek
        vurusKontrol = [g1, g2, g3, g4]                                 #eğer bir yeri vurmadıysa kontrol etmek için bir kopya
        if [atis1, atis2] in gemi1:                                     #atış için seçilen koordinatlarla gemi koordinatları tutuyorsa döngüye gir
            oyun_alani[atis1 - 1][atis2 - 1] = 'x'                      #atış koordinatlrını x'e çevir
            print("Tebrikler bir gemi vurdunuz.")                       #gemiyi vurduğunu ve 1 birimlik olduğu için direk batırdınız yaz
            print("Tebrikler bir gemi batırdınız.")
            g1 = g1 + 1                                                 #gemi 1'in kaç parçasını vurulduğunu kontrol etmek için g1'i arttır
        if [atis1, atis2] in gemi2:                                     #alttaki if'ler içinde yukarıdaki açıklama geçerli !!!!!!!!!!!!!!!!!!!!
            oyun_alani[atis1 - 1][atis2 - 1] = 'x'
            print("Tebrikler bir gemi vurdunuz.")
            g2 = g2 + 1
            if g2 == 2:
                print("Tebrikler bir gemi batırdınız.")

        if [atis1, atis2] in gemi3:
            oyun_alani[atis1 - 1][atis2 - 1] = 'x'
            print("Tebrikler bir gemi vurdunuz.")
            g3 = g3 + 1
            if g3 == 3:
                print("Tebrikler bir gemi batırdınız.")

        if [atis1, atis2] in gemi4:
            oyun_alani[atis1 - 1][atis2 - 1] = 'x'
            print("Tebrikler bir gemi vurdunuz.")
            g4 = g4 + 1
            if g4 == 4:
                print("Tebrikler bir gemi batırdınız.")

        if vurusKontrol == [g1, g2, g3, g4]:                #if'leri geçmeden önceki vurulan parçalar sonrakine eşitse vurmadığını belirt
            print("Malesef isabet edemediniz.")
        if [g1, g2, g3, g4] == [1, 2, 3, 4]:                #tüm gemilerin tüm parçalarının vurulduğunu belirt while'dan çık
            print("Tebrikler ", kalan_hak, " puan ile oyunu kazandınız.")
            break
        if kalan_hak == 0:                                  #haklarının bittiğini belirt while'dan çık
            print("Malesef kaybettiniz.")
            break

if __name__ == '__main__':
    while True:
        mod = input("Oyunda gemilerin yerleri gözükecekse 1'i gözükmeyecekse 2'yi tuşlayın: ")
        if mod == "1" or mod == "2":                        #1'i mi 2'yi mi seçti kontrolü
            break
    oyun(mod)                                               #oyunun oynacağı fonksiyona git, modunda hangisi olduğunu götür
    while True:
        if yeniden_baslama() == "1":                        #yeniden başlatmak istiyorsa oyun fonksiyonuna yine git
            oyun(mod)
        else:
            break