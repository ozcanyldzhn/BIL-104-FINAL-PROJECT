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