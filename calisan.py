from insan import Insan


class Calisan(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__tecrube = tecrube
        self.__maas = maas
        self.__sektor = sektor

    #                          Get/Set Metotları Başlangıç                         #
    def get_sektor(self):
        return self.__sektor

    def set_sektor(self, sektor):
        self.__sektor = sektor

    def get_tecrube(self):
        return self.__tecrube

    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube

    def get_maas(self):
        return self.__maas

    def set_maas(self, maas):
        self.__maas = maas
    #                          Get/Set Metotları Bitiş                         #
    def zam_hakki(self):
        zam_oranı = 0
        if self.__tecrube < 24:
            return self.__maas*zam_oranı/100 + self.__maas
        elif self.__tecrube < 48 and self.__maas < 15000:
            zam_oranı = self.__maas % self.__tecrube
            return self.__maas*zam_oranı/100 + self.__maas
        elif self.__tecrube >= 48 and self.__maas < 25000:
            zam_oranı = (self.__maas % self.__tecrube)/2
            return self.__maas*zam_oranı/100 + self.__maas
    def guncel_maas(self):
        self.__maas = self.zam_hakki()
        return self.__maas
    def __str__(self):
        return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nTecrübe: {int(self.get_tecrube()/12)} ay\nYeni Maaş: {self.guncel_maas()}"