#!/usr/bin/env python3
"""
metrik.py - pengukur gaya teks bahasa Indonesia untuk skill humanizer-indonesia.

Versi 1.2. Ambang dikalibrasi ulang dari rentang korpus yang sebenarnya, bukan dari
target ideal. Kalibrasi 1.0 dan 1.1 memakai target yang lebih ketat daripada tulisan
penulis sendiri, dan potongan tulisan manusianya gagal di empat baris. Lihat bagian 1
voice-prib-id.md. Kepadatan kata pemadat ditambahkan sebagai diagnostik tanpa ambang.

Perubahan 1.1, seluruhnya berasal dari pemakaian nyata:
  - verba ringan dideteksi lewat pola konstruksi, bukan daftar pasangan tetap
  - dua metrik baru: proporsi kalimat panjang dan kepadatan koordinasi klausa
  - deret pembuka kalimat seragam per paragraf, sebagai diagnostik tanpa ambang
  - saran perbaikan simpangan baku memeriksa kalimat terpanjang lebih dulu
  - blok metadata dan afiliasi dibuang sebelum pengukuran

Pakai:
    python3 metrik.py berkas.md --preset akademik
    cat teks.txt | python3 metrik.py -
"""

import argparse
import re
import statistics
import sys

KONEKTOR = [
    "Selain itu", "Namun demikian", "Di sisi lain", "Oleh karena itu",
    "Dengan demikian", "Lebih lanjut", "Sementara itu", "Akan tetapi",
    "Oleh sebab itu", "Walaupun demikian", "Sayangnya", "Di samping itu",
    "Lebih jauh lagi", "Sehubungan dengan itu",
]

VERBA_PENGOSONG = r"melakukan|memberikan|mengalami|melaksanakan|menjalankan|mengadakan"
NOMINA_TURUNAN = r"(?:pe|ke)(?!pada\b|tika\b|mbali\b|mudian\b|luar\b|dua\b|tiga\b)[a-z]{3,}"
POLA_VERBA_RINGAN = re.compile(r"\b(?:" + VERBA_PENGOSONG + r")\s+" + NOMINA_TURUNAN + r"\b", re.I)

PEMADAT = re.compile(
    r"\b(?:akan|telah|sudah|dapat|bisa|suatu|untuk|yang|melalui|hal|merupakan|"
    r"adalah|dilakukan|terhadap|tersebut|ini|itu)\b", re.I)

POLA_KOORDINASI = re.compile(r",\s*(?:dan|serta|lalu|kemudian|sehingga|sedangkan|tetapi)\b", re.I)

FRASA_KOSONG = [
    "sangat penting", "tidak dapat dipungkiri", "memegang peranan penting",
    "menjadi kunci utama", "menjadi faktor kunci", "berperan vital",
    "aspek vital", "tak lepas dari", "semakin krusial", "patut diperhatikan",
    "di era", "seiring dengan perkembangan", "dapat disimpulkan bahwa",
]

PEMBUKA_KONEKTOR = ("namun", "selain itu", "akan tetapi", "tetapi", "sedangkan",
                    "meski", "walaupun", "oleh karena", "dengan demikian",
                    "sementara", "kemudian", "selanjutnya", "jadi", "sehingga",
                    "karena itu", "sebaliknya")
PEMBUKA_KETERANGAN = ("pada", "dalam", "di ", "untuk", "setelah", "sebelum",
                      "ketika", "saat", "karena", "begitu", "dengan",
                      "berdasarkan", "dari", "sejak", "menurut", "selama",
                      "tanpa", "jika", "bila", "melalui", "terhadap")

PRESET = {
    # Ambang 1.2: batas atas diambil dari nilai tertinggi yang benar-benar muncul di
    # korpus tingkat A dan B, dengan sedikit kelonggaran. Prinsipnya, tulisan penulis
    # sendiri harus lulus. Baris dalam SUMBER_INSTRUKSI adalah pengecualian: ambangnya
    # berasal dari permintaan penulis dan memang lebih ketat daripada korpusnya.
    "akademik": {
        "rerata": (14.0, 20.0), "sd": (6.4, None), "konektor": (None, 0.40),
        "verba_ringan": (None, 0.40), "enum_seperti": (None, 1.00),
        "merupakan_per_1000": (None, 4.00), "dash": (None, 0),
        "panjang_pct": (None, 20.0), "koordinasi": (None, 1.50),
    },
    "ajar": {
        "rerata": (16.0, 21.0), "sd": (6.4, None), "konektor": (None, 0.40),
        "verba_ringan": (None, 0.40), "enum_seperti": (None, 1.00),
        "merupakan_per_1000": (None, 6.10), "dash": (None, 0),
        "panjang_pct": (None, 20.0), "koordinasi": (None, 1.50),
    },
    "semiformal": {
        "rerata": (13.0, 17.0), "sd": (6.4, None), "konektor": (None, 0.40),
        "verba_ringan": (None, 0.40), "enum_seperti": (None, 1.00),
        "merupakan_per_1000": (None, 1.00), "dash": (None, 0),
        "panjang_pct": (None, 15.0), "koordinasi": (None, 1.50),
    },
}

SUMBER_INSTRUKSI = {"enum_seperti", "dash"}
AMBANG_PANJANG = 28

LEWATI = re.compile(
    r"^\s*(\||!\[|#{1,6}\s|\[\d+\]|\d+\.\t|Gambar\s|Tabel\s|Pers\.|https?://|"
    r"Jl\.|e?ISSN|doi:|Vol\.|\u00a9|>\s|E-?mail|Received|Accepted|Published)", re.I)


def ambil_prosa(teks):
    teks = re.split(
        r"(?im)^#{0,6}\s*(daftar pustaka|referensi|references|ucapan terima kasih)\s*$",
        teks)[0]
    baris = [b for b in teks.split("\n") if b.strip() and not LEWATI.match(b)]
    body = " ".join(baris)
    body = re.sub(r"`{1,3}[^`]*`{1,3}", " ", body)
    body = re.sub(r"\$[^$]*\$", " ", body)
    body = re.sub(r"[*_]{1,3}", "", body)
    return re.sub(r"\s+", " ", body).strip()


def pecah_kalimat(body):
    body = re.sub(r"\b(dkk|dll|dsb|hlm|No|Gambar|Tabel|Pers)\.", r"\1<DOT>", body)
    body = re.sub(r"(\d)[.,](\d)", r"\1<DEC>\2", body)
    hasil = []
    for k in re.split(r"(?<=[.!?])\s+", body):
        k = k.replace("<DOT>", ".").replace("<DEC>", ",").strip()
        if len(k.split()) > 3:
            hasil.append(k)
    return hasil


def jenis_pembuka(kalimat):
    l = kalimat.lower()
    if l.startswith(PEMBUKA_KONEKTOR):
        return "K"
    if l.startswith(PEMBUKA_KETERANGAN):
        return "T"
    return "S"


def deret_pembuka(teks):
    hasil = []
    for p in teks.split("\n\n"):
        if not p.strip() or p.lstrip().startswith(("#", "|", "[")):
            continue
        kal = pecah_kalimat(ambil_prosa(p))
        if len(kal) < 3:
            continue
        pola = "".join(jenis_pembuka(k) for k in kal)
        hasil.append((pola, max(len(x) for x in re.findall(r"S+|T+|K+", pola))))
    return hasil


def ukur(teks):
    body = ambil_prosa(teks)
    kal = pecah_kalimat(body)
    if not kal:
        return None
    panjang = [len(k.split()) for k in kal]
    kata = sum(panjang)
    low = body.lower()
    lpj = [k for k in kal if len(k.split()) >= AMBANG_PANJANG]
    koord = [len(POLA_KOORDINASI.findall(k)) for k in lpj]
    seperti = re.findall(r"\b(?:seperti|antara lain|misalnya|di antaranya)\b[^.]{0,150}", low)
    enum = [s for s in seperti if re.search(r",\s*(?:dan|serta)\b", s)]
    rujukan = [s for s in seperti if re.match(r"seperti (yang|pada|terlihat|ditunjukkan|dijelaskan)", s)]
    return {
        "kalimat": len(kal), "kata": kata,
        "rerata": statistics.mean(panjang), "sd": statistics.pstdev(panjang),
        "terpendek": min(panjang), "terpanjang": max(panjang),
        "pendek_pct": sum(1 for p in panjang if p <= 10) / len(panjang) * 100,
        "panjang_pct": len(lpj) / len(kal) * 100,
        "koordinasi": statistics.mean(koord) if koord else 0.0,
        "n_panjang": len(lpj),
        "konektor": sum(len(re.findall(r"\b" + k.lower() + r"\b", low)) for k in KONEKTOR) / kata * 100,
        "buka_konektor_pct": sum(1 for k in kal if any(k.lower().startswith(c.lower()) for c in KONEKTOR)) / len(kal) * 100,
        "verba_ringan": len(POLA_VERBA_RINGAN.findall(body)) / kata * 100,
        "contoh_ringan": [x.group(0) for x in POLA_VERBA_RINGAN.finditer(body)][:3],
        "merupakan": len(re.findall(r"\bmerupakan\b", low)),
        "adalah": len(re.findall(r"\badalah\b", low)),
        "merupakan_per_1000": len(re.findall(r"\bmerupakan\b", low)) / kata * 1000,
        "enum_seperti": len(enum) / kata * 1000,
        "n_enum": len(enum), "n_rujukan": len(rujukan),
        "dimana": len(re.findall(r"\bdimana\b", low)),
        "yang_mana": len(re.findall(r"\byang mana\b", low)),
        "frasa_kosong": sum(low.count(f) for f in FRASA_KOSONG),
        "dash": body.count("\u2014") + len(re.findall(r"(?<!\d)\u2013|\u2013(?!\d)", body)),
        "en_rentang": len(re.findall(r"\d\s?\u2013\s?\d", body)),
        "pemadat": len(PEMADAT.findall(body)) / kata * 1000,
        "contoh_enum": enum[:3], "deret": deret_pembuka(teks),
    }


def status(nilai, rentang):
    lo, hi = rentang
    if lo is not None and nilai < lo:
        return "PERIKSA (terlalu rendah)"
    if hi is not None and nilai > hi:
        return "PERIKSA (terlalu tinggi)"
    return "LULUS"


def cetak(m, nama_preset):
    p = PRESET[nama_preset]
    print("Preset: " + nama_preset + "   kalimat: " + str(m["kalimat"]) + "   kata: " + str(m["kata"]))
    print("=" * 74)
    baris = [
        ("Rerata panjang kalimat", "rerata", "%.1f"),
        ("Simpangan baku", "sd", "%.1f"),
        ("Kalimat 28 kata ke atas (persen)", "panjang_pct", "%.1f"),
        ("Koordinasi pada kalimat panjang", "koordinasi", "%.2f"),
        ("Konektor per 100 kata", "konektor", "%.2f"),
        ("Verba ringan per 100 kata", "verba_ringan", "%.2f"),
        ("Enumerasi per 1.000 kata *", "enum_seperti", "%.2f"),
        ("merupakan per 1.000 kata", "merupakan_per_1000", "%.2f"),
        ("Em dash dan en dash *", "dash", "%d"),
    ]
    for label, kunci, fmt in baris:
        lo, hi = p[kunci]
        target = (("%g sampai %g" % (lo, hi)) if lo is not None and hi is not None
                  else (("maks %g" % hi) if lo is None else ("min %g" % lo)))
        print("  %-34s %7s  target %-14s %s" % (label, fmt % m[kunci], target, status(m[kunci], p[kunci])))
    print("  * ambang dari instruksi penulis, lebih ketat daripada korpus historis")
    print("-" * 74)
    print("Diagnostik tanpa ambang:")
    print("  Kalimat terpendek %d kata, terpanjang %d kata" % (m["terpendek"], m["terpanjang"]))
    print("  Kalimat 10 kata atau kurang: %.1f persen" % m["pendek_pct"])
    print("  Kalimat panjang: %d buah" % m["n_panjang"])
    print("  Kalimat dibuka konektor: %.1f persen" % m["buka_konektor_pct"])
    print("  merupakan %d berbanding adalah %d" % (m["merupakan"], m["adalah"]))
    print("  Enumerasi %d, rujukan 'seperti yang' %d (rujukan tidak disunting)" % (m["n_enum"], m["n_rujukan"]))
    print("  dimana %d, yang mana %d" % (m["dimana"], m["yang_mana"]))
    print("  Frasa kosong terdeteksi: %d" % m["frasa_kosong"])
    print("  En dash sebagai rentang angka: %d (tidak dihitung pelanggaran)" % m["en_rentang"])
    print("  Kepadatan kata pemadat: %.1f per 1.000 kata" % m["pemadat"])
    print("    Korpus penulis berkisar 73 sampai 139. Tanpa ambang, dan BUKAN sasaran.")
    print("    Angka jauh di bawah 73 menandakan prosa dimampatkan lebih ketat daripada")
    print("    kebiasaan penulis. Longgarkan dengan mengembalikan frasa yang wajar,")
    print("    bukan dengan menyisipkan kata isian.")
    if m["deret"]:
        print("  Pola pembuka per paragraf: " + ", ".join(s for s, _ in m["deret"]))
        print("  Deret pembuka sejenis terpanjang: %d" % max(d for _, d in m["deret"]))
        print("    S subjek langsung, T keterangan, K konektor. Tanpa ambang:")
        print("    korpus penulis sendiri mencapai deret 5 sampai 7, jadi deret")
        print("    panjang bukan bukti tulisan AI. Pakai sebagai bahan pertimbangan")
        print("    bila satu paragraf terasa monoton.")
    if m["contoh_ringan"]:
        print("")
        print("  Verba ringan yang terdeteksi:")
        for c in m["contoh_ringan"]:
            print("    > " + c)
    if m["contoh_enum"]:
        print("")
        print("  Enumerasi yang perlu ditinjau:")
        for c in m["contoh_enum"]:
            print("    > " + c[:82])
    saran(m, p)


def saran(m, p):
    catatan = []
    if m["sd"] < p["sd"][0]:
        if m["terpanjang"] < 30 and m["pendek_pct"] >= 20:
            catatan.append(
                "Simpangan baku rendah karena rentangnya sempit di ujung atas. Kalimat "
                "pendek sudah cukup banyak. Panjangkan dua atau tiga kalimat penjelas "
                "lewat klausa relatif atau keterangan sisipan, JANGAN lewat rangkaian "
                "koma dan 'dan', karena itu menaikkan baris koordinasi.")
        elif m["pendek_pct"] < 15:
            catatan.append(
                "Simpangan baku rendah karena kalimat pendek terlalu sedikit. Tambahkan "
                "kalimat pendek penutup paragraf, lihat bagian 2.9 voice-prib-id.md.")
        else:
            catatan.append(
                "Simpangan baku rendah meski kedua ujung terisi. Periksa apakah sebagian "
                "besar kalimat menumpuk di rentang menengah.")
    if m["koordinasi"] > p["koordinasi"][1]:
        catatan.append(
            "Koordinasi klausa di atas kebiasaan korpus (maks 1,50). Ubah sebagian jadi "
            "subordinasi. Jangan pecah semuanya: potongan tulisan manusia penulis "
            "sendiri berada di 1,50 dan tetap terbaca wajar.")
    if m["panjang_pct"] > p["panjang_pct"][1]:
        catatan.append(
            "Kalimat panjang terlalu sering dipakai. Korpus penulis memakainya pada 8 "
            "sampai 15 persen kalimat. Memecah semuanya bukan jalan keluar, karena itu "
            "justru menurunkan simpangan baku. Pecah sebagian, sisakan beberapa.")
    if m["pemadat"] < 73:
        catatan.append(
            "Kepadatan kata pemadat di bawah rentang korpus (73 sampai 139). Prosanya lebih mampat "
            "daripada tulisan penulis sendiri. Kembalikan frasa yang wajar, misalnya "
            "'penting untuk disampaikan' alih-alih 'penting disebut'. Jangan menambah "
            "kata isian kosong hanya untuk menaikkan angka ini.")
    if catatan:
        print("")
        for c in catatan:
            print("  Saran: " + c)


def main():
    ap = argparse.ArgumentParser(description="Ukur metrik gaya teks Indonesia.")
    ap.add_argument("berkas")
    ap.add_argument("--preset", default="akademik", choices=sorted(PRESET))
    a = ap.parse_args()
    teks = sys.stdin.read() if a.berkas == "-" else open(a.berkas, encoding="utf-8").read()
    m = ukur(teks)
    if m is None:
        print("Tidak ada prosa yang bisa diukur.")
        sys.exit(1)
    cetak(m, a.preset)


if __name__ == "__main__":
    main()
