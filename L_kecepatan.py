class mobil:
    def __init__(self, merek, kecepatan=0):
        self.merek = merek
        self.kecepatan = kecepatan
        
    def tambah_kecepatan(self, delta):
        self.kecepatan += delta
        
    def info(self):
        print(f"merek mobil: {self.merek} kecepatan: {self.kecepatan} km/jam")
        
mobill= mobil("kuda")
mobill.tambah_kecepatan(50)
mobill.info()