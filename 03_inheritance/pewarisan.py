class Pegawai:
    def __init__(self, nama, gaji):
      self.nama = nama
      self.gaji = gaji

class Manager(Pegawai):
    def __init__(self, nama, gaji, tunjangan):
      super().__init__(nama, gaji)
      self.tunjangan = tunjangan

    def info_manager(self):
        return f"Nama: {self.nama}, Gaji: {self.gaji}, Tunjangan: {self.tunjangan}"

manager1 = Manager("Alice", 5000000, 1000000)
print(manager1.info_manager())
