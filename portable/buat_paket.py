#!/usr/bin/env python3
"""
buat_paket.py - membuat paket portabel humanizer-indonesia untuk ChatGPT dan Gemini.

ChatGPT (Custom GPT) dan Gemini (Gem) menerima berkas pengetahuan sebagai daftar datar,
tanpa folder. Skrip ini menyalin berkas skill dari akar repo ke satu ZIP datar, sehingga
paket selalu sama dengan versi skill yang sedang ada di repo.

Pakai, dari akar repo atau dari folder portable:
    python3 portable/buat_paket.py

Hasil: portable/dist/humanizer-indonesia-portable.zip
"""

import pathlib
import re
import zipfile

PORTABLE = pathlib.Path(__file__).resolve().parent
AKAR = PORTABLE.parent

BERKAS = [
    (PORTABLE / "INSTRUKSI.md", "INSTRUKSI.md"),
    (AKAR / "SKILL.md", "SKILL.md"),
    (AKAR / "references" / "id-ai-tells.md", "id-ai-tells.md"),
    (AKAR / "references" / "voice-prib-id.md", "voice-prib-id.md"),
    (AKAR / "scripts" / "metrik.py", "metrik.py"),
    (AKAR / "LICENSE", "LICENSE"),
]


def versi_skill():
    teks = (AKAR / "SKILL.md").read_text(encoding="utf-8")
    m = re.search(r"\*\*Versi ([\d.]+)", teks)
    return m.group(1) if m else "?"


def main():
    hilang = [str(sumber) for sumber, _ in BERKAS if not sumber.exists()]
    if hilang:
        raise SystemExit("Berkas tidak ditemukan: " + ", ".join(hilang))
    dist = PORTABLE / "dist"
    dist.mkdir(exist_ok=True)
    keluaran = dist / "humanizer-indonesia-portable.zip"
    with zipfile.ZipFile(keluaran, "w", zipfile.ZIP_DEFLATED) as z:
        for sumber, nama in BERKAS:
            z.write(sumber, nama)
    print("Paket versi skill %s: %s" % (versi_skill(), keluaran))
    for _, nama in BERKAS:
        print("  " + nama)


if __name__ == "__main__":
    main()
