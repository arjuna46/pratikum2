class DaftarNilaiMahasiswa:
    def __init__(self):
        self.data_mahasiswa = []

    def tambah(self, nama, nilai):
        mahasiswa_baru = {'nama': nama, 'nilai': nilai}
        self.data_mahasiswa.append(mahasiswa_baru)
        print(f"Data mahasiswa {nama} berhasil ditambahkan.")

    def tampilkan(self):
        if not self.data_mahasiswa:
            print("Data mahasiswa kosong.")
        else:
            print("Daftar Nilai Mahasiswa:")
            for mahasiswa in self.data_mahasiswa:
                print(f"Nama: {mahasiswa['nama']}, Nilai: {mahasiswa['nilai']}")

    def hapus(self, nama):
        for mahasiswa in self.data_mahasiswa:
            if mahasiswa['nama'] == nama:
                self.data_mahasiswa.remove(mahasiswa)
                print(f"Data mahasiswa {nama} berhasil dihapus.")
                return
        print(f"Data mahasiswa {nama} tidak ditemukan.")

    def ubah(self, nama, nilai_baru):
        for mahasiswa in self.data_mahasiswa:
            if mahasiswa['nama'] == nama:
                mahasiswa['nilai'] = nilai_baru
                print(f"Data mahasiswa {nama} berhasil diubah menjadi nilai {nilai_baru}.")
                return
        print(f"Data mahasiswa {nama} tidak ditemukan.")

# Contoh penggunaan class
daftar_nilai = DaftarNilaiMahasiswa()

daftar_nilai.tambah("Junn", 85)
daftar_nilai.tambah("Arjun", 92)
daftar_nilai.tambah("Juna", 78)
daftar_nilai.tampilkan()
daftar_nilai.ubah("Arjun", 95)
daftar_nilai.tampilkan()
daftar_nilai.hapus("Juna")
daftar_nilai.tampilkan()
