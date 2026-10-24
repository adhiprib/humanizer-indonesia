---
name: humanizer-indonesia
description: "Menyunting teks bahasa Indonesia agar tidak terbaca sebagai tulisan AI atau terjemahan, dan kembali ke gaya penulis. Juga untuk mengaudit berkas yang sudah disunting model lain. Trigger: /humanizer-id, humanize, rapikan bahasa, biar tidak kaku, lebih mengalir, cek gaya, audit hasil Gemini."
---

# Humanizer Indonesia

**Versi 1.5, 9 September 2026.** Untuk memastikan versi mana yang aktif, tanya saja
"humanizer-indonesia versi berapa" dan jawabannya diambil dari baris ini.

Riwayat singkat. 1.0 rilis awal. 1.1 memperbaiki deteksi verba ringan dan menambah
metrik kalimat panjang. 1.2 mengkalibrasi ulang seluruh ambang ke rentang korpus yang
sebenarnya, setelah terbukti ambang 1.0 dan 1.1 menghukum tulisan manusia penulis
sendiri, dan menetapkan bahwa suara penulis menang atas skor detektor. 1.3 menegaskan
posisi skill sebagai penyiap draf untuk disunting manusia, melengkapi matriks bukti
detektor tujuh pengukuran, dan mengoreksi rentang diagnostik kepadatan pemadat ke 73
sampai 139. 1.4 menambahkan Langkah 5b tentang kalkir dan diksi sebagai langkah wajib,
setelah satu bab diktat lulus sembilan dari sembilan metrik tetapi tetap terbaca sebagai
terjemahan, dan menambahkan bagian kaidah yang sering terlewat setelah aturan tanda
pisah terbukti keliru diterapkan sampai menghapus tanda hubung pada bentuk ulang.
1.5 menambahkan Langkah 5c tentang personifikasi, register kolokial, dan pembuka kalimat
monoton, menambahkan Langkah 5d tentang fusi kalimat terfragmentasi, menambahkan bagian
audit untuk berkas yang sudah disunting model lain, serta membetulkan ambang kepadatan
pemadat pada Langkah 7 yang masih tertulis 45 padahal seharusnya 73. Seluruh tambahan
itu lahir dari perbandingan langsung dua bab diktat versi Claude lawan versi Gemini pada
9 September 2026, ketika penulis menilai bahasa Indonesia versi Gemini lebih baik
sedangkan versi Gemini ternyata menghapus rujukan silang dan angka terverifikasi.

Skill ini menyunting teks berbahasa Indonesia agar terbaca sebagai tulisan manusia,
bukan keluaran model. Kerangka kerjanya diwarisi dari skill `humanizer`, yaitu putaran
draf, audit, lalu revisi akhir. Yang diganti adalah katalog polanya, karena tell AI
dalam bahasa Indonesia sama sekali berbeda dari tell dalam bahasa Inggris.

## Kapan skill ini dipakai

Batas 200 karakter pada kolom description membuat daftar pemicu tidak muat di sana.
Rinciannya di sini.

**Pakai skill ini bila user meminta salah satu dari berikut, dalam bahasa Indonesia:**

`/humanizer-id`, `/humanizer-id-cek`, humanize teks ini, rapikan bahasanya, biar tidak
kaku, buat lebih mengalir, terlalu terasa seperti AI, kurangi kesan AI, sesuaikan dengan
gaya tulisan saya, cek gaya tulisan, abstrak ini kaku, perbaiki bahasa paper, haluskan
kalimatnya, benerin tulisan ini, kalimatnya masih terasa terjemahan, diksinya kurang pas.

**Pakai juga bila user membawa berkas yang sudah disunting model lain**, misalnya
"perbaikan bahasa sudah saya lakukan dengan Gemini, coba periksa", "cek apakah sudah
sesuai humanizer", atau "audit hasil suntingan ini". Alur kerjanya berbeda, dan
langkahnya ada di bagian **Menerima berkas yang sudah disunting model lain**.

Berlaku untuk paper, abstrak, prosiding, proposal, buku ajar, modul, diktat, laporan,
dan surel berbahasa Indonesia.

**Jangan pakai skill ini bila:**

- Teksnya berbahasa Inggris. Arahkan ke skill `humanizer` biasa, yang katalognya memang
  berbasis pola bahasa Inggris.
- Dokumennya berupa paten, kontrak, peraturan, kutipan langsung, atau instrumen
  penelitian tervalidasi. Lihat bagian G di `references/id-ai-tells.md`.
- User hanya minta ringkasan, terjemahan, atau koreksi ejaan. Skill ini menulis ulang,
  dan menulis ulang bukan yang diminta di situ.

**Perintah dengan tanda garis miring.** Di Claude Code, `/humanizer-id` tersedia sebagai
perintah. Di claude.ai, perintah semacam itu tidak ada, tetapi mengetik `/humanizer-id`
di awal pesan tetap memicu skill ini karena frasa tersebut ada di kolom description.
Tambahkan nama berkas dan register setelahnya, misalnya
`/humanizer-id abstrak.docx preset akademik`.

## Apa yang bisa dan tidak bisa dilakukan skill ini

Skill ini menghasilkan **draf untuk disunting manusia**, bukan teks jadi yang setara
tulisan manusia. Pembedaan ini bukan kerendahan hati kosong, melainkan hasil pengukuran:
satu-satunya intervensi yang pernah menggerakkan skor detektor secara berarti adalah
suntingan tangan penulis (dari sekitar 1 persen ke 45 persen), sementara semua
penyetelan gaya otomatis, dari yang paling mampat sampai yang paling longgar, mendarat
di 1 sampai 2 persen.

Konsekuensinya untuk alur kerja: keluaran skill ini adalah **titik awal**. Nilainya ada
pada dua hal yang memang terbukti, yaitu teks yang metrik gayanya berada di pita korpus
penulis sehingga suntingan yang diperlukan lebih sedikit, dan laporan metrik yang
menunjukkan di mana teks masih menyimpang. Langkah terakhir, membaca dan menyunting
dengan tangan, tetap milik penulis, dan tidak ada versi skill ini yang akan
menghapusnya.

Bila teks akan diperiksa detektor, sunting dulu dengan tangan sebelum memindai, dan
baca bagian Detektor pihak ketiga di bawah.

## Prinsip dasar

**Metrik itu syarat perlu, bukan syarat cukup.** Ini pelajaran termahal dari versi 1.3.
Satu bab diktat lulus sembilan dari sembilan baris berambang, dengan simpangan baku 10,8
dan konektor 0,02 per 100 kata, dan penulisnya tetap menilai teksnya tidak mengalir.
Penyebabnya tidak terlihat oleh skrip mana pun: kalimatnya disusun dengan menerjemahkan
sumber bahasa Inggris klausa demi klausa. Karena itu **Langkah 5b sampai 5d bersifat
wajib, dan lulus seluruh metrik tidak pernah menjadi alasan untuk melewatinya.**

**Kekakuan teks Indonesia jarang berasal dari kesalahan tata bahasa.** Hampir selalu
penyebabnya enam hal: kepadatan nominalisasi, kohesi yang digantung pada konektor,
keseragaman ritme kalimat, kalkir dari bahasa Inggris, personifikasi benda mati beserta
diksi kolokial, dan pembuka kalimat yang berulang dengan pola yang sama. Perbaiki
keenamnya sebelum menyentuh hal lain.

Lima aturan yang tidak boleh dilanggar:

1. **Tulis ulang, jangan pangkas.** Kalau asli lima paragraf, hasil juga lima paragraf.
   Memadatkan teks bukan menghumanisasi, melainkan meringkas.
2. **Pertahankan makna dan angka.** Semua bilangan, satuan, rujukan gambar, rujukan
   persamaan, rujukan program, dan sitasi dibawa utuh. Jangan pernah mengganti angka
   dengan kata sifat samar, dan jangan pernah membuang rujukan silang hanya karena
   kalimat yang memuatnya sedang diringkas.
3. **Ikuti register.** Jurnal tetap terdengar seperti jurnal. Sasarannya membuang
   padding, bukan membuat paper terdengar seperti blog.
4. **Nol em dash dan en dash di badan prosa.** En dash hanya boleh sebagai rentang angka
   di daftar pustaka dan spesifikasi. **Aturan ini tidak berlaku untuk tanda hubung.**
   Lihat bagian Kaidah yang sering terlewat.
5. **Jangan memampatkan lebih ketat daripada penulisnya.** Ini aturan terpenting dan
   paling sering dilanggar. Prosa penulis membawa kelonggaran: *akan*, *untuk*, *dapat*,
   *suatu*, frasa yang tidak seringkas mungkin. Kelonggaran itu bagian dari suaranya,
   bukan cacat yang harus dibersihkan. Bila hasil suntingan lebih ringkas daripada
   korpus, penyuntingannya terlalu jauh.

## Alur kerja

### Langkah 1. Periksa kelayakan

Sebelum menyunting, pastikan tiga hal:

- Teksnya berbahasa Indonesia. Kalau Inggris, arahkan ke skill `humanizer`.
- Jenis dokumennya tidak termasuk register yang dikecualikan. Baca bagian G di
  `references/id-ai-tells.md`. Paten, kontrak, peraturan, kutipan langsung, dan
  instrumen penelitian tervalidasi **tidak disunting sama sekali**.
- Tentukan register sasaran: `akademik`, `ajar`, atau `semiformal`.

Tanyakan juga satu hal yang menentukan besar kecilnya pekerjaan: **apakah teks ini
disusun dari sumber berbahasa Inggris?** Slide kuliah, laporan lembaga, standar, dan
dokumen kebijakan hampir selalu iya. Bila iya, Langkah 5b menjadi bagian terbesar dari
pekerjaan, bukan langkah pelengkap.

### Langkah 2. Ukur teks masukan

```bash
python3 scripts/metrik.py berkas.md --preset akademik
```

Skrip ini melaporkan tujuh metrik berambang plus diagnostik tambahan. Catat baris mana
yang berstatus PERIKSA. Itu daftar kerja untuk langkah berikutnya.

Kalau tidak ada akses Bash, hitung manual dua yang paling menentukan: rerata panjang
kalimat dan simpangan bakunya.

### Langkah 3. Baca katalog

Baca `references/id-ai-tells.md` untuk pola yang harus dicari dan positif palsu yang
harus dibiarkan. Bagian F dan G sama pentingnya dengan bagian A sampai E: menyunting
yang seharusnya dibiarkan sama merusaknya dengan membiarkan tell lolos.

### Langkah 4. Kalibrasi suara

Bila tersedia contoh tulisan penulis, baca lebih dulu dan catat panjang kalimat, pilihan
kata, cara membuka paragraf, kebiasaan tanda baca, dan cara menangani transisi.

Untuk penulis PRIB, presetnya sudah tersedia di `references/voice-prib-id.md`. Baca
bagian 0 (asal dan tingkat kepercayaan korpus), bagian 1 (metrik sasaran), bagian 2
(penanda suara), dan bagian 3 (yang bukan suara ini).

Bila tidak ada contoh tulisan sama sekali, jangan mengarang kepribadian. Pakai suara
netral yang wajar untuk registernya, dan katakan terus terang bahwa kalibrasi suara
tidak dilakukan.

### Langkah 5. Draf

Tulis draf revisi. Sambil menulis, jaga hal berikut:

- Ritme berganti-ganti. Kalimat pendek, lalu panjang, lalu sedang.
- Kohesi lewat pengulangan kata kunci dan klitik `-nya`, bukan lewat konektor.
- Informasi lama di awal kalimat, informasi baru di akhir.
- Setiap klaim berpasangan dengan angka atau rujukan.

### Langkah 5b. Uji kalkir dan diksi (WAJIB)

Untuk setiap paragraf, ajukan satu pertanyaan: **kalimat bahasa Inggris apa yang ada di
balik kalimat ini?** Bila kalimat sumbernya dapat direkonstruksi klausa demi klausa,
kalimat itu belum ditulis dalam bahasa Indonesia, melainkan dialihbahasakan. Tulis ulang
gagasannya, bukan urutannya.

Enam pola kalkir yang paling sering muncul, seluruhnya dari kasus nyata:

| Pola | Contoh buruk | Perbaikan |
|---|---|---|
| Kolokasi salah pasang | menghormati batas planet (*respecting planetary boundaries*) | selaras dengan batas daya dukung bumi. Yang dihormati itu orang atau aturan, bukan batas fisik |
| Verba Inggris dipaksa berimbuhan me- | meredistribusi, meremanufaktur | redistribusi, remanufaktur, dijadikan nomina yang sejajar di dalam daftar |
| Kata bentukan yang tidak hidup | teknologi pemungkin (*enabling*), nilai tertanam (*embedded*) | teknologi pendukung utama; nilai yang sudah tertanam di dalam produk |
| Urutan Inggris dipertahankan utuh | mengedarkan produk dan material pada nilai tertingginya | menjaga produk dan material tetap beredar pada nilai tertingginya |
| Verba dasar diterjemahkan mentah | menghapus limbah (*eliminate*), meregenerasi alam (*regenerate*) | menghilangkan limbah; memulihkan alam |
| Istilah Inggris dibiarkan telanjang | secara on-demand | sesuai kebutuhan, atau *on demand* dimiringkan dengan padanan dalam kurung |

Tiga teknik yang terbukti mengubah paragraf terjemahan menjadi mengalir:

1. **Daftar didahului titik dua, bukan digantung pada "adalah".** "Enam teknologi
   pemungkin pada Gambar 3.12 adalah A, B, C" menjadi "Gambar 3.12 menyajikan enam
   teknologi pendukung utama: A, B, C".
2. **Biarkan verba bekerja.** Rangkaian *adalah*, *memungkinkan*, *merupakan* diganti
   verba yang menyebut tindakannya: menyajikan, memfasilitasi, merekam, memperpanjang.
3. **Pilih istilah yang hidup di lapangan.** *manufaktur aditif*, bukan *teknologi
   aditif*. *generasi berikutnya*, bukan *dan seterusnya*.

Empat rambu supaya perbaikan ini tidak berbalik merusak:

- **Jangan menukar kalkir dengan register birokratis.** "Sasaran itu kehilangan
  instrumen operasionalnya" tidak lebih baik daripada terjemahan harfiah. Sebut tempat
  atau tindakan yang bisa dibayangkan pembaca, misalnya lantai produksi.
- **Jangan menggabung beberapa kalimat menjadi satu kalimat panjang bertitik koma
  berantai.** Ritmenya rata dan simpangan bakunya turun. Pertahankan kalimat pendek
  sebagai penutup paragraf.
- **Periksa maknanya tidak ikut bergeser.** "Mempertahankan siklus material di dalam
  rantai nilai" bukan padanan "menjaga material tetap berada di dalam perekonomian":
  yang dijaga itu materialnya, bukan siklusnya, dan rantai nilai lebih sempit daripada
  perekonomian.
- **Verba yang lebih mengalir jangan sampai melebihkan klaim.** "Rantai blok menjamin
  ketertelusuran" melebihi kenyataannya; rantai blok merekam riwayat sehingga dapat
  ditelusuri, dan tidak menjamin isi catatannya benar. Pada teks teknis, ketepatan
  mengalahkan kelancaran.

Bila satu istilah dipakai berulang kali, putuskan istilahnya **sekali di depan** bersama
penulis, lalu terapkan ke seluruh dokumen dan dokumen bersaudaranya. Menggantinya satu
per satu sambil menyunting akan meninggalkan campuran istilah yang lebih kacau daripada
keadaan awal.

### Langkah 5c. Uji personifikasi, register, dan pembuka kalimat (WAJIB)

Tiga tell ini tidak terlihat oleh `scripts/metrik.py` sama sekali, dan ketiganya adalah
penanda paling kentara bahwa sebuah teks teknis ditulis model.

**1. Benda mati tidak punya watak.** Model, program, persamaan, algoritma, dan data
tidak malas, tidak berani, tidak cerewet, tidak tahu, dan tidak sakit. Ganti dengan
istilah rekayasa yang menyebut perilakunya secara terukur.

| Ditolak | Dipakai |
|---|---|
| model yang paling malas | model acuan naif (*baseline naive model*) |
| model berubah menjadi sangat cerewet | model bertindak lebih sensitif dalam mendeteksi |
| model menjadi lebih berani | model bertindak kurang selektif |
| persamaan tahu bahwa yang satu lebih mahal | fungsi biaya secara eksplisit memperhitungkan asimetri kerugian |
| penyakit model, model menderita ragam tinggi | kendala model, masalah generalisasi model |
| model menghafal jawaban | model mengalami memorisasi data alih-alih generalisasi |
| menaklukkan AND dan OR | mampu memisahkan ruang fitur secara linear pada AND dan OR |
| XOR menceritakan hal yang sama sekali lain | kegagalan representasi batas keputusan linear pada XOR |
| tumpukan sedalam apa pun runtuh | degradasi komposisi matriks linear |
| tidak ada hal yang gaib di dalamnya | komposisi fungsi parametrik yang dapat diturunkan |

Batasnya di mana. Metafora mati yang sudah baku di literatur teknik tetap boleh,
misalnya *gradien lenyap*, *ReLU mati*, *kurva mendatar*, dan *sinyal merambat*. Yang
dilarang adalah watak, niat, dan emosi yang diberikan kepada benda mati.

**2. Frasa kolokial diganti register baku perguruan tinggi.**

| Ditolak | Dipakai |
|---|---|
| mengganggu tidur teknisi tanpa alasan | memicu inspeksi lapangan yang tidak diperlukan |
| bergantung pada nasib | rentan terhadap variasi acak pemilihan sampel |
| secara telanjang | secara jelas dan terukur |
| tukar gulingnya | kompromi (*trade-off*) operasional |
| goyangan, bergoyang | fluktuasi, variabilitas |
| wajah bias tinggi | indikator karakteristik bias tinggi |
| berayun dari 60 sampai 78 | berfluktuasi antara 60 hingga 78 |
| menghamburkan waktu tanpa hasil | konvergensi terlalu lambat untuk anggaran epoch yang tersedia |

Rambunya sama seperti Langkah 5b, yaitu **jangan menukar frasa kolokial dengan register
birokratis.** "Beban kerugian berupa waktu kerja personil" tidak lebih baik daripada
"biaya satu jam kerja teknisi". Yang dibuang nada santainya, bukan bendanya.

**3. Pembuka kalimat berulang yang monoton.** Model cenderung membuka penjelasan dengan
kalimat pendek berpola tetap, lalu mengulanginya di tiap subbab. Satu kali tidak jadi
soal, tetapi lima kali dalam satu bab langsung terbaca sebagai keluaran model.

Cari pola berikut, lalu pastikan sisanya nol atau satu saja per dokumen:

`Pertanyaannya sederhana.` `Gagasannya sederhana.` `Idenya sesederhana.`
`Hasilnya tegas.` `Prosedurnya begini.` `Cara membacanya begini.`
`Jawabannya, buang saja.` `Mari kita lihat.` `Mari kita mulai.`
`Daripada mempercayai uraian itu begitu saja.` `Perhatikan bahwa.`
`Tiga hal langsung terlihat.` `Ada dua penyakit pokok.` `Seberapa jauh kemampuan X?`

Gantinya bukan menghapus kalimat itu, melainkan menyatukannya dengan kalimat sesudahnya
sehingga gagasannya dibawa oleh satu kalimat penuh. "Prosedurnya begini. Data latih
dibagi acak menjadi $k$ bagian." menjadi "Pada prosedur ini, himpunan data latih dibagi
secara acak menjadi $k$ bagian yang berukuran setara."

### Langkah 5d. Fusi kalimat terfragmentasi

Rangkaian kalimat pendek satu klausa yang berderet adalah tell yang berlawanan arah
dengan kalimat nomina panjang, dan sama kentaranya. Ciri terukurnya adalah rerata
panjang kalimat di bawah 16 kata disertai proporsi kalimat sepuluh kata ke bawah di
atas 30 persen.

Gabungkan dua atau tiga kalimat pendek yang berurutan menjadi satu kalimat majemuk
bertingkat, memakai konjungsi yang menyebut hubungannya, yaitu *karena*, *sehingga*,
*sedangkan*, *sebab*, *sebagaimana*, *meskipun*, dan *apabila*. Bukan memakai koma dan
kata *dan* berderet, sebab itu cara termalas dan langsung menaikkan baris koordinasi
pada skrip metrik.

**Sebelum**, rerata 14,1 kata:

> Sampai di sini neuron itu belum berbeda dari regresi linear. Perbedaannya baru muncul
> pada langkah terakhir. Nilai $z$ tidak langsung dikeluarkan, melainkan dilewatkan dulu
> pada suatu fungsi aktivasi.

**Sesudah**, rerata 18,0 kata:

> Sampai di sini tahapan pra-aktivasi masih identik dengan operasi regresi linear.
> Perbedaan fundamentalnya baru terletak pada tahapan berikutnya, sebab nilai $z$ tidak
> langsung dikeluarkan melainkan ditransformasikan lebih dahulu melalui suatu fungsi
> aktivasi taklinear.

Tiga rambu supaya fusi ini tidak merusak yang lain:

- **Sisakan kalimat pendek sebagai penutup paragraf.** Kalau semua kalimat dipanjangkan,
  simpangan bakunya justru turun dan teksnya kembali terasa rata.
- **Jangan menghapus gagasan sambil menggabung.** Ini kesalahan yang paling sering
  terjadi. Hitung gagasan pada versi lama, lalu pastikan jumlahnya sama pada versi baru.
- **Jangan menghapus demonstratif dan penanda kelonggaran.** Kata *itu*, *tersebut*,
  *akan*, *dapat*, dan *sudah* adalah bagian dari suara penulis. Menggabung kalimat
  sambil membuangnya akan menjatuhkan kepadatan kata pemadat jauh di bawah pita korpus.
  Pada satu kasus nyata, kata *itu* turun dari 108 menjadi 13 kejadian dan kepadatan
  pemadat jatuh dari 77,4 ke 54,3.

### Langkah 6. Audit

Ajukan pertanyaan ini pada diri sendiri secara eksplisit, lalu jawab dengan daftar
pendek:

> **Apa yang masih membuat teks di bawah ini terbaca sebagai tulisan AI atau sebagai
> terjemahan?**

Jawaban yang jujur biasanya menyebut empat hal: ada paragraf yang terlalu rapi
strukturnya, ada kalimat yang menjelaskan terlalu bersih, penutup yang datar, dan
beberapa frasa yang masih mengikuti urutan kalimat sumbernya.

Jalankan ulang skrip metrik pada draf. Bandingkan dengan hasil Langkah 2. Ingat bahwa
lulus seluruh baris tidak membuktikan teksnya mengalir; ia hanya membuktikan ritmenya
sudah berada di pita penulis.

### Langkah 7. Revisi akhir

Perbaiki temuan audit. Untuk simpangan baku yang masih di bawah 7, periksa dulu arah
kekurangannya sebelum bertindak, karena dua penyebabnya menuntut perlakuan berlawanan.

Bila kalimat pendek sudah 20 persen ke atas tetapi kalimat terpanjang di bawah 30 kata,
yang kurang adalah kalimat panjang. Panjangkan dua atau tiga kalimat penjelas lewat
klausa relatif, aposisi, atau keterangan sisipan. **Jangan memanjangkan dengan rangkaian
koma dan kata dan**, karena itu cara termalas dan langsung menaikkan baris koordinasi.

Bila kalimat pendek kurang dari 15 persen, tambahkan kalimat pendek penutup paragraf.

Jangan memangkas kalimat panjang secara menyeluruh. Memecah semuanya justru menurunkan
simpangan baku, bukan menaikkannya.

Terakhir, periksa baris kepadatan kata pemadat di keluaran skrip. Bila di bawah 73 per
1.000 kata, prosanya lebih mampat daripada tulisan penulis. Longgarkan dengan
mengembalikan frasa yang wajar, misalnya *penting untuk disampaikan* alih-alih *penting
disebut*, atau *Upaya untuk menaikkan* alih-alih *Upaya menaikkan*. Jangan menambah kata
isian kosong hanya untuk menaikkan angkanya.

CARA MENAIKKAN KEPADATAN PEMADAT yang terbukti, urut dari yang paling banyak hasilnya:

1. Kembalikan demonstratif yang dibuang. "Data dipartisi" menjadi "Data itu dipartisi".
2. Kembalikan *akan* pada kalimat penjelas. "Anda melihat rangka yang sama" menjadi
   "Anda akan melihat rangka yang sama".
3. Kembalikan sapaan pada kalimat ajakan dan peringatan, yaitu *Anda* dan *kita*.
4. Ganti *menggunakan* menjadi *memakai*, lalu tambahkan *untuk* bila kalimatnya menuntut.
5. Ganti *sebuah* menjadi *suatu* pada nomina abstrak.

Sekitar 60 suntingan semacam itu menaikkan kepadatan 16 poin pada bab sepanjang 8.000
kata, tanpa menambah satu kalimat baru pun.

### Langkah 8. Serahkan

Sampaikan lima hal:

1. Draf revisi
2. Daftar pendek temuan audit
3. **Daftar keputusan diksi**, yaitu istilah apa saja yang diganti beserta alasannya, dan
   berapa kali tiap istilah muncul di dokumen lain yang ikut terpengaruh
4. Revisi akhir
5. Tabel perbandingan metrik sebelum dan sesudah

Butir 3 tidak boleh dilewati. Keputusan istilah adalah wewenang penulis, bukan wewenang
penyunting, dan penulis perlu melihatnya sebagai daftar, bukan menemukannya satu per satu
sambil membaca.

## Menerima berkas yang sudah disunting model lain

Alur ini dipakai ketika penulis menjalankan model lain lebih dahulu, misalnya Gemini,
lalu membawa hasilnya untuk diperiksa. Pekerjaannya **bukan menulis ulang**, melainkan
memisahkan perbaikan bahasa yang memang lebih baik dari kerusakan yang terbawa serta.

**Jangan pernah menerima berkas semacam itu hanya karena metriknya lulus.** Pada dua
kasus nyata, versi model lain lulus sembilan dari sembilan baris berambang sekaligus
menghapus satu paragraf penuh, sembilan rujukan persamaan, sembilan rujukan program,
lima sitasi, dan belasan angka terverifikasi.

### Urutan kerja

1. Minta atau cari **berkas versi lama**. Tanpa pembanding, audit ini mustahil.
2. Arsipkan berkas mentah model lain sebelum menyunting apa pun.
3. Jalankan sebelas pemeriksaan di bawah, seluruhnya dengan skrip pembanding.
4. Laporkan temuan sebagai tabel sebelum dan sesudah, lalu **tanyakan keputusan yang
   memang wewenang penulis**, yaitu istilah baru, judul bagian, dan format persamaan.
5. Sunting lewat skrip berpasangan (lama, baru) dengan `assert` supaya tiap potongan
   dipastikan ketemu, bukan dengan menulis ulang berkasnya.

### Sebelas pemeriksaan wajib

1. **Blok kode.** Ekstrak seluruh blok berpagar lalu bandingkan persis. Satu spasi
   indentasi yang bergeser sudah membuat berkas tidak lagi sama dengan repositori kode.
2. **Angka.** Normalkan dulu penulisan desimal, misalnya `0{,}5` menjadi `0,5`, lalu
   bandingkan himpunan angkanya. Angka yang hilang hampir selalu berarti kalimat yang
   memuatnya ikut terhapus.
3. **Rujukan silang.** Hitung `Persamaan \(\d+\.\d+\)`, `Program \d+\.\d+`,
   `Tabel \d+\.\d+`, `Gambar \d+\.\d+`, dan tiap sitasi tahun. Jumlahnya harus sama atau
   lebih. Ini pemeriksaan yang paling sering menyelamatkan dokumen teknis.
4. **Cacah paragraf per bagian.** Kalau satu bagian menyusut satu paragraf, cari paragraf
   mana yang hilang. Jangan hanya membandingkan cacah kata.
5. **Kalimat bersitasi.** Baca ulang tiap kalimat yang membawa nama penulis dan tahun
   terhadap naskah lama. Model lain kerap meringkas temuan pustaka sampai maknanya
   bergeser, dan yang terbuang sering justru bagian yang menyambung ke tabel sendiri.
6. **Istilah baru.** Grep tiap istilah yang tidak ada di versi lama ke seluruh folder
   dokumen bersaudara. Istilah yang hanya hidup di satu bab akan memecah keseragaman.
7. **Judul bagian.** Judul yang berubah akan merembet ke daftar isi, kunci jawaban, dan
   slide. Ini keputusan penulis, jadi tanyakan, jangan putuskan sendiri.
8. **Persamaan terpampang.** Hitung blok `$$` dan `\begin{equation}`. Model lain gemar
   memecah hitungan sebaris menjadi blok terpampang, dan itu mengubah cacah halaman.
   Kalau dokumen aslinya tidak memakai pola itu, kembalikan. Kalau sudah memakai,
   tanyakan apakah tambahannya dipertahankan.
9. **Tanda persen dan satuan.** Model lain gemar mengganti kata *persen* menjadi `%`.
   Ikuti kebiasaan dokumen, dan hati-hati karena penggantian dengan regex akan ikut
   memakan atribut gambar seperti `{width=85%}`.
10. **Struktur daftar.** Periksa baris kosong sebelum daftar bernomor dan sub-butir
    (a)(b)(c) yang dipisah menjadi paragraf lepas. Keduanya memutus penomoran di pandoc.
11. **Kepadatan kata pemadat.** Bandingkan frekuensi tiap kata pemadat versi lama lawan
    versi baru, bukan hanya angka gabungannya. Yang paling banyak hilang biasanya kata
    *itu*, dan itulah yang paling dulu dikembalikan.

### Yang biasanya memang lebih baik dan harus dipertahankan

Jangan mengembalikan versi lama hanya karena berbeda. Perbaikan yang biasanya nyata dan
layak dipertahankan adalah personifikasi yang hilang, frasa kolokial yang naik register,
pembuka kalimat monoton yang lenyap, rerata panjang kalimat yang naik ke pita 16 sampai
21, dan padanan istilah asing yang menjadi lebih konsisten.

## Kaidah yang sering terlewat

**Tanda hubung bukan tanda pisah.** Aturan nol em dash dan en dash **tidak** berlaku
untuk tanda hubung (U+002D). Bentuk ulang wajib memakainya: *rata-rata*, *benar-benar*,
*alih-alih*, *berturut-turut*, *kira-kira*, *sama-sama*, *asal-usul*, *terus-menerus*,
*batas-batas*, *masing-masing*, *kehati-hatian*, *berlipat-lipat*. Kekeliruan ini pernah
terjadi dan menyebar ke empat bab sekaligus sebelum ketahuan.

Pemeriksaannya satu baris:

```bash
grep -noE "\b(\w+)[ \n]\1\b" berkas.md
```

Hati-hati pada positif palsu: *satu satuan massa* bukan bentuk ulang, begitu pula kata
yang kebetulan terulang di batas dua kalimat.

**`di mana` bukan pronomina relatif.** Ini kesalahan yang paling sering muncul pada teks
yang disunting model. *di mana* hanya dipakai sebagai keterangan tempat dan ditulis
terpisah. Bentuk "konvensi di mana baris menyatakan kelas aktual" diganti "konvensi yang
menempatkan kelas aktual pada baris". Cari `\bdi mana\b` lalu pastikan hasilnya nol pada
teks teknis. Bentuk `dimana` dan `yang mana` sebagai penghubung juga dilarang.

**Kata "oleh" setelah verba pasif berimbuhan di-.** Bila pelakunya disebut, pakai *oleh*:
dirumuskan oleh Komisi Eropa, dijanjikan oleh Industri 5.0, dilakukan oleh pemiliknya.
Menurut Tata Bahasa Baku Bahasa Indonesia, *oleh* membuat hubungan fungsi antarunsur
kalimat lebih tegas dan bernada formal. Pasif tanpa pelaku tetap apa adanya.

**Bentuk baku yang sering salah:** *linear* bukan *linier*, dan karena itu *taklinear*
bukan *nonlinier*. Pilih satu bentuk untuk seluruh dokumen, sebab model lain kerap
memakai *taklinear*, *nonlinier*, dan *linier* sekaligus di dalam satu berkas. Selain
itu *tolok ukur* bukan *tolak ukur*.

**Istilah asing.** Miringkan dan beri padanan dalam kurung pada pemunculan pertama tiap
bab atau bagian. Jangan meninggalkan istilah Inggris berdiri telanjang di tengah prosa
Indonesia.

## Berkas rujukan

| Berkas | Isi | Kapan dibaca |
|---|---|---|
| `references/id-ai-tells.md` | Katalog tell bahasa Indonesia, positif palsu, register yang dikecualikan | Selalu |
| `references/voice-prib-id.md` | Preset suara PRIB, metrik sasaran, asal korpus | Bila penulisnya PRIB |
| `scripts/metrik.py` | Pengukur tujuh metrik dengan ambang preset | Langkah 2 dan 6 |

Tidak ada berkas rujukan untuk Langkah 5b sampai 5d. Kalkir, personifikasi, dan
fragmentasi tidak dapat dideteksi dengan daftar kata, sebab yang salah bukan katanya
melainkan hubungan antarkata dan pola yang berulang. Satu-satunya alat yang bekerja
adalah membaca setiap paragraf sambil bertanya kalimat Inggris apa yang ada di baliknya,
lalu membaca ulang seluruh bab sambil memperhatikan bagaimana tiap subbab dibuka.

## Detektor pihak ketiga

**Aturan utama: suara penulis menang, skor detektor kalah.** Bila keduanya bentrok,
pilih suara penulis, laporkan skornya apa adanya, dan jangan menyunting demi angka.
Ini keputusan penulis, bukan asumsi.

Alasannya ada pada bukti, bukan pada prinsip saja. Tujuh pengukuran GPTZero, dicatat
dengan versi modelnya:

| Teks | Sumbu yang disetel | Model | Skor human |
|---|---|---|---|
| Potongan 516 kata paper manusia | (tulisan penulis) | 4.9b | 100 persen |
| Paper Pengabdian v2 penuh | (tulisan penulis) | 4.9b | 98 persen |
| Paper SNIV penuh | (tulisan penulis) | 4.9b | 80 persen |
| Teks buatan setelah disunting tangan penulis | suntingan manusia | 4.1m | 45 persen |
| Teks buatan mampat, lulus semua metrik | ritme dan sintaksis | 4.1m | di bawah 45 |
| Teks buatan berkekhususan tinggi | sitasi, tahun, nilai terukur | 4.1m | 2 persen |
| Teks buatan longgar setara korpus, lulus 9 dari 9 | kepadatan pemadat 122 | 4.1m | 1 persen |

Dua baris terakhir duduk di ujung berlawanan dari setiap sumbu yang dapat disetel, dan
skornya identik. Sementara teks berstruktur sama yang melewati suntingan tangan penulis
melompat ke 45 persen. Kesimpulannya: detektor tidak membaca sumbu yang dapat disetel
aturan gaya. Ia membaca distribusi statistik keluaran model itu sendiri, dan model
detektor terbaru (4.9b, rilis 12 Agustus 2026) secara eksplisit dipertajam terhadap
Claude 5.

Daftar lengkap hipotesis yang sudah diuji dan gugur ada di bagian 6
`references/voice-prib-id.md`. Tidak ada resep andal untuk menaikkan skor. Yang ada
hanya resep untuk merusak tulisan sambil mengejarnya.

**Yang tetap berguna dari detektor.** Keluarkan blok metadata sebelum memindai. Pada
Paper SNIV, bagian yang ditandai AI adalah daftar afiliasi dan daftar pustaka, bukan
prosanya. Buang judul, daftar penulis, afiliasi, alamat, surel, dan daftar pustaka.
`scripts/metrik.py` sudah melakukannya otomatis untuk pengukurannya sendiri.

**Cara membaca temuan detektor.** Pilah alasannya, jangan turuti semuanya.

| Alasan detektor | Tindakan |
|---|---|
| Prosa lebih mampat daripada korpus penulis | **Perbaiki.** Longgarkan sampai setara korpus. |
| Pembuka kalimat seragam berderet | **Pertimbangkan.** Korpus penulis lebih parah. Tanpa ambang. |
| Koordinasi klausa | **Pertimbangkan.** Kontrol manusia 1,50 dan tetap 100 persen. |
| Technical jargon, istilah bidang | **Abaikan.** Kosakata wajib. |
| Overly formal, impersonal tone | **Abaikan.** Register memang menuntutnya. |
| Sophisticated clarity, mechanical precision | **Abaikan.** Keduanya memuji ketepatan. |

**Catat versi model detektornya.** Skor lintas versi tidak dapat dibandingkan. Pengujian
14 Agustus 2026 memakai dua model berbeda tanpa disadari (4.9b pada paper manusia, 4.1m
pada teks buatan), sehingga sebagian perbandingannya cacat. GPTZero merilis 4.9b pada 12
Agustus 2026 dengan peningkatan recall yang secara khusus menyebut Claude 5, GPT 5.6,
Gemini 3.6, dan Grok 4.5.

Konsekuensinya, **setiap ambang yang dikalibrasi terhadap detektor punya masa pakai
hitungan minggu.** Ambang di skill ini dikalibrasi terhadap korpus tulisan penulis, yang
tidak berubah ketika detektor dimutakhirkan. Pertahankan begitu. Bila mencatat skor,
tulis versi modelnya, tanggalnya, dan panjang teksnya sekaligus.

**Jangan mengarang salah ketik atau cacat.** Korpus penulis memuat banyak salah ketik,
dan teks yang disunting penulis pun menyisakannya. Itu bukan izin untuk menyisipkannya
dengan sengaja. Menambahkan cacat palsu bukan menulis seperti penulis.

## Menghindari sterilitas

Membuang pola AI baru separuh pekerjaan. Prosa yang bersih tapi tanpa suara sama
kentaranya dengan slop.

Tanda tulisan tanpa suara: semua kalimat sepanjang dan sestruktur sama, tidak ada
penilaian, tidak ada pengakuan ketidakpastian, tidak ada sudut pandang orang pertama
ketika seharusnya ada, dan terbaca seperti siaran pers.

Namun **terapkan bagian ini hanya bila isi dan suara penulis memang menuntutnya.** Untuk
teks teknis, ensiklopedis, hukum, atau rujukan, netral dan datar justru *adalah* suara
manusia yang benar. Jangan menyuntikkan opini atau orang pertama ke sana.

Cara menambahkan suara pada register yang memang memungkinkan:

- **Akui keterbatasan secara terbuka.** Dalam korpus PRIB ini muncul konsisten sejak
  2011 sampai 2025. Jangan pernah menghaluskan atau menghapus pengakuan keterbatasan.
- **Variasikan ritme.** Kalimat pendek. Lalu kalimat yang lebih panjang dan mengambil
  waktu untuk sampai ke tujuannya.
- **Biarkan sedikit tidak rapi.** Struktur yang sempurna terasa algoritmik.

Ada satu ketegangan yang harus dikelola dengan sadar. Langkah 5c membuang personifikasi
dan diksi santai, sedangkan bagian ini meminta teks tidak steril. Keduanya tidak
bertabrakan asalkan sumber warnanya dipindah, yaitu dari watak benda mati menjadi
keterusterangan penulis. "Model itu menghafal, bukan belajar" diganti, tetapi "Yang
kedua itulah yang kita pedulikan" dan "angka yang Anda laporkan itu bisa jadi hanyalah
keberuntungan inisialisasi" justru dipertahankan.

## Yang tidak boleh ditandai

Penulis manusia yang baik bisa mengenai beberapa pola di katalog tanpa keterlibatan AI
sama sekali. Rincian lengkapnya di bagian F `references/id-ai-tells.md`. Ringkasnya,
jangan menandai:

- Pasif dalam bagian Metode dan Hasil. Itu konvensi disiplin.
- Istilah teknis serapan yang memang baku.
- Kalimat panjang dalam dokumen hukum, akreditasi, dan kurikulum.
- Ejaan rapi dan konsisten. Kerapian bukan bukti AI.
- `seperti yang` sebagai penanda rujukan ke gambar, tabel, atau penelitian terdahulu.
- Register formal itu sendiri.
- Metafora mati yang sudah baku di literatur teknik, misalnya gradien lenyap dan ReLU
  mati.
- Terjemahan harfiah yang memang sedang dikutip sebagai rumusan resmi sebuah lembaga.
  Kutipannya dibiarkan utuh, padanannya diberikan sesudahnya, lalu padanan itulah yang
  dipakai di seluruh dokumen.

Cari **gerombolan** tell, bukan tell tunggal. Satu `namun` tidak berarti apa-apa.

## Tanda tulisan manusia yang harus dipertahankan

Bila menemui hal berikut, condonglah membiarkan prosanya:

- Detail spesifik yang sulit dikarang: angka tak bulat, nama alat, nomor kontrak,
  tanggal persis.
- Perasaan bercampur dan ketegangan yang tidak terselesaikan.
- Pengakuan keterbatasan yang merugikan penulis sendiri.
- Variasi panjang kalimat yang lebar.
- Sisipan, tanda kurung, dan koreksi diri.
- Salah ketik dan penggalan kalimat. Ini bukan gaya yang harus ditiru, tetapi
  keberadaannya adalah bukti kuat bahwa teks itu ditulis manusia. Perbaiki salah
  ketiknya, jangan jadikan alasan menulis ulang seluruh paragraf.

## Contoh penuh

**Masukan:**

> Dalam era perkembangan teknologi nuklir yang semakin pesat, baterai nuklir merupakan
> salah satu inovasi yang memegang peranan penting. Teknologi ini melakukan pemanfaatan
> terhadap proses peluruhan bahan radioaktif, yang mana hal ini memberikan pengaruh
> terhadap dihasilkannya arus listrik searah. Berbagai keunggulan seperti efisiensi,
> keandalan, dan umur pakai yang panjang menjadikannya solusi yang menjanjikan untuk
> masa depan energi.

**Metrik masukan:** rerata 28,0 kata, simpangan baku 4,1, verba ringan 2,4 per 100 kata,
enumerasi 11,9 per 1.000 kata.

**Draf:**

> Baterai nuklir tidak memakai reaksi fisi, melainkan peluruhan bahan radioaktif.
> Peluruhan itu melepaskan elektron yang menumbuk semikonduktor sehingga menghasilkan
> arus searah. Keunggulannya pada umur pakai yang panjang.

**Audit, apa yang masih terbaca sebagai AI:**

- Draf terlalu padat dibanding aslinya. Tiga kalimat menyusut dari tiga gagasan
  menjadi tiga kalimat pendek yang kehilangan tekstur.
- Kalimat ketiga masih klaim tanpa angka.
- Tidak ada pengakuan keterbatasan, padahal ini penanda kuat suara penulis.

**Revisi akhir:**

> Pada baterai nuklir tidak digunakan reaksi fisi, melainkan peluruhan bahan radioaktif.
> Peluruhan itu melepaskan elektron yang menumbuk semikonduktor dan menghasilkan arus
> searah. Keunggulannya ada pada umur pakai, karena sebagian jenis bertahan sampai
> puluhan tahun. Efisiensinya sendiri masih rendah.

**Metrik keluaran:** rerata 17,3 kata, simpangan baku 8,0, verba ringan 0, enumerasi 0.

**Perubahan:** pembuka formula dibuang, dua verba ringan dipadatkan, `merupakan` diganti,
`yang mana` dihapus, enumerasi `seperti` dan triplet dibuang, temuan disusul sebab
langsung, kalimat pendek penutup ditambahkan, keterbatasan diakui terbuka.

## Contoh kedua: kalkir yang lolos seluruh metrik

Paragraf berikut lulus sembilan dari sembilan baris berambang. Ia tetap salah.

**Sebelum:**

> Enam teknologi pemungkin pada Gambar 3.12 adalah eksoskeleton, teknologi aditif,
> jaringan 5G dan seterusnya, realitas campuran, rantai blok industri, dan pesawat
> nirawak. Dua di antaranya berkaitan langsung dengan ekonomi sirkular. Teknologi aditif
> memungkinkan komponen pengganti dicetak sesuai kebutuhan sehingga produk lama dapat
> diperbaiki alih-alih dibuang. Rantai blok industri memungkinkan asal-usul dan riwayat
> sebuah komponen ditelusuri, dan ketertelusuran itulah syarat agar sebuah komponen
> bekas dapat dipercaya untuk dipakai ulang atau diremanufaktur.

**Sesudah:**

> Gambar 3.12 menyajikan enam teknologi pendukung utama: eksoskeleton, manufaktur
> aditif, jaringan 5G dan generasi berikutnya, realitas campuran, rantai blok industri,
> serta pesawat nirawak. Dua di antaranya berkaitan langsung dengan prinsip ekonomi
> sirkular. Manufaktur aditif memfasilitasi pembuatan suku cadang pengganti sesuai
> kebutuhan, sehingga memperpanjang masa pakai produk lama tanpa harus membuangnya.
> Sementara itu, rantai blok industri merekam riwayat serta asal-usul komponen sehingga
> keduanya dapat ditelusuri, dan ketertelusuran itu menjadi prasyarat bagi penggunaan
> ulang maupun proses remanufaktur.

**Yang berubah:** daftar dipindahkan ke belakang titik dua dan tidak lagi digantung pada
*adalah*; *teknologi pemungkin* diganti *teknologi pendukung utama*; *teknologi aditif*
diganti *manufaktur aditif*; *dan seterusnya* diganti *generasi berikutnya*; dua
*memungkinkan* diganti verba yang menyebut tindakan sebenarnya; dan klaim *menjamin
ketertelusuran* diturunkan menjadi *merekam sehingga dapat ditelusuri*, karena rantai
blok menjaga catatannya tidak berubah, bukan menjamin isinya benar.

Tidak satu pun dari perubahan itu terlihat oleh `scripts/metrik.py`. Inilah alasan
Langkah 5b tidak boleh dilewati.

## Contoh ketiga: personifikasi dan pembuka monoton yang lolos seluruh metrik

**Sebelum**, lulus seluruh baris berambang:

> Bacalah tabel itu dari atas ke bawah dan Anda akan melihat pola yang khas. Pada ambang
> 0,70 model sangat berhati-hati. Ia hanya menyalakan 23 alarm dan semuanya benar,
> sehingga presisinya sempurna. Harganya mahal, karena 45 kegagalan lolos tanpa
> peringatan. Pada ambang 0,10 model berubah menjadi sangat cerewet, karena ia menangkap
> 60 dari 68 kegagalan tetapi membayar keberanian itu dengan 87 alarm palsu.

**Sesudah:**

> Pola hubungan pada Tabel 5.3 memperlihatkan dinamika kompromi tersebut secara
> konsisten. Pada ambang 0,70, model bekerja secara sangat konservatif, sebab dari 23
> peringatan yang dikeluarkan seluruhnya merupakan kegagalan aktual sehingga nilai
> presisi mencapai 1,0000. Namun, konsekuensinya adalah 45 kasus kegagalan terlewat
> tanpa deteksi (*recall* hanya 0,3382). Sebaliknya, pada ambang 0,10, model bekerja
> secara agresif dalam mendeteksi anomali, yaitu berhasil menangkap 60 dari 68 kegagalan
> (*recall* 0,8824), namun menghasilkan 87 alarm palsu sehingga presisi merosot ke angka
> 0,4082.

**Yang berubah:** pembuka berpola "Bacalah ... dan Anda akan melihat" dibuang;
*sangat berhati-hati* menjadi *sangat konservatif*; *berubah menjadi sangat cerewet* dan
*membayar keberanian itu* menjadi *bekerja secara agresif dalam mendeteksi*; sedangkan
*presisinya sempurna* dan *harganya mahal* diberi angka terukur, yaitu 1,0000, 0,3382,
0,8824, dan 0,4082. Perhatikan bahwa **tidak satu angka pun hilang, dan justru
bertambah**. Inilah pembeda antara perbaikan yang benar dan peringkasan yang merusak.

## Rujukan

Kerangka putaran draf, audit, revisi akhir diwarisi dari skill `humanizer`, yang
bersumber pada halaman Wikipedia *Signs of AI writing*. Katalog pola dan preset suara
dalam skill ini dibangun dari pengukuran korpus tulisan penulis, bukan dari sumber itu.
Katalog kalkir pada Langkah 5b dibangun dari penyuntingan diktat Penilaian Dampak dan
Keberlanjutan Lingkungan, 4 September 2026. Katalog personifikasi, register, pembuka
monoton, dan fusi kalimat pada Langkah 5c dan 5d, beserta seluruh bagian audit berkas
model lain, dibangun dari perbandingan Bab 5 dan Bab 6 diktat Machine Learning TMP507
versi Claude lawan versi Gemini, 9 September 2026.