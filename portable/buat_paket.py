#!/usr/bin/env python3
"""
buat_paket.py - membuat paket portabel humanizer-indonesia untuk ChatGPT dan Gemini.

Dua paket dibuat dari berkas yang sedang ada di repo, sehingga isinya selalu sama
dengan versi skill di repo dan tidak ada aturan yang dicabangkan.

1. humanizer-indonesia-portable.zip
   ZIP datar untuk Project ChatGPT, Custom GPT, dan Gem di Gemini (selama akun belum
   berpindah ke skill). INSTRUKSI.md ditempel ke kolom instruksi, berkas lainnya
   diunggah satu per satu.

2. humanizer-indonesia-gemini-skill.zip, beserta folder humanizer-indonesia/
   Skill Gemini (pengganti Gem sejak 17 November 2026). SKILL.md di akar paket
   dibangkitkan dari frontmatter SKILL.md repo dan isi INSTRUKSI.md. Aturan lengkap
   dari SKILL.md repo ikut sebagai aturan-lengkap.md. Semua berkas berada di akar,
   tanpa subfolder, sama dengan susunan ZIP yang diunduh dari Gemini. metrik.py tidak
   disertakan, karena pada uji 18 November 2026 Gemini Chat menolak menjalankan skill
   yang memuat skrip; rujukan ke metrik.py di instruksi ikut disesuaikan.

Pakai, dari akar repo atau dari folder portable:
    python3 portable/buat_paket.py

Hasil ada di portable/dist/.
"""

import pathlib
import re
import shutil
import zipfile

PORTABLE = pathlib.Path(__file__).resolve().parent
AKAR = PORTABLE.parent
DIST = PORTABLE / "dist"

SKILL = AKAR / "SKILL.md"
INSTRUKSI = PORTABLE / "INSTRUKSI.md"
TELLS = AKAR / "references" / "id-ai-tells.md"
VOICE = AKAR / "references" / "voice-prib-id.md"
METRIK = AKAR / "scripts" / "metrik.py"
LISENSI = AKAR / "LICENSE"

BERKAS_CHATGPT = [
    (INSTRUKSI, "INSTRUKSI.md"),
    (SKILL, "SKILL.md"),
    (TELLS, "id-ai-tells.md"),
    (VOICE, "voice-prib-id.md"),
    (METRIK, "metrik.py"),
    (LISENSI, "LICENSE"),
]

NAMA_ATURAN = "aturan-lengkap.md"

# Penyesuaian INSTRUKSI.md untuk skill Gemini tanpa metrik.py. Setiap potongan harus
# ditemukan tepat satu kali; jika INSTRUKSI.md berubah, skrip berhenti dan potongan ini
# perlu diperbarui.
GANTI_GEMINI = [
    (
        "- `metrik.py`: pengukur metrik gaya.",
        "- `metrik.py` tidak disertakan di skill Gemini, karena Gemini Chat tidak menjalankan"
        " skill yang memuat skrip. Langkah 2 selalu berakhir pada **hitungan manual** atau"
        " **tidak diukur**. Untuk angka yang sebenarnya, sarankan pengguna menjalankan"
        " `metrik.py` dari repo di komputernya.",
    ),
    (
        "`id-ai-tells.md`, `voice-prib-id.md`, dan `metrik.py` sebagai padanan jalur"
        " `references/` dan `scripts/` dalam skill.",
        "`id-ai-tells.md` dan `voice-prib-id.md` sebagai padanan jalur `references/` dalam"
        " skill.",
    ),
]
NAMA_SKILL_GEMINI = "humanizer-indonesia"


def baca(p):
    return p.read_text(encoding="utf-8")


def versi_skill():
    m = re.search(r"\*\*Versi ([\d.]+)", baca(SKILL))
    return m.group(1) if m else "?"


def pisah_frontmatter(teks):
    m = re.match(r"^---\n(.*?)\n---\n", teks, re.S)
    if not m:
        raise SystemExit("SKILL.md tidak diawali frontmatter YAML")
    return m.group(1), teks[m.end():].lstrip("\n")


def skill_gemini():
    """SKILL.md untuk Gemini: frontmatter repo + isi INSTRUKSI.md."""
    frontmatter, _ = pisah_frontmatter(baca(SKILL))
    if not re.search(r"^name: %s$" % NAMA_SKILL_GEMINI, frontmatter, re.M):
        raise SystemExit("name di frontmatter SKILL.md bukan %s" % NAMA_SKILL_GEMINI)
    isi = baca(INSTRUKSI)
    jumlah = isi.count("`SKILL.md`")
    if jumlah == 0:
        raise SystemExit("INSTRUKSI.md tidak lagi merujuk `SKILL.md`; periksa skrip ini")
    isi = isi.replace("`SKILL.md`", "`%s`" % NAMA_ATURAN)
    for lama, baru in GANTI_GEMINI:
        if isi.count(lama) != 1:
            raise SystemExit("Potongan INSTRUKSI.md tidak ditemukan: " + lama[:60])
        isi = isi.replace(lama, baru)
    catatan = (
        "> Paket skill Gemini, aturan versi %s. Berkas ini dibangkitkan oleh\n"
        "> `portable/buat_paket.py` dari `portable/INSTRUKSI.md`. Aturan lengkap dan\n"
        "> nomor versi ada di `%s`, yaitu salinan `SKILL.md` repo tanpa frontmatter.\n"
        "> Jangan menyunting berkas ini langsung; sunting sumbernya lalu bangkitkan ulang.\n\n"
        % (versi_skill(), NAMA_ATURAN)
    )
    judul, _, sisa = isi.partition("\n")
    return "---\n%s\n---\n\n%s\n\n%s%s" % (frontmatter, judul, catatan, sisa.lstrip("\n"))


def aturan_lengkap():
    _, isi = pisah_frontmatter(baca(SKILL))
    return isi


def buat_chatgpt():
    keluaran = DIST / "humanizer-indonesia-portable.zip"
    with zipfile.ZipFile(keluaran, "w", zipfile.ZIP_DEFLATED) as z:
        for sumber, nama in BERKAS_CHATGPT:
            z.write(sumber, nama)
    return keluaran, [n for _, n in BERKAS_CHATGPT]


def buat_gemini():
    folder = DIST / NAMA_SKILL_GEMINI
    if folder.exists():
        shutil.rmtree(folder)
    folder.mkdir(parents=True)
    (folder / "SKILL.md").write_text(skill_gemini(), encoding="utf-8")
    (folder / NAMA_ATURAN).write_text(aturan_lengkap(), encoding="utf-8")
    for sumber, nama in [
        (TELLS, "id-ai-tells.md"),
        (VOICE, "voice-prib-id.md"),
        # Berkas tanpa ekstensi belum tentu diterima pengunggah skill Gemini.
        (LISENSI, "LICENSE.txt"),
    ]:
        shutil.copyfile(sumber, folder / nama)
    nama_berkas = sorted(p.name for p in folder.iterdir())
    keluaran = DIST / "humanizer-indonesia-gemini-skill.zip"
    with zipfile.ZipFile(keluaran, "w", zipfile.ZIP_DEFLATED) as z:
        # SKILL.md langsung di akar ZIP, sesuai syarat unggah skill Gemini.
        for nama in nama_berkas:
            z.write(folder / nama, nama)
    return keluaran, folder, nama_berkas


def main():
    sumber = [SKILL, INSTRUKSI, TELLS, VOICE, METRIK, LISENSI]
    hilang = [str(p) for p in sumber if not p.exists()]
    if hilang:
        raise SystemExit("Berkas tidak ditemukan: " + ", ".join(hilang))
    DIST.mkdir(exist_ok=True)

    print("Aturan skill versi %s" % versi_skill())
    zip_gpt, isi_gpt = buat_chatgpt()
    print("\nChatGPT: %s" % zip_gpt)
    for nama in isi_gpt:
        print("  " + nama)
    zip_gem, folder_gem, isi_gem = buat_gemini()
    print("\nGemini: %s" % zip_gem)
    print("  (folder yang sama untuk unggah folder: %s)" % folder_gem)
    for nama in isi_gem:
        print("  " + nama)


if __name__ == "__main__":
    main()
