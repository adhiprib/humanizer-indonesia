# Memakai humanizer-indonesia di ChatGPT dan Gemini

Folder ini berisi versi portabel skill untuk ChatGPT dan Gemini, termasuk versi web dan
aplikasi HP. Isinya tetap mengacu ke berkas skill di akar repo, jadi tidak ada aturan
yang dicabangkan. Yang ditambahkan hanya dua hal: instruksi ringkas yang muat di kolom
instruksi kedua platform, dan skrip untuk membuat paket berkas pengetahuan.

| Berkas | Isi |
|---|---|
| `INSTRUKSI.md` | Teks yang ditempel ke kolom instruksi Custom GPT atau Gem, sekitar 5.700 karakter |
| `buat_paket.py` | Membuat ZIP datar berisi instruksi dan seluruh berkas skill |

## Membuat paket

```bash
python3 portable/buat_paket.py
```

Hasilnya `portable/dist/humanizer-indonesia-portable.zip`, berisi lima berkas tanpa
folder: `INSTRUKSI.md`, `SKILL.md`, `id-ai-tells.md`, `voice-prib-id.md`, dan
`metrik.py`. Jalankan ulang setiap kali skill diperbarui supaya paketnya ikut mutakhir.
Folder `dist/` tidak ikut di-commit.

## Mana yang dipilih

| Platform | Skrip metrik | Catatan |
|---|---|---|
| ChatGPT, fitur Skills | jalan | Paling dekat dengan cara kerja di Claude. Ketersediaannya bergantung paket akun |
| ChatGPT, Custom GPT | jalan, bila Code Interpreter aktif | Pilihan paling pasti tersedia |
| Gemini, Gem | tidak jalan | Metrik dihitung manual sebagai perkiraan |

## ChatGPT, fitur Skills

ChatGPT memakai format `SKILL.md` yang sama dengan Claude. Unggah ZIP folder skill di akar
repo (yang juga dipakai untuk Claude), bukan paket portabel, lewat menu **Skills** di
profil. Bila menu itu tidak ada di akun Anda, pakai Custom GPT.

## ChatGPT, Custom GPT

1. Buka editor GPT di chatgpt.com. Bila menu pembuatan tidak muncul di aplikasi HP, buka
   chatgpt.com di peramban HP.
2. Pilih tab **Configure**.
3. **Name**: Humanizer Indonesia. **Description**: Menyunting teks bahasa Indonesia agar
   tidak kaku dan tidak terasa seperti terjemahan.
4. **Instructions**: tempel seluruh isi `INSTRUKSI.md`.
5. **Knowledge**: unggah empat berkas lain dari paket, yaitu `SKILL.md`,
   `id-ai-tells.md`, `voice-prib-id.md`, dan `metrik.py`.
6. **Capabilities**: aktifkan **Code Interpreter & Data Analysis** supaya `metrik.py`
   bisa dijalankan.
7. Simpan dengan akses **Only me**, karena `voice-prib-id.md` memuat data korpus pribadi
   penulis.

## Gemini, Gem

1. Buka gemini.google.com, pilih **Gems**, lalu **New Gem**. Bila menu itu tidak ada di
   aplikasi HP, buka situsnya di peramban HP.
2. **Instructions**: tempel seluruh isi `INSTRUKSI.md`. Jangan pakai tombol penulisan
   ulang instruksi otomatis, karena Gemini akan meringkasnya.
3. **Knowledge**: unggah empat berkas yang sama.
4. **Default tool**: biarkan tanpa tool bawaan.

Gem tidak dapat menjalankan `metrik.py`. Instruksinya sudah menyuruh model menghitung
rerata dan simpangan baku secara manual dan menyatakan bahwa angkanya perkiraan. Untuk
pengukuran yang sebenarnya, jalankan `metrik.py` di komputer atau di ChatGPT.

## Bila berkas ditolak saat diunggah

Sebagian platform menolak ekstensi `.md` atau `.py`. Ganti ekstensinya menjadi `.txt`,
misalnya `SKILL.md.txt` dan `metrik.py.txt`. Instruksi sudah menangani nama
`metrik.py.txt`.

## Uji setelah memasang

Tempel paragraf masukan dari bagian **Contoh penuh** di `SKILL.md`, lalu periksa tiga
hal pada hasilnya:

1. Jumlah paragraf dan gagasan sama dengan masukan.
2. Tidak ada em dash, en dash, *merupakan*, atau *yang mana*.
3. Ada daftar keputusan diksi dan tabel metrik sebelum dan sesudah.

Ulangi dengan satu paragraf dari dokumen Anda yang memuat angka, rujukan Gambar atau
Tabel, dan sitasi. Hitung semuanya sebelum dan sesudah. Gemini dan ChatGPT lebih sering
meringkas daripada Claude, dan kehilangan rujukan silang adalah kerusakan yang paling
sering terjadi.

## Batasan

Model lain tidak membaca berkas pengetahuan seteliti Claude membaca skill. Aturan yang
paling penting karena itu ditulis ulang di `INSTRUKSI.md`, bukan hanya dirujuk. Hasilnya
tetap draf untuk disunting manusia, dan tetap tidak dibuat untuk lolos detektor AI.
