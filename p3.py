# nama file p3.py 
# Isikan email anda dan copy semua cell code yang dengan komentar #Graded

# untuk revisi dan resubmisi sebelum deadline
# silakan di resubmit dengan nilai variable priority yang lebih besar dari
# nilai priority submisi sebelumnya
# JIKA TIDAK ADA VARIABLE priority DIANGGAP priority=0
priority = 0

#netacad email cth: 'abcd@gmail.com'
email='khairulr59@gmail.com'
 
# copy-paste semua #Graded cells YANG SUDAH ANDA KERJAKAN di bawah ini

# Graded
def caesar_encript(txt,shift):
  pass
  # Mulai Kode anda di sini
  v = ""
  simpan = 0
  for data in txt:
    if (ord(data) >= 97) and (ord(data) <= 122):
      nilai = ord(data)
      baru = (ord(data) + shift)
      if (nilai + shift) > 122:
        simpan = (nilai + shift) - 122
        baru = 97 + (simpan-1)
      if (nilai + shift) < 97:
        simpan = 97 - (nilai + shift)
        baru = 122 - (simpan-1)

      v = v + str(chr(baru))

    elif (ord(data) >= 65) and (ord(data) <= 90):
      nilai = ord(data)
      
      baru = (ord(data) + shift)
      if (nilai + shift) > 90:
        simpan = (nilai + shift) - 90
        baru = 65 + (simpan-1)
      if (nilai + shift) < 65:
        simpan = 65 - (nilai + shift)
        baru = 90 - (simpan-1)

      v = v + str(chr(baru))
    
    else:
      v = v + data


  return v

# Fungsi Decript caesar
def caesar_decript(chiper,shift):
  return caesar_encript(chiper,-shift)



# Graded
 
# Fungsi mengacak urutan
def shuffle_order(txt,order):
  return ''.join([txt[i] for i in order])
 
# Fungsi untuk mengurutkan kembali sesuai order
def deshuffle_order(sftxt,order):
  pass
  # Mulai Kode anda di sini
  hasil = ""
  simpan = 0
  panjang = len(order)
  for i in range(panjang):
    for y in range(panjang):
      if i == order[y]:
        simpan = y
        break

    hasil = hasil + str(sftxt[y])

  return hasil