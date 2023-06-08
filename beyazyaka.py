
from calisan import Calisan

class BeyazYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, tesvik_primi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__tesvik_primi = tesvik_primi
        self.__maas = maas

    def get_tesvik_primi(self):
        return self.__tesvik_primi

    def set_tesvik_primi(self, tesvik_primi):
        self.__tesvik_primi = tesvik_primi

    def get_maas(self):
        return self.__maas

    def set_maas(self, maas):
        self.__maas = self.zam_hakki()
        return self.__maas

    def zam_hakki(self):
        if self.get_tecrube() < 24:
            return self.__tesvik_primi + self.__maas
        elif self.get_tecrube() < 48 and self.get_maas() < 15000:
            return (self.get_maas() % self.get_tecrube())*5 + self.__tesvik_primi + self.__maas
        elif self.get_tecrube() >= 48 and self.get_maas() < 25000:
            return (self.get_maas() % self.get_tecrube())*4 + self.__tesvik_primi + self.__maas

    def __str__(self):
        return f"{super().__str__()}\nTeşvik Prim: {self.__tesvik_primi}"