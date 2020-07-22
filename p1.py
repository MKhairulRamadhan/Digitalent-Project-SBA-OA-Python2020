# nama file p1.py 
# Isikan email anda dan copy semua cell code yang dengan komentar #Graded
# Isikan juga priority file

# untuk resubmisi, grader hanya akan mengambil priority yang paling besar
# jadi kalau anda ingin merevisi kode anda:
# silakan di resubmit dengan nilai variable priority yang lebih besar dari
# nilai priority submisi sebelumnya
# JIKA TIDAK ADA VARIABLE priority DIANGGAP priority=0

priority = 0


#netacad email cth: 'abcd@gmail.com'
email='khairulr59@gmail.com'

# copy-paste semua #Graded cells di bawah ini

# PASTE KODE ANDA DISINI 
#Graded

# Manual, filter, list comprehension
def letter_catalog(items,letter='A'):
  pass
  # MULAI KODEMU DI SINI
  list = []
  for data in items:
    if data[0] == letter:
      list.append(data)

  if len(list) == 0:
    return (list);
  else:
    return (list)

#Graded

def counter_item(items):
  pass
  # MULAI KODEMU DI SINI
  data = {}

  for v in items:
    if v not in data:
      data[v] = 1;
    else:
      data[v] = data[v]+1;

  return( data )

#Graded

# dua variable berikut jangan diubah
fruits = ['Apple','Avocado','Banana','Blackberries','Blueberries','Cherries','Date Fruit','Grapes','Guava','Jackfruit','Kiwifruit']
prices = [6,5,3,10,12,7,14,15,8,7,9]

# list buah
chart = ['Blueberries','Blueberries','Grapes','Apple','Apple','Apple','Blueberries','Guava','Jackfruit','Blueberries','Jackfruit']

# MULAI KODEMU DI SINI
fruit_price = {}
for x in range(0,len(fruits)):
  fruit_price[fruits[x]] = prices[x];

def total_price(dcounter,fprice):
  pass
  # MULAI KODEMU DI SINI
  price_f = 0
  for value in dcounter:
    price_f += fprice[value]*dcounter[value];

  return(price_f)

#Graded

def discounted_price(total,discount,minprice=100):
  pass
  # MULAI KODEMU DI SINI
  if(total >= minprice):
    persentase = 0
    persentase = (discount/100)*total
    total_v = total - round(persentase,2)
    return(round(total_v,2))
  else:
    return (total)


#Graded

def print_summary(items,fprice):
  pass
  # MULAI KODEMU DI SINI
  items.sort()
  dcounter = counter_item(items)

  price_f = 0
  for value in dcounter:
    price_f += fprice[value]*dcounter[value];
    print(str(dcounter[value]) + " " + str(value) + " : " + str(fprice[value]*dcounter[value]))

  print("total : " + str(price_f))
  print("discount price : " + str(discounted_price(price_f,10,minprice=100)))