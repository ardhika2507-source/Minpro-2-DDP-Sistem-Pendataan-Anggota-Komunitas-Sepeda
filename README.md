# Sistem Pendataan Anggota Komunitas Sepeda

Mini Project 2 – Dasar-Dasar Pemrograman

| | |
|---|---|
| Nama | _Muhammad Ardhika Prasanjayu_ |
| NIM | _2609116108_ |
| KELAS | _C_ |
| SOAL | _Genap_ |

---

## 1. Deskripsi Singkat Program

Program ini digunakan untuk mendata anggota komunitas sepeda. Setiap anggota punya ID otomatis, nama, kategori sepeda (road bike, mtb, fixie, sepeda lipat), jumlah iuran, dan tanggal bergabung. Data disimpan di (`data_anggota.json`) sehingga tidak hilang saat program ditutup. Pengguna harus login dulu. Role **admin** bisa menambah, melihat, mencari, mengubah, dan menghapus data. Role **user** hanya bisa melihat dan mencari data.

**Data yang dicatat tiap anggota:** ID otomatis (`AGT001`, `AGT002`, dst.), nama, kategori sepeda (road bike, mtb, fixie, sepeda lipat), iuran, dan tanggal bergabung.

**Hak akses tiap role:**

| Fitur | Admin | User |
|---|:---:|:---:|
| Lihat data | ✔ | ✔ |
| Cari data | ✔ | ✔ |
| Tambah data | ✔ | ✘ |
| Ubah data | ✔ | ✘ |
| Hapus data | ✔ | ✘ |

**Akun buat coba:** `admin` / `admin123` dan `user` / `user123`

**Kesesuaian dengan ketentuan tugas:**

| Ketentuan | Penerapan di program |
|---|---|
| Validasi input pakai conditional | `if/elif/else` di semua input (nama, kategori, iuran, ID, pilihan menu) |
| Dictionary | `users`, `KATEGORI`, `data_anggota` |
| Function | 19 fungsi (login, CRUD, menu, dan fungsi pendukung) |
| Login username dan password | Fungsi `login()`, maksimal 3 kali coba |
| Minimal 2 role, 1 role CRUD lengkap | `admin` (CRUD lengkap) dan `user` (lihat dan cari) |
| Library Python | `json`, `os`, `getpass`, `datetime`, `msvcrt` |

---

## 2. Flowchart dan Penjelasan Alur

### Flowchart 1 – Alur Utama (Login dan Role)

<img width="717" height="935" alt="Screenshot 2026-10-04 222325" src="https://github.com/user-attachments/assets/6dd21b98-8982-4bb0-b2fa-cbc053501115" />

1. Program mulai, lalu **muat data** dari file JSON dulu.
2. **Menu awal** muncul. Pilih `0` kalau mau keluar, pilih `1` kalau mau login.
3. Kalau login, pengguna isi **username dan password**, terus sistem cek valid atau tidak.
4. Kalau **tidak valid**, sistem cek sudah berapa kali nyoba. Selama masih kurang dari 3 kali, pengguna disuruh isi ulang. Kalau sudah 3 kali, balik ke menu awal.
5. Kalau **valid**, sistem cek **role**-nya. `admin` masuk ke menu admin (CRUD lengkap), `user` masuk ke menu user (cuma lihat dan cari).
6. Habis **logout**, program balik lagi ke menu awal.

### Flowchart 2 – Menu Admin (CRUD)

<img width="732" height="927" alt="Screenshot 2026-10-04 222343" src="https://github.com/user-attachments/assets/1f541d97-3268-4274-8af9-27c00e1721a2" />

1. Menu admin muncul, lalu admin masukin pilihan menu.
2. Pilihannya dicek satu-satu: `1` tambah, `2` lihat, `3` cari, `4` ubah, `5` hapus, `0` logout.
3. Setelah satu aksi selesai, program **balik lagi ke menu admin**.
4. Pilihan `0` mengakhiri sesi admin dan balik ke menu awal. Kalau pilihannya di luar itu, muncul pesan "pilihan tidak valid" dan admin disuruh input lagi.

Menu user alurnya sama, tapi cuma ada `1` lihat, `2` cari, dan `0` logout.

---

## 3. Dokumentasi Program

### Struktur data (Dictionary)

```python
users = {"admin": {"password": "admin123", "role": "admin"},
         "user": {"password": "user123", "role": "user"}}

KATEGORI = {"1": "road bike", "2": "mtb", "3": "fixie", "4": "sepeda lipat"}

data_anggota = {
    "AGT001": {"nama": "Adit", "kategori": "mtb",
               "iuran": 2000, "tgl_gabung": "2026-10-04"},
}
```

### Fungsi-fungsi

| Fungsi | Keterangan |
|---|---|
| `muat_data()`, `simpan_data()` | Baca dan tulis data anggota ke `data_anggota.json` |
| `format_rupiah()` | Ubah angka jadi format `Rp2.000` |
| `input_password()` | Input password yang tampil sebagai `*` |
| `login()` | Cek username dan password (maksimal 3 kali), lalu mengembalikan role |
| `tampilkan_menu_awal()`, `tampilkan_menu_admin()`, `tampilkan_menu_user()` | Mencetak menu |
| `buat_id()` | Bikin ID otomatis dari nomor terbesar yang sudah ada |
| `input_kategori()` | Tampilkan pilihan kategori dan cek pilihannya valid atau tidak |
| `tambah_data()` | **Create**: tambah anggota baru dengan validasi |
| `lihat_data()`, `tampilkan_tabel()` | **Read**: tampilkan tabel anggota dan total iuran |
| `cari_data()` | **Read**: cari berdasarkan sebagian nama atau kategori |
| `ubah_data()` | **Update**: ubah nama, kategori, atau iuran (kosongin kalau tidak mau diubah) |
| `hapus_data()` | **Delete**: hapus anggota setelah konfirmasi y/n |
| `menu_admin()`, `menu_user()` | Menu sesuai role |
| `main()` | Menu awal, login, lalu pilih menu sesuai role |

### Bagian-bagian pentingnya

- **Role:** `login()` mengembalikan `"admin"` atau `"user"`. Dari nilai itu, `main()` manggil `menu_admin()` atau `menu_user()`. Di `menu_user()` memang tidak ada pilihan tambah, ubah, dan hapus, jadi user biasa tidak bisa mengubah data.
- **Validasi:** setiap input dicek pakai `if`. Kalau tidak valid, fungsinya langsung `return` dan datanya tidak disimpan.
- **Penyimpanan:** setiap tambah, ubah, dan hapus langsung manggil `simpan_data()`, jadi datanya tetap aman waktu program dijalankan lagi.

---

## 4. Penerapan Nilai Tambah

### Error handling

Kalau ada input yang salah, program tidak langsung berhenti atau error, tapi menampilkan pesan dan lanjut jalan.

| Lokasi | Error yang ditangani | Hasilnya |
|---|---|---|
| `tambah_data()` | `ValueError` (iuran bukan angka) | Muncul pesan, data batal ditambahkan |
| `ubah_data()` | `ValueError` (iuran bukan angka) | Iuran tidak diubah, data lain tetap tersimpan |
| `muat_data()` | `json.JSONDecodeError` (file rusak) | Program pakai data kosong |
| `simpan_data()` | `OSError` (gagal nulis file) | Muncul pesan gagal menyimpan |
| `input_password()` | `ImportError` (bukan Windows) | Otomatis pindah ke `getpass` |

```python
try:
    iuran = int(iuran_input)
except ValueError:
    print("iuran harus berupa angka! data batal ditambahkan.")
    return
```

### Library yang digunakan

| Library | Dipakai untuk |
|---|---|
| `json` | Simpan dan baca data anggota |
| `os` | Cek file data sudah ada atau belum |
| `getpass` | Input password tersembunyi (cadangan kalau bukan Windows) |
| `datetime` | Isi tanggal bergabung otomatis |
| `msvcrt` | Munculin `*` waktu ngetik password di Windows |

---

## 5. Dokumentasi Output

### Gambar 1 – Menu awal dan login gagal

<img width="487" height="247" alt="Screenshot 2026-10-05 002025" src="https://github.com/user-attachments/assets/ffe55239-fc09-46f3-b23e-e9f9896b86ec" />

Password yang salah langsung ditolak dan sisa percobaannya berkurang.

### Gambar 2 – Login admin berhasil

<img width="491" height="261" alt="Screenshot 2026-10-05 002335" src="https://github.com/user-attachments/assets/dcdbb6ee-4f19-43d2-bbfa-470502dbb00b" />

Admin dapat enam pilihan menu, termasuk tambah, ubah, dan hapus.

### Gambar 3 – Validasi input tambah data

<img width="457" height="70" alt="Screenshot 2026-10-05 003142" src="https://github.com/user-attachments/assets/a34336d1-9e9a-4df4-89d4-8915e0035e0b" />
<img width="432" height="202" alt="Screenshot 2026-10-05 003201" src="https://github.com/user-attachments/assets/01df7e8f-05d8-41eb-aee9-603cef42251f" />
<img width="466" height="230" alt="Screenshot 2026-10-05 003209" src="https://github.com/user-attachments/assets/7be5091b-5bfb-48e9-aef3-0a5a1ec93188" />

Tiga input yang salah (nama kosong, kategori di luar pilihan, iuran berupa huruf) ditolak dengan pesan yang jelas, dan programnya tetap jalan.

### Gambar 4 – Tambah data berhasil

<img width="585" height="227" alt="Screenshot 2026-10-05 003612" src="https://github.com/user-attachments/assets/9c809391-caef-4d0f-a4e8-89dd7f268a4a" />

Kalau semua input benar, data tersimpan dengan ID otomatis. Nama juga otomatis jadi huruf kapital di awal kata.

### Gambar 5 – Lihat semua data

<img width="733" height="222" alt="Screenshot 2026-10-05 003757" src="https://github.com/user-attachments/assets/742fdac1-b911-422e-b5da-9788a3db714b" />

Semua anggota tampil dalam tabel, lengkap dengan jumlah anggota dan total iuran yang dihitung otomatis. Tanggalnya ngikutin hari kamu jalanin program.

### Gambar 6 – Cari data

<img width="710" height="162" alt="Screenshot 2026-10-05 003947" src="https://github.com/user-attachments/assets/93041e5e-1a59-4bb1-9cfb-62e27f040a72" />

Pencarian nampilin anggota yang nama atau kategorinya cocok sama kata kunci.

### Gambar 7 – Ubah data

<img width="567" height="277" alt="Screenshot 2026-10-05 004253" src="https://github.com/user-attachments/assets/1eab73f9-deb3-4403-aa45-10c0755aed0c" />

Di sini nama Adit diubah menjadi apas, dan kategorinya diganti dari fixie ke mtb dan iurannya jadi 10000.

### Gambar 8 – Hapus data

<img width="712" height="371" alt="Screenshot 2026-10-05 004730" src="https://github.com/user-attachments/assets/5f48a6d6-4dff-4bf1-a1fb-21098a8430d9" />

Sebelum dihapus, program tanya konfirmasi dulu supaya data tidak hilang gara-gara salah input. Kalau jawabannya `n`, penghapusan dibatalkan.

### Gambar 9 – Pilihan tidak valid dan logout

<img width="441" height="212" alt="Screenshot 2026-10-05 004837" src="https://github.com/user-attachments/assets/3f6b3bc0-0f46-442c-b948-8011ec707c75" />
<img width="523" height="320" alt="Screenshot 2026-10-05 004949" src="https://github.com/user-attachments/assets/19aae55a-e2cc-4b5f-b655-40a1c214e4b6" />

Angka di luar menu ditolak dan programnya tidak berhenti. Pilihan `0` balik ke menu awal.

### Gambar 10 – Menu user (akses terbatas)

<img width="760" height="452" alt="Screenshot 2026-10-05 005114" src="https://github.com/user-attachments/assets/af928fc8-fb21-43d3-a1ac-8fdb2fbfe293" />

User cuma dapat menu lihat dan cari, tidak ada tambah, ubah, atau hapus. Ini buktiin kalau hak akses antar role memang beda. Data yang tampil juga sudah sesuai hasil hapus Apas tadi.

### Gambar 11 – Isi file `data_anggota.json` dan keluar program

<img width="557" height="487" alt="Screenshot 2026-10-05 005324" src="https://github.com/user-attachments/assets/4444b36b-0c79-419c-93c6-0abdc6ab59e9" />
<img width="527" height="156" alt="Screenshot 2026-10-05 005508" src="https://github.com/user-attachments/assets/699f6a4b-25d4-47b8-878f-df5694bdad6e" />


Data tersimpan permanen di file JSON, dan isinya sama dengan hasil ubah (Gambar 7) dan hapus (Gambar 8). Pilih `0` di menu awal buat keluar dari program.
