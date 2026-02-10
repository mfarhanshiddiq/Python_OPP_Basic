class tabungan:
    def __init__(self, saldo = 200000):
      self.__saldo = saldo

    def deposit(self, amount):
      if amount > 0:
        self.__saldo += amount
        print(f"Deposit sebesar {amount}. Saldo sekarang: {self.__saldo}")
      else:
        print("Jumlah deposit harus positif.")

    def tarik(self, amount):
      if amount > 0:
        if self.__saldo >= amount:
          self.__saldo -= amount
          print(f"Penarikan sebesar {amount}. Saldo sekarang: {self.__saldo}")
        else:
          print(f"Saldo tidak mencukupi. Saldo saat ini: {self.__saldo}")
      else:
        print("Jumlah penarikan harus positif.")

    def get_saldo(self):
      return self.__saldo

my_tabungan = tabungan()
print(f"Saldo awal: {my_tabungan.get_saldo()}")

my_tabungan.deposit(50000)
my_tabungan.tarik(50000000)
print(f"Saldo akhir: {my_tabungan.get_saldo()}")
