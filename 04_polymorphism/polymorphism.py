class Kendaraan:
  def __init__(self, jenis_bahan_bakar):
    self.jenis_bahan_bakar = jenis_bahan_bakar

class Mobil(Kendaraan):
  def __init__(self):
    super().__init__("Bensin")
    self.jenis_bahan_bakar = "Bensin"

class Motor(Kendaraan):
  def __init__(self):
    super().__init__("Solar")
    self.jenis_bahan_bakar = "Solar"

mobil1 = Mobil()
motor1 = Motor()

print(f"Mobil: {mobil1.jenis_bahan_bakar}")
print(f"Motor: {motor1.jenis_bahan_bakar}")
