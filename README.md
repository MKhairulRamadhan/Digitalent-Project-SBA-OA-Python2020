# Digitalent-Project-SBA-OA-Python2020
### P3
1. Buatlah fungsi caesar_encript, dengan argumen txt (string) dan shift (intiger) seperti dibawah ini. Yang melakukan peng-ekripsian menggunakan metode Caesar terhadap string txt. Keluaran dari fungsi ini berupa string terenkripsi / chiper text.

hint: method yang mungkin berguna:

    ord(), chr()
    string method: .isalpha(), .islower(), dll
    jumlah karakter abjad 26
    nilai ord dari abjad/huruf berurutan

2. Buatlah fungsi deshuffle_order, dengan argument sftxt (string) dan order (list). Yang akan mengembalikan urutan string kembali seperti semula sebelum di-shuffle. Sedemikian hingga:

deshuffle_order(shuffle_order(txt,order),order) == txt

hint: list method .index()

3. Buatlah fungsi send_batch dengan argument txt (string), batch_order (list), dan shift (int). Fungsi ini akan memecah text menjadi bagian-bagian yang lebih kecil sesuai dengan panjang dari batch_order, di mana batch_order tersebut merupakan list index untuk men-shuffle setiap batch dengan menggunakan fungsi di nomor 2. Keluaran fungsi ini berupa list batch teks terenkripsi.

Note: tambahkan underscore di akhir (sebelum dipecah menjadi batches) jika panjang txt belum memenuhi kelipatan panjang satu batch yaitu len(batch_order).

Hint: Lihat intro 3 dan gambar, gunakan library math jika diperlukan

### p2 :Monte Carlo
1. Buatlah sebuah fungsi isPointInCircle dengan posisional argument x,y,r dan keyword argument center dengan default value sebuah tupple dua nilai (0,0). Untuk menentukan apakah titik (x,y) berada di dalam atau di luar lingkaran L(center,r). Keluaran fungsi isPointInCircle merupakan suatu nilai boolean, True Jika titik (x,y) berada di dalam lingkaran dan False Jika berada di luar.

Note: titik yang berada tepat di lingkaran dikategorikan sebagai dalam, maka True.

2. generateRandomSquarePoints dengan dua positional argumen n dan length, dan keyword argument center default: tupple(0,0). Fungsi ini akan mengeluarkan suatu list dengan jumlah n titik random [x,y] yang berada di dalam suatu kotak persegi dengan panjang length dan titik tengah center. Keluaran fungsi merupakan list dari n titik random [x,y], cth: [[x1,y1],...,[xn,yn]].

hint:

    Jarak titik tengah center ke tepi persegi sama dengan length/2.
    Untuk menghasilkan nilai random, gunakan random.uniform, penjelasan random.uniform. Untuk menentukan nilai a dan b dari fungsi random.uniform, coba perhatikan gambar di cell bawah dengan center=(0,0). Note: harus fleksible ketika titik center berubah.
    Gunakan list comprehension untuk men-generate n titik x,y tersebut.
    Untuk menyelesaikan hanya butuh ubah satu baris kode, ganti None value, dengan kode anda.

3. Buatlah fungsi MCCircleArea dengan positional argument r dan keyword argument dengan default n=100 dan center=(0,0), untuk menghitung luas lingkaran dengan jari-jari r dengan mengestimasi dari n titik random. Keluaran fungsi merupakan suatu nilai yang menunjukkan estimasi luas lingkaran tersebut.

hint:

    gunakan fungsi yang sudah dibuat di atas isPointInCircle dan generateRandomSquarePoints.
    perhatikan gambar lingkaran dan persegi di atas, jari-jari r lingkaran sama dengan setengah dari panjang sisi persegi.
    lingkaran dan persegi memiliki pusat yang sama.


4. Buatlah fungsi LLNPiMC untuk mengestimasi nilai pi dengan positional argumen nsim dan nsample. nsample merupakan jumlah sample titik-titik random untuk menghitung luas lingkaran berjari-jari 1 (maka Luas = π) dan nsim merupakan jumlah simulasi untuk menghitung nilai rata-rata atau mean dari estimasi nilai π. Keluaran fungsi merupakan nilai mean dari simulasi tersebut (estimasi nilai π).

5. Buatlah fungsi relativeError, dengan argument act yang merupakan nilai aktual, dan est yang merupakan nilai estimasi.


