<div align="center">

# 📚 REPOSITORY TUGAS PEMROGRAMAN
### Sistem Pemesanan Tiket Travel Muhammad Yurcell Nabil

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![RAPTOR](https://img.shields.io/badge/Flowchart-RAPTOR-00599C?style=for-the-badge)
![VS Code](https://img.shields.io/badge/IDE-VS%20Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

<p align="center">
  <b>Belajar • Coding • Flowchart • Dokumentasi</b>
</p>

</div>

---

## 👤 Identitas Mahasiswa

| Keterangan | Data |
| :--- | :--- |
| **👨‍🎓 Nama** | Muhammad Yurcell Nabil |
| **🆔 NIM** | 2609116073 |
| **🏫 Kelas** | B |
| **🎓 Program Studi** | Sistem Informasi |
| **🏛️ Universitas** | Universitas Mulawarman |
| **📚 Mata Kuliah** | Dasar-Dasar Pemrograman |
| **📅 Tahun** | 2026 |

---


### FLOWCHART

<img width="1131" height="882" alt="WhatsApp Image 2026-10-06 at 23 53 03" src="https://github.com/user-attachments/assets/579d9f1b-df40-496a-8a60-89eff24d1281" />




## 📌 1. Informasi Program

### 🏷️ Nama Program
**Sistem Pemesanan Tiket Travel Muhammad Yurcell Nabil**

### 📖 Deskripsi
Program ini merupakan aplikasi berbasis *Command Line Interface* (CLI) yang dibangun menggunakan bahasa pemrograman **Python**. Aplikasi ini dirancang untuk mengelola transaksi pemesanan tiket travel antarkota (Balikpapan, Samarinda, Tenggarong, IKN), alokasi armada mobil secara *real-time*, pencetakan bukti tiket, serta manajemen data transaksi sesuai dengan *role* pengguna (Admin & User).

---

## 🎯 2. Tujuan Program

1. Memahami konsep otentikasi login multi-role (*Admin* & *User*).
2. Memahami penggunaan variabel dan struktur data (*List*, *Dictionary*).
3. Memahami penggunaan input dinamis dan *formatting* output terminal.
4. Memahami penggunaan *conditional statement* bercabang.
5. Memahami perulangan (*looping*) untuk navigasi menu berulang.
6. Mengimplementasikan manipulasi elemen list (alokasi dan pengembalian unit mobil).
7. Membuat kalkulasi total biaya otomatis berdasarkan rute dan jumlah penumpang.
8. Melatih kemampuan *debugging* dan penanganan validasi input error.

---

## ⚙️ 3. Fitur Program

| No | Fitur | Fungsi | Status |
| -: | :--- | :--- | :---: |
| 1 | 🔐 **Login System** | Verifikasi multi-user/role berbasis dictionary | ✅ |
| 2 | 🎟️️ **Pemesanan Tiket** | Input data pemesan, rute, alokasi armada, & cetak bukti | ✅ |
| 3 | 👀 **Lihat Data** | Menampilkan seluruh riwayat transaksi tiket | ✅ |
| 4 | ✏️ **Ubah Data** | Mengubah data pemesan (Khusus Admin) | ✅ |
| 5 | 🗑️ **Batal Tiket** | Membatalkan pesanan & mengembalikan stok armada (Khusus Admin) | ✅ |
| 6 | 🚪 **Keluar** | Mengakhiri sesi program | ✅ |

---

## 📥 4. Input - Process - Output

### 📥 Input
* **Credentials Login:** `username`, `password`
* **Data Pemesan:** `nama`, `hp`, `jadwal`, `jemput`
* **Pilihan Menu & Opsi:** `pilih_rute`, `penumpang`, `pilih_mobil`, `pilih_bayar`

### ⚙️ Process
1. Autentikasi input username dan password terhadap dictionary `akun`.
2. Pemetaan tarif dasar berdasarkan rute yang dipilih.
3. Alokasi unit mobil: menghapus armada dari `mobil` saat dipesan dan mengembalikannya jika dibatalkan.
4. Kalkulasi biaya: $\text{Total Biaya} = \text{Harga Rute} \times \text{Jumlah Penumpang}$.
5. Penyimpanan record transaksi ke dalam list multidimensi `data`.

### 📤 Output
* Tampilan status login dan kode *security random*.
* Menu sistem interaktif sesuai hak akses.
* Struk/Bukti Transaksi Tiket Travel.
* Daftar riwayat seluruh transaksi tiket.

---

## 📊 5. Tabel Variabel

| No | Nama Variabel | Tipe Data | Fungsi |
| -: | :--- | :--- | :--- |
| 1 | `akun` | `Dictionary` | Menyimpan kredensial dan role pengguna |
| 2 | `data` | `List` | Menyimpan seluruh record transaksi pemesanan |
| 3 | `mobil` | `List` | Menyimpan daftar armada mobil yang tersedia |
| 4 | `book` | `Integer` | ID unik / kode booking otomatis (dimulai dari 101) |
| 5 | `harga` | `Integer` | Tarif dasar per penumpang |
| 6 | `total` | `Integer` | Total harga yang harus dibayar pemesan |

---

## 🧠 6. Konsep Pemrograman yang Digunakan

### 6.1 Variabel & Dictionary Data Structure
```python
akun = {
    "admin": {"password": "123", "role": "admin"},
    "yc": {"password": "123", "role": "admin"},
    "user": {"password": "123", "role": "user"},
    "yp": {"password": "123", "role": "user"}
}


pilih_rute = input("Pilih Rute (1-3): ")
rute_map = {
    "1": ("Balikpapan-Samarinda", 100000),
    "2": ("Samarinda-Tenggarong", 60000),
    "3": ("Balikpapan-IKN", 120000)
}
rute, harga = rute_map[pilih_rute]


# Menghapus unit yang terpilih dari stok armada
jenis = mobil.pop(idx_mobil)

# Mengembalikan armada saat tiket dibatalkan
mobil.append(item[7])
```

### 💻 7. Source Code

import os
import random
import time

akun = {
    "admin": {"password": "123", "role": "admin"},
    "yc": {"password": "123", "role": "admin"},
    "user": {"password": "123", "role": "user"},
    "yp": {"password": "123", "role": "user"}
}

data = []
mobil = ["Avanza Grand", "Innova Reborn", "Toyota Rush", "Fortuner"]
book = 101

def login():
    while True:
        print("\n=== LOGIN SISTEM TRAVEL ===")
        username = input("Username: ")
        password = input("Password: ")

        if username in akun and akun[username]["password"] == password:
            role = akun[username]["role"]
            print(f"Login berhasil sebagai {role.capitalize()}")
            return role
        
        print("Username atau password salah!")

# Sisa logika program dijalankan via loop utama pada main.py


###🖥️ 8. Tangkapan Layar & Output Program

=== BUKTI TIKET TRAVEL ===
Kode    : YURCELL-101
Pemesan : Budi Santoso
No HP   : 081234567890
Rute    : Balikpapan-Samarinda
Jadwal  : 10:00 WITA
Mobil   : Innova Reborn
Jemput  : Bandara SAMS Sepinggan
Total   : Rp 200,000
Bayar   : QRIS
Status  : LUNAS

### 🛠️ 9. Teknologi yang Digunakan
Python 3.x - Bahasa Pemrograman Utama
RAPTOR - Perancangan Algoritma & Flowchart
Git & GitHub - Version Control & Repositori Kode
VS Code - Integrated Development Environment (IDE)


### 10. output


### login sebagai admin


<img width="661" height="200" alt="Screenshot 2026-10-06 222325" src="https://github.com/user-attachments/assets/208229f6-0656-4d6d-b14c-aefd66a90262" />


<img width="674" height="208" alt="Screenshot 2026-10-06 222356" src="https://github.com/user-attachments/assets/cf51edf2-ca7f-42d9-bb21-2afa9786cf97" />


<img width="665" height="206" alt="Screenshot 2026-10-06 222432" src="https://github.com/user-attachments/assets/b4e5f1e7-887b-422b-9b7d-bde56a724cdd" />


<img width="668" height="205" alt="Screenshot 2026-10-06 222505" src="https://github.com/user-attachments/assets/b14338c2-3053-4dba-b8e9-203f2043214b" />


<img width="677" height="206" alt="Screenshot 2026-10-06 222519" src="https://github.com/user-attachments/assets/2d7e905c-4c88-4f70-9260-a6f28ce7b5f3" />


<img width="638" height="209" alt="Screenshot 2026-10-06 222558" src="https://github.com/user-attachments/assets/03151983-b712-4e5c-ba79-84a1b6248164" />


<img width="674" height="206" alt="Screenshot 2026-10-06 222629" src="https://github.com/user-attachments/assets/0d25bc39-6852-4426-8c89-45a93c56cbf9" />


<img width="665" height="210" alt="Screenshot 2026-10-06 222655" src="https://github.com/user-attachments/assets/8777391d-72b5-4578-93a7-2b70cfc4616b" />


<img width="673" height="209" alt="Screenshot 2026-10-06 222728" src="https://github.com/user-attachments/assets/2f70c498-85d3-4ebe-a606-b4e70c2ad516" />


<img width="665" height="205" alt="Screenshot 2026-10-06 222754" src="https://github.com/user-attachments/assets/dd737b3f-3f69-4219-bf6d-b30790a75540" />


<img width="679" height="205" alt="Screenshot 2026-10-06 222806" src="https://github.com/user-attachments/assets/b9197453-5ec5-4322-a090-b6692e62f86a" />

### 1. Proses Login dan Menu Utama (Gambar 1)
Autentikasi User:   Username: yc   Password: 123   Setelah berhasil login, sistem memberikan konfirmasi "Login berhasil sebagai Admin" beserta Kode Login: 9097.   Tampilan Menu Utama:
Sistem menampilkan 5 opsi menu navigasi utama untuk pengguna dengan peran Admin:   Pemesanan Tiket   Lihat Data   Ubah Data   Batal Tiket   Keluar  


### 2. Form Pemesanan Tiket / Create (Gambar 1 & 2)
Admin memilih Menu 1 (Pemesanan Tiket) dan mengisi data rincian pemesanan:   Data Pemesan: Nama Pemesan = yc, Nomor HP/WA = 0822.   Pilihan Rute:Balikpapan-Samarinda (100k)   Samarinda-Tenggarong (60k)   Balikpapan-IKN (120k)   Dipilih Rute 1 (Balikpapan-Samarinda).   Detail Perjalanan: Jadwal Berangkat = 08, Jumlah Penumpang = 2, Lokasi Titik Jemput = unmul.   Pilihan Kendaraan:Avanza Grand   Innova Reborn   Toyota Rush   Fortuner   Dipilih Kendaraan 4 (Fortuner) dengan Total Biaya Rp 200.000.   Metode Pembayaran:Transfer Bank   E-Wallet   QRIS   Dipilih Pembayaran 2 (E-Wallet).  


### 3. Output Bukti Tiket & Melihat Data / Read (Gambar 2)Bukti Tiket Travel (Rincian Transaksi):
Kode Tiket: YURCELL-101   Pemesan: yc | No HP: 0822   Rute: Balikpapan-Samarinda | Jadwal: 08   Mobil: Fortuner | Jemput: unmul   Total: Rp 200000 | Bayar: E-Wallet | Status: LUNAS   Melihat Daftar Pemesanan (Menu 2):


### Admin memilih Menu 2 (Lihat Data) untuk menampilkan ringkasan data tersimpan:
1 | YURCELL-101 | yc | 0822 | Balikpapan-Samarinda | Fortuner | Rp 200000.   4. Pengubahan Data Pemesanan / Update (Gambar 2 & 3)


### Admin memilih Menu 3 (Ubah Data Pemesanan) 
untuk memperbarui atribut tiket secara bertahap:   Mengubah Nama Pemesan:   Input nama lama (yc), pilih Opsi 1 (Nama), input nama baru (yy).   Respon: "Data berhasil diubah!".   Mengubah Nomor HP:   Input nama (yy), pilih Opsi 2 (No HP), input nomor baru (08333).   Respon: "Data berhasil diubah!".   Mengubah Titik Penjemputan:   Input nama (yy), pilih Opsi 3 (Titik Jemput), input lokasi baru (ft).   Respon: "Data berhasil diubah!".   5. Pembatalan Tiket & Sesi Keluar / Delete & Exit (Gambar 4)Membatalkan Tiket (Menu 4):


### Admin memilih Menu 4 (Batal Tiket),
lalu memasukkan nama pemesan (yy).   Respon: "Pesanan berhasil dibatalkan!".   Keluar dari Sistem (Menu 5):


### Admin memilih Menu 5 (Keluar).
Respon: "Terima kasih telah menggunakan sistem pemesanan tiket!" dan program selesai dijalankan.

### login sebagai user
<img width="673" height="204" alt="Screenshot 2026-10-06 200418" src="https://github.com/user-attachments/assets/802df1eb-c7ad-477a-9ce3-dcef22a82f45" />


<img width="673" height="206" alt="Screenshot 2026-10-06 200547" src="https://github.com/user-attachments/assets/83b64c0f-3973-45ad-8967-6a13be083cba" />


<img width="672" height="207" alt="Screenshot 2026-10-06 200623" src="https://github.com/user-attachments/assets/b63f7b08-5972-4b81-ad17-de8d51c0ec6b" />


<img width="670" height="206" alt="Screenshot 2026-10-06 200640" src="https://github.com/user-attachments/assets/679d29ff-f646-4226-ac06-c8d8b46898e6" />


<img width="668" height="205" alt="Screenshot 2026-10-06 200729" src="https://github.com/user-attachments/assets/9401b43c-bd2d-4fad-bf9b-a23d48e6a772" />


<img width="665" height="204" alt="Screenshot 2026-10-06 200749" src="https://github.com/user-attachments/assets/a0be8aa6-440b-4349-b09f-9f5e0915379f" />


<img width="665" height="204" alt="Screenshot 2026-10-06 200803" src="https://github.com/user-attachments/assets/57e4b667-8074-421f-99e3-1388f9e87390" />



### 1. Autentikasi & Menu Utama User (Gambar 1)Login User:
Pengguna melakukan login menggunakan kredensial Username: yp dan Password: 123. Setelah berhasil, sistem mengonfirmasi "Login berhasil sebagai User" dan menerbitkan kode login otomatis 3643.   Menu Akses Terbatas: Berbeda dari akun Admin yang memiliki akses edit/hapus data, akun User hanya diberikan 3 pilihan navigasi utama:   Pemesanan Tiket   Lihat Data   Keluar  


### 2. Pengisian Form Pemesanan Tiket (Gambar 1 & 2)User memilih Menu 1 (Pemesanan Tiket) dan menginput parameter pemesanan:
Identitas Pemesan: Nama Pemesan = yp, Nomor HP/WA = 08923.   Rute Perjalanan: Dipilih Opsi 1 untuk rute Balikpapan-Samarinda (100k).   Detail Operasional: Jadwal Berangkat = 06, Jumlah Penumpang = 2, Lokasi Titik Jemput = unmul.   Tipe Kendaraan: Dipilih Opsi 4 untuk kendaraan Fortuner dengan penyesuaian biaya menjadi Rp 200.000.   Metode Pembayaran: Dipilih Opsi 3 yaitu QRIS.   3. Penerbitan Bukti Tiket & Penampilan Data (Gambar 2)Cetak Bukti Tiket:
Setelah pembayaran dikonfirmasi, sistem langsung mencetak e-ticket lengkap:   Kode Tiket: YURCELL-101   Detail: Pemesan yp | No HP 08923 | Rute Balikpapan-Samarinda | Jadwal 06 | Mobil Fortuner | Titik Jemput unmul   Status: Total Rp 200000 | Pembayaran QRIS | Status LUNAS   Melihat Data Pemesanan (Menu 2):
User mengecek daftar tiket tersimpan melalui Menu 2 (Lihat Data). Sistem menampilkan baris ringkasan data perjalanan yang telah didaftarkan:
1 | YURCELL-101 | yp | 08923 | Balikpapan-Samarinda | Fortuner | Rp 200000.   


### 4. Penutupan Sesi Program (Gambar 3)Keluar dari Program (Menu 5):
User memilih opsi 5 (Keluar) pamenu utama.   


### Output menampilkan :
Sistem menampilkan ucapan penutup "Terima kasih telah menggunakan sistem pemesanan tiket!" dan menghentikan eksekusi terminal.



### ⭐ TERIMA KASIH ⭐
Learning to Code • Coding to Learn
