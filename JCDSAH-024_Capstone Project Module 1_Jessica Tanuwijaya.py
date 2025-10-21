from datetime import datetime
data_pasien = {
    0: {"Nama":"Robby Honor","Umur":31,"Gender":"Pria","Diagnosis":"Covid-19",
        "Tgl_Masuk":"2025-10-10","Dokter_Spesialis":"Tidak","Rawat_Inap":"Ya","Jenis_Kamar":"VIP",
        "Lab":"Ya","Operasi":"Tidak","Alamat":"Jl. Sidorukun No. 42, Medan","Pekerjaan":"Pegawai Swasta"},
    1: {"Nama":"Indah Kartika","Umur":29,"Gender":"Wanita","Diagnosis":"Eksim",
        "Tgl_Masuk":"2025-10-18","Dokter_Spesialis":"Ya","Rawat_Inap":"Tidak","Jenis_Kamar":"NA",
        "Lab":"Tidak","Operasi":"Tidak","Alamat":"Jl. Alumunium No. 99, Medan","Pekerjaan":"Guru"},
    2: {"Nama":"Zachary Juni","Umur":20,"Gender":"Pria","Diagnosis":"Pneumonia",
        "Tgl_Masuk":"2025-10-15","Dokter_Spesialis":"Ya","Rawat_Inap":"Ya","Jenis_Kamar":"Reguler",
        "Lab":"Ya","Operasi":"Ya","Alamat":"Jl. Cemara Asri No. 7A, Medan","Pekerjaan":"Mahasiswa"},
}

#1. Lihat Data Pasien
def tampilkan_pasien():
    print("\n=== Daftar Data Pasien Rumah Sakit XYZ ===")
    print(f"{'Index':<5} | {'Nama':<20} | {'Umur':<4} | {'Gender':<11} | {'Diagnosis':<12} | {'Tgl Masuk':<12} | {'Spesialis':<10} | {'R.Inap':<6} | {'Kamar':<8} | {'Lab':<6} | {'Operasi':<8} | {'Alamat':<35} | {'Pekerjaan':<15}")
    print("-" * 190)

    for i, pasien in data_pasien.items():
        print(f"{i:<5} | {pasien['Nama']:<20} | {pasien['Umur']:<4} | {pasien['Gender']:<11} | {pasien['Diagnosis']:<12} | {pasien['Tgl_Masuk']:<12} | {pasien['Dokter_Spesialis']:<10} | {pasien['Rawat_Inap']:<6} | {pasien['Jenis_Kamar']:<8} | {pasien['Lab']:<6} | {pasien['Operasi']:<8} | {pasien['Alamat']:<35} | {pasien['Pekerjaan']:<15}")
    print()
def lihat_data():
    tampilkan_pasien()

# 2. Tambah Data
def tambah_data():
    tampilkan_pasien()
    print("\n=== Tambah Data Pasien ===")
    index_baru = max(data_pasien.keys()) + 1

    nama = input("Nama Pasien: ").title()
    umur_input = input("Umur Pasien: ").strip()
    if not umur_input.isdigit():
        print("Input tidak valid! Harus angka.")
        return
    umur = int(umur_input)
    while True:
        gender = input("Gender (Pria/Wanita): ").strip().title()
        if gender in ["Pria", "Wanita"]:
            break
        else:
            print("Input tidak valid! Ketik 'Pria' atau 'Wanita'.")

    diagnosis = input("Diagnosis: ").title()
    tgl_masuk = input("Tanggal Masuk RS (YYYY-MM-DD): ")
    while True:
        dokter_spesialis = input("Dokter Spesialis? (Ya/Tidak): ").strip().title()
        if dokter_spesialis in ["Ya", "Tidak"]:
            break
        else:
            print("Input tidak valid! Ketik 'ya' atau 'tidak'.")

    
    while True:
        rawat_inap = input("Rawat Inap? (Ya/Tidak): ").strip().title()
        if rawat_inap in ["Ya", "Tidak"]:
            break
        else:
            print("Input tidak valid! Ketik 'ya' atau 'tidak'.")

    if rawat_inap == "Ya":
        while True:
            jenis_kamar = input("Jenis Kamar (Vip/Reguler): ").strip().title()
            if jenis_kamar in ["Vip", "Reguler"]:
                break
            else:
                print("Input tidak valid! Ketik 'VIP' atau 'Reguler'.")
    else:
        jenis_kamar = "NA"


    while True:
        lab = input("Periksa Lab? (Ya/Tidak): ").strip().title()
        if lab in ["Ya", "Tidak"]:
            break
        else:
            print("Input tidak valid! Ketik 'ya' atau 'tidak'.")


    while True:
        operasi = input("Operasi? (Ya/Tidak): ").strip().title()
        if operasi in ["Ya", "Tidak"]:
            break
        else:
            print("Input tidak valid! Ketik 'ya' atau 'tidak'.")

    alamat = input("Alamat Pasien: ").title()
    pekerjaan = input("Pekerjaan Pasien: ").title()

    data_pasien[index_baru] = {
        "Nama": nama, "Umur": umur, "Gender": gender,
        "Diagnosis": diagnosis, "Tgl_Masuk": tgl_masuk,
        "Dokter_Spesialis": dokter_spesialis, "Rawat_Inap": rawat_inap,
        "Jenis_Kamar": jenis_kamar, "Lab": lab, "Operasi": operasi,
        "Alamat": alamat, "Pekerjaan": pekerjaan
    }

    print("\nData pasien berhasil ditambahkan!\n")
    tampilkan_pasien()

# 3. Update Data
def update_data():
    print("\n=== Update Data Pasien ===")
    tampilkan_pasien()
    index_input = input("Masukkan index pasien yang ingin diubah: ").strip()

    if not index_input.isdigit():
        print("Input tidak valid! Harus angka.")
        return
    index = int(index_input)

    if index in data_pasien:
        pasien = data_pasien[index]
        print("\nData pasien saat ini:")
        for x, y in pasien.items():
            print(f"{x}: {y}")

        kolom = input("\nMasukkan nama kolom yang ingin diubah (contoh: Nama, Umur, Diagnosis, dll): ").strip().title()
        kolom = kolom.replace(" ", "_")
        if kolom not in pasien:
            print("Kolom tidak ditemukan! Pastikan ejaan sesuai.")
            return

        nilai_baru = input("Masukkan nilai baru: ").strip()
        pasien[kolom] = nilai_baru
        print("\nData pasien berhasil diupdate!")
    else:
        print("Index tidak ditemukan.")
    
    tampilkan_pasien()

# 4. Hapus Data
def hapus_data():
    print("\n=== Hapus Data Pasien ===")
    tampilkan_pasien()
    index = int(input("Masukkan index pasien yang ingin dihapus: "))

    if index in data_pasien:
        del data_pasien[index]
        print("Data pasien berhasil dihapus!")
    else:
        print("Index tidak ditemukan.")
    tampilkan_pasien()

# 5. Surat Sakit
def surat_sakit():
    print("\n=== Pengajuan Surat Sakit ===")
    tampilkan_pasien()

    index_input = input("Masukkan index pasien: ").strip()
    if not index_input.isdigit():
        print("Input tidak valid! Harus angka.")
        return

    index = int(index_input)
    if index not in data_pasien:
        print("Index tidak ditemukan.")
        return
    pasien = data_pasien[index]

    hari_input = input("Berapa hari izin sakit: ").strip()
    if not hari_input.isdigit():
        print("Input tidak valid! Harus angka.")
        return
    hari_izin = int(hari_input)

    print("\n=============================== Surat Keterangan Sakit RS XYZ ===============================\n")
    print("Dengan ini menerangkan bahwa berdasarkan hasil pemeriksaan yang telah dilakukan kepada pasien:")
    print(f"Nama      : {pasien['Nama']}")
    print(f"Umur      : {pasien['Umur']}")
    print(f"Alamat    : {pasien['Alamat']}")
    print(f"Pekerjaan : {pasien['Pekerjaan']}")
    print(f"Diagnosa  : {pasien['Diagnosis']}\n")
    print(f"Diberikan istirahat selama {hari_izin} hari terhitung mulai tanggal {pasien['Tgl_Masuk']}\n")
    print("Demikian surat keterangan ini diberikan untuk diketahui dan dipergunakan seperlunya.")

    print("==============================================================================================")

# 6. Invoice
def invoice():
    print("\n=== Invoice untuk Pasien ===")
    tampilkan_pasien()

    index_input = input("Masukkan index pasien: ").strip()
    if not index_input.isdigit():
        print("Index tidak ditemukan.")
        return
    index = int(index_input)
    if index not in data_pasien:
        print("Index tidak ditemukan.")
        return

    pasien = data_pasien[index]

    obat_input = input("Jumlah obat: ").strip()
    if not obat_input.isdigit():
        print("Input tidak valid! Harus angka.")
        return
    jumlah_obat = int(obat_input)

    if pasien["Dokter_Spesialis"].title() == "Ya":
        biaya_dokter_per_hari = 300000
        jenis_dokter = "Dokter Spesialis"
    else:
        biaya_dokter_per_hari = 150000
        jenis_dokter = "Dokter Umum"

    if pasien["Rawat_Inap"].title() == "Ya":
        tgl_masuk_str = pasien["Tgl_Masuk"].strip()
        if len(tgl_masuk_str) == 10:
            tgl_masuk = datetime.strptime(tgl_masuk_str, "%Y-%m-%d")
            tgl_hari_ini = datetime.today()
            lama_inap = (tgl_hari_ini - tgl_masuk).days
            if lama_inap < 1:
                lama_inap = 1
        else:
            lama_inap = 1
        biaya_dokter = biaya_dokter_per_hari * lama_inap
        if pasien["Jenis_Kamar"].lower() == "vip":
            biaya_kamar = 800000 * lama_inap
        else:
            biaya_kamar = 500000 * lama_inap
    else:
        biaya_dokter = biaya_dokter_per_hari
        biaya_kamar = 0
        lama_inap = 1

    biaya_obat = jumlah_obat * 30000
    biaya_lab = 300000 if pasien["Lab"].lower() == "ya" else 0
    biaya_operasi = 10000000 if pasien["Operasi"].lower() == "ya" else 0

    subtotal = biaya_dokter + biaya_kamar + biaya_obat + biaya_lab + biaya_operasi
    biaya_rs = int(subtotal * 0.10)
    total = subtotal + biaya_rs

    print("\n-------------- INVOICE RUMAH SAKIT XYZ ----------------")
    print(f"Nama          : {pasien['Nama']}")
    print(f"Umur          : {pasien['Umur']}")
    print(f"Gender        : {pasien['Gender']}")
    print(f"Diagnosis     : {pasien['Diagnosis']}")
    print(f"Jenis Kamar   : {pasien['Jenis_Kamar']}")
    print(f"Tanggal Masuk : {pasien['Tgl_Masuk']}")
    print(f"Tanggal Print : {datetime.today().strftime('%Y-%m-%d')}")
    print("-------------------------------------------------------")
    print(f"Biaya Dokter                 : Rp{biaya_dokter:,}")
    print(f"({jenis_dokter:<10} x {lama_inap} hari)")
    print(f"Biaya Rawat Inap             : Rp{biaya_kamar:,}")
    print(f"(Kamar ({pasien['Jenis_Kamar']}) x {lama_inap} hari)")
    print(f"Obat (Rp30,000 x {jumlah_obat})         : Rp{biaya_obat:,}")
    print(f"Pemeriksaan Lab              : Rp{biaya_lab:,}")
    print(f"Biaya Operasi                : Rp{biaya_operasi:,}")
    print("------------------------------------------------------")
    print(f"Subtotal                     : Rp{subtotal:,}")
    print(f"Biaya Operasional RS (10%)   : Rp{biaya_rs:,}")
    print(f"TOTAL PEMBAYARAN             : Rp{total:,}")
    print("------------------------------------------------------")
    print("Invoice berhasil dibuat!")


# Tampilan Menu
def main():
    while True:
        print("\n=== Sistem Data Pasien Rumah Sakit XYZ ===")
        print("1. Lihat Data Pasien")
        print("2. Tambah Data Pasien")
        print("3. Update Data Pasien")
        print("4. Hapus Data Pasien")
        print("5. Pengajuan Surat Sakit")
        print("6. Invoice untuk Pasien")
        print("0. Keluar")

        pilihan = input("Pilih menu (0-6): ")

        if pilihan == "1":
            lihat_data()
        elif pilihan == "2":
            tambah_data()
        elif pilihan == "3":
            update_data()
        elif pilihan == "4":
            hapus_data()
        elif pilihan == "5":
            surat_sakit()
        elif pilihan == "6":
            invoice()
        elif pilihan == "0":
            print("Bye! Terima kasih sudah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid, coba lagi!")

main()