from abc import ABC, abstractmethod

#class abstract
class Hewan(ABC):

  @abstractmethod
  def suara(self):
    pass

#sub class kucing
class Kucing(Hewan):
  def suara(self):
    return "Meow"

class Anjing(Hewan):
  def suara(self):
    return "Bark"

kucing1 = Kucing()
anjing1 = Anjing()

print(f"Kucing: {kucing1.suara()}")
print(f"Anjing: {anjing1.suara()}")
