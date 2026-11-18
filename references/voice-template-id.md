# Preset Suara: [NAMA] (Bahasa Indonesia)

Kerangka kosong untuk menyusun preset suara sendiri. Salin berkas ini menjadi
`voice-namaanda-id.md`, lalu isi setiap bagian dari tulisan Anda sendiri. Contoh preset
yang sudah lengkap ada di `voice-prib-id.md`.

**Berkas ini bukan preset.** Selama masih berisi tanda kurung siku seperti [NAMA], skill
memperlakukannya sebagai kerangka dan tidak memakainya untuk menyunting.

Aturan format: keluaran tidak memuat em dash (U+2014) maupun en dash (U+2013) di badan
prosa, kecuali penulis memang memakainya dan menyatakannya di bagian 2.

---

## 0. Korpus dan dasar bukti

Daftar tulisan yang menjadi dasar preset. Pakai tulisan yang Anda susun sendiri tanpa
bantuan AI. Jika tidak yakin, cantumkan tahunnya: tulisan sebelum 2023 lebih aman sebagai
patokan.

| Tingkat | Dokumen | Tahun | Register | Alasan |
|---|---|---|---|---|
| A. Patokan | [judul] | [tahun] | [akademik, ajar, atau semiformal] | [penulis tunggal, tanpa AI] |
| B. Pendukung | [judul] | [tahun] | [register] | [misalnya catatan kuliah atau blog] |
| D. Tidak dipakai | [judul] | [tahun] | [register] | [misalnya banyak penulis, atau disunting AI] |

Tingkat keyakinan tiap penanda di bagian 2:

- **[K]** terkonfirmasi, muncul di tiga dokumen atau lebih
- **[S]** stabil, muncul pada tulisan lama maupun baru
- **[T]** tentatif, baru dari satu dokumen

## 1. Metrik sasaran

Jalankan `python3 scripts/metrik.py tulisan.md --preset akademik` pada setiap dokumen
tingkat A dan B, lalu salin angkanya ke sini. Angka diambil dari tulisan Anda, bukan dari
norma umum.

| Dokumen | Rerata panjang kalimat | Simpangan baku | Konektor per 100 kata | Kepadatan pemadat |
|---|---|---|---|---|
| [judul] | [angka] | [angka] | [angka] | [angka] |

Rentang yang dipakai sebagai sasaran penyuntingan:

| Metrik | Min | Maks |
|---|---|---|
| Rerata panjang kalimat | [angka] | [angka] |
| Simpangan baku | [angka] | [angka] |
| Kalimat 28 kata ke atas | [persen] | [persen] |
| Konektor per 100 kata | [angka] | [angka] |
| *merupakan* per 1.000 kata | [angka] | [angka] |

Prinsipnya, tulisan Anda sendiri harus lulus. Jika tulisan Anda berstatus PERIKSA pada
ambang bawaan `metrik.py`, ambang itulah yang perlu disesuaikan di `PRESET`, bukan
tulisannya.

## 2. Penanda suara

Kebiasaan yang membuat tulisan terasa sebagai tulisan Anda. Tulis satu subbagian per
kebiasaan, lengkap dengan contoh kalimat asli dari korpus.

### 2.1 [Nama kebiasaan] **[K/S/T]**

[Uraian singkat, misalnya: memakai *adalah* alih-alih *merupakan*; membuka paragraf
langsung dengan angka; memakai *kita* pada penalaran.]

> [Contoh kalimat asli dari dokumen tingkat A.]

### 2.2 [Nama kebiasaan] **[K/S/T]**

[Uraian dan contoh.]

## 3. Yang bukan suara ini

Pola yang tidak pernah muncul di tulisan Anda. Jika muncul di hasil suntingan, pola itu
sisipan model.

| Absen dari korpus | Tindakan |
|---|---|
| [pola] | [penggantinya] |

## 4. Contoh penerapan

Satu paragraf keluaran AI beserta versi yang sudah disunting ke suara Anda.

**Sebelum:**

> [paragraf keluaran AI]

**Sesudah:**

> [paragraf yang sama dalam suara Anda]

## 5. Yang masih kurang

[Register yang belum terwakili, dokumen yang tahunnya belum pasti, atau penanda yang masih
tentatif.]
