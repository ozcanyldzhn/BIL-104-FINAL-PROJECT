from insan import Insan
class Issiz(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, tecrube):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__uyruk = uyruk
        self.__tecrube_dict = tecrube

    def get_sektor(self):
        return self.__sektor

    def set_sektor(self):
        self.__sektor = sektor

    def get_statu(self):
        return self.__statu

    def set_statu(self):
        self.__statu = statu
    def get_uyruk(self):
        return self.__uyruk

    def set_uyruk(self, uyruk):
        self.__uyruk = uyruk

    def get_tecrube_dict(self):
        return self.__tecrube_dict

    def set_tecrube_dict(self, tecrube_dict):
        self.__tecrube_dict = tecrube_dict

    def statu_bul(self):
        max_statu = None
        sonuc = 0

        for statu, tecrube in self.__tecrube_dict.items():
            if statu == "mavi yaka":
                etki = tecrube * 0.20
            elif statu == "beyaz yaka":
                etki = tecrube * 0.35
            elif statu == "yönetici":
                etki = tecrube * 0.45
            else:
                etki = 0

            if etki > sonuc:
                sonuc = etki
                max_statu = statu

        return max_statu

    def __str__(self):
        max_statu = self.statu_bul()

        return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nUyruk: {self.get_uyruk()}\nEn uygun statü: {max_statu}"