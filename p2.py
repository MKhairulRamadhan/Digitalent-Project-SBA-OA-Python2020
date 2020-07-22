# nama file p1.py 
# Isikan email anda dan copy semua cell code yang dengan komentar #Graded
# Isikan juga priority file

# untuk resubmisi, grader hanya akan mengambil priority yang paling besar
# jadi kalau anda ingin merevisi kode anda:
# silakan di resubmit dengan nilai variable priority yang lebih besar dari
# nilai priority submisi sebelumnya
# JIKA TIDAK ADA VARIABLE priority DIANGGAP priority=0

priority = 1


#netacad email cth: 'abcd@gmail.com'
email='khairulr59@gmail.com'

# copy-paste semua #Graded cells di bawah ini

# PASTE KODE ANDA DISINI 
#Graded

import math
import random
#Graded

def isPointInCircle(x,y,r,center=(0,0)):
  # MULAI KODEMU DI SINI
  pass
  return ((((x - center[0])**2) + ((y - center[1])**2)) <= (r**2))


  #Graded

def generateRandomSquarePoints(n,length,center=(0,0)):
  # MULAI KODEMU DI SINI
  minx = center[0]-length/2
  miny = center[1]-length/2

  maxx = center[0]+length/2
  maxy = center[1]+length/2
  
  list2 = []
  # Gunakan list comprehension dengan variable minx, miny, length, dan n
  for i in range(n):
    data1 = random.uniform(minx, maxx)
    data2 = random.uniform(miny, maxy)

    list2.append([data1,data2])

  points = list2

  return points

  #Graded

def MCCircleArea(r,n=100,center=(0,0)):
  # MULAI KODEMU DI SINI
  pass
  hitung = 0;
  points = generateRandomSquarePoints(n,(r*2))
  for data in points:
    if isPointInCircle(data[0],data[1],r,center=(0,0)):
      hitung += 1

  luas = (hitung/n)*((r*2)*(r*2))
  return luas

  #Graded

def LLNPiMC(nsim,nsample):
  # MULAI KODEMU DI SINI
  pass
  pi = 0
  for i in range(nsim):
    luas = MCCircleArea(1,nsample,center=(0,0))
    pi += luas

  return pi/nsim

  # Graded
  
def relativeError(act,est):
  
  # MULAI KODEMU DI SINI
  pass
  error = abs((est-act)/act)*100
  return error