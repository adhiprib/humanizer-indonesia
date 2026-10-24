# Tell AI dalam Teks Bahasa Indonesia

Modul referensi untuk skill `humanizer`. Dimuat hanya ketika teks masukan berbahasa
Indonesia. Katalog di SKILL.md induk diturunkan dari pola bahasa Inggris dan tidak
berlaku di sini. Jangan mencari em dash, "vibrant tapestry", atau rule of three versi
Inggris pada teks Indonesia.

Aturan format: modul ini dan seluruh keluaran penyuntingan **tidak boleh memuat em dash
(U+2014) maupun en dash (U+2013)**. En dash hanya diizinkan pada rentang angka di dalam
daftar pustaka, misalnya nomor halaman 189-194. Di badan prosa, gunakan koma, titik dua,
tanda kurung, atau pecah jadi dua kalimat.

Prinsip kerja: **kekakuan teks Indonesia jarang disebabkan oleh kesalahan tata bahasa.**
Hampir selalu penyebabnya adalah kepadatan nominalisasi, kohesi yang digantung pada
konektor, dan keseragaman ritme kalimat. Perbaiki tiga hal itu lebih dulu sebelum
menyentuh diksi.

---

## A. Sintaksis

### A1. Nominalisasi berlebih (penyebab kekakuan nomor satu)

Verba diubah jadi nomina, lalu dipasangkan dengan verba ringan (*melakukan*,
*memberikan*, *mengalami*, *melaksanakan*). Kalimat jadi panjang tanpa menambah makna.

| Kaku | Wajar |
|---|---|
| melakukan pengukuran terhadap | mengukur |
| melakukan analisis terhadap | menganalisis |
| memberikan pengaruh terhadap | memengaruhi |
| mengalami peningkatan sebesar | naik |
| melaksanakan pengujian | menguji |
| melakukan perbandingan antara | membandingkan |
| memberikan kontribusi terhadap | menyumbang, berperan dalam |

**Sebelum:** Penelitian ini melakukan pengukuran terhadap laju perpindahan kalor yang
mengalami peningkatan sebesar 12%.

**Sesudah:** Laju perpindahan kalor yang terukur naik 12%.

Ambang: bila lebih dari 1 konstruksi verba ringan per 100 kata, tandai.

### A2. Pasif refleks

Bahasa Indonesia ilmiah memang banyak memakai pasif, dan itu sah (lihat F1). Yang
menjadi tell adalah pasif yang dipakai ketika pelakunya jelas dan aktif terasa lebih
wajar, terutama pola *dilakukan*, *dilaksanakan*, *diperoleh*, *ditunjukkan* yang
menumpuk dalam satu paragraf.

**Sebelum:** Simulasi dilakukan dengan menggunakan perangkat lunak OpenFOAM. Hasil
diperoleh setelah iterasi konvergen. Grafik ditampilkan pada Gambar 3.

**Sesudah:** Simulasi memakai OpenFOAM. Setelah iterasi konvergen, hasilnya tampak pada
Gambar 3.

### A3. *yang mana* dan *dimana* sebagai pronomina relatif

Keduanya kalke dari *which* dan *where*. Dalam bahasa Indonesia baku, *yang mana* hanya
sah dalam kalimat tanya pilihan ("Yang mana yang Anda pilih?"), dan *di mana* hanya sah
sebagai keterangan tempat yang sesungguhnya, ditulis terpisah.

**Sebelum:** Pengujian dilakukan pada suhu 85°C, dimana nilai CHF mulai teramati.

**Sesudah:** Pengujian dilakukan pada suhu 85°C. Pada suhu itu nilai CHF mulai teramati.

Pengecualian penting: dalam dokumen paten dan kontrak, *dimana* adalah bagian dari
formula baku yang tidak boleh diubah. Lihat G1.

**Sebelum:** Sistem menggunakan pendingin alami, yang mana hal ini mengurangi konsumsi
daya.

**Sesudah:** Sistem menggunakan pendingin alami sehingga konsumsi dayanya turun.

### A4. Keseragaman panjang kalimat

Teks AI berbahasa Indonesia cenderung menghasilkan kalimat 20 sampai 28 kata secara terus
menerus dengan struktur yang sama (Subjek, *merupakan* atau *adalah*, predikat nominal).
Tulisan manusia berganti-ganti: kalimat 8 kata lalu 30 kata lalu 14 kata.

Ukur simpangan baku panjang kalimat. Di bawah 6 kata, ritmenya datar dan perlu dipecah.

### A5. *merupakan* sebagai kopula default

Sah untuk definisi sejati. Menjadi tell ketika muncul di setiap kalimat pembuka
paragraf, atau ketika kalimatnya sebenarnya punya verba sendiri.

**Sebelum:** Konveksi merupakan mekanisme perpindahan kalor yang melibatkan pergerakan
fluida.

**Sesudah (definisi, biarkan):** Konveksi adalah perpindahan kalor yang melibatkan
pergerakan fluida.

**Sebelum:** Hal ini merupakan penyebab terjadinya penurunan efisiensi.

**Sesudah:** Efisiensinya turun karena hal ini.

---

## B. Leksikal

### B1. Pleonasme

*adalah merupakan*, *agar supaya*, *demi untuk*, *sangat ... sekali*, *banyak faktor-faktor*,
*para hadirin sekalian*, *saling bertukar satu sama lain*, *naik ke atas*, *turun ke bawah*,
*sejak dari*, *disebabkan karena*.

### B2. Intensifier dan frasa kosong

*sangat penting*, *tidak dapat dipungkiri*, *memegang peranan penting*, *menjadi kunci
utama*, *menjadi faktor kunci*, *berperan vital*, *aspek vital*, *tak lepas dari*,
*semakin krusial*, *patut diperhatikan*, *menjadi sorotan*, *di tengah derasnya*.

Uji: hapus frasanya. Bila maknanya utuh, buang.

Pada register akademik, *mengupas* dan *mengupas tuntas* bernada jurnalistik. Pakai
*membahas* atau *menguraikan*.

### B3. Kosakata bergengsi tanpa fungsi

*mengoptimalkan* (untuk hal yang tidak dioptimasi), *mengimplementasikan* (untuk
"memakai"), *merealisasikan*, *mengakomodasi*, *holistik*, *komprehensif*, *signifikan*
di luar konteks statistik, *krusial*, *esensial*, *fundamental*, *masif*.

Catatan: dalam teks teknis, *signifikan* dengan nilai-p adalah pemakaian sah. Jangan
diratakan.

---

## C. Kohesi, sumber utama rasa tersendat

### C1. Konektor bertumpuk

Tell paling khas. Setiap paragraf dibuka konektor: *Selain itu*, *Namun demikian*,
*Di sisi lain*, *Oleh karena itu*, *Oleh sebab itu*, *Lebih lanjut*, *Dengan demikian*.

Bahasa Indonesia yang mengalir menyambung kalimat lewat **pengulangan kata kunci** dan
**klitik -nya**, bukan lewat konektor. Konektor dipakai hanya ketika hubungan logisnya
benar-benar tidak dapat ditebak dari urutan.

**Sebelum:**
> Chimney menghasilkan draft alami. Selain itu, laju alirannya bergantung pada tinggi
> cerobong. Di sisi lain, temperatur dinding juga berpengaruh. Oleh karena itu,
> keduanya harus diperhitungkan.

**Sesudah:**
> Chimney menghasilkan draft alami. Besarnya bergantung pada tinggi cerobong dan
> temperatur dinding, sehingga keduanya harus masuk perhitungan.

Ambang: lebih dari 3 konektor antarkalimat per 100 kata, atau lebih dari separuh
paragraf dibuka konektor, tandai.

### C2. Informasi baru diletakkan di depan

Bahasa Indonesia mengalir bila tiap kalimat dibuka dengan informasi yang sudah dikenal
pembaca dari kalimat sebelumnya. Teks AI sering membalik urutan itu, dan hasilnya terasa
melompat meski tata bahasanya benar.

**Sebelum:** Efisiensi termal meningkat pada konfigurasi tapered. Penyempitan penampang
di bagian atas cerobong menyebabkan hal tersebut.

**Sesudah:** Efisiensi termal meningkat pada konfigurasi tapered. Kenaikannya berasal
dari penyempitan penampang di bagian atas cerobong.

---

## D. Struktur wacana

### D1. Formula pembuka

*Seiring dengan perkembangan teknologi yang semakin pesat*, *Di era digital saat ini*,
*Dalam dunia yang serba cepat*, *Tidak dapat dipungkiri bahwa*, *Sebagaimana kita ketahui
bersama*.

Ganti dengan pernyataan spesifik yang langsung masuk ke pokok bahasan.

### D2. Formula penutup

*Dengan demikian, dapat disimpulkan bahwa*, *Sebagai penutup*, *Pada akhirnya*, ditambah
kalimat yang mengulang judul dan menyebut sesuatu itu *sangat penting*.

### D3. Triplet

Versi Indonesia dari rule of three: *efektif, efisien, dan berkelanjutan*; *cepat, tepat,
dan akurat*; *aman, nyaman, dan andal*. Bila ketiganya tidak membawa informasi berbeda,
sisakan satu.

### D4. Enumerasi bersandar *seperti*

Model gemar memasang contoh berderet di belakang kata *seperti*, *antara lain*,
*misalnya*, *di antaranya*, dan *seperti halnya*. Hasilnya kalimat gemuk yang isinya
sebenarnya satu gagasan.

Bedakan dua fungsi, karena hanya satu yang perlu disunting:

| Fungsi | Contoh | Tindakan |
|---|---|---|
| Enumerasi | Bahan bubuk seperti sodium sulfat, NaCl, EDTA 4NA, dan sitrus | tandai, pertimbangkan bentuk lain |
| Komparatif atau rujukan | seperti yang ditunjukkan pada Gambar 2 | **biarkan**, ini konstruksi sah |

Penggantinya bergantung isi. Bila daftarnya penting dan paralel, pakai daftar bernomor
terpisah. Bila hanya ilustrasi, sebut satu contoh terkuat lalu buang sisanya. Bila
seluruh anggota memang perlu, jadikan objek langsung tanpa *seperti*: "Bahan bubuknya
sodium sulfat, NaCl, EDTA 4NA, dan sitrus."

Ambang: lebih dari 1 enumerasi *seperti* per 1.000 kata sudah di atas kebiasaan penulis.

### D5. Topic sentence di setiap paragraf

Tiap paragraf dibuka kalimat tesis eksplisit, lalu tiga kalimat pendukung, lalu kalimat
simpul. Polanya terlalu rapi. Manusia sering langsung masuk ke detail dan membiarkan
kesimpulannya tersirat.

### D7. Penyangkalan antisipatif

Pola *X, bukan berarti Y*, *Ini bukan berarti ...*, *bukan sekadar X, melainkan Y*, dan
*bukan X, melainkan Y* di ujung kalimat. Teks model menyangkal kesimpulan yang tidak pernah
diajukan pembaca, lalu menyelipkan maksud sebenarnya lewat kontras. Penulis menilai pola ini
sebagai AI slop yang paling mudah dikenali (24 Oktober 2026). Nyatakan isinya secara
positif. Sasaran nol per dokumen, dan `scripts/metrik.py` menghitungnya.

### D6. Penomoran dan bullet yang tidak perlu

Teks AI memecah prosa jadi daftar bahkan ketika hubungan antarbutirnya naratif. Dalam
buku ajar dan jurnal, gabungkan kembali jadi paragraf kecuali butirnya memang paralel.

---

## E. Uji baca cepat

Jalankan sebelum dan sesudah penyuntingan:

| Metrik | Ambang mencurigakan |
|---|---|
| Rerata panjang kalimat | lebih dari 24 kata |
| Simpangan baku panjang kalimat | kurang dari 6 kata |
| Konektor antarkalimat per 100 kata | lebih dari 3 |
| Konstruksi verba ringan per 100 kata | lebih dari 1 |
| Paragraf dibuka konektor | lebih dari 50% |
| Rasio pasif | lebih dari 60% di luar bagian Metode |
| Enumerasi *seperti* per 1.000 kata | lebih dari 1 |
| Em dash atau en dash di badan prosa | lebih dari 0 |

---

## F. Jangan ditandai (positif palsu khas Indonesia)

**F1. Pasif dalam teks ilmiah.** Bagian Metode dan Hasil memang lazim pasif, dan itu
konvensi disiplin, bukan tell. Yang ditandai hanya pasif di luar konteks itu.

**F2. Istilah teknis serapan.** *Konveksi*, *entalpi*, *konduktivitas*, *turbulensi*
adalah istilah baku. Jangan diganti padanan yang lebih jarang dipakai.

**F3. Kalimat panjang dalam teks hukum dan regulasi.** Dokumen akreditasi, kurikulum,
dan peraturan memang berkalimat panjang karena harus presisi.

**F4. Ejaan yang rapi dan konsisten.** Penulis akademik terlatih menulis rapi.

**F5. *merupakan* pada definisi sejati.** Lihat A5.

**F6. *seperti yang* sebagai penanda rujukan.** Lihat D4. Konstruksi ini justru lazim
dalam penulisan ilmiah untuk menunjuk gambar, tabel, dan penelitian terdahulu.

**F7. Register formal itu sendiri.** Bahasa Indonesia akademik memang lebih formal
daripada bahasa Inggris akademik. Sasarannya bukan membuat jurnal terdengar seperti blog,
melainkan menghilangkan padding sambil mempertahankan register.


---

## G. Register yang dikecualikan seluruhnya

Pada jenis dokumen berikut, **jangan jalankan modul ini sama sekali**. Konstruksi yang di
tempat lain dianggap tell justru merupakan syarat sah dokumennya, dan menyuntingnya
menimbulkan kerugian nyata.

**G1. Paten dan dokumen kekayaan intelektual.** Frasa *Invensi ini mengenai*, *yang
dicirikan dengan*, *sesuai dengan klaim 1*, dan *dimana* adalah formula baku. Enumerasi
lengkap di belakang *seperti* pada bagian Klaim bukan gaya, melainkan penentu luas
perlindungan hukum: memangkasnya mempersempit klaim dan dapat merugikan pemohon.

**G2. Kontrak, peraturan, dan dokumen hukum lain.** Pengulangan istilah yang di prosa
biasa terasa kaku justru mencegah ambiguitas tafsir.

**G3. Kutipan langsung, judul, dan nama diri.** Tidak pernah disunting.

**G4. Instrumen penelitian yang sudah tervalidasi.** Butir kuesioner, skala Likert, dan
soal ujian yang sudah diuji validitasnya tidak boleh diubah kata-katanya, karena
perubahan redaksi membatalkan validasi.
