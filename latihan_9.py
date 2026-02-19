def pilih_aktivitas_greedy(activities):
    """
    Memilih aktivitas maksimum yang tidak bentrok menggunakan pendekatan greedy.
    'activities' adalah list of list, format: [nama_aktivitas, start_time, finish_time]
    
    Fungsi ini TIDAK BERUBAH dari kode sebelumnya.
    """
    
    # Langkah 2: Sortir aktivitas berdasarkan finish time (elemen indeks ke-2)
    activities.sort(key=lambda x: x[2])
    
    # List untuk menyimpan hasil
    hasil_terpilih = []
    
    # Langkah 4: Aktivitas pertama selalu dipilih
    if not activities:
        return []
        
    i = 0
    hasil_terpilih.append(activities[i])
    
    # Langkah 5: Catat waktu selesai dari aktivitas yang terakhir dipilih
    waktu_selesai_terakhir = activities[i][2]
    
    # Langkah 6: Loop sisa aktivitas
    for j in range(1, len(activities)):
        
        waktu_mulai_sekarang = activities[j][1]
        
        # Langkah 7 & 8: Cek apakah aktivitas ini compatible (tidak bentrok)
        if waktu_mulai_sekarang >= waktu_selesai_terakhir:
            hasil_terpilih.append(activities[j])
            waktu_selesai_terakhir = activities[j][2] # Update waktu selesai
            
    return hasil_terpilih

# --- Program Utama (Versi Input Pengguna) ---

# Buat list kosong untuk menampung data dari pengguna
data_aktivitas = []

print("--- Program Pemilihan Aktivitas Greedy ---")

# 1. Tanya pengguna berapa banyak aktivitas yang ingin dimasukkan
while True:
    try:
        jumlah_aktivitas = int(input("Masukkan jumlah total aktivitas: "))
        if jumlah_aktivitas > 0:
            break
        else:
            print("Jumlah harus lebih dari 0.")
    except ValueError:
        print("Input tidak valid. Masukkan angka.")

print("\n--- Masukkan Detail Aktivitas ---")

# 2. Loop sebanyak jumlah aktivitas untuk meminta detail
for i in range(jumlah_aktivitas):
    print(f"--- Aktivitas ke-{i + 1} ---")
    
    # Minta Nama Aktivitas
    nama = input(f"Nama Aktivitas {i + 1} (cth: A1): ")
    
    # Minta Waktu Mulai (dengan validasi angka)
    while True:
        try:
            start_time = int(input(f"Waktu Mulai (angka): "))
            break
        except ValueError:
            print("Input tidak valid. Masukkan angka.")
            
    # Minta Waktu Selesai (dengan validasi angka)
    while True:
        try:
            finish_time = int(input(f"Waktu Selesai (angka): "))
            if finish_time >= start_time:
                break
            else:
                print("Error: Waktu selesai tidak boleh lebih awal dari waktu mulai.")
        except ValueError:
            print("Input tidak valid. Masukkan angka.")
            
    # Tambahkan data aktivitas dari pengguna ke list utama
    data_aktivitas.append([nama, start_time, finish_time])

print(f"\nData aktivitas yang Anda masukkan (belum di-sortir): {data_aktivitas}\n")

# 3. Jalankan algoritma greedy pada data yang baru saja dimasukkan
aktivitas_terpilih = pilih_aktivitas_greedy(data_aktivitas)

# 4. Cetak hasilnya
print("--- Hasil Algoritma Greedy ---")
print(f"Total aktivitas yang bisa dipilih: {len(aktivitas_terpilih)}")
print("Daftar aktivitas terpilih (tidak bentrok):")
for aktivitas in aktivitas_terpilih:
    print(f"- {aktivitas[0]} (Jadwal: {aktivitas[1]} s/d {aktivitas[2]})")