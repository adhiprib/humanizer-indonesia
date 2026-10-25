# Memakai humanizer-indonesia di ChatGPT dan Gemini

Folder ini berisi instruksi portabel dan pembuat paket berkas untuk ChatGPT dan Gemini.
Aturan penyuntingan tetap berasal dari `SKILL.md` dan berkas referensi di akar repo,
sehingga tidak ada aturan yang dicabangkan. Versi aturan mengikuti baris versi di
`SKILL.md`. Versi rilis paket dapat berbeda bila perubahannya hanya menyangkut kemasan,
misalnya rilis v1.6.1 yang memuat aturan versi 1.6.

| Berkas | Isi |
|---|---|
| `INSTRUKSI.md` | Teks yang ditempel ke instruksi Project ChatGPT, Custom GPT, atau Gem |
| `buat_paket.py` | Membuat ZIP datar berisi instruksi, berkas skill, dan lisensi |

Video tutorial pemasangan:
[ChatGPT melalui Project](https://youtu.be/1m0B6j2egko) dan
[Gemini melalui Gem](https://youtu.be/5NclZSGfZfk).

## Membuat paket

Jalankan dari akar repo:

```bash
python3 portable/buat_paket.py
```

Hasilnya `portable/dist/humanizer-indonesia-portable.zip`, berisi enam berkas tanpa
folder: `INSTRUKSI.md`, `SKILL.md`, `id-ai-tells.md`, `voice-prib-id.md`, `metrik.py`,
dan `LICENSE`. Ekstrak ZIP itu dulu, karena isi `INSTRUKSI.md` ditempel dan berkas
lainnya diunggah satu per satu. ZIP ini bukan paket plugin.

Unggahan di ChatGPT dan Gemini tidak tersinkron dengan GitHub. Setiap kali skill
diperbarui, jalankan ulang skrip ini lalu ganti berkas yang sudah diunggah. Folder
`dist/` tidak ikut di-commit.

## Pilih jalur

| Jalur | Cara memakai | Skrip metrik |
|---|---|---|
| Project ChatGPT | Instruksi Project dan berkas Project | Jalan bila alat Python tersedia dan skrip dapat diakses |
| Custom GPT | Instructions dan Knowledge, bila editornya ada di akun | Jalan bila kapabilitas analisis data aktif dan skrip dapat diakses |
| Plugin ChatGPT | Skill dikemas sebagai plugin, untuk web, desktop, dan HP | Bergantung alat yang tersedia |
| Skill di ChatGPT desktop atau Codex | Folder skill, sama seperti untuk Claude Code | Bergantung alat yang tersedia |
| Gem di Gemini | Instructions dan Knowledge | Tidak jalan, metrik ditulis *tidak diukur* atau hitungan manual |

Menurut dokumentasi OpenAI, skill mandiri hanya tersedia di aplikasi desktop ChatGPT,
Codex CLI, dan ekstensi IDE. Di ChatGPT web dan HP, skill hanya dapat dipakai bila
dikemas sebagai plugin. Karena itu tidak ada menu umum untuk mengunggah ZIP skill
dari profil ChatGPT web atau HP.

Ketersediaan Custom GPT juga sedang berubah. OpenAI sedang memindahkan Custom GPT ke
plugin, tetapi panduan migrasinya ditulis untuk workspace Enterprise dan tidak
menyebut jadwal untuk paket lain. Untuk akun pribadi, Project adalah jalur yang paling
aman.

## ChatGPT melalui Project

1. Buat Project baru khusus penyuntingan bahasa Indonesia.
2. Tempel isi `INSTRUKSI.md` ke instruksi Project. Bila kolomnya terlalu pendek,
   unggah `INSTRUKSI.md` sebagai berkas dan tulis di kolom instruksi bahwa berkas itu
   wajib dibaca dan diikuti.
3. Unggah `SKILL.md`, `id-ai-tells.md`, `voice-prib-id.md`, dan `metrik.py` sebagai
   berkas Project.
4. Mulai percakapan dari dalam Project, lalu sebut registernya: `akademik`, `ajar`,
   atau `semiformal`.
5. Untuk mengaudit hasil model lain, lampirkan naskah sebelum dan sesudah disunting.

Berkas yang diunggah ke Project berfungsi sebagai rujukan. Mengunggah `SKILL.md` ke
Project tidak sama dengan memasangnya sebagai skill.

## ChatGPT melalui Custom GPT

Pakai jalur ini bila editor Custom GPT masih tersedia di akun Anda.

1. Buka editor GPT di ChatGPT web, sebaiknya dari peramban laptop karena tidak semua
   pengaturan tampil di aplikasi HP.
2. Isi nama **Humanizer Indonesia** dan deskripsi singkat tugasnya.
3. **Instructions**: tempel seluruh isi `INSTRUKSI.md`.
4. **Knowledge**: unggah empat berkas pendukung. Aturan yang wajib dipatuhi sudah ada
   di Instructions, karena isi Knowledge hanya dicari saat diperlukan dan tidak selalu
   dibaca utuh.
5. Aktifkan **Code Interpreter & Data Analysis** atau kapabilitas analisis data dengan
   nama lain yang setara.
6. Simpan dengan akses privat selama pengujian. Pengaturan ini tidak membuat berkas di
   repo menjadi privat, karena `voice-prib-id.md` sudah terbuka di GitHub.
7. Jalankan uji di bawah. Kapabilitas yang aktif belum tentu berarti skrip benar-benar
   dijalankan pada setiap permintaan.

Berkas Knowledge belum tentu tersedia sebagai berkas utuh bagi alat eksekusi. Bila
skrip tidak dapat diakses, lampirkan `metrik.py` langsung di percakapan.

## ChatGPT melalui skill atau plugin

Di aplikasi desktop ChatGPT dan Codex, folder repo ini dapat dipasang sebagai skill
mengikuti panduan lokasi skill di produk tersebut. Untuk web dan HP, skill perlu
dikemas sebagai plugin mengikuti panduan plugin resmi OpenAI. Paket ZIP dari
`buat_paket.py` maupun ZIP folder untuk Claude tidak dapat langsung dipasang sebagai
plugin.

## Gemini melalui Gem

1. Buka gemini.google.com di peramban, pilih **Gems**, lalu buat Gem baru. Aplikasi
   Gemini di HP dipakai untuk menjalankan Gem yang sudah dibuat, sedangkan pembuatan
   dan pengubahannya dilakukan di situs web.
2. **Name**: Humanizer Indonesia.
3. **Instructions**: tempel seluruh isi `INSTRUKSI.md`. Jangan pakai tombol penulisan
   ulang instruksi otomatis, karena Gemini akan meringkasnya.
4. **Knowledge**: unggah empat berkas pendukung.

Berkas Knowledge di Gem diperlakukan sebagai dokumen rujukan dan tidak dapat
dijalankan, jadi `metrik.py` tidak jalan di sana. Instruksinya sudah mengatur bahwa
metrik ditulis *tidak diukur*, atau diberi label *hitungan manual* lengkap dengan
panjang tiap kalimat. Untuk angka yang sebenarnya, jalankan `metrik.py` di komputer.

## Bila berkas ditolak saat diunggah

Pemilih berkas di peramban HP kadang menolak ekstensi `.md` atau `.py`. Tambahkan
akhiran `.txt` tanpa mengubah isinya, misalnya `SKILL.md.txt` dan `metrik.py.txt`.
Instruksi sudah menangani nama `metrik.py.txt`, yaitu menyalinnya kembali menjadi
`metrik.py` sebelum dijalankan.

## Uji setelah memasang

1. Tanyakan versi skill dan daftar berkas yang berhasil dibaca. Jawabannya harus
   menyebut versi dari `SKILL.md`, bukan tebakan.
2. Tempel paragraf masukan dari bagian **Contoh penuh** di `SKILL.md`. Periksa jumlah
   paragraf dan gagasan, register, tanda baca, dan daftar keputusan diksi. Kata
   *merupakan* tidak harus nol, karena ambangnya mengikuti preset.
3. Bila skrip dapat dijalankan, ukur teks sebelum dan sesudah dengan preset yang sama,
   lalu cocokkan hasilnya dengan `metrik.py` di komputer untuk teks yang identik.
4. Ulangi dengan naskah yang memuat angka, satuan, sitasi, rujukan Gambar dan Tabel,
   persamaan, dan blok kode. Pastikan semuanya tetap utuh.
5. Uji juga saat skrip tidak dapat dijalankan. Hasil yang benar menyebut keterbatasan
   itu dan tidak memuat angka rekaan.

## Batasan

Belum ada pengujian lintas model yang cukup untuk menyimpulkan bahwa ChatGPT atau
Gemini lebih sering meringkas daripada Claude. Yang tercatat baru satu kasus, yaitu
perbandingan dua bab diktat pada 9 September 2026, ketika versi Gemini menghapus
rujukan silang dan angka terverifikasi. Catat setiap temuan baru beserta model,
tanggal, dan naskahnya.

Instruksi tidak menjamin semua rujukan dibaca utuh atau setiap aturan selalu dipatuhi.
Hasilnya tetap draf untuk disunting manusia dan tidak dibuat untuk lolos detektor AI.

## Dokumentasi resmi

Diperiksa 25 Oktober 2026.

- [Build skills](https://learn.chatgpt.com/docs/build-skills)
- [Build plugins](https://learn.chatgpt.com/docs/build-plugins)
- [Projects and chats](https://learn.chatgpt.com/docs/projects)
- [Moving your custom GPT workflows to plugins](https://learn.chatgpt.com/docs/migrate-custom-gpts)

Petunjuk Gem diperiksa silang oleh Gemini pada tanggal yang sama. Nama kolom, batas
unggahan, dan ketersediaan editor pada akun tertentu belum diuji langsung lewat
antarmuka.
