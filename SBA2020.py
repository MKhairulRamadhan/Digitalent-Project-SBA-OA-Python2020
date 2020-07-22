'''
namafile: sba.py
Lembar kerja/script Latihan SBA
'''
# >>>>>>LEMBAR KERJA>>>>>>>>>
# lembar ini hanya berisi pendefinisian fungsi dan class saja
 
#email netacad
email = 'khairulr59@gmail.com'
 
# >>>>>>Soal 1
def fungsiIO():
  pass
  # Mulai kode anda dari sini
  data = input("")
  data = data.split()

  data.sort()

  urut = []
  for v in data:
  	urut.append(int(v))

  urut.sort()

  for i in urut:
  	print("*"*i)
 
# >>>>>>Akhir Soal 1 

# >>>>>>Soal 2
def caseShopia(txt):
  pass
  # Mulai kode anda dari sini
  hasil = ""
  for data in txt:
  	if (ord(data) >= 97) and (ord(data) <= 122):
  		hasil += data.upper()
  	elif (ord(data) >= 65) and (ord(data) <= 90):
  		hasil += data.lower()
  
  return hasil
# >>>>>>Akhir Soal 2 

# Jangan diubah biarkan seperti ini
dcur2idr = {'USD': 14425, 'EUR': 16225, 'AUD': 9925, 'CAD': 10500, 
             'GBP': 17800, 'CHF': 15200, 'SGD': 10375, 'HKD': 1775, 
             'JPY': 132500, 'MYR': 3250, 'SAR': 3500, 'WON': 10750, 
             'IDR': 1}
 
# >>>>>> Soal 3 
def usd2eur(usd):
  pass
  # Mulai kode anda dari sini
  idr_simpan = dcur2idr['USD']*usd
  hasil = idr_simpan/dcur2idr['EUR']
  return hasil
 
# >>>>>>Akhir Soal 3 


# >>>>>>Soal 4 
class MoneyChanger:

  def __init__(self,dcurrency,base='IDR',percent=2):
    pass
    # Mulai kode anda dari sini
    self.dcurrency = dcurrency
    self.base = base
    self.percent = percent
    self.change_base(base)
 
  def selling_price(self,nominal,curr):
    pass
    # Mulai kode anda dari sini
    idr_data = dcur2idr[curr] *  nominal
    hasil = idr_data / dcur2idr[self.base]

    hasil_persen = self.percent*hasil/100
    hasil += hasil_persen
    return hasil
 
  def buying_price(self,nominal,curr):
    pass
    # Mulai kode anda dari sini
    idr_data = dcur2idr[curr] *  nominal
    hasil = idr_data / dcur2idr[self.base]

    hasil_persen = self.percent*hasil/100
    hasil -= hasil_persen
    return hasil
 
  def change_base(self,new_base):
    pass
    # Mulai kode anda dari sini
    self.base = new_base

 
 
# >>>>>>Akhir Soal 4 
 
# >>>>>>AKHIR LEMBAR KERJA>>>>>>>>>