class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    def info_mahasiswa(self):
        return f"Nama: {self.nama}\nNIM: {self.nim}\nJurusan: {self.jurusan}"

mhs1 = Mahasiswa("Muhammad Farhan Shiddiq", "065118213", "Ilmu Komputer")

print(mhs1.info_mahasiswa())
