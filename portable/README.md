# Memakai humanizer-indonesia di ChatGPT dan Gemini

Folder ini berisi instruksi portabel dan pembuat paket berkas untuk ChatGPT dan Gemini.
Aturan penyuntingan tetap berasal dari `SKILL.md` dan berkas referensi di akar repo,
sehingga tidak ada aturan yang dicabangkan. Versi aturan mengikuti baris versi di
`SKILL.md`. Versi rilis paket dapat berbeda bila perubahannya hanya menyangkut kemasan,
misalnya rilis v1.6.1 yang memuat aturan versi 1.6.

| Berkas | Isi |
|---|---|
| `INSTRUKSI.md` | Teks yang ditempel ke instruksi Project ChatGPT, Custom GPT, atau Gem, sekaligus isi `SKILL.md` paket skill Gemini |
| `buat_paket.py` | Membuat ZIP datar untuk ChatGPT dan Gem, serta paket skill untuk Gemini |

Video tutorial pemasangan:
[ChatGPT melalui Project](https://youtu.be/1m0B6j2egko) dan
[Gemini melalui Gem](https://youtu.be/5NclZSGfZfk). Video Gemini memakai Gem, yang mulai
17 November 2026 dipindahkan bertahap menjadi skill. Langkah skill ada di bagian
**Gemini melalui skill** di bawah.

## Membuat paket

Jalankan dari akar repo:

```bash
python3 portable/buat_paket.py
```

Hasilnya ada di `portable/dist/`:

| Hasil | Untuk | Isi |
|---|---|---|
| `humanizer-indonesia-portable.zip` | ChatGPT dan Gem | Enam berkas tanpa folder: `INSTRUKSI.md`, `SKILL.md`, `id-ai-tells.md`, `voice-prib-id.md`, `metrik.py`, `LICENSE` |
| `humanizer-indonesia-gemini-skill.zip` dan folder `humanizer-indonesia/` | Skill Gemini | `SKILL.md`, `aturan-lengkap.md`, `id-ai-tells.md`, `voice-prib-id.md`, `LICENSE.txt` |

ZIP datar diekstrak dulu, karena isi `INSTRUKSI.md` ditempel dan berkas lainnya
diunggah satu per satu. ZIP ini bukan paket plugin.

Pada paket skill Gemini, `SKILL.md` dibangkitkan dari frontmatter `SKILL.md` repo dan isi
`INSTRUKSI.md`, sedangkan `SKILL.md` repo ikut sebagai `aturan-lengkap.md`. Nama itu
dipakai karena Gemini mewajibkan berkas bernama `SKILL.md` di akar paket sebagai
instruksi skill. Seluruh berkas diletakkan di akar tanpa subfolder, sama dengan susunan
ZIP yang diunduh dari Gemini. `metrik.py` tidak disertakan, karena Gemini Chat menolak
menjalankan skill yang memuat skrip (lihat **Skrip metrik** di bagian Gemini), dan
rujukan ke skrip itu di `SKILL.md` paket ikut disesuaikan. `LICENSE` diberi ekstensi
`.txt` karena berkas tanpa ekstensi tidak tercantum di daftar jenis berkas yang didukung.

Unggahan di ChatGPT dan Gemini tidak tersinkron dengan GitHub. Setiap kali skill
diperbarui, jalankan ulang skrip ini lalu ganti berkas yang sudah diunggah. Di Gemini,
pakai **Replace skill**, karena berkas skill hanya dapat diganti dengan mengunggah ulang
seluruh skill beserta berkas rujukannya. Folder `dist/` tidak ikut di-commit.

## Pilih jalur

| Jalur | Cara memakai | Skrip metrik |
|---|---|---|
| Project ChatGPT | Instruksi Project dan berkas Project | Jalan bila alat Python tersedia dan skrip dapat diakses |
| Custom GPT | Instructions dan Knowledge, bila editornya ada di akun | Jalan bila kapabilitas analisis data aktif dan skrip dapat diakses |
| Plugin ChatGPT | Skill dikemas sebagai plugin, untuk web, desktop, dan HP | Bergantung alat yang tersedia |
| Skill di ChatGPT desktop atau Codex | Folder skill, sama seperti untuk Claude Code | Bergantung alat yang tersedia |
| Gem di Gemini | Instructions dan Knowledge, selama Gem belum dipindahkan ke skill | Tidak jalan, metrik ditulis *tidak diukur* atau hitungan manual |
| Skill di Gemini | Unggah paket skill, lalu panggil dengan `@` di chat | Tidak disertakan; metrik ditulis *tidak diukur* atau hitungan manual |

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

## Gemini melalui skill

Mulai 17 November 2026, Gem pada akun Google pribadi dipindahkan menjadi skill secara
otomatis dan bertahap, tidak serentak untuk semua akun. Akun Workspace bisnis menyusul
pada Maret 2027 dan akun pendidikan pada Juni 2027. Selama Gem di akun belum dipindahkan,
jalur **Gemini melalui Gem** di bawah tetap dapat dipakai.
Skill Gemini mensyaratkan pengguna berusia 18 tahun ke atas dan masuk dengan akun Google.

Jika Gem humanizer-indonesia sudah dipindahkan, skill hasilnya memuat aturan versi yang
terpasang di Gem itu, dan pemindahan otomatis belum tentu membawa setiap rincian dengan
benar. Ganti dengan paket versi terbaru lewat salah satu cara di bawah.

**Cara A, unggah ZIP (dianjurkan).**

1. Buka gemini.google.com di peramban laptop. Unggah skill hanya tersedia di aplikasi web.
2. Buka halaman **Skills**, pilih **Create**, lalu **Upload**.
3. Seret dan lepas `humanizer-indonesia-gemini-skill.zip` ke jendela unggah, atau klik
   tautan **files** lalu pilih ZIP itu.
4. Periksa nama, deskripsi, dan instruksi yang terbaca, lalu pilih **Create**. Jangan
   memakai **Edit with Gemini** untuk merapikan instruksi, karena Gemini akan meringkasnya.

ZIP hanya diterima jika belum ada skill bernama `humanizer-indonesia` di akun. Jika skill
itu sudah ada, misalnya hasil pemindahan Gem atau unggahan versi sebelumnya, buka skill
tersebut lalu pilih **More** dan **Replace skill**, atau hapus dulu skill lamanya.

Skill yang sudah dibuat dapat diunduh kembali dari Gemini sebagai ZIP. Unduhan itu berisi
`SKILL.md` dan berkas rujukan di akar ZIP tanpa subfolder, sama dengan susunan paket ini,
sehingga dapat dipakai sebagai cadangan atau dibagikan.

**Cara B, buat manual.** Pakai cara ini jika ZIP ditolak. Pilih **Create**, lalu
**Create manually**. Formulirnya berisi tiga kolom. Isi **Name** dengan
`humanizer-indonesia`, isi **Description** dengan teks `description` dari frontmatter
`SKILL.md` paket, lalu tempel isi `SKILL.md` paket di bawah frontmatter ke
**Instructions**. Pilih **Add files** di kanan atas, lalu tambahkan `aturan-lengkap.md`,
`id-ai-tells.md`, dan `voice-prib-id.md` satu per satu lewat tautan **files**, karena
seret dan lepas berkas lepasan tidak berfungsi di jendela ini pada uji 18 November 2026.
Jangan menambahkan `metrik.py`. Jendela ini hanya menerima PDF, CSV, PY, TXT, dan MD.
`LICENSE.txt` boleh dilewati. Setelah itu pilih **Create**.

**Memakai skill.** Di chat, ketik `@`, pilih humanizer-indonesia, lalu tempel teks dan
sebut registernya. Pada uji 18 November 2026, skill dipanggil dengan `@`; versi aplikasi
yang lebih lama memakai `/`. Gemini juga dapat memakai skill yang aktif secara otomatis
ketika relevan, tetapi memanggilnya secara eksplisit lebih dapat diandalkan.

**Skrip metrik.** Dokumentasi Google menerima `.py` sebagai berkas skill, tetapi pada uji
18 November 2026 Gemini Chat menyatakan skill yang memuat `metrik.py` sudah terpasang
namun tidak dapat dijalankan di Gemini Chat karena mengandung skrip yang dapat
dieksekusi. Karena itu `metrik.py` dikeluarkan dari paket skill Gemini. Metrik ditulis
*tidak diukur*, atau diberi label *hitungan manual* lengkap dengan panjang tiap kalimat.
Untuk angka yang sebenarnya, jalankan `metrik.py` di komputer. Jika Gemini menawarkan
untuk menghapus skrip dari skill, tolak dan unggah ulang paket ini saja, karena
pengubahan oleh Gemini dapat meringkas instruksinya.

## Gemini melalui Gem

Jalur ini untuk akun yang Gem-nya belum dipindahkan ke skill. Menurut pemberitahuan di
halaman Gems, Gem tetap dapat dipakai dan diubah sampai dipindahkan, dan pemindahannya
berjalan bertahap. Pakai `humanizer-indonesia-portable.zip`. Akun yang sudah memiliki
menu Skills dapat memakai kedua jalur sekaligus selama Gem-nya belum dipindahkan.

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

Ketika Gem ini nanti dipindahkan, Google menyebut sebagian berkas Gem mungkin perlu
diselamatkan sendiri. Berkas Knowledge humanizer-indonesia semuanya ada di paket skill,
jadi tidak ada yang perlu diselamatkan. Ganti saja isi skill hasil pemindahan dengan
paket skill Gemini lewat **Replace skill**.

## Memakai preset suara sendiri

`voice-prib-id.md` adalah preset suara penulis repo ini. Untuk memakai suara Anda sendiri,
susun berkas `voice-namaanda-id.md` dari kerangka `references/voice-template-id.md`
dengan prompt di README utama, bagian **Memakai preset suara sendiri**. Setelah itu:

- **Project ChatGPT, Custom GPT, atau Gem:** unggah berkas preset Anda bersama berkas lain.
  `voice-prib-id.md` boleh tidak diunggah.
- **Skill Gemini:** tambahkan berkas preset ke dalam ZIP paket skill sebelum diunggah, atau
  lewat **Add files** pada formulir manual.

Instruksi portabel mengenali berkas apa pun bernama `voice-*.md`, jadi isi `INSTRUKSI.md`
tidak perlu diubah. Tanpa preset, Anda tetap dapat melampirkan contoh tulisan sendiri di
percakapan.

## Bila berkas ditolak saat diunggah

Pemilih berkas di peramban HP kadang menolak ekstensi `.md` atau `.py`. Tambahkan
akhiran `.txt` tanpa mengubah isinya, misalnya `SKILL.md.txt` dan `metrik.py.txt`.
Instruksi sudah menangani nama `metrik.py.txt`, yaitu menyalinnya kembali menjadi
`metrik.py` sebelum dijalankan.

## Uji setelah memasang

1. Tanyakan versi skill dan daftar berkas yang berhasil dibaca. Jawabannya harus
   menyebut versi dari `SKILL.md` (di paket Gemini: `aturan-lengkap.md`), bukan tebakan.
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

Dokumentasi OpenAI diperiksa 25 Oktober 2026.

- [Build skills](https://learn.chatgpt.com/docs/build-skills)
- [Build plugins](https://learn.chatgpt.com/docs/build-plugins)
- [Projects and chats](https://learn.chatgpt.com/docs/projects)
- [Moving your custom GPT workflows to plugins](https://learn.chatgpt.com/docs/migrate-custom-gpts)

Dokumentasi Google diperiksa 18 November 2026:

- [Create & manage skills for Gemini Apps](https://support.google.com/gemini/answer/17094296)
- [About the transition from Gems to skills](https://support.google.com/gemini/answer/18560919)

Unggah ZIP, formulir **Create manually**, jendela **Add files**, unduhan skill, penolakan
skill berskrip di Gemini Chat, pemanggilan skill tanpa `metrik.py` dengan `@`, dan
pemberitahuan pemindahan Gem sudah diuji langsung pada akun pribadi penulis pada
18 November 2026. Tombol **Replace skill** dan **Edit with Gemini** diambil dari
dokumentasi dan belum diuji.
