
from calisan import Calisan

class MaviYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yipranma_payi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube,maas)
        self.__tecrube = tecrube
        self.__maas = maas
        self.__yipranma_payi = float(yipranma_payi)

    def get_maas(self):
        return self.__maas

    def set_maas(self, maas):
        self.__maas = self.zam_hakki()
        return self.__maas

    def get_yipranma_payi(self):
        return self.__yipranma_payi

    def set_yipranma_payi(self, yipranma_payi):
        if isinstance(yipranma_payi, float) and 0 <= yipranma_payi <= 1:
            self.__yipranma_payi = yipranma_payi
        else:
            raise ValueError("Geçersiz yıpranma payı girdisi.")

    def zam_hakki(self):
        zam_oranı = self.__yipranma_payi*10
        if self.__tecrube < 24:
            return  self.__maas + self.__maas*zam_oranı/100
        elif self.__tecrube < 48 and self.__maas < 15000:
            zam_oranı = (self.__maas % self.__tecrube) / 2 + zam_oranı
            return  self.__maas + self.__maas*zam_oranı/100
        elif self.__tecrube >= 48 and self.__maas < 25000:
            zam_oranı = (self.__maas % self.__tecrube)/3 + zam_oranı
            return  self.__maas + self.__maas*zam_oranı/100
    def guncel_maas(self):
        self.__maas = self.zam_hakki()
        return self.__maas

    def __str__(self):
        return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nTecrübe: {int(self.get_tecrube()/12)} ay\nYeni Maaş: {self.guncel_maas()}"

