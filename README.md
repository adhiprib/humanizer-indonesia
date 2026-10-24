# Humanizer Indonesia

Skill Claude untuk menyunting teks bahasa Indonesia agar tidak terbaca kaku, tidak terasa
seperti keluaran model atau terjemahan, dan kembali ke gaya penulisnya. Skill ini juga
bisa dipakai untuk mengaudit berkas yang sudah disunting model lain, misalnya hasil
suntingan Gemini atau ChatGPT.

Versi saat ini: **1.5** (9 September 2026). Riwayat perubahan ada di bagian atas
[`SKILL.md`](SKILL.md).

## Penting: ini bukan alat untuk lolos detektor AI

Skill ini **tidak** dibuat untuk menyiasati detektor AI seperti GPTZero, dan memang tidak
akan berhasil untuk itu. Teks yang disunting dengan skill ini **tetap akan terdeteksi
sebagai tulisan AI**. Pengukuran yang tercatat di `SKILL.md` menunjukkan bahwa semua
penyetelan gaya otomatis mendarat di skor human sekitar 1 sampai 2 persen pada GPTZero.
Satu-satunya hal yang terbukti menggeser skor secara berarti adalah suntingan tangan
penulisnya sendiri.

Tujuan skill ini adalah membuat teks **lebih luwes dan enak dibaca**: membuang
nominalisasi yang menumpuk, konektor yang berlebihan, ritme kalimat yang seragam, kalkir
dari bahasa Inggris, dan pola khas keluaran model lainnya. Hasilnya adalah **draf untuk
disunting manusia**, bukan teks jadi. Membaca ulang dan menyunting dengan tangan tetap
menjadi tugas penulis.

Gunakan dengan jujur. Bila institusi, jurnal, atau dosen Anda mewajibkan pengungkapan
pemakaian AI, ungkapkan.

## Tentang berkas rujukan suara

Berkas [`references/voice-prib-id.md`](references/voice-prib-id.md) adalah **preset
suara milik penulis repo ini** (Pribadi Mumpuni Adhi, disingkat PRIB), disusun dari
korpus tulisannya sendiri tahun 2008 sampai 2025. Ambang pada `scripts/metrik.py` juga
dikalibrasi terhadap korpus yang sama.

Berkas ini disertakan sebagai contoh lengkap seperti apa preset suara yang baik. **Anda
bebas menggantinya sesuai kebutuhan**, dan sebaiknya memang diganti bila Anda ingin
hasil suntingan mengikuti gaya Anda sendiri. Lihat bagian
[Mengganti preset suara](#mengganti-preset-suara).

Bila tidak ada preset yang cocok, skill ini akan memakai suara netral yang wajar untuk
registernya dan menyatakan terus terang bahwa kalibrasi suara tidak dilakukan.

## Isi repo

| Berkas | Isi |
|---|---|
| `SKILL.md` | Instruksi utama skill: alur kerja delapan langkah, kaidah, contoh |
| `references/id-ai-tells.md` | Katalog pola khas tulisan AI dalam bahasa Indonesia, positif palsu, dan register yang dikecualikan |
| `references/voice-prib-id.md` | Preset suara penulis (contoh, silakan diganti) |
| `scripts/metrik.py` | Pengukur metrik gaya teks Indonesia, tanpa dependensi di luar pustaka standar Python |

## Pemasangan

**Claude.ai (web, desktop, mobile).** Unduh repo ini sebagai ZIP (tombol *Code* lalu
*Download ZIP*), pastikan folder `humanizer-indonesia` berada di akar arsip, lalu unggah
lewat pengaturan Skills di Claude. Panduan resminya ada di
[support.claude.com](https://support.claude.com).

**Claude Code.** Salin folder ini ke direktori skill pribadi Anda:

```bash
git clone https://github.com/<akun>/humanizer-indonesia.git ~/.claude/skills/humanizer-indonesia
```

## Cara memakai

Panggil dengan `/humanizer-id`, atau cukup minta dalam bahasa biasa, misalnya
"rapikan bahasa abstrak ini", "biar tidak kaku", "kalimatnya masih terasa terjemahan",
atau "audit hasil suntingan Gemini ini".

Skill ini cocok untuk paper, abstrak, prosiding, proposal, buku ajar, modul, diktat,
laporan, dan surel berbahasa Indonesia. Skill ini **tidak** dipakai untuk teks berbahasa
Inggris, dokumen hukum (paten, kontrak, peraturan), kutipan langsung, atau instrumen
penelitian tervalidasi.

### Menjalankan pengukur metrik secara langsung

```bash
python3 scripts/metrik.py berkas.md --preset akademik
cat teks.txt | python3 scripts/metrik.py -
```

Preset yang tersedia: `akademik`, `ajar`, `semiformal`.

## Mengganti preset suara

1. Kumpulkan contoh tulisan Anda sendiri, idealnya yang ditulis **tanpa bantuan AI**.
   Semakin banyak dan semakin beragam registernya, semakin baik.
2. Buat berkas baru, misalnya `references/voice-namaanda-id.md`, dengan mengikuti
   struktur `voice-prib-id.md`: asal dan tingkat kepercayaan korpus, metrik sasaran,
   penanda suara, dan hal yang bukan suara Anda. Claude bisa membantu menyusunnya dari
   contoh tulisan yang Anda berikan.
3. Ubah rujukan di `SKILL.md`, yaitu pada **Langkah 4. Kalibrasi suara** dan tabel
   **Berkas rujukan**, agar menunjuk ke berkas Anda.
4. Bila perlu, sesuaikan ambang di `PRESET` pada `scripts/metrik.py` dengan rentang
   metrik tulisan Anda sendiri. Jalankan skrip pada beberapa tulisan Anda untuk melihat
   rentangnya.

Berkas `voice-prib-id.md` boleh dihapus setelah preset Anda siap.

## Asal-usul

Skill ini dikembangkan dari skill **humanizer** karya blader,
[github.com/blader/humanizer](https://github.com/blader/humanizer) (lisensi MIT), yang
menyunting teks bahasa Inggris berdasarkan panduan *Signs of AI writing* dari Wikipedia.
Terima kasih kepada pembuatnya.

Yang diwarisi dari skill tersebut adalah kerangka kerjanya, yaitu putaran draf, audit,
lalu revisi akhir. Katalog polanya disusun ulang sepenuhnya untuk bahasa Indonesia,
karena pola khas tulisan AI dalam bahasa Indonesia berbeda jauh dari pola dalam bahasa
Inggris. Preset suara, pengukur metrik, dan langkah-langkah kalkir, personifikasi, serta
audit berkas suntingan model lain merupakan tambahan baru.

Untuk menyunting teks berbahasa Inggris, pakai skill aslinya.

## Lisensi

[MIT](LICENSE). Anda bebas memakai, menyalin, mengubah, dan menyebarkan skill ini,
termasuk mengganti preset suaranya, selama pemberitahuan hak cipta dan lisensi tetap
disertakan.
