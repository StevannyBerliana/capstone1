from datetime import datetime
import random
import string
from tabulate import tabulate
import regex as re

# Koleksi data penjualan dan pemasaran
data = [
    {
        "id_transaksi": "TRX324",
        "tanggal_transaksi": "01-02-2024",
        "nama_barang": "Laptop",
        "jumlah_penjualan": 10,
        "harga": 7000000,
        "total_penjualan": 7000000 * 10,
        "metode_pemasaran": "Ads Sosial Media",
        "biaya_pemasaran": 500000
    },
    {
        "id_transaksi": "TRX198",
        "tanggal_transaksi": "02-02-2024",
        "nama_barang": "Smartphone",
        "jumlah_penjualan": 15,
        "harga": 5000000,
        "total_penjualan": 5000000 * 15,
        "metode_pemasaran": "Email Marketing",
        "biaya_pemasaran": 300000
    },
    {
        "id_transaksi": "TRX567",
        "tanggal_transaksi": "03-02-2024",
        "nama_barang": "Headset",
        "jumlah_penjualan": 25,
        "harga": 150000,
        "total_penjualan": 150000 * 25,
        "metode_pemasaran": "Seo",
        "biaya_pemasaran": 100000
    },
    {
        "id_transaksi": "TRX892",
        "tanggal_transaksi": "04-02-2024",
        "nama_barang": "Tablet",
        "jumlah_penjualan": 30,
        "harga": 3500000,
        "total_penjualan": 3500000 * 30,
        "metode_pemasaran": "Ads Sosial Media",
        "biaya_pemasaran": 200000
    },
    {
        "id_transaksi": "TRX610",
        "tanggal_transaksi": "05-02-2024",
        "nama_barang": "Smartwatch",
        "jumlah_penjualan": 20,
        "harga": 2000000,
        "total_penjualan": 2000000 * 20,
        "metode_pemasaran": "Email Marketing",
        "biaya_pemasaran": 150000
    },
    {
        "id_transaksi": "TRX943",
        "tanggal_transaksi": "06-02-2024",
        "nama_barang": "Laptop",
        "jumlah_penjualan": 50,
        "harga": 300000,
        "total_penjualan": 300000 * 50,
        "metode_pemasaran": "Seo",
        "biaya_pemasaran": 50000
    },
    {
        "id_transaksi": "TRX759",
        "tanggal_transaksi": "07-02-2024",
        "nama_barang": "Smartphone",
        "jumlah_penjualan": 40,
        "harga": 150000,
        "total_penjualan": 150000 * 40,
        "metode_pemasaran": "Ads Sosial Media",
        "biaya_pemasaran": 75000
    },
    {
        "id_transaksi": "TRX312",
        "tanggal_transaksi": "08-02-2024",
        "nama_barang": "Smartwatch",
        "jumlah_penjualan": 12,
        "harga": 5000000,
        "total_penjualan": 5000000 * 12,
        "metode_pemasaran": "Email Marketing",
        "biaya_pemasaran": 300000
    },
    {
        "id_transaksi": "TRX285",
        "tanggal_transaksi": "09-02-2024",
        "nama_barang": "Headset",
        "jumlah_penjualan": 18,
        "harga": 1200000,
        "total_penjualan": 1200000 * 18,
        "metode_pemasaran": "Seo",
        "biaya_pemasaran": 100000
    },
    {
        "id_transaksi": "TRX534",
        "tanggal_transaksi": "10-02-2024",
        "nama_barang": "Laptop",
        "jumlah_penjualan": 8,
        "harga": 2500000,
        "total_penjualan": 2500000 * 8,
        "metode_pemasaran": "Ads Sosial Media",
        "biaya_pemasaran": 150000
    }
]


# Fungsi read data
def baca_data():
    print("\n=== Data Penjualan dan Pemasaran ===")
    print(tabulate(data, headers="keys", tablefmt="fancy_grid"))


# definisikan function utk validasi angka
def validasi_tanggal(custom):
    while True:
        tanggal = input("Masukkan tanggal transaksi (DD-MM-YYYY): ").strip()
        try:
            datetime.strptime(tanggal, "%d-%m-%Y")
            return tanggal  # Jika valid, kembalikan nilai tanggal
        except ValueError:
            print("Format tanggal salah! Gunakan format DD-MM-YYYY.")

def validasi_angka(custom):
    while True:
        angka = input(custom)
        if angka.isdigit():
            angka = int(angka)
            return angka
        else:
            print("Harus berupa angka. Silakan coba lagi.")

def validasi_barang(custom):
    while True:
        nama_barang = input(custom)
        if nama_barang.lower() in ["laptop", "smartphone", "smartwatch", "headset", "tablet"]:
            break
        else:
            print("Nama barang tidak valid. Silakan coba lagi.")
    return nama_barang

def validasi_metode(custom):
    while True:
        metode_pemasaran = input(custom)
        if metode_pemasaran.lower() in ["ads sosial media", "email marketing", "seo"]:
            break
        else:
            print("Metode pemasaran tidak valid. Silakan coba lagi.")
    return metode_pemasaran

# Fungsi untuk menghasilkan ID transaksi acak
def generate_random_id():
    # return "TRX" + ''.join(random.choices(string.digits, k=3))
    id_baru = f'TRX{random.randint(100, 999)}'
    if any(transaksi['id_transaksi'] == id_baru for transaksi in data):
        return generate_random_id()
    return id_baru
    

# Fungsi untuk menambahkan data penjualan
def tambah_data():
    print("\n=== Menambahkan Data Penjualan dan Pemasaran===")
    
    tanggal_transaksi = validasi_tanggal("Masukkan Tanggal Transaksi (YYYY-MM-DD):")
    nama_barang = validasi_barang("Masukkan Nama Barang (laptop, smartphone, smartwatch, headset, tablet): ")
    jumlah_penjualan = validasi_angka("Masukkan Jumlah Penjualan: ")
    harga = validasi_angka("Masukkan Harga: ")
    metode_pemasaran = validasi_metode("Masukkan Metode Pemasaran (ads sosial media, email marketing, seo): ")
    biaya_pemasaran = validasi_angka("Masukkan Biaya Pemasaran: ")
    
    # generate id_transaksi acak
    id_transaksi = generate_random_id() 
    
    # Total penjualan = jumlah * harga
    total_penjualan = jumlah_penjualan * harga
    
    transaksi = {
        "id_transaksi": id_transaksi,
        "tanggal_transaksi": tanggal_transaksi,
        "nama_barang": nama_barang.capitalize(),
        "jumlah_penjualan": jumlah_penjualan,
        "harga": harga,
        "total_penjualan": total_penjualan,
        "metode_pemasaran": metode_pemasaran.title(),
        "biaya_pemasaran": biaya_pemasaran,
    }
    
    data.append(transaksi)
    print("\nData Penjualan Berhasil Ditambahkan!\n")
    baca_data()


# Fungsi untuk mengupdate data penjualan
def update_data():
    while True:
        baca_data()  # Menampilkan data transaksi
        kode = input("\nMasukkan ID Transaksi yang ingin diubah: ").strip().upper()
        item = next((transaksi for transaksi in data if transaksi["id_transaksi"] == kode), None)

        if item:
            while True:
                print("\n1. Nama Barang")
                print("2. Jumlah Penjualan")
                print("3. Harga")
                print("4. Metode Pemasaran")
                print("5. Biaya Pemasaran")
                print("6. Kembali")
                pilihan = validasi_angka("\nMasukkan nomor pilihan: ")

                if pilihan == 1:
                    item["nama_barang"] = validasi_barang("\nMasukkan Nama Barang Baru: ").capitalize()
                elif pilihan == 2:
                    item["jumlah_penjualan"] = validasi_angka("\nMasukkan Jumlah Penjualan Baru: ")
                    item["total_penjualan"] = item["jumlah_penjualan"] * item["harga"]
                    print(f"Total Penjualan setelah perubahan: {item['total_penjualan']}")  
                elif pilihan == 3:
                    item["harga"] = validasi_angka("\nMasukkan Harga Baru: ")
                    item["total_penjualan"] = item["jumlah_penjualan"] * item["harga"]
                    print(f"Total Penjualan setelah perubahan: {item['total_penjualan']}") 
                elif pilihan == 4:
                    item["metode_pemasaran"] = validasi_metode("\nMasukkan Metode Pemasaran Baru: ").title()
                elif pilihan == 5:
                    item["biaya_pemasaran"] = validasi_angka("\nMasukkan Biaya Pemasaran Baru: ")
                elif pilihan == 6:
                    break  # Kembali ke menu sebelumnya
                else:
                    print("\nPilihan tidak valid! Silakan coba lagi.")
                    continue

                print("\nData berhasil diperbarui!")
                baca_data()  # Menampilkan data yang sudah diperbarui

                while True:
                    lanjut = input("\nApakah ingin memperbarui data lain? (y/n): ").lower()
                    if lanjut in ('y', 'n'):
                        break
                    print("Masukkan hanya 'y' untuk lanjut atau 'n' untuk kembali.")
                if lanjut != 'y':
                    return
        else:
            print("\nID Transaksi tidak ditemukan! Silakan coba lagi.")

recycle_bin = []

# Fungsi menghapus data (dengan pemindahan ke Recycle Bin)

def hapus_data():
    while True:
        baca_data()
        kode = input("\nMasukkan ID Transaksi yang ingin dihapus: ").strip().upper()
        item = next((transaksi for transaksi in data if transaksi["id_transaksi"] == kode), None)

        if item:
            recycle_bin.append(item)  # Simpan ke Recycle Bin
            data.remove(item)  # Hapus dari data utama
            print("\nData Penjualan Berhasil Dihapus ke Recycle Bin!\n")
            baca_data()
            break
        else:
            print("\nID Transaksi tidak ditemukan! Silakan coba lagi.")

# Fungsi untuk menampilkan dan merestore data dari Recycle Bin

def restore_data():
    if not recycle_bin:
        print("\nRecycle Bin kosong! Tidak ada data yang bisa dipulihkan.\n")
        return

    print("\n=== Data di Recycle Bin ===")
    print(tabulate(recycle_bin, headers="keys", tablefmt="fancy_grid"))

    kode = input("\nMasukkan ID Transaksi yang ingin dipulihkan: ").strip().upper()
    item = next((transaksi for transaksi in recycle_bin if transaksi["id_transaksi"] == kode), None)

    if item:
        data.append(item)  # Kembalikan ke data utama
        recycle_bin.remove(item)  # Hapus dari Recycle Bin
        print("\nData Berhasil Dipulihkan!\n")
        baca_data()
    else:
        print("\nID tidak ditemukan di Recycle Bin!")

def filter_nama_barang_dan_metode():
    daftar_barang = ["laptop", "smartphone", "smartwatch", "headset", "tablet"]
    daftar_metode = ["ads sosial media", "email marketing", "seo"]

    while True:
        print("\n=== Filter Berdasarkan Nama Barang dan Metode Pemasaran ===")
        # Memilih apakah ingin memfilter berdasarkan nama barang atau metode pemasaran
        filter_pilih = input("Pilih filter: \n1. Nama Barang\n2. Metode Pemasaran\nMasukkan pilihan (1/2): ").strip()

        # Validasi input filter_pilih
        if filter_pilih not in ['1', '2']:
            print("Pilihan tidak valid. Silakan masukkan 1 untuk Nama Barang atau 2 untuk Metode Pemasaran.")
            continue
        
        # Filter berdasarkan Nama Barang
        if filter_pilih == '1':
            while True:
                nama_barang = input("Masukkan nama barang yang ingin dicari (laptop, smartphone, smartwatch, headset, tablet): ").lower()
                if nama_barang in daftar_barang:
                    filtered_data = [transaksi for transaksi in data if transaksi['nama_barang'].lower() == nama_barang]
                    break
                else:
                    print("Nama barang tidak valid. Silakan pilih salah satu dari: laptop, smartphone, smartwatch, headset, tablet.")

        # Filter berdasarkan Metode Pemasaran
        elif filter_pilih == '2':
            while True:
                metode_pemasaran = input("Masukkan metode pemasaran yang ingin dicari (ads sosial media, email marketing, seo): ").lower()
                # Gunakan .lower() agar perbandingan lebih fleksibel
                if metode_pemasaran in daftar_metode:
                    filtered_data = [transaksi for transaksi in data if transaksi['metode_pemasaran'].lower() == metode_pemasaran]
                    break
                else:
                    print("Metode pemasaran tidak valid. Silakan pilih salah satu dari: ads sosial media, email marketing, seo.")

        # Menampilkan hasil pencarian
        if filtered_data:
            print(tabulate(filtered_data, headers="keys", tablefmt="fancy_grid"))
        else:
            print("Tidak ada data yang ditemukan sesuai dengan filter yang dipilih.")

        # Menanyakan apakah ingin memfilter lagi
        lanjut = input("\nApakah ingin memfilter lagi? (y/n): ").lower()
        if lanjut != 'y':
            print("Terima kasih telah menggunakan fitur filter!")
            break

from tabulate import tabulate

def laporan_penjualan():
    print("\n=== Laporan Penjualan ===")
    
    # Penjualan Tertinggi dan Terendah
    transaksi_tertinggi = max(data, key=lambda x: x['total_penjualan'])
    transaksi_terendah = min(data, key=lambda x: x['total_penjualan'])
    
    laporan_transaksi = [
        ["Penjualan Tertinggi", transaksi_tertinggi['id_transaksi'], transaksi_tertinggi['nama_barang'], transaksi_tertinggi['total_penjualan']],
        ["Penjualan Terendah", transaksi_terendah['id_transaksi'], transaksi_terendah['nama_barang'], transaksi_terendah['total_penjualan']]
    ]
    
    print(tabulate(laporan_transaksi, headers=["Kategori", "ID Transaksi", "Nama Barang", "Total Penjualan"], tablefmt="grid"))
    
    # Barang dengan Total Penjualan Tertinggi & Terendah
    barang_terjual = {}
    for transaksi in data:
        nama_barang = transaksi['nama_barang']
        if nama_barang in barang_terjual:
            barang_terjual[nama_barang] += transaksi['jumlah_penjualan']
        else:
            barang_terjual[nama_barang] = transaksi['jumlah_penjualan']
    
    barang_tertinggi = max(barang_terjual, key=barang_terjual.get)
    barang_terendah = min(barang_terjual, key=barang_terjual.get)
    
    laporan_barang = [
        ["Barang Terlaris", barang_tertinggi, barang_terjual[barang_tertinggi]],
        ["Barang Paling Sedikit Terjual", barang_terendah, barang_terjual[barang_terendah]]
    ]
    
    print(tabulate(laporan_barang, headers=["Kategori", "Nama Barang", "Jumlah Terjual"], tablefmt="grid"))
    
    # Metode Pemasaran Paling Berpengaruh
    pemasaran_efektif = {}
    for transaksi in data:
        metode = transaksi['metode_pemasaran']
        if metode in pemasaran_efektif:
            pemasaran_efektif[metode] += transaksi['total_penjualan']
        else:
            pemasaran_efektif[metode] = transaksi['total_penjualan']
    
    metode_terbaik = max(pemasaran_efektif, key=pemasaran_efektif.get)
    laporan_pemasaran = [[metode, total] for metode, total in pemasaran_efektif.items()]
    
    print(tabulate(laporan_pemasaran, headers=["Metode Pemasaran", "Total Penjualan"], tablefmt="grid"))
    print(f"\nMetode Pemasaran Paling Efektif: {metode_terbaik}")
  

def menu_utama():
    while True:
        print("\n=== Menu Utama ===")
        print("1. Tampilkan Data")
        print("2. Tambah Data")
        print("3. Update Data")
        print("4. Hapus Data")
        print("5. Pulihkan Data")
        print("6. Cari Data Berdasarkan Nama Barang dan Metode Pemasaran")
        print("7. Tampilkan Laporan Penjualan")
        print("8. Keluar")

        pilihan = input("Masukkan Pilihan (1/2/3/4/5/6/7): ")

        if pilihan == "1":
            baca_data()
        elif pilihan == "2":
            tambah_data()
        elif pilihan == "3":
            update_data()
        elif pilihan == "4":
            hapus_data()
        elif pilihan == "5":
            restore_data()
        elif pilihan == "6":
            filter_nama_barang_dan_metode()
        elif pilihan == "7":
            laporan_penjualan()
        elif pilihan == "8":
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

menu_utama()