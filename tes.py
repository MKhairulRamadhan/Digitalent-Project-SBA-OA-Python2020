'''
namafile: latihanSBA.py
Lembar kerja/script Latihan SBA
'''
# >>>>>>LEMBAR KERJA>>>>>>>>>
# lembar ini hanya berisi pendefinisian fungsi dan class saja

#email netacad, JANGAN SAMPAI LUPA >>>>>>><<<<<<<
email = 'khairulr59@gmail.com'

#soal 1
class titik2d:  

  # parameterized constructor 
  def __init__(self, x, y): 
    self.x = x
    self.y = y 
    
  def ambiltitik(self):
    hasil = (self.x,self.y)
    return hasil

  def tambahkan(self,titik):
    self.x = self.x + titik.x
    self.y = self.y + titik.y

# soal 2
def run():
  simpan = input("Masukan angka: ")
  simpan = simpan.split()
  angka1 = int(simpan[0])
  angka2 = int(simpan[1])

  return titik2d(angka1,angka2)

# >>>>>>AKHIR LEMBAR KERJA>>>>>>>>>



if __name__ == '__main__':
  # >>>>>TEST DI SINI>>>>>>
  # gunakan BLOCK MAIN ini untuk mengetes

  # untuk pengetesan kode hanya boleh di bagian sini
  # silakan test sesuka hati di sini
  t1 = run()
  print('titik1:',t1.ambiltitik())

  # >>>>>AKHIR TEST DI SINI>>>>>>
