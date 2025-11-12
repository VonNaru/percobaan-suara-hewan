# Mendefinisikan class exception baru bernama UsiaTidakValidError
# Ini mewarisi (inherits) dari class Exception bawaan Python.
class UsiaTidakValidError(Exception):
    """Exception untuk usia yang tidak logis."""
    
    def __init__(self, usia, pesan="Usia tidak valid."):
        self.usia = usia
        self.pesan = pesan
        super().__init__(self.pesan)

def dapat_pesan(umur):
    if umur < 18:
        return "Anda masih dibawah umur"
    elif umur >= 18 and umur <= 45:
        return "Anda masih produktif"
    elif umur >= 45 and umur <= 70:
        return "Anda sudah memasuki masa pensiun"
    else:
        return "Tua bangka elu"
        
def input_usia():
    usia = int(input("Masukkan usia Anda: "))
    
    if usia < 0:
        raise UsiaTidakValidError(usia, "Usia tidak boleh negatif.")
    elif usia > 120:
        raise UsiaTidakValidError(usia, "Usia terlalu besar untuk manusia.")
        
    return usia


try:
    umur = input_usia()
    pesan = dapat_pesan(umur)
    print("Pesan:", pesan)
    print("Usia Anda adalah:", umur)
except UsiaTidakValidError as e:
    print(f"Error: {e.pesan} (diberikan: {e.usia})")
except ValueError:
    print("Error: Input harus berupa angka.")