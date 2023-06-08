import pandas as pd

from insan import Insan
from issiz import Issiz
from calisan import Calisan
from maviyaka import MaviYaka
from beyazyaka import BeyazYaka

if __name__ == "__main__":
        # Insan sınıfı için 2 nesne üretme
        insan1 = Insan("12345678901", "Sabri", "Yılmaz", 21, "Erkek", "Türk")
        insan2 = Insan("98765432109", "Ayşe", "Demir", 25, "Kadın", "Türk")

        # Issiz sınıfı için 3 nesne üretme
        issiz1 = Issiz("12345678901", "Ali", "Selimoglu", 33, "Erkek", "Türk",
                       {"mavi yaka": 2, "beyaz yaka": 3, "yönetici": 5})
        issiz2 = Issiz("98765432109", "Ayşe", "Kurt", 27, "Kadın", "Türk",
                       {"mavi yaka": 1, "beyaz yaka": 4, "yönetici": 2})
        issiz3 = Issiz("65498732109", "Mehmet", "Ali", 31, "Erkek", "Türk",
                       {"mavi yaka": 3, "beyaz yaka": 2, "yönetici": 7})

        # Calisan sınıfı için 3 nesne üretme
        calisan1 = Calisan("12345678901", "Kamuran", "Bamboç", 19, "Erkek", "Türk", "diğer", 27, 5000)
        calisan2 = Calisan("98765432109", "İlayda", "Kara", 28, "Kadın", "Türk", "Finans", 33, 7000)
        calisan3 = Calisan("65498732109", "Uğur", "Akgün", 39, "Erkek", "Türk", "inşaat", 21, 9000)

        # MaviYaka sınıfı için 3 nesne üretme
        maviyaka1 = MaviYaka("12345678901", "Murat", "Selimoglu", 34, "Erkek", "Türk", "IT", 24, 5000, 0.3)
        maviyaka2 = MaviYaka("98765432109", "İrem", "AY", 36, "Kadın", "Türk", "Finans", 9, 17000, 0.4)
        maviyaka3 = MaviYaka("65498732109", "Mehmet", "Alın", 38, "Erkek", "Türk", "Mühendislik", 17, 9000, 0.7)

        # BeyazYaka sınıfı için 3 nesne üretme
        beyazyaka1 = BeyazYaka("12345678901", "Mamo", "Selimoglu", 31, "Erkek", "Türk", "IT", 37, 5000, 1000)
        beyazyaka2 = BeyazYaka("98765432109", "Simay", "Kurt", 45, "Kadın", "Türk", "Finans", 39, 7000, 1500)
        beyazyaka3 = BeyazYaka("65498732109", "Yiğit", "Sengoz", 41, "Erkek", "Türk", "Mühendislik", 20, 9000, 2000)

        # Tüm nesnelerin değerlerini içeren bir sözlük oluşturma
        data = {
            "Nesne Değeri": ["İnsan","İnsan","İşsiz","İşsiz","İşsiz","Çalışan", "Çalışan", "Çalışan", "Mavi Yaka", "Mavi Yaka", "Mavi Yaka",
                             "Beyaz Yaka", "Beyaz Yaka", "Beyaz Yaka"],
            "TC No": [insan1.get_tc_no(),insan2.get_tc_no(),issiz1.get_tc_no(),issiz2.get_tc_no(),issiz3.get_tc_no(),
                      calisan1.get_tc_no(), calisan2.get_tc_no(), calisan3.get_tc_no(),
                      maviyaka1.get_tc_no(), maviyaka2.get_tc_no(), maviyaka3.get_tc_no(),
                      beyazyaka1.get_tc_no(), beyazyaka2.get_tc_no(), beyazyaka3.get_tc_no()],
            "Ad": [insan1.get_ad(),insan2.get_ad(),issiz1.get_ad(),issiz2.get_ad(),issiz3.get_ad(),
                   calisan1.get_ad(), calisan2.get_ad(), calisan3.get_ad(),
                   maviyaka1.get_ad(), maviyaka2.get_ad(), maviyaka3.get_ad(),
                   beyazyaka1.get_ad(), beyazyaka2.get_ad(), beyazyaka3.get_ad()],
            "Soyad": [insan1.get_soyad(),insan2.get_soyad(),issiz2.get_soyad(),issiz2.get_soyad(),issiz2.get_soyad(),
                      calisan1.get_soyad(), calisan2.get_soyad(), calisan3.get_soyad(),
                      maviyaka1.get_soyad(), maviyaka2.get_soyad(), maviyaka3.get_soyad(),
                      beyazyaka1.get_soyad(), beyazyaka2.get_soyad(), beyazyaka3.get_soyad()],
            "Yaş": [insan1.get_yas(),insan2.get_yas(),issiz1.get_yas(),issiz2.get_yas(),issiz3.get_yas(),
                    calisan1.get_yas(), calisan2.get_yas(), calisan3.get_yas(),
                    maviyaka1.get_yas(), maviyaka2.get_yas(), maviyaka3.get_yas(),
                    beyazyaka1.get_yas(), beyazyaka2.get_yas(), beyazyaka3.get_yas()],
            "Cinsiyet": [insan1.get_cinsiyet(),insan2.get_cinsiyet(),issiz1.get_cinsiyet(),issiz2.get_cinsiyet(),issiz3.get_cinsiyet(),
                         calisan1.get_cinsiyet(), calisan2.get_cinsiyet(), calisan3.get_cinsiyet(),
                         maviyaka1.get_cinsiyet(), maviyaka2.get_cinsiyet(), maviyaka3.get_cinsiyet(),
                         beyazyaka1.get_cinsiyet(), beyazyaka2.get_cinsiyet(), beyazyaka3.get_cinsiyet()],
            "Uyruk": [insan1.get_uyruk(), insan2.get_uyruk(), issiz1.get_uyruk(), issiz2.get_uyruk(), issiz3.get_uyruk(), calisan1.get_uyruk(), calisan2.get_uyruk(), calisan3.get_uyruk(),
                      maviyaka1.get_uyruk(), maviyaka2.get_uyruk(), maviyaka3.get_uyruk(),
                      beyazyaka1.get_uyruk(), beyazyaka2.get_uyruk(), beyazyaka3.get_uyruk()],
            "Sektör": [None,None,None,None,None,calisan1.get_sektor(),calisan2.get_sektor(),calisan3.get_sektor(),
                       maviyaka1.get_sektor(),maviyaka2.get_sektor(),maviyaka3.get_sektor(),beyazyaka1.get_sektor(),beyazyaka2.get_sektor(),beyazyaka3.get_sektor()],
            "Tecrübe": [None, None, None, None, None,
                        float(f"{calisan1.get_tecrube() / 12:.1f}"),
                        float(f"{calisan2.get_tecrube() / 12:.1f}"),
                        float(f"{calisan3.get_tecrube() / 12:.1f}"),
                        float(f"{maviyaka1.get_tecrube() / 12:.1f}"),
                        float(f"{maviyaka2.get_tecrube() / 12:.1f}"),
                        float(f"{maviyaka3.get_tecrube() / 12:.1f}"),
                        float(f"{beyazyaka1.get_tecrube() / 12:.1f}"),
                        float(f"{beyazyaka2.get_tecrube() / 12:.1f}"),
                        float(f"{beyazyaka3.get_tecrube() / 12:.1f}")],
            "Maaş": [0, 0, 0, 0, 0,
                        float(f"{calisan1.get_maas() :.1f}"),
                        float(f"{calisan2.get_maas() :.1f}"),
                        float(f"{calisan3.get_maas() :.1f}"),
                        float(f"{maviyaka1.get_maas() :.1f}"),
                        float(f"{maviyaka2.get_maas() :.1f}"),
                        float(f"{maviyaka3.get_maas() :.1f}"),
                        float(f"{beyazyaka1.get_maas() :.1f}"),
                        float(f"{beyazyaka2.get_maas() :.1f}"),
                        float(f"{beyazyaka3.get_maas() :.1f}")],
            "Teşvik Primi": [None,None,None,None,None,None,None,None,None,None,None,
                             float(f"{beyazyaka1.get_tesvik_primi() :.2f}"),
                             float(f"{beyazyaka2.get_tesvik_primi() :.2f}"),
                             float(f"{beyazyaka3.get_tesvik_primi() :.2f}")],
            "Yıpranma Payı": [None,None,None,None,None,None,None,None,
                        float(f"{maviyaka1.get_yipranma_payi() :.2f}"),
                        float(f"{maviyaka2.get_yipranma_payi() :.2f}"),
                        float(f"{maviyaka3.get_yipranma_payi() :.2f}"),None,None,None],
            "Yeni Maaş": [None,None,None,None,None,
                          float(f"{calisan1.guncel_maas() :.2f}"),
                          float(f"{calisan2.guncel_maas() :.2f}"),
                          float(f"{calisan3.guncel_maas() :.2f}"),
                          float(f"{maviyaka1.guncel_maas() :.2f}"),
                          float(f"{maviyaka2.guncel_maas() :.2f}"),
                          float(f"{maviyaka3.guncel_maas() :.2f}"),
                          float(f"{beyazyaka1.guncel_maas() :.2f}"),
                          float(f"{beyazyaka2.guncel_maas() :.1f}"),
                          float(f"{beyazyaka3.guncel_maas() :.2f}")
                          ]

        }
        # DataFrame oluşturma
        df = pd.DataFrame(data)
        # Bazı Yerlerde Kullanıldı
        df.fillna(0, inplace=True)

        # DataFrame'i yazdırma
        print(df)
        # B)Şıkkı Tecrübe ve yeni maaşları gruplandırıp yazdırma
        # "Yeni Maaş" sütunundaki non-numeric karakterleri temizleme
        df["Yeni Maaş"] = pd.to_numeric(df["Yeni Maaş"], errors="coerce")

        # Gruplandırma ve ortalamaları hesaplama
        tecrube_ortalamalari = df.groupby("Nesne Değeri")["Tecrübe"].mean()
        yeni_maas_ortalamalari = df.groupby("Nesne Değeri")["Yeni Maaş"].mean()

        # Sonuçları yazdırma
        print("Tecrübe Ortalamaları:")
        print(tecrube_ortalamalari)

        print("\nYeni Maaş Ortalamaları:")
        print(yeni_maas_ortalamalari, "\n")

        # Maaşı 15000 TL üzerinde olanların toplam sayısını bulma
        ust_15k_maas = df[df["Yeni Maaş"] > 15000]
        toplam_sayi = len(ust_15k_maas)

        print("Maaşı 15000 TL üzerinde olanların toplam sayısı:", toplam_sayi, "\n")
        print("# DataFrame'i yeni maaşa göre küçükten büyüğe sıralama")

        # DataFrame'i yeni maaşa göre küçükten büyüğe sıralama
        df_sorted = df.sort_values(by="Yeni Maaş")

        # Sıralanmış DataFrame'i yazdırma
        print(df_sorted)

        # Tecrübesi 3 seneden fazla olan Beyaz yakalıları bulma               E şıkkı
        beyaz_yakalilar = df[df["Nesne Değeri"] == "Beyaz Yaka"]
        tecrube_filtre = beyaz_yakalilar["Tecrübe"] > 3
        beyaz_yaka_yazdirma = beyaz_yakalilar[tecrube_filtre]

        # Sonucu yazdırma
        print(beyaz_yaka_yazdirma)

        print("\nYeni maaşı 1000 TL üzerinde olan için 2-5 satırları")
        # Yeni maaşı 10000 TL üzerinde olanların 2-5 satırlarını seçme
        filtre = df["Yeni Maaş"] > 10000
        secim = df[filtre].iloc[1:5, [1, 12]]

        # Sonucu yazdırma
        print(secim, "\n")

        print("Yeni DataFrame Oluşturma")
        # Yeni DataFrame'i oluşturma
        yeni_df = df[["Ad", "Soyad", "Sektör", "Yeni Maaş"]]

        # Yeni DataFrame'i yazdırma
        print(yeni_df)