# Preset Suara: PRIB (Bahasa Indonesia)

Modul referensi untuk skill `humanizer`. Dipakai bersama `references/id-ai-tells.md`.

Aturan format mutlak: keluaran **tidak boleh memuat em dash (U+2014) maupun en dash
(U+2013)** di badan prosa. Dasarnya bukan selera, melainkan data korpus di bagian 0.

---

## 0. Korpus dan dasar bukti

14 dokumen, rentang 2008 sampai 2025.

**Aturan korpus yang mengikat.** Penulis mulai memakai bantuan AI dalam penulisan setelah
2022. Dokumen bertahun 2023 ke atas **tidak boleh dipakai sebagai patokan suara** kecuali
penulis menyatakan secara eksplisit bahwa bagian tertentu ditulis tanpa bantuan. Tahun
terbit karena itu bukan sekadar metadata, melainkan syarat kelayakan.

### Tingkat kepercayaan menurut asal

| Tingkat | Dokumen | Tahun | Alasan |
|---|---|---|---|
| **A. Patokan** | Baterai Nuklir Beta, prinsip satelit GEO | 2011, 2012 | penulis tunggal, pra-AI |
| **A. Patokan** | Paper Pengabdian v2 | 2021 | penulis pertama, pra-AI |
| **A. Patokan** | Abstract dynotest | pra-2023 | tunggal, salah ketik dan fragmen menandakan draf tanpa bantuan |
| **B. Pendukung** | cosmology bab4, Fuel Design, PR inti | 2011 | catatan kuliah, register ekspositori |
| **B. Pendukung** | Cara membuat yoghurt | 2009 | blog, satu-satunya sampel semi-formal |
| **C. Perlu dipastikan** | Paper SNIV | ? | metrik cocok pita A, tapi tahun terbit belum diketahui |
| **D. Tidak dipakai** | Jurnal Pengmas Pade | 2025 | dikonfirmasi banyak dipengaruhi AI |
| **D. Tidak dipakai** | Prosiding ED PCO | 2021 | penulis pertama Syamsudin, lihat bagian 0.1 |
| **D. Tidak dipakai** | Paten S00202110995 | 2021 | disusun konsultan HKI, genre hukum |
| **D. Tidak dipakai** | Paper final, Alat Ukur Smes | 2011, 2008 | 7 penulis; sebagian besar kutipan web |

**Tindakan yang tertunda:** pastikan tahun terbit Paper SNIV. Bila 2023 ke atas, turunkan
ke tingkat D dan hitung ulang seluruh sasaran akademik di bagian 1 tanpa dokumen itu.

### 0.1 Kontrol negatif yang memvalidasi metrik

Prosiding ED PCO dan Paper Pengabdian v2 sama-sama terbit 2021, satu institusi, satu
lingkungan riset, dan nama penulis beririsan. Bedanya hanya siapa yang memegang pena.

| Ukuran | Paper Pengabdian (penulis-1 Prib) | Prosiding ED (penulis-1 Syamsudin) |
|---|---|---|
| Rerata panjang kalimat | 17,2 | 25,7 |
| Simpangan baku | 8,2 | 13,8 |
| Enumerasi *seperti* per 1.000 kata | 1,84 | 2,09 |
| *dimana* | 0 | 3 |

Pemisahan ini terjadi pada tahun, topik, dan institusi yang sama. Artinya metrik di
bagian 1 memang mengukur penulis, bukan bidang atau genre. Simpan tabel ini: bila di
kemudian hari penyuntingan menghasilkan angka yang mendekati kolom kanan, presetnya gagal.

### 0.2 Garis dasar detektor

`Paper_Pengabdian_v2` diuji GPTZero dengan hasil 98 persen human, dan `Paper_SNIV` 80
persen human. Keduanya tulisan manusia, pra-2022. Bagian yang ditandai AI pada SNIV
adalah blok afiliasi dan daftar pustaka, bukan prosanya.

Konsekuensinya, sasaran skor untuk teks hasil penyuntingan adalah pita 80 sampai 98
persen human, bukan 100 persen. Hasil ini juga memperkuat status `Paper_SNIV` sebagai
tulisan tanpa bantuan AI, meski pertanyaan tahun terbitnya tetap terbuka karena detektor
tidak dapat menjawabnya.

### 0.3 Register yang dikecualikan

Preset ini **tidak dijalankan** pada dokumen paten, kontrak, peraturan, instrumen
penelitian tervalidasi, dan kutipan langsung. Rinciannya di bagian G modul
`id-ai-tells.md`. Paten S00202110995 dipakai sebagai contoh kasus di sana.

Tingkat keyakinan tiap penanda:

- **[K]** terkonfirmasi, muncul di tiga dokumen bebas atau lebih, lintas dekade
- **[S]** stabil sepanjang waktu, terukur di korpus 2011 maupun 2021 sampai 2025
- **[T]** tentatif, satu dokumen saja, perlu konfirmasi korpus baru
- **[X]** pudar, kuat di korpus lama tapi hilang di korpus baru, jangan dipakai lagi

---

## 1. Metrik sasaran

Angka diambil dari korpus, bukan dari norma umum.

### Terukur per dokumen

| Dokumen | Tahun | Rerata | SD | Konektor/100kt | Buka *Pada* | Verba ringan |
|---|---|---|---|---|---|---|
| Baterai Nuklir Beta | 2011 | 18,0 | 6,9 | 2,18 | 15,2% | 0,00 |
| prinsip satelit GEO | 2012 | 16,9 | 6,5 | 2,15 | 6,1% | 0,00 |
| cosmology bab4 | 2011 | 19,2 | 7,5 | 1,78 | 0% | 0,00 |
| Cara membuat yoghurt | 2009 | 14,7 | 7,4 | 0,95 | 0% | 0,00 |
| Paper Pengabdian v2 | 2021 | 17,2 | 8,2 | 0,80 | 6,3% | 0,18 |
| Paper SNIV | 2022 | 17,1 | 8,9 | 0,67 | 3,8% | 0,04 |
| Abstract dynotest | pra-2023 | 16,6 | 8,4 | 1,20 | 0% | 0,00 |
| Jurnal Pengmas Pade | 2025 | 19,4 | 11,1 | 1,15 | 0% | 0,00 |
| *Prosiding ED (bukan Prib)* | 2021 | *25,7* | *13,8* | *1,25* | *3,6%* | *0,21* |

### Sasaran penyuntingan

**Kalibrasi 1.2. Dua kalibrasi sebelumnya salah arah dan harus dicatat.**

Versi 1.0 dan 1.1 memasang ambang lebih ketat daripada tulisan penulis sendiri. Buktinya
telak: potongan 516 kata dari `Paper_Pengabdian_v2`, tulisan manusia yang dinilai GPTZero
100 persen human, **gagal di empat baris** (koordinasi 1,50, verba ringan 0,39, enumerasi
5,81, merupakan 1,94). Sementara teks buatan yang lulus kesembilan baris hanya mendapat
45 persen. Ambangnya, bukan tulisannya, yang keliru.

Penyebabnya sama tiga kali: memakai rerata dokumen penuh untuk menetapkan ambang,
padahal rerata menutupi bagian yang jauh lebih padat. Ambang 1.2 diambil dari **nilai
tertinggi yang benar-benar muncul** di korpus, bukan dari rerata.

Rentang terukur, delapan dokumen tingkat A dan B:

| Metrik | Min korpus | Maks korpus | Ambang 1.1 (salah) | Ambang 1.2 |
|---|---|---|---|---|
| Rerata panjang kalimat | 14,5 | 19,2 | 14 sampai 19 | 14 sampai 20 |
| Simpangan baku | 6,5 | 9,8 | min 7,0 | min 6,4 |
| Kalimat 28 kata ke atas | 5,6% | 20,0% | maks 15% | maks 20% |
| Koordinasi pada kalimat panjang | 0,25 | 1,50 | maks 0,70 | maks 1,50 |
| Konektor per 100 kata | 0,00 | 0,36 | maks 0,40 | maks 0,40 |
| Verba ringan per 100 kata | 0,00 | 0,39 | maks 0,20 | maks 0,40 |
| *merupakan* per 1.000 kata | 0,00 | 6,02 | maks 1,50 | maks 4,00 akademik |

Prinsip yang mengikat sejak sekarang: **tulisan penulis sendiri harus lulus.** Ambang yang
menghukum korpusnya adalah ambang yang salah, bukan tulisan yang salah.

Dua baris tetap lebih ketat daripada korpus, dan itu disengaja:

| Baris | Korpus | Ambang | Alasan |
|---|---|---|---|
| Enumerasi per 1.000 kata | sampai 5,81 | maks 1,00 | permintaan penulis |
| Em dash dan en dash | sampai 7 | 0 | permintaan penulis |

Dokumen penulis akan berstatus PERIKSA di dua baris itu. Itu perilaku yang diharapkan,
bukan tanda tulisan AI.

Verifikasi ambang: seluruh dokumen tingkat A lulus enam dari tujuh baris, dan satu-satunya
yang berstatus PERIKSA adalah baris berbasis instruksi. Kontrol negatif Prosiding ED gagal
di baris rerata panjang kalimat. Itulah perilaku yang diharapkan.

---

## 2. Penanda suara

### 2.1 Tanpa tanda pisah **[K][S]**

Em dash nol di sepuluh dari sebelas dokumen. En dash muncul hanya sebagai rentang angka
di daftar pustaka dan spesifikasi (2007-2010, 600-1200 °C, 189-194), tidak pernah sebagai
tanda baca prosa. Ini penanda paling konsisten dalam seluruh korpus.

Pengganti yang dipakai penulis: koma, titik dua, tanda kurung, atau pecah jadi dua
kalimat. Sisipan penjelas hampir selalu masuk tanda kurung, bukan diapit tanda pisah.

### 2.2 Enumerasi *seperti* dihindari **[K][S]**

Enam enumerasi dalam 13.000 kata, sekitar 0,46 per 1.000 kata. Sebaliknya, konstruksi
rujukan *seperti yang* dipakai bebas dan sering (11 dari 12 kemunculan *seperti* di
Paper SNIV). Jangan menyunting yang kedua.

Cara penulis menyajikan daftar tanpa *seperti*:

> Nilai-nilai yang diukur pada eksperimen adalah laju aliran (*Q*), suhu inlet (*T*in),
> suhu permukaan (*T*w), tegangan (*V*), dan arus (*I*).

Daftar dijadikan objek atau predikat langsung. Kalau butirnya panjang atau paralel,
dipisah ke daftar bernomor tersendiri, bukan digantung di tengah kalimat.

### 2.3 *adalah* lebih disukai daripada *merupakan* **[K][S]**

Rasio konsisten di seluruh korpus. Paper SNIV: *adalah* 28 kali, *merupakan* 2 kali.
Baterai Nuklir Beta: 11 berbanding 3. Paper Pengabdian: 7 berbanding 1.

Saat menyunting keluaran AI, ganti *merupakan* jadi *adalah*, atau bongkar jadi kalimat
berverba penuh. Sisakan *merupakan* hanya bila kalimatnya benar-benar definisi dan
*adalah* sudah dipakai di kalimat sebelahnya.

### 2.4 Glosarium dalam kurung untuk istilah asing **[K][S]**

Muncul di sembilan dokumen, tak berubah sejak 2011. Istilah asing dimiringkan, padanan
atau akronim dalam kurung. Arah bisa dua-duanya tergantung mana yang lebih lazim di
lapangan.

> peluruhan (*decay*) · kendaraan pembawa (*launch vehicle*) · orbit rendah ekuator (LEO)
> fenomena habis terbakar (*burnout*) · hulu (*upstream*) · studi percontohan (*pilot study*)
> persepsi diri (*self-reported confidence*)

Istilah asing tidak dihindari dan tidak dipaksa dicarikan padanan yang jarang dipakai.
Notasi matematis dimiringkan konsisten: *q*, *T*w, *W*, *R*2.

### 2.5 Angka spesifik dipertahankan **[K][S]**

Korpus penuh bilangan konkret yang tidak dibulatkan: 66,7 keV; 862,42 kW/m2; 3,43 sampai
11,710 kW/m2 °C; 0,038 m dari hulu; 71,4% responden; 3,55 menjadi 4,78. Jangan pernah
mengganti angka dengan kata sifat samar seperti *cukup besar* atau *sangat tinggi* saat
menyunting.

Pola turunannya: klaim selalu berpasangan dengan angka atau rujukan gambar. Kalimat
penilaian tanpa dasar terukur nyaris tidak ada.

### 2.6 Penjelasan sebab langsung setelah temuan **[K][S]**

Ritme paling konsisten dalam teks hasil. Nyatakan yang teramati, lalu sebab, tanpa
kalimat jembatan.

> Suhu permukaan mengalami penurunan apabila nilai dari laju aliran dinaikkan. Hal ini
> disebabkan karena semakin tinggi laju aliran maka laju pendinginan semakin baik.

Frasa penyambungnya berulang: *Hal ini disebabkan*, *Artinya*, *Terlihat bahwa*,
*Hasilnya*. Semuanya pendek dan langsung, bukan konektor wacana panjang.

### 2.7 Pembatasan diri yang eksplisit **[K]**

Keterbatasan disebut terbuka, bukan disamarkan. Muncul di korpus 2011 sampai 2025.

> Namun, sistem yang kami rancang belum dicoba secara langsung sehingga belum ditemukan
> tegangan set point yang sesuai dengan kondisi lapangan. (2011)

> Nilai ini memang masih di bawah dari maksimum heat flux pada reaktor BWR/6. Akan tetapi
> eksperimen ini dilakukan pada tekanan atmosfer jauh dari tekanan operasi. (2022)

Saat menyunting, jangan menghaluskan atau menghapus pengakuan keterbatasan. Ini bagian
dari suara, bukan kelemahan draf.

### 2.8 *kita* inklusif dalam penalaran **[K][S]**

Dipakai saat mengajak pembaca menelusuri perhitungan, bahkan di dalam paper.

> Karena terdapat dua termokopel maka kita bisa mendapatkan dua nilai bilangan Nusselt.
> Jika nilai dari *quality* dihitung kita akan mendapatkan nilai yang negatif.

Untuk pelaku penelitian dipakai *kami*, tidak pernah *penulis* di badan teks. *Penulis*
hanya muncul di bagian Ucapan Terima Kasih.

### 2.9 Kalimat panjang dibangun lewat subordinasi **[K][S]**

Korpus memakai kalimat 28 kata ke atas pada 8,3 sampai 14,9 persen kalimat, dengan
koordinasi rerata 0,29 sampai 0,67 per kalimat panjang. Panjangnya berasal dari klausa
relatif, aposisi, dan keterangan sisipan, bukan dari rangkaian *A, dan B, dan C*.

> Nilai *coefficient heat transfer* minimum didapatkan sebesar 3,43 kW/m2 pada laju
> aliran massa 0,013 kg/s dan nilai maksimum sebesar 11,710 kW/m2 pada laju aliran
> massa 0,037 kg/s.

Penyimpangan pada sumbu ini terbukti memicu penandaan detektor, dan ia satu-satunya
temuan detektor yang layak diperbaiki. Rinciannya di bagian Detektor pada SKILL.md.

### 2.10 Kalimat pendek penutup paragraf **[K][S]**

Setelah satu atau dua kalimat penjelas panjang, paragraf ditutup kalimat pendek yang
menyimpulkan atau menilai.

> Manfaatnya sangat besar untuk meningkatkan kualitas permainan. (2008)
> Efisiensinya sendiri masih rendah.
> Hasilnya menunjukkan tren positif di seluruh domain yang diukur. (2025)

Inilah sumber utama variasi ritme. Kalau simpangan baku panjang kalimat terlalu rendah,
di sinilah perbaikannya dilakukan.

### 2.11 *si* dan sisipan santai dalam teks teknis **[T]**

Muncul di dua dokumen 2011, hilang dari korpus 2021 ke atas.

> waktu hidup si baterai · akhirnya Einstein membuang si Λ

Turunkan ke opsional. Pakai hanya untuk buku ajar atau materi kuliah, tidak untuk jurnal.

### 2.12 Pembuka *Pada X, ...* **[X] pudar**

Dulu penanda dominan: 15,2% kalimat di Baterai Nuklir Beta, 16,7% di Fuel Design.
Sekarang turun ke 3,8% (Paper SNIV), 6,3% (Paper Pengabdian), dan 0% (Jurnal Pengmas).

**Jangan lagi dijadikan sasaran.** Biarkan muncul alami di kisaran 4 sampai 6%. Menyuntik
pola ini ke teks baru akan menghasilkan suara Prib 2011, bukan Prib sekarang.

### 2.13 Register semi-formal **[T]**

Hanya satu sampel (`Cara membuat yoghurt`, 2009, tulisan blog). Semua tentatif:

- Partikel percakapan: *sih*, *ko*, *aja*, *ga* (bukan *nggak* atau *tidak*), *udah*
- Pertanyaan retoris menyela ke pembaca: "hayo kira-kira berapa derajat Celcius kah?"
- Sisipan kurung bernada bercanda: "(ga wajib sih)", "(ya iyalah...)"
- Pembuka berjangkar waktu konkret: "Hari Sabtu tanggal 14 Februari 2009 yang lalu saya..."
- Penutup merendah dan mengundang koreksi: "Correct Me If I Wrong (CMIIW)"
- **Refleks fisikawan bocor ke konteks santai**: suhu resep yoghurt ditulis dalam Kelvin
  (334 K, 313 K, 314 K). Penanda paling sulit dipalsukan dalam korpus. Kalau menulis teks
  santai bertopik teknis, satuan dan presisi tetap dibawa masuk apa adanya.

---

## 3. Yang bukan suara ini

Daftar tindakan saat menyunting keluaran AI. Semuanya absen dari korpus bersih, jadi
kemunculannya berarti sisipan model.

| Absen dari korpus | Tindakan |
|---|---|
| Em dash dan en dash di prosa | ganti koma, titik dua, kurung, atau pecah kalimat |
| Enumerasi *seperti a, b, c* | jadikan objek langsung, atau daftar bernomor terpisah |
| Verba ringan berlebih (di atas 0,40 per 100 kata) | padatkan sebagian, bukan semuanya |
| *merupakan* sebagai kopula default | ganti *adalah*, atau bongkar jadi verba penuh |
| Pembuka formula (*Seiring dengan perkembangan teknologi*) | ganti pernyataan spesifik |
| Penutup formula (*Dengan demikian dapat disimpulkan bahwa*) | tutup dengan temuan konkret |
| Triplet berima (*efektif, efisien, berkelanjutan*) | sisakan satu |
| *yang mana* dan *dimana* sebagai pronomina relatif | ganti *sehingga*, *yang*, atau pecah kalimat |
| Intensifier kosong (*berperan vital*, *menjadi faktor kunci*) | hapus atau ganti angka |
| Klaim tanpa angka atau rujukan gambar | tambahkan dasar, atau turunkan jadi dugaan |
| Kalimat seragam 24 kata ke atas | pecah, sisipkan kalimat pendek penutup paragraf |
| Koordinasi di atas 1,50 | ubah sebagian jadi subordinasi, jangan pecah semuanya |
| Prosa lebih mampat daripada korpus (pemadat di bawah 45 per 1.000 kata) | kembalikan frasa yang wajar |

**Koreksi terhadap versi awal.** Versi 1.0 menyatakan bahwa kalimat berjalin longgar
dalam korpus adalah artefak draf dan bukan penanda gaya. Bagian itu **salah**, dan sudah
dibuktikan salah oleh suntingan penulis atas teks buatan. Setiap suntingannya bergerak
melawan arahan pemampatan: menambah *akan*, *untuk*, *melalui*, *suatu*, mengubah
*bukan konvensi kosong* jadi *bukanlah suatu konvensi yang kosong*, dan memakai
subordinator ganda *Karena ..., sehingga membuat ...*. Kelonggaran itu cara penulis
menulis, bukan cacat draf.

Yang tetap berlaku: **jangan mengarang salah ketik.** Korpus memang memuat banyak salah
ketik, tetapi menyisipkannya dengan sengaja bukan menulis seperti penulis, melainkan
memalsukan cacat. Perbaiki salah ketik, biarkan kelonggarannya.

---

## 4. Contoh penerapan

**Keluaran AI:**

> Dalam era perkembangan teknologi nuklir yang semakin pesat, baterai nuklir merupakan
> salah satu inovasi yang memegang peranan penting. Teknologi ini melakukan pemanfaatan
> terhadap proses peluruhan bahan radioaktif, yang mana hal ini memberikan pengaruh
> terhadap dihasilkannya arus listrik searah. Berbagai keunggulan seperti efisiensi,
> keandalan, dan umur pakai yang panjang menjadikannya solusi yang menjanjikan untuk masa
> depan energi.

**Setelah disunting ke preset:**

> Pada baterai nuklir tidak digunakan reaksi fisi, melainkan peluruhan bahan radioaktif.
> Peluruhan itu melepaskan elektron yang menumbuk semikonduktor dan menghasilkan arus
> searah. Keunggulannya ada pada umur pakai, karena sebagian jenis bertahan sampai
> puluhan tahun. Efisiensinya sendiri masih rendah.

Perubahan: pembuka formula dibuang, dua verba ringan dipadatkan, *merupakan* diganti,
*yang mana* dihapus, enumerasi *seperti* dan triplet dibuang, temuan disusul sebab
langsung, kalimat pendek penutup ditambahkan, keterbatasan diakui terbuka. Rerata turun
dari 28 ke 17 kata, simpangan baku naik dari 4 ke 8.

---

## 5. Yang masih kurang

**Catatan rentang 2015 sampai 2022.** Penulis menempuh S3 pada masa itu dan menulis
hampir seluruhnya dalam bahasa Inggris. Rentang itu **tidak akan terisi**, dan tidak perlu
dikejar. Pita akademik preset ini karena itu bersandar pada 2011, 2012, dan 2021. Catat
sebagai batas yang diketahui, bukan sebagai kekurangan yang tertunda.

| Register | Status | Kebutuhan |
|---|---|---|
| Akademik jurnal | **memadai** untuk kerja awal, 2 dokumen bersih 2021 sampai 2022 | 2 sampai 3 paper lagi 2023 ke atas, penulis tunggal atau bagian sendiri ditandai |
| Bahan ajar | **kosong**, cosmology bab4 hanya proksi catatan baca | 2 sampai 3 bab modul atau diktat terkini |
| Semi-formal | 1 dokumen 2009, register blog | 5 sampai 10 surel atau laporan internal; blog bukan pengganti surel |
| Proposal internal | **rintisan**, 1 dokumen 166 kata | 3 sampai 5 abstrak proposal atau laporan kemajuan pra-2023 |
| Dokumen kelembagaan | **kosong** | proposal S3 Terapan, dokumen akreditasi, RPS |

Status `Jurnal_Pengmas_Pade_rev2h` sudah dikonfirmasi terpengaruh AI dan diturunkan ke
tingkat D. Yang tersisa satu: tahun terbit Paper SNIV.

Karena rentang 2015 sampai 2022 berbahasa Inggris dan tidak akan terisi, tambahan yang
paling berguna sekarang adalah dokumen **pra-2023 berbahasa Indonesia** yang belum
tergabung: bab modul, diktat, surel, dan abstrak proposal. Semuanya menambah register,
bukan menambah tahun.


---

## 6. Hipotesis yang sudah diuji dan gugur

Dicatat agar tidak diulang.

| Hipotesis | Uji | Hasil |
|---|---|---|
| Skor rendah karena teks terlalu pendek | Potongan 516 kata tulisan manusia dipindai | **Gugur.** 100 persen human pada panjang yang sama |
| Skor rendah karena kekhususan faktual rendah | Versi dengan sitasi, tahun, dan nilai terukur, kepadatan 108,8 setara kontrol | **Gugur telak.** Turun ke 2 persen human |
| Kepadatan partikel penegas menentukan | Diukur lintas korpus | **Gugur.** Tidak monoton: 14,42 memberi 98%, 1,86 memberi 80% |
| Deret pembuka seragam adalah tell | Diukur lintas korpus | **Sebagian.** Nyata tapi korpus penulis lebih parah, jadi tanpa ambang |
| Koordinasi klausa berlebih adalah tell | Diukur lintas korpus | **Sebagian.** Kontrol manusia 1,50 dan tetap 100 persen |
| Pemampatan berlebih menjauhkan dari suara penulis | Suntingan penulis atas teks buatan | **Bertahan.** Semua suntingan menambah kelonggaran |

| Kepadatan pemadat menentukan skor detektor | v5 longgar (pemadat 122, dalam rentang korpus) dipindai | **Gugur.** 1 persen human, setara v4 yang mampat |

Catatan penutup detektor, setelah tujuh pengukuran: teks buatan mendarat di 1 sampai 2
persen apa pun setelan gayanya, tulisan penulis di 80 sampai 100 persen, dan satu-satunya
yang pernah berada di tengah (45 persen) adalah teks buatan yang disunting tangan
penulis. Sumbu yang membedakan bukan gaya yang dapat disetel. Berhenti mencari kenopnya.
