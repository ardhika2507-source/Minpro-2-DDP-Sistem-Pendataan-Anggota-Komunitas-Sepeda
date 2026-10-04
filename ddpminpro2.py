import json
import os
import getpass
from datetime import date

FILE_ANGGOTA = "data_anggota.json"


users = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"},
}


KATEGORI = {
    "1": "road bike",
    "2": "mtb",
    "3": "fixie",
    "4": "sepeda lipat",
}



def muat_data():
    """membaca data anggota dari file json"""
    if os.path.exists(FILE_ANGGOTA):
        try:
            with open(FILE_ANGGOTA, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("file data rusak, prodram memakai data kosong.")
    return {}


def simpan_data(data_anggota):
    """menyimpan data anggota ke file json"""
    try:
        with open(FILE_ANGGOTA, "w") as f:
            json.dump(data_anggota, f, indent=4)
    except OSError:
        print("gagal menyimoan data ke file.")


def format_rupiah(angka):
    return "Rp" + f"{angka:,}".replace(",", ".")



def input_password(pesan):
    """input password, setiap huruf yang diketik tampil sebagai bintang (*)"""
    try:
        import msvcrt
    except ImportError:
        return getpass.getpass(pesan)

    print(pesan, end="", flush=True)
    hasil = ""
    while True:
        huruf = msvcrt.getwch()
        if huruf in ("\r", "\n"):
            print()
            return hasil
        elif huruf == "\x03":
            raise KeyboardInterrupt
        elif huruf == "\b":
            if len(hasil) > 0:
                hasil = hasil[:-1]
                print("\b \b", end="", flush=True)
        elif huruf in ("\x00", "\xe0"):
            msvcrt.getwch()
        else:
            hasil += huruf
            print("*", end="", flush=True)


def login():
    """login maksimal 3 kali, mengembalikan role (admin/user) atau None"""
    print("\n===== login =====")
    for sisa in range(3, 0, -1):
        username = input("username : ").strip()
        password = input_password("paswword : ")

        if username == "" or password == "":
            print(f"username/password tidak boleh kosong! sisa percobaan: {sisa - 1}")
        elif username in users and users[username]["password"] == password:
            print(f"login berhasil, selamat datang {username}!")
            return users[username]["role"]
        else:
            print(f"username/password salah! sisa percobaan: {sisa - 1}")
    print("percobaan login habis.")
    return None



def tampilkan_menu_awal():
    print("\n===== sistem pendataan anggota komunitas sepeda =====")
    print("1. login")
    print("0. keluar")


def tampilkan_menu_admin():
    print("\n===== menu admin =====")
    print("1. tambah data anggota")
    print("2. lihat semua data anggota")
    print("3. cari data anggota")
    print("4. ubah data anggota")
    print("5. hapus data anggota")
    print("0. logout")


def tampilkan_menu_user():
    print("\n===== menu user =====")
    print("1. lihat semua data anggota")
    print("2. cari data anggota")
    print("0. logout")



def buat_id(data_anggota):
    terbesar = 0
    for id_anggota in data_anggota:
        terbesar = max(terbesar, int(id_anggota[3:]))
    return f"AGT{terbesar + 1:03d}"


def input_kategori():
    """memilih kategori sepeda dari data KATEGORI, None jika tidak valid"""
    print("kategori sepeda:")
    for kode, nama in KATEGORI.items():
        print(f" {kode}. {nama}")
    pilihan = input("pilih kategori (1-$: ").strip()
    if pilihan in KATEGORI:
        return KATEGORI[pilihan]
    return None


def tambah_data(data_anggota):
    """CREATE"""
    print("\n-- tambah data anggota baru --")
    nama = input("masukkan nama anggota: ").strip()

    if nama == "":
        print("nama tidak boleh kosong! data batal ditambahkan.")
        return

    kategori = input_kategori()
    if kategori is None:
        print("kategori tidak valid! data batal ditambahkan.")
        return

    iuran_input = input("masukkan jumlah iuran (angka): ").strip()
    try:
        iuran = int(iuran_input)
    except ValueError:
        print("iuran harus berupa angka! data batal ditambahkan.")
        return

    if iuran <= 0:
        print("iuran harus lebih dari 0! data batal ditambahkan>")
        return

    id_baru = buat_id(data_anggota)
    data_anggota[id_baru] = {
        "nama": nama.title(),
        "kategori": kategori,
        "iuran": iuran,
        "tgl_gabung": str(date.today()),
    }
    simpan_data(data_anggota)
    print(f"data anggota '{nama.title()}' berhasil ditambahkan dengan ID {id_baru}!")


def tampilkan_tabel(data):
    print("-" * 74)
    print(f"{'ID':<9}{'nama':<20}{'kategori':<15}{'iuran':<13}{'bergabung':<12}")
    print("-" * 74)
    for id_anggota, d in data.items():
        print(f"{id_anggota:<9}{d['nama']:<20}{d['kategori']:<15}"
              f"{format_rupiah(d['iuran']):<13}{d['tgl_gabung']:<12}")
    print("-" * 74)


def lihat_data(data_anggota):
    """RAED"""
    print("\n-- daftar semua anggota --")

    if len(data_anggota) == 0:
        print("belum ada data anggota yang disimpan.")
        return

    tampilkan_tabel(data_anggota)
    total = sum(d["iuran"] for d in data_anggota.values())
    print(f"jumlah anggota: {len(data_anggota)} | total iuran: {format_rupiah(total)}")


def cari_data(data_anggota):
    """READ (pencarian berdasarkan nama atau kategori)"""
    print("\n-- cari data anggota --")

    if len(data_anggota) == 0:
        print("belum ada data anggota yang tersimpan.")
        return
    
    kata_kunci = input("masukkan nama/kategori yang dicari: ").strip().lower()
    if kata_kunci == "":
        print("kata kunci tidak boleh kosong!")
        return

    hasil = {}
    for id_anggota, d in data_anggota.items():
        if kata_kunci in d["nama"].lower() or kata_kunci in d["kategori"].lower():
            hasil[id_anggota] = d

    if len(hasil) == 0:
        print("data anggota tersebut tidak ditemukan.")
    else:
        tampilkan_tabel(hasil)


def ubah_data(data_anggota):
    """UPDATE (kosongkan input untk tidak mengubah)"""
    print("\n-- ubah data anggota --")

    if len(data_anggota) == 0:
        print("belum ada data anggota ayng tersimpan.")
        return

    lihat_data(data_anggota)
    id_anggota = input("\nmasukkan ID anggota yang ingin diubah: ").strip().upper()

    if id_anggota not in data_anggota:
        print("ID tidak ditemukan!")
        return

    d = data_anggota[id_anggota]
    print("kosongkan lalu enter jika tidak ingin mengubah.")

    nama = input(f"nama baru [{d['nama']}]: ").strip()
    if nama != "":
        d["nama"] = nama.title()

    ganti_kategori = input("ubah kategori? (y/n): ").strip().lower()
    if ganti_kategori == "y":
        kategori = input_kategori()
        if kategori is None:
            print("kategori tidak valid, kategori tidak diubah.")
        else:
            d["kategori"] + kategori

    iuran_input = input(f"iuran baru [{d['iuran']}]: ").strip()
    if iuran_input != "":
        try:
            iuran = int(iuran_input)
            if iuran <= 0:
                print("iuran harus lebih dari 0, iuran tidak diubah.")
            else:
                d["iuran"] = iuran
        except ValueError:
            print("iuran harus berupa angka, iuran tidak diubah.")

    simpan_data(data_anggota)
    print("data anggota berhasil diubah.")


def hapus_data(data_anggota):
    """DELETE"""
    print("\n-- hapus data anggota --")

    if len(data_anggota) == 0:
        print("belum ada data anggota yang tersimpan.")
        return

    lihat_data(data_anggota)
    id_anggota = input("\nmasukkan ID anggota yangb ingin dihapus: ").strip().upper()

    if id_anggota not in data_anggota:
        print("ID tidak ditemukan!")
        return

    yakin = input(f"yakin hapus '{data_anggota[id_anggota]['nama']}'? (y/n): ").strip().lower()
    if yakin == "y":
        anggota_terhapus = data_anggota.pop(id_anggota)
        simpan_data(data_anggota)
        print(f"data anggota '{anggota_terhapus['nama']}' berhasil dihapus.")
    else:
        print("penghapusan dibatalkan.")



def menu_admin(data_anggota):
    """admin: CRUD lengkap"""
    while True:
        tampilkan_menu_admin()
        pilihan = input("pilih menu (0-5): ").strip()

        if pilihan == "1":
            tambah_data(data_anggota)
        elif pilihan == "2":
            lihat_data(data_anggota)
        elif pilihan == "3":
            cari_data(data_anggota)
        elif pilihan == "4":
            ubah_data(data_anggota)
        elif pilihan == "5":
            hapus_data(data_anggota)
        elif pilihan == "0":
            print("logout berhasil.")
            break
        else:
            print("pilihan tidak valid! silahkan masukkan 0-5.")


def menu_user(data_anggota):
    """user: hanya lihat & cari"""
    while True:
        tampilkan_menu_user()
        pilihan = input("pilih menu (0-2): ").strip()

        if pilihan == "1":
            lihat_data(data_anggota)
        elif pilihan == "2":
            cari_data(data_anggota)
        elif pilihan == "0":
            print("logout berhasil.")
            break
        else:
            print("pilihan tidak valid! silahkan masukkan 0-2.")


def main():
    data_anggota = muat_data()
    while True:
        tampilkan_menu_awal()
        pilihan = input("pilih menu (0-1): ").strip()

        if pilihan == "1":
            role = login()
            if role == "admin":
                menu_admin(data_anggota)
            elif role == "user":
                menu_user(data_anggota)
        elif pilihan == "0":
            print("terimakasih telah menggunakan program ini")
            break
        else:
            print("piliha tidak valid! silahkan masukkan 0 atau 1.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nprogram dihentikan.")