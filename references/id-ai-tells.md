# Tell AI dalam Teks Bahasa Indonesia

Modul referensi untuk skill `humanizer-indonesia`. Dimuat hanya ketika teks masukan berbahasa
Indonesia. Katalog skill `humanizer` (skill asal) diturunkan dari pola bahasa Inggris dan tidak
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

Ambang: jika lebih dari 1 konstruksi verba ringan per 100 kata, tandai.

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

### A6. Preposisi yang menghilangkan subjek

Kalimat dibuka *Dalam*, *Pada*, atau *Bagi*, lalu langsung disusul verba aktif. Frasa
pembukanya menjadi keterangan, sehingga kalimat itu tidak lagi punya subjek. Kesalahan ini
lazim pada tulisan manusia maupun keluaran model, dan sering muncul ketika dua kalimat
digabung tanpa membaca ulang.

**Sebelum:** Dalam penelitian ini menunjukkan bahwa sistem dapat menyimpan berkas.

**Sesudah:** Penelitian ini menunjukkan bahwa sistem dapat menyimpan berkas. Jika
keterangannya ingin dipertahankan, pakai pasif: Dalam penelitian ini ditunjukkan bahwa ...

Bentuk yang sudah bersubjek (*Pada penelitian ini, kami menunjukkan ...*) tidak disunting.
`scripts/metrik.py` menghitungnya sejak 7 November 2026.

### A7. Konjungsi berpasangan

Konjungsi subordinatif di anak kalimat tidak dipasangkan lagi dengan konjungsi di induk
kalimat. Pola *Meskipun ..., tetapi ...*, *Walaupun ..., namun ...*, dan *Karena ...,
maka ...* adalah kalke dari kebiasaan bahasa daerah atau dari *although ..., but ...*.
Pilih salah satu konjungsinya.

**Sebelum:** Meskipun akurasinya tinggi, tetapi galat masih muncul pada data minoritas.

**Sesudah:** Meskipun akurasinya tinggi, galat masih muncul pada data minoritas.

*Jika ..., maka ...* sengaja tidak dihitung karena lazim pada rumusan matematika dan logika.

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

Uji: hapus frasanya. Jika maknanya utuh, buang.

Pada register akademik, *mengupas* dan *mengupas tuntas* bernada jurnalistik. Pakai
*membahas* atau *menguraikan*.

### B3. Kosakata bergengsi tanpa fungsi

*mengoptimalkan* (untuk hal yang tidak dioptimasi), *mengimplementasikan* (untuk
"memakai"), *merealisasikan*, *mengakomodasi*, *holistik*, *komprehensif*, *signifikan*
di luar konteks statistik, *krusial*, *esensial*, *fundamental*, *masif*.

Catatan: dalam teks teknis, *signifikan* dengan nilai-p adalah pemakaian sah. Jangan
diratakan.

### B4. Modalitas bertumpuk dan derajat kepastian yang bergeser

Satu klausa cukup membawa satu penanda ketidakpastian. *mungkin dapat berpotensi
menurunkan* dipadatkan menjadi *berpotensi menurunkan* atau *dapat menurunkan*, dipilih
sesuai tingkat buktinya.

Derajat kepastian kira-kira berjenjang begini. Fakta empiris memakai *menunjukkan* dan
*menghasilkan*, inferensi memakai *mengindikasikan* dan *berkorelasi dengan*, sedangkan
hipotesis memakai *diduga*, *diproyeksikan*, dan *berpotensi*. Penyuntingan tidak boleh
menggeser jenjang itu ke arah mana pun. *Mengindikasikan* tidak diganti *membuktikan*,
*diharapkan dapat membantu* tidak diganti *terbukti membantu*, dan hasil pengujian yang
sudah terukur tidak diturunkan menjadi *diduga menunjukkan*. Jika jenjang aslinya keliru
terhadap datanya, catat di poin konfirmasi (Langkah 8 SKILL.md) dan biarkan penulis yang
memutuskan.

### B5. Otoritas tanpa rujukan dan klaim mutlak

*Banyak peneliti sepakat bahwa ...*, *para ahli menyatakan ...*, dan *berbagai studi
menunjukkan ...* tanpa satu sitasi pun adalah cara model menyatakan klaim umum dengan nada
berwibawa. Jangan mengarang sitasinya. Pindahkan ke poin konfirmasi dengan catatan bahwa
klaim itu perlu rujukan, atau ubah menjadi klaim yang memang dapat ditanggung naskahnya.

Hal yang sama berlaku untuk kata mutlak *pasti*, *selalu*, *tidak pernah*, dan *tanpa
cacat* yang tidak disertai data.

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

Bahasa Indonesia mengalir jika tiap kalimat dibuka dengan informasi yang sudah dikenal
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
dan akurat*; *aman, nyaman, dan andal*. Jika ketiganya tidak membawa informasi berbeda,
sisakan satu.

Pada teks ajar dan teks teknis, ketiga butir sering sama-sama bermakna, dan GPTZero tetap
menandainya sebagai *Everything in threes*. Bab 9 diktat perubahan iklim (31 Oktober 2026)
ditandai empat kali walaupun tidak satu butir pun yang kosong. Daftar tiga butir semacam
itu ditangani dengan salah satu dari empat tindakan berikut, seluruhnya diambil dari kasus
Bab 9 itu.

| Tindakan | Sebelum | Sesudah |
|---|---|---|
| Buang butir yang tidak membawa informasi baru | *efektif, efisien, dan berkelanjutan* | sisakan satu, atau ganti dengan angka |
| Nyatakan hierarki yang tersembunyi | menjelaskan peran atmosfer, sirkulasi udara, dan arus laut di dalam sistem iklim bumi | menjelaskan peran atmosfer dan laut di dalam sistem iklim bumi, termasuk sirkulasi udara dan arus laut |
| Pindahkan butir yang hubungannya berbeda ke kalimat sendiri | dapat dipicu oleh berkurangnya gas rumah kaca, letusan gunung api besar, atau perubahan aktivitas matahari | Dalam sejarah bumi, pendinginan semacam itu pernah dipicu oleh letusan gunung api besar atau perubahan aktivitas matahari. Berkurangnya gas rumah kaca di atmosfer juga dapat memicunya. |
| Pecah kompetensi yang digabung dan sebut urutan kerjanya | Menjelaskan peran penggunaan energi sebagai sumber utama emisi, menghitung emisi CO2 dari pembakaran bahan bakar, dan menguraikan pertumbuhan emisi dengan identitas Kaya. | 4. Menjelaskan peran penggunaan energi sebagai sumber utama emisi. 5. Menghitung emisi CO2 dari pembakaran bahan bakar, lalu menguraikan pertumbuhannya dengan identitas Kaya. |

Pada contoh kedua, sirkulasi udara adalah bagian dari atmosfer dan arus laut bagian dari
laut, sehingga daftar aslinya memang tidak sejajar. Menyatakan hierarkinya menghapus
triplet sekaligus membuat isinya lebih tepat. Pada contoh keempat, jika capaian
pembelajaran diambil dari RPS, pemecahannya ikut mengubah RPS dan menjadi keputusan
penulis.

**Deret sejajar.** Deret empat butir yang kata pertamanya berbentuk seragam juga ditandai,
misalnya *meningkatnya suhu udara, berubahnya curah hujan, naiknya muka air laut, dan
meningkatnya intensitas kejadian ekstrem*. Pecah bentuknya menjadi klausa yang berpasangan:
*Suhu udara dan muka air laut naik, sementara pola curah hujan berubah dan intensitas
kejadian ekstrem meningkat.* Jika deret itu dirujuk kembali dengan nomor (*fenomena
keempat*), jadikan daftar bernomor.

**Yang tidak ditandai dan tidak perlu disunting.** Daftar istilah empat butir ke atas yang
bentuknya beragam, misalnya *cuaca, iklim, pemanasan global, dan perubahan iklim* atau
*suhu, curah hujan, angin, muka air laut, dan kejadian ekstrem*, lolos dari GPTZero pada
bab yang sama. Daftar panjang semacam itu juga kebiasaan penulis (bagian 2.2
`voice-prib-id.md`).

`scripts/metrik.py` menghitung triplet dan deret sejajar sebagai diagnostik tanpa ambang.
Setelah perbaikan 31 Oktober 2026, temuan skrip sama persis dengan GPTZero pada tiga teks
yang sudah dipindai: Bab 9 empat lawan empat, esai FCEV nol lawan nol, dan tulisan opini
penulis satu lawan satu. Tetap tinjau tiap temuan sebelum menyunting.

**Triplet adalah soal frekuensi.** Penulis sendiri menulis triplet secara otomatis
(*seperti panas bumi, solar, dan angin*) pada tulisan opini tanpa AI yang mendapat human
98 persen. GPTZero memberi label *1.6x more likely used by AI*, yang berarti manusia juga
memakainya, hanya lebih jarang. Patokan sementara dari tulisan itu adalah sekitar 1,5
triplet per 1.000 kata. Angka ini baru berasal dari satu teks, jadi tentatif. Yang
ditangani adalah gerombolan triplet, seperti empat temuan dalam sekitar 200 kata pada
potongan Bab 9, bukan satu triplet yang muncul sesekali.

### D4. Enumerasi bersandar *seperti*

Model gemar memasang contoh berderet di belakang kata *seperti*, *antara lain*,
*misalnya*, *di antaranya*, dan *seperti halnya*. Hasilnya kalimat gemuk yang isinya
sebenarnya satu gagasan.

Bedakan dua fungsi, karena hanya satu yang perlu disunting:

| Fungsi | Contoh | Tindakan |
|---|---|---|
| Enumerasi | Bahan bubuk seperti sodium sulfat, NaCl, EDTA 4NA, dan sitrus | tandai, pertimbangkan bentuk lain |
| Komparatif atau rujukan | seperti yang ditunjukkan pada Gambar 2 | **biarkan**, ini konstruksi sah |

Penggantinya bergantung isi. Jika daftarnya penting dan paralel, pakai daftar bernomor
terpisah. Jika hanya ilustrasi, sebut satu contoh terkuat lalu buang sisanya. Jika
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

### D8. Kalimat pembuka penanda arah

Kalimat pembuka paragraf yang hanya mengumumkan topik, misalnya *Kemudian ada tantangan
infrastruktur.* atau *Peluang yang menurut saya paling kuat datang dari sumber energinya.*
Isinya dapat dihapus tanpa ada informasi yang hilang. Pada esai FCEV (26 Oktober 2026),
kalimat semacam ini menjadi sumber kalimat AI terbanyak, termasuk yang sudah dibuka kata
penghubung. Satukan dengan fakta pertama paragraf itu. Pola ini kerabat dekat D5, dan
`scripts/metrik.py` belum menghitungnya.

### D6. Penomoran dan bullet yang tidak perlu

Teks AI memecah prosa jadi daftar bahkan ketika hubungan antarbutirnya naratif. Dalam
buku ajar dan jurnal, gabungkan kembali jadi paragraf kecuali butirnya memang paralel.

### D9. Sitasi formulaik

Model merangkai sitasi dengan pola yang sama berulang kali: *Menurut Santoso (2020) ...
Senada dengan itu, Wijaya (2021) ... Menurut Nugroho (2022) ...*. Tiap kalimat dibuka nama
peneliti, dan hubungan antartemuan hanya dinyatakan lewat *senada* atau *sejalan*.

Fokuskan kalimat pada temuannya, lalu pindahkan nama dan tahun ke dalam kurung. Rujukan
yang menyatakan hal yang sama digabung dalam satu kurung, misalnya *(Santoso, 2020; Wijaya,
2021)*. Jika temuannya berbeda, sebut perbedaannya, karena di situlah sintesisnya.

Yang boleh diubah hanya posisi sitasi di dalam kalimat. Isi temuan, nama, tahun, dan
urutan rujukan dibawa utuh, sesuai prinsip dasar nomor 2 di SKILL.md. Gaya naratif yang
dipakai konsisten dan memang diminta jurnal dibiarkan (F8).

`scripts/metrik.py` menghitung frasa *senada dengan itu* dan kerabatnya, serta kalimat
berpola *Menurut Nama (tahun)* jika jumlahnya tiga atau lebih.

### D10. Rujukan spasial semu

*Dapat dilihat pada tabel di bawah ini* dan *Berdasarkan grafik di atas* menunjuk posisi,
padahal posisi tabel dan gambar berpindah ketika tata letak berubah. Rujuk dengan nomor:
*Tabel 4.2 menyajikan ...*, atau *Hasil pengujian (Gambar 3.1) menunjukkan ...*.

Jika naskah aslinya belum memberi nomor, **jangan mengarang nomornya.** Tulis catatan di
poin konfirmasi, misalnya "tabel hasil pengujian belum bernomor, beri nomor lalu rujuk",
dan biarkan penulis menetapkannya.

### D11. Residu percakapan dan format dekoratif

Sisa percakapan model yang ikut tersalin ke naskah: *Tentu, berikut draf revisinya*,
*Semoga membantu*, *Jangan ragu untuk ...*. Hapus seluruhnya. Pada teks akademik dan
laporan resmi, emoji, simbol dekoratif, dan cetak tebal acak di tengah paragraf juga
dibuang. Cetak tebal hanya untuk istilah yang sedang didefinisikan.

Judul bagian berbentuk pertanyaan retoris atau bergaya artikel populer (*Mengapa Timbal?
Jawabannya Mengejutkan*) diganti frasa deskriptif berbasis topik, kecuali registernya
memang populer.

### D12. Rentang semu

*mulai dari X hingga Y* hanya sah jika X dan Y memang ujung suatu spektrum yang nyata,
misalnya rentang daya atau rentang suhu. Jika X dan Y hanya dua contoh yang tidak berada
pada satu skala, sebut keduanya secara langsung. `scripts/metrik.py` menghitungnya sebagai
diagnostik, dan sebagian besar temuan pada teks teknis sah.

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

**F8. Sitasi naratif yang menjadi konvensi jurnal.** Jika penulis memakai *Nugroho (2022)
menemukan ...* secara konsisten dan gaya itu yang diminta jurnal, D9 tidak dijalankan.

**F9. Kesejajaran gramatikal di dalam daftar.** Butir satu daftar memang harus berbentuk
sama secara tata bahasa. *mengumpulkan data, analisis hasil, dan menguji model* keliru
karena mencampur nomina dengan verba. Ini tidak bertentangan dengan deret sejajar di D3:
yang ditandai D3 adalah deret empat butir ke atas yang dibuka nominalisasi seragam
(*meningkatnya ..., berubahnya ...*), dan perbaikannya mengubah deret itu menjadi klausa
sehingga bentuk butirnya tetap sejajar.

**F10. Partikel *pun* pada konjungsi baku.** *meskipun*, *walaupun*, *kendatipun*,
*maupun*, *adapun*, *bagaimanapun*, dan *sekalipun* (sebagai konjungsi) ditulis serangkai.
Hanya *pun* sesudah kata tanya dan nomina yang ditulis terpisah: *apa pun*, *siapa pun*,
*data ini pun*.


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
