import random  # Mengambil library random untuk membuat angka acak. Di program ini dipakai untuk kode login 1000-9999.
import time    # Mengambil library time untuk mengatur waktu. Dipakai pada time.sleep(1) agar program berhenti sementara 1 detik.
import os      # Mengambil library os untuk menjalankan perintah sistem operasi. Dipakai untuk membersihkan layar terminal dengan "cls".


# ========================== DATA AWAL ==========================

akun = {  # Variabel "akun" bertipe dictionary. Isinya menyimpan username, password, dan role setiap akun.
    "admin": {"password": "123", "role": "admin"}, # Username admin, password 123, memiliki role Admin.
    "yc": {"password": "123", "role": "admin"},    # Username yc juga memiliki hak akses sebagai Admin.
    "user": {"password": "123", "role": "user"},   # Username user memiliki role User biasa.
    "yp": {"password": "123", "role": "user"}      # Username yp juga memiliki role User biasa.
}
# Dictionary menggunakan konsep key dan value.
# Contoh key "admin" memiliki value berupa dictionary lagi: password dan role.
# Pada minpro saya ini dictionary "akun" sudah dibuat, tetapi belum dipakai langsung pada fungsi login().
# Proses login masih menggunakan pengecekan manual melalui if username == "admin" atau "yc".

data = []  # List kosong yang akan digunakan untuk menyimpan seluruh transaksi pemesanan selama program berjalan.
# Setiap satu transaksi akan dimasukkan sebagai sebuah list ke dalam "data".

mobil = ["Avanza Grand", "Innova Reborn", "Toyota Rush", "Fortuner"]  # List berisi mobil yang masih tersedia.
# List menggunakan index mulai dari 0:
# mobil[0] = Avanza Grand
# mobil[1] = Innova Reborn
# mobil[2] = Toyota Rush
# mobil[3] = Fortuner
# Mobil yang sudah dipilih akan dihapus dari list, lalu dikembalikan lagi jika tiket dibatalkan.

book = 101  # Variabel integer untuk nomor booking awal. Tiket pertama akan memiliki kode YURCELL-101.
# Setelah pemesanan berhasil, book ditambah 1 sehingga tiket berikutnya menjadi YURCELL-102, YURCELL-103, dst.


# ========================== FUNGSI LOGIN ==========================

def login():  # Membuat fungsi bernama login() untuk menangani proses autentikasi dan menentukan role pengguna.
    while True:  # Perulangan tanpa batas, Akan terus meminta login sampai username dan password benar.
        print("\n=== LOGIN SISTEM TRAVEL ===")  # Menampilkan judul login. \n berarti membuat baris baru terlebih dahulu.

        username = input("Username: ")  # Meminta username dari keyboard dan menyimpannya ke variabel string "username".
        password = input("Password: ")  # Meminta password dari keyboard dan menyimpannya ke variabel string "password".

        if username == "admin" or username == "yc":  # Mengecek apakah username merupakan salah satu akun Admin.
            # "or" berarti cukup salah satu kondisi yang benar.

            if password == "123":  # Setelah username Admin cocok, password dicek apakah sama "123".
                print("Login berhasil sebagai Admin")  # Memberi informasi bahwa login sebagai Admin berhasil.
                return "admin"  # Menghentikan fungsi login() sekaligus mengirim nilai "admin" ke pemanggil fungsi.

        elif username == "user" or username == "yp":  # Jika bukan Admin, cek apakah username termasuk User.
            # kondisi berikutnya jika kondisi if sebelumnya salah.

            if password == "123":  # Mengecek password User.
                print("Login berhasil sebagai User")  # Menampilkan bahwa login berhasil sebagai User.
                return "user"  # Menghentikan fungsi login() dan mengembalikan nilai "user".

        print("Username atau password salah!")  # Muncul jika tidak ada return, berarti login salah.
        # Karena masih berada dalam while True, setelah pesan ini program otomatis kembali meminta username dan password.


# ========================== FUNGSI LIHAT DATA ==========================

def lihat_data():  # Fungsi untuk menampilkan daftar transaksi yang tersimpan di dalam list "data".
    print("\n--- DAFTAR PEMESANAN TIKET ---")  # Menampilkan judul daftar transaksi.

    if data == []:  # Mengecek apakah list data masih kosong. [] berarti list kosong.
        print("Belum ada data transaksi pesanan.")  # Ditampilkan jika belum pernah ada pemesanan.

    else:  # Dijalankan jika list data sudah memiliki isi.
        nomor = 1  # Variabel integer untuk nomor urut tampilan transaksi, dimulai dari 1.

        for item in data:  # Perulangan untuk mengambil setiap transaksi dari list data satu per satu.
            # "item" merupakan variabel sementara yang berisi satu transaksi pada setiap putaran.

            print(
                nomor,                    # Menampilkan nomor urut transaksi.
                "| YURCELL-", item[0],    # item[0] = nomor booking.
                "|", item[1],             # item[1] = nama pemesan.
                "|", item[2],             # item[2] = nomor HP.
                "|", item[3],             # item[3] = rute perjalanan.
                "|", item[7],             # item[7] = jenis mobil.
                "| Rp", item[8]           # item[8] = total harga.
            )

            nomor = nomor + 1  # Nomor urut ditambah 1 setelah satu transaksi selesai ditampilkan.
            # Misalnya transaksi pertama nomor 1, berikutnya menjadi 2, lalu 3, dan seterusnya.


# ========================== PROGRAM UTAMA ==========================

os.system("cls")  # Membersihkan layar terminal pada Windows agar tampilan program lebih rapi saat pertama dijalankan.

role = login()  # Memanggil fungsi login() lalu menyimpan nilai return-nya ke variabel "role".
# Jika login Admin berhasil: role = "admin".
# Jika login User berhasil: role = "user".
# Variabel role nantinya menentukan menu mana yang boleh diakses.

time.sleep(1)  # Memberikan jeda selama 1 detik setelah login sebelum program dilanjutkan.

print("Kode Login:", random.randint(1000, 9999))  # Membuat angka acak 4 digit dari 1000 sampai 9999.
# randint(a, b) menghasilkan angka bulat acak antara a sampai b.
# Kode ini hanya ditampilkan dan belum digunakan untuk proses verifikasi/OTP.


# ========================== MENU UTAMA ==========================

while True:  # Perulangan utama program. Akan terus berjalan sampai pengguna memilih menu 5 dan terkena break.
    print("\nSISTEM PEMESANAN TIKET TRAVEL MUHAMMAD YURCELL NABIL")  # Menampilkan nama sistem.

    if role == "admin":  # Jika hasil login menunjukkan role Admin, tampilkan semua menu.
        print("Role : Admin")          # Menampilkan role pengguna.
        print("1. Pemesanan Tiket")   # Admin dapat membuat pemesanan baru.
        print("2. Lihat Data")        # Admin dapat melihat seluruh transaksi.
        print("3. Ubah Data")         # Admin dapat mengubah data pelanggan tertentu.
        print("4. Batal Tiket")       # Admin dapat membatalkan tiket.
        print("5. Keluar")            # Admin dapat keluar dari sistem.

    else:  # Jika role bukan admin, berarti pengguna adalah User.
        print("Role : User")          # Menampilkan role User.
        print("1. Pemesanan Tiket")   # User dapat membuat pemesanan.
        print("2. Lihat Data")        # User dapat melihat data transaksi.
        print("5. Keluar")            # User dapat keluar.
        # Menu 3 dan 4 tidak ditampilkan kepada User karena hanya Admin yang memiliki hak akses tersebut.

    menu = input("Pilih menu: ")  # Menyimpan pilihan menu dari pengguna ke variabel string "menu".


    # ==================== VALIDASI MENU ADMIN ====================

    if role == "admin":  # Jika pengguna Admin, pilihan valid adalah 1, 2, 3, 4, atau 5.
        while menu != "1" and menu != "2" and menu != "3" and menu != "4" and menu != "5":
            # while berjalan jika semua perbandingan di atas benar.
            # Artinya selama menu bukan 1, bukan 2, bukan 3, bukan 4, dan bukan 5, input dianggap salah.

            print("Pilihan tidak valid!")  # Memberi tahu bahwa input tidak sesuai.
            menu = input("Pilih menu: ")  # Meminta Admin memilih ulang sampai memasukkan angka yang benar.


    # ==================== VALIDASI MENU USER ====================

    else:  # Jika pengguna adalah User, hanya menu 1, 2, dan 5 yang diperbolehkan.
        while menu != "1" and menu != "2" and menu != "5":
            # Misalnya User mengetik 3 atau 4, kondisi tetap benar dan input akan ditolak.

            print("User hanya dapat memilih menu 1, 2, atau 5!")  # Menjelaskan hak akses User.
            menu = input("Pilih menu: ")  # Meminta User menginput ulang.


    # MENU 1 - PEMESANAN TIKET
    

    if menu == "1":  # Jika menu yang dipilih adalah 1, program masuk ke form pemesanan tiket.
        print("\n--- FORM PEMESANAN TIKET ---")  # Menampilkan judul form.


        #  INPUT NAMA 

        nama = input("Nama Pemesan: ")  # Meminta nama pelanggan dan menyimpannya ke variabel string "nama".

        while nama == "":  # Mengecek apakah nama kosong. "" berarti tidak ada karakter yang dimasukkan.
            nama = input("Nama wajib diisi: ")  # Jika kosong, nama diminta terus sampai diisi.


        #  INPUT NOMOR HP 

        hp = input("Nomor HP/WA: ")  # Menyimpan nomor HP sebagai string.
        # Nomor HP cocok menggunakan string karena tidak digunakan dalam perhitungan matematika.
        # Dengan string, angka 0 di depan nomor HP juga tidak akan hilang.

        while hp == "":  # Mengecek apakah nomor HP kosong.
            hp = input("No HP wajib diisi: ")  # Meminta input ulang jika kosong.


        #  MENAMPILKAN RUTE 

        print("\nDAFTAR RUTE")                         # Menampilkan judul daftar rute.
        print("1. Balikpapan-Samarinda (100k)")       # Rute 1 dengan harga Rp100.000/orang.
        print("2. Samarinda-Tenggarong (60k)")        # Rute 2 dengan harga Rp60.000/orang.
        print("3. Balikpapan-IKN (120k)")             # Rute 3 dengan harga Rp120.000/orang.

        pilih_rute = input("Pilih Rute (1-3): ")  # Menyimpan pilihan rute sebagai string.

        while pilih_rute != "1" and pilih_rute != "2" and pilih_rute != "3":
            # Selama pilihan bukan 1, 2, atau 3, program meminta input ulang.

            pilih_rute = input("Ulangi (1-3): ")


        #  MENENTUKAN RUTE DAN HARGA 

        if pilih_rute == "1":  # Jika pengguna memilih rute nomor 1.
            rute, harga = "Balikpapan-Samarinda", 100000
            # Python dapat mengisi dua variabel sekaligus.

        elif pilih_rute == "2":  # Jika pengguna memilih rute nomor 2.
            rute, harga = "Samarinda-Tenggarong", 60000

        else:  # pengguna memilih no 3.
            rute, harga = "Balikpapan-IKN", 120000

        # Variabel "rute" bertipe string untuk nama perjalanan.
        # Variabel "harga" bertipe integer agar bisa dipakai dalam perhitungan biaya.


        #  INPUT JADWAL 

        jadwal = input("Jadwal Berangkat: ")  # Menyimpan jadwal keberangkatan.
        # Jadwal masih berupa input bebas, misalnya "08.00", "Senin 08.00", atau "10 Oktober 2026".

        while jadwal == "":  # Jadwal tidak boleh kosong.
            jadwal = input("Jadwal wajib diisi: ")  # Meminta jadwal kembali jika tidak diisi.


        #  JUMLAH PENUMPANG 

        penumpang = input("Jumlah Penumpang (1-5): ")  # Menyimpan jumlah penumpang dalam bentuk string.

        while penumpang != "1" and penumpang != "2" and penumpang != "3" and penumpang != "4" and penumpang != "5":
            # Validasi agar jumlah penumpang hanya boleh 1 sampai 5.

            penumpang = input("Ulangi (1-5): ") #meminta memilih 1-5


        #  TITIK JEMPUT 

        jemput = input("Lokasi Titik Jemput: ")  # Menyimpan lokasi penjemputan pelanggan.

        while jemput == "":  # Mengecek apakah titik jemput kosong.
            jemput = input("Titik jemput wajib diisi: ")  # Minta ulang jika kosong.


        #  CEK KETERSEDIAAN MOBIL 

        if mobil == []:  # Mengecek apakah list "mobil" sudah tidak memiliki isi.
            print("Maaf, mobil terpakai semua!")  # Pesan jika semua mobil sedang digunakan.
            continue  # Menghentikan proses pemesanan pada putaran ini dan kembali ke awal menu utama

        #  MENAMPILKAN MOBIL 

        print("\nMOBIL TERSEDIA")  # Menampilkan judul daftar mobil.

        nomor = 1  # Nomor urut tampilan mobil dimulai dari 1.

        for item in mobil:  # Mengambil nama mobil yang masih tersedia satu per satu.
            print(nomor, ".", item)  
            nomor = nomor + 1  # Menambah nomor urut mobil.


        #  MEMILIH MOBIL 

        pilih_mobil = input("Pilih Mobil: ")  # Menyimpan nomor mobil yang dipilih.

        if pilih_mobil == "1":  # Jika memilih nomor 1.
            jenis = mobil[0]  # Mengambil elemen pertama dari list mobil.

        elif pilih_mobil == "2" and mobil[1:2] != []:
            # Digunakan untuk mengecek apakah elemen pada index 1 masih tersedia.
            jenis = mobil[1]

        elif pilih_mobil == "3" and mobil[2:3] != []:
            # Mengecek keberadaan index 2 sebelum mengakses mobil[2].
            jenis = mobil[2]

        elif pilih_mobil == "4" and mobil[3:4] != []:
            # Mengecek keberadaan index 3 sebelum mengakses mobil[3].
            jenis = mobil[3]

        else:  # Dijalanakan jika pilihan mobil tidak sesuai dengan mobil yang tersedia.
            print("Pilihan mobil tidak tersedia!")
            continue  # Membatalkan proses pemesanan saat itu dan kembali ke menu utama.

        mobil.remove(jenis)  # Menghapus mobil yang dipilih dari list mobil tersedia.
        # Contoh jenis = "Avanza Grand".
        # Setelah mobil.remove(jenis), Avanza tidak muncul lagi pada daftar mobil.
        # Ini menyatakan bahwa mobil sedang digunakan oleh pelanggan.


        #  MENGHITUNG TOTAL 

        if penumpang == "1":  # Jika jumlah penumpang 1.
            total = harga  # Total cukup sama dengan harga satu tiket.

        elif penumpang == "2":  # Jika jumlah penumpang 2.
            total = harga * 2  # Harga tiket dikalikan 2.

        elif penumpang == "3":  # Jika jumlah penumpang 3.
            total = harga * 3 # Harga tiket dikalikan 3.

        elif penumpang == "4":  # Jika jumlah penumpang 4.
            total = harga * 4  #Harga tiket dikalikan 4.

        else:  # Karena jumlah sebelumnya sudah divalidasi, else berarti penumpang = 5.
            total = harga * 5 #Harga tiket dikalikan 5.

        # Variabel "total" bertipe integer.
        # Secara konsep rumusnya adalah: total harga = harga per orang × jumlah penumpang.

        print("\nTotal Biaya: Rp", total)  # Menampilkan jumlah yang harus dibayar pelanggan.


        #  METODE PEMBAYARAN 

        print("1. Transfer Bank")  # Pilihan pembayaran nomor 1.
        print("2. E-Wallet")       # Pilihan pembayaran nomor 2.
        print("3. QRIS")           # Pilihan pembayaran nomor 3.

        pilih_bayar = input("Pilih Pembayaran (1-3): ")  # Menyimpan nomor pilihan pembayaran.

        while pilih_bayar != "1" and pilih_bayar != "2" and pilih_bayar != "3":
            # Selama pilihan bukan 1, 2, atau 3, pengguna diminta mengulang.

            pilih_bayar = input("Ulangi (1-3): ")

        if pilih_bayar == "1":  # Pembayaran pake Transfer bank
            bayar = "Transfer Bank"  # Menyimpan nama metode pembayaran.

        elif pilih_bayar == "2":  # Pembayaran pake E-wallet
            bayar = "E-Wallet"

        else:  # Pembayaran pake qris
            bayar = "QRIS"


        #  MENYIMPAN TRANSAKSI 

        data.append([
            book,       # item[0] = nomor booking, contoh 101.
            nama,       # item[1] = nama pemesan.
            hp,         # item[2] = nomor HP/WA.
            rute,       # item[3] = nama rute perjalanan.
            jadwal,     # item[4] = jadwal keberangkatan.
            jemput,     # item[5] = lokasi titik jemput.
            penumpang,  # item[6] = jumlah penumpang.
            jenis,      # item[7] = jenis mobil yang digunakan.
            total,      # item[8] = total biaya.
            bayar       # item[9] = metode pembayaran.
        ])
        # append() berarti menambahkan elemen baru ke bagian akhir sebuah list.
        # Di sini satu transaksi berupa satu list, lalu list tersebut dimasukkan ke dalam list besar "data".

        #  CETAK BUKTI TIKET 

        print("\n=== BUKTI TIKET TRAVEL ===")  # Menampilkan judul tiket.
        print("Kode    : YURCELL-", book)       # Menampilkan kode booking.
        print("Pemesan :", nama)                # Menampilkan nama pemesan.
        print("No HP   :", hp)                  # Menampilkan nomor HP.
        print("Rute    :", rute)                # Menampilkan rute perjalanan.
        print("Jadwal  :", jadwal)              # Menampilkan jadwal keberangkatan.
        print("Mobil   :", jenis)                # Menampilkan mobil yang digunakan.
        print("Jemput  :", jemput)               # Menampilkan titik jemput.
        print("Total   : Rp", total)             # Menampilkan total harga.
        print("Bayar   :", bayar)                # Menampilkan metode pembayaran.
        print("Status  : LUNAS")                 # Semua transaksi pada program ini langsung dianggap lunas.
        
        book = book + 1  # Menambah nomor booking untuk transaksi berikutnya.

    # MENU 2 - LIHAT DATA

    elif menu == "2":  # Jika menu yang dipilih adalah 2.
        lihat_data()  # Memanggil fungsi lihat_data() yang sebelumnya sudah dibuat.
        # Fungsi akan mengecek apakah transaksi kosong, Jika ada transaksi data ditampilkan satu per satu.


    # MENU 3 - UBAH DATA
    
    elif menu == "3":  # Menu ini hanya dapat dicapai oleh Admin karena User tidak diberi akses menu 3.
        print("\n--- UBAH DATA PEMESANAN ---")  # Menampilkan judul fitur ubah data.

        cari = input("Nama Pemesan: ")  # Meminta nama pelanggan yang datanya ingin diubah.
        ketemu = False  # Variabel Boolean. False berarti data belum ditemukan, Boolean memiliki dua nilai: True dan False.

        for item in data:  # Mengecek setiap transaksi di dalam data satu per satu.

            if cari == item[1]:  # Membandingkan nama yang dicari dengan item[1], yaitu nama pemesan.
                ketemu = True  # Jika sama, ubah nilai ketemu menjadi True sebagai tanda data ditemukan.

                print("1. Nama")   # Pilihan untuk mengubah nama.
                print("2. No HP")  # Pilihan untuk mengubah nomor HP.
                print("3. Titik Jemput")  # Pilihan untuk mengubah lokasi jemput.

                ubah = input("Pilih (1-3): ")  # Menyimpan jenis data yang ingin diubah.

                while ubah != "1" and ubah != "2" and ubah != "3":
                    # Validasi agar pilihan hanya boleh 1, 2, atau 3.

                    ubah = input("Ulangi (1-3): ") # Memilih jenis data yang ingin di ubah

                baru = input("Data Baru: ")  # Menyimpan nilai baru yang akan menggantikan nilai lama.

                if ubah == "1":  # Jika Admin memilih mengubah nama.
                    item[1] = baru  # item[1] yang sebelumnya nama lama diganti dengan nilai "baru".

                elif ubah == "2":  # Jika Admin memilih mengubah nomor HP.
                    item[2] = baru  # item[2] adalah nomor HP.

                else:  # Karena pilihan sudah divalidasi 1-3, else berarti pilihan 3.
                    item[5] = baru  # item[5] adalah titik jemput.

                print("Data berhasil diubah!")  # Pesan bahwa proses edit berhasil.

                break  # Menghentikan perulangan for karena transaksi sudah ditemukan dan diubah.
                # Tanpa break, program akan terus mengecek transaksi berikutnya meskipun data sudah berhasil diubah.

        if ketemu == False:  # Setelah seluruh transaksi diperiksa, jika ketemu masih False berarti nama tidak ada.
            print("Data tidak ditemukan!") # data ditemukan


    # MENU 4 - BATAL TIKET
    
    elif menu == "4":  # Menu pembatalan tiket, hanya dapat digunakan Admin.
        print("\n--- BATAL TIKET ---")  # Menampilkan judul pembatalan.

        cari = input("Nama Pemesan: ")  # Meminta nama pelanggan yang tiketnya ingin dibatalkan.
        ketemu = False  # Awalnya transaksi dianggap belum ditemukan.

        for item in data:  # Mencari nama tersebut pada semua transaksi satu per satu.

            if cari == item[1]:  # item[1] merupakan nama pemesan.
                mobil.append(item[7])
                # item[7] adalah jenis mobil.
                # append() menambahkan mobil tersebut kembali ke list "mobil".
                # Hal ini dilakukan karena setelah tiket dibatalkan, mobil dianggap tersedia kembali.

                data.remove(item)
                # remove() menghapus seluruh transaksi tersebut dari list "data" jadi transaksi pelanggan benar-benar dibatalkan.

                ketemu = True  # Mengubah penanda menjadi True karena transaksi ditemukan.

                print("Pesanan berhasil dibatalkan!")  # Menampilkan pesan berhasil.

                break  # Menghentikan pencarian karena transaksi yang dimaksud sudah ditemukan dan dihapus.

        if ketemu == False:  # Jika tidak pernah menemukan nama yang sama.
            print("Data tidak ditemukan!") # data ditemukan


    # MENU 5 - KELUAR
    
    elif menu == "5":  # Jika pengguna memilih nomor 5.
        print("\nTerima kasih telah menggunakan sistem pemesanan tiket!")  # Menampilkan pesan penutup.

        break  # Menghentikan while True pada menu utama, karena perulangan utama berhenti, program selesai dijalankan.