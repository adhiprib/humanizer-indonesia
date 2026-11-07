#!/usr/bin/env python3
"""
metrik.py - pengukur gaya teks bahasa Indonesia untuk skill humanizer-indonesia.

Versi 1.4 (skill 1.7) menambah dua diagnostik tanpa ambang. Pertama, triplet, yaitu daftar
tepat tiga butir "A, B, dan C" (juga "atau" dan "serta") dengan atau tanpa kata "seperti".
Baris enumerasi hanya menangkap daftar yang diawali "seperti", sehingga lima triplet yang
ditandai GPTZero pada esai fuel cell (26 Oktober 2026) tercatat nol. Kedua, kalimat pendek
(7 kata ke bawah) yang berdiri tanpa penghubung di awal atau tengah paragraf, sebab
GPTZero menandai "Kondisi di bumi berbeda." dan penulis memang menambahkan penghubung pada
kalimat semacam itu (bagian 2.15 voice-prib-id.md). Kalimat pendek penutup paragraf tidak
dihitung, karena itu penanda suara penulis (bagian 2.10).

Tambahan 31 Oktober 2026, masih versi 1.4. Detektor triplet kini juga menangkap butir
berupa frasa verba sampai 10 kata ("menghitung emisi CO2 dari pembakaran bahan bakar") dan
daftar kedua yang dibuka "serta" atau "dan" di dalam kalimat yang sama. Diagnostik baru
deret sejajar menghitung daftar empat butir ke atas yang kata pertamanya berbentuk seragam
(-nya, me-, ber-, di-, pe-an, ke-an). Keduanya lahir dari Bab 9 diktat perubahan iklim
yang empat kali ditandai Everything in threes oleh GPTZero; versi sebelumnya hanya
menangkap satu. Perbaikan kedua pada hari yang sama: "maka", "artinya", "terutama",
"khususnya", dan "hampir" tidak lagi dihitung sebagai butir, dan segmen pembuka yang
panjang dihitung sebagai butir keempat. Temuan skrip kini sama dengan GPTZero pada Bab 9
(4), esai FCEV (0), dan tulisan opini penulis (1).

Tambahan 7 November 2026, masih versi 1.4. Sembilan diagnostik kaidah dan wacana tanpa
ambang: preposisi yang menghilangkan subjek,
konjungsi berpasangan, rujukan spasial semu, bentuk tidak baku dan bentuk terikat yang
ditulis terpisah, modalitas bertumpuk, otoritas tanpa rujukan, sitasi formulaik, residu
percakapan chatbot, dan rentang semu. Satu diagnostik lagi menghitung kalimat yang memuat
*saya* di luar kutipan langsung, hanya pada preset akademik dan ajar. Pada contoh Sesudah di SKILL.md dan pada
voice-prib-id.md, kesembilannya mencatat nol temuan.

Versi 1.3 (skill 1.6) menambah baris diagnostik penyangkalan antisipatif, yaitu pola
"bukan berarti" dan "bukan X, melainkan Y", dengan sasaran nol.

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

# Penyangkalan antisipatif (ditambahkan versi 1.3 skrip, skill 1.6). 'tidak berarti'
# sengaja tidak dihitung karena sah dalam makna statistik.
POLA_SANGKAL = re.compile(
    r"\bbukan\s+berarti\b|\bbukan\s+sekadar\b[^.]{0,80}?\bmelainkan\b"
    r"|\bbukan\s+[^.,]{1,60},\s*melainkan\b", re.I)

# Tambahan 7 November 2026, masih versi 1.4. Diagnostik kaidah dan wacana, semuanya tanpa
# ambang. Setiap temuan ditinjau dulu sebelum menyunting.
VERBA_LAPOR = (r"menunjukkan|menjelaskan|membahas|memperlihatkan|membuktikan|menyimpulkan|"
               r"menyatakan|mengungkapkan|menguraikan|memaparkan|menghasilkan|diperoleh")
POLA_SUBJEK_HILANG = re.compile(
    r"^(?:Dalam|Pada|Di dalam|Bagi|Menurut)\s+[^,]{3,60}?\s+(?:ini\s+|tersebut\s+)?(?:"
    + VERBA_LAPOR + r")\b", re.I)

POLA_KONJ_GANDA = re.compile(
    r"\b(?:meskipun|walaupun|walau|kendatipun|biarpun|sekalipun)\b[^.]{3,160}?,\s*"
    r"(?:tetapi|namun|akan tetapi)\b"
    r"|\b(?:karena|oleh karena|sebab)\b[^.]{3,160}?,\s*maka\b", re.I)

POLA_RUJUKAN_SPASIAL = re.compile(
    r"\b(?:tabel|gambar|grafik|diagram|persamaan|bagan|kurva)\s+(?:di|pada bagian|yang ada di)\s+"
    r"(?:atas|bawah)\b|\b(?:di atas|di bawah) ini\b(?=[^.]{0,40}\b(?:tabel|gambar|grafik)\b)", re.I)

BENTUK_TIDAK_BAKU = {
    "mempengaruhi": "memengaruhi", "merubah": "mengubah",
    "dirubah": "diubah", "mensintesis": "menyintesis",
    "mensukseskan": "menyukseskan", "mentaati": "menaati", "menterjemahkan": "menerjemahkan",
    "analisa": "analisis", "menganalisa": "menganalisis", "praktek": "praktik",
    "resiko": "risiko", "standarisasi": "standardisasi", "efektifitas": "efektivitas",
    "aktifitas": "aktivitas", "produktifitas": "produktivitas", "kreatifitas": "kreativitas",
    "sensitifitas": "sensitivitas", "selektifitas": "selektivitas", "sistim": "sistem",
    "linier": "linear", "nonlinier": "taklinear atau nonlinear", "apapun": "apa pun",
    "siapapun": "siapa pun", "manapun": "mana pun", "kapanpun": "kapan pun",
    "dimanapun": "di mana pun", "ijin": "izin", "obyek": "objek",
    "subyek": "subjek", "kwalitas": "kualitas", "nampak": "tampak", "himbauan": "imbauan",
}
POLA_TERIKAT = re.compile(
    r"\b(?:pasca|antar|multi|non|pra|sub|semi|swa|tuna|purna|nir)\s+"
    r"(?!jemput\b|dan\b|atau\b|yang\b)[a-z]{3,}", re.I)
POLA_TOLAK_UKUR = re.compile(r"\btolak\s+ukur\b", re.I)

POLA_MODAL_GANDA = re.compile(
    r"\b(?:mungkin|barangkali|kemungkinan besar)\s+(?:dapat|bisa|berpotensi|akan dapat|diduga)\b"
    r"|\bberpotensi\s+(?:dapat|bisa|mungkin)\b|\b(?:dapat|bisa)\s+berpotensi\b"
    r"|\bdiduga\s+(?:mungkin|dapat)\b", re.I)

POLA_OTORITAS = re.compile(
    r"\b(?:banyak|sebagian besar|para|berbagai)\s+(?:peneliti|ahli|pakar|studi|penelitian|kajian|"
    r"literatur)\b(?:\s+\w+){0,4}\s+(?:sepakat|menyatakan|menunjukkan|meyakini|berpendapat|"
    r"telah membuktikan)", re.I)

POLA_SITASI_FORMULA = re.compile(
    r"\b(?:senada dengan (?:itu|hal tersebut|pendapat)|sejalan dengan (?:itu|hal tersebut|pendapat)|"
    r"hal (?:serupa|senada|yang sama) (?:juga )?(?:diungkapkan|dikemukakan|disampaikan|dinyatakan))\b",
    re.I)
POLA_MENURUT_PENULIS = re.compile(r"^Menurut\s+[A-Z][\w\-]+(?:\s+(?:dkk\.?|et al\.?|dan\s+[A-Z][\w\-]+))?\s*\(\d{4}")

POLA_RESIDU_BOT = re.compile(
    r"\b(?:tentu,? berikut|berikut (?:adalah )?(?:draf|versi|revisi|hasil suntingan)|"
    r"semoga membantu|semoga penjelasan ini membantu|jangan ragu untuk|"
    r"apakah ada yang ingin (?:anda )?(?:tanyakan|tambahkan))\b", re.I)

POLA_RENTANG_SEMU = re.compile(r"\bmulai dari\s+[^.,]{2,50}?\s+(?:hingga|sampai)\b", re.I)

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


BUKAN_BUTIR = PEMBUKA_KONEKTOR + PEMBUKA_KETERANGAN + (
    "secara", "yang", "masing-masing", "dan", "atau", "serta", "bahwa", "agar", "supaya",
    "bagi", "termasuk", "yaitu", "yakni", "berbeda", "dibandingkan", "maka", "artinya",
    "terutama", "khususnya", "hampir")


def _bukan_butir(seg):
    return (seg.strip().lower() + " ").startswith(BUKAN_BUTIR)


POLA_VERBA = re.compile(r"^(?:me|ber|ter|di)[a-z]{3,}$", re.I)
PENGHUBUNG_DAFTAR = ("dan ", "serta ", "atau ")


def _kata1(seg):
    w = seg.strip().split()
    return w[0].lower() if w else ""


def cari_triplet(kal):
    """Daftar tepat tiga butir "A, B, dan C" (juga atau/serta). Isi kurung dibuang dulu.
    B maksimal 6 kata, atau 10 kata bila B frasa verba (menghitung ..., berubah ...).
    A boleh ekor klausa panjang, termasuk klausa yang dibuka "serta" atau "dan" (daftar
    kedua di dalam kalimat yang sama). Segmen sebelum A dihitung sebagai butir keempat
    kecuali diawali keterangan atau konektor (klausa pembuka)."""
    hasil = []
    for k in kal:
        kk = re.sub(r"\([^)]*\)", "", re.sub(r"(\d),(\d)", r"\1<D>\2", k))
        for m in re.finditer(r",?\s+(?:dan|atau|serta)\s+", kk):
            r = list(reversed(kk[:m.start()].split(",")))
            if len(r) < 2:
                continue
            nb, na = len(r[0].split()), len(r[1].split())
            batas_b = 10 if POLA_VERBA.match(_kata1(r[0])) else 6
            if not 1 <= nb <= batas_b or _bukan_butir(r[0]) or na == 0:
                continue
            a_dibuka_penghubung = (r[1].strip().lower().startswith(PENGHUBUNG_DAFTAR)
                                   and na >= 3)
            if not a_dibuka_penghubung:
                if na <= 8 and _bukan_butir(r[1]):
                    continue
                if len(r) == 2 and na <= 3 and nb >= 4:
                    continue  # frasa pembuka pendek, misalnya "Kelemahannya, PEMFC memerlukan ..."
                if na <= 6 and len(r) > 2 and r[2].strip() and (
                        len(r) > 3 or not _bukan_butir(r[2]) or len(r[2].split()) > 3):
                    continue
            hasil.append(k)
            break
    return hasil


def _templat(kata):
    """Bentuk kata pertama butir: nominalisasi -nya, verba me-/ber-/di-, atau nomina pe-an/ke-an."""
    if len(kata) > 5 and kata.endswith("nya"):
        return "-nya"
    for awalan in ("me", "ber", "di"):
        if POLA_VERBA.match(kata) and kata.startswith(awalan):
            return awalan + "-"
    if kata.startswith("pe") and kata.endswith("an"):
        return "pe-an"
    if kata.startswith("ke") and kata.endswith("an"):
        return "ke-an"
    return None


def deret_sejajar(kal):
    """Daftar empat butir atau lebih yang kata pertama setiap butirnya berbentuk sama,
    misalnya "meningkatnya ..., berubahnya ..., naiknya ..., dan meningkatnya ...".
    GPTZero menandai deret semacam ini sebagai Everything in threes (31 Oktober 2026)."""
    hasil = []
    for k in kal:
        kk = re.sub(r"\([^)]*\)", "", re.sub(r"(\d),(\d)", r"\1<D>\2", k))
        for m in re.finditer(r",?\s+(?:dan|atau|serta)\s+", kk):
            c = re.split(r"[,.;]", kk[m.end():])[0]
            butir = [c]
            for seg in reversed(kk[:m.start()].split(",")):
                if ":" in seg:
                    butir.append(seg.split(":")[-1])
                    break
                if len(seg.split()) > 6 or _bukan_butir(seg):
                    break
                butir.append(seg)
            templat = {_templat(_kata1(b)) for b in butir}
            if len(butir) >= 4 and len(templat) == 1 and None not in templat:
                hasil.append(k)
                break
    return hasil


def pendek_lepas(teks):
    """Kalimat 7 kata ke bawah, bukan kalimat terakhir paragraf, tanpa penghubung di depan."""
    hasil = []
    for p in teks.split("\n\n"):
        if not p.strip() or p.lstrip().startswith(("#", "|", "[")):
            continue
        kal = pecah_kalimat(ambil_prosa(p))
        for k in kal[:-1]:
            if len(k.split()) <= 7 and not k.lower().startswith(PEMBUKA_KONEKTOR):
                hasil.append(k)
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
        "sangkal": len(POLA_SANGKAL.findall(body)),
        "contoh_sangkal": [x.group(0) for x in POLA_SANGKAL.finditer(body)][:3],
        "dash": body.count("\u2014") + len(re.findall(r"(?<!\d)\u2013|\u2013(?!\d)", body)),
        "en_rentang": len(re.findall(r"\d\s?\u2013\s?\d", body)),
        "pemadat": len(PEMADAT.findall(body)) / kata * 1000,
        "contoh_enum": enum[:3], "deret": deret_pembuka(teks),
        "triplet": cari_triplet(kal), "pendek_lepas": pendek_lepas(teks),
        "sejajar": deret_sejajar(kal),
        "kaidah": periksa_kaidah(kal, body),
    }


def periksa_kaidah(kal, body):
    """Diagnostik tambahan 7 November 2026. Mengembalikan {nama: [contoh, ...]}."""
    h = {}
    h["subjek_hilang"] = [k for k in kal if POLA_SUBJEK_HILANG.match(k)]
    h["konjungsi_ganda"] = [m.group(0) for m in POLA_KONJ_GANDA.finditer(body)]
    h["rujukan_spasial"] = [m.group(0) for m in POLA_RUJUKAN_SPASIAL.finditer(body)]
    tb = []
    for w in re.findall(r"\b[a-z]+\b", body.lower()):
        if w in BENTUK_TIDAK_BAKU:
            tb.append("%s -> %s" % (w, BENTUK_TIDAK_BAKU[w]))
    tb += ["%s -> serangkai" % m.group(0) for m in POLA_TERIKAT.finditer(body)]
    tb += ["tolak ukur -> tolok ukur" for _ in POLA_TOLAK_UKUR.finditer(body)]
    h["tidak_baku"] = tb
    h["modal_ganda"] = [m.group(0) for m in POLA_MODAL_GANDA.finditer(body)]
    h["otoritas"] = [m.group(0) for m in POLA_OTORITAS.finditer(body)
                     if "(" not in body[m.end():m.end() + 120].split(".")[0]]
    formula = [m.group(0) for m in POLA_SITASI_FORMULA.finditer(body)]
    menurut = [k[:60] for k in kal if POLA_MENURUT_PENULIS.match(k)]
    h["sitasi_formula"] = formula + (menurut if len(menurut) >= 3 else [])
    h["residu_bot"] = [m.group(0) for m in POLA_RESIDU_BOT.finditer(body)]
    h["rentang_semu"] = [m.group(0) for m in POLA_RENTANG_SEMU.finditer(body)]
    tanpa_kutipan = re.sub(r'["\u201c][^"\u201d]*["\u201d]', " ", body)
    h["saya"] = [k[:70] for k in pecah_kalimat(tanpa_kutipan) if re.search(r"\b(?:saya|aku|ku)\b", k, re.I)]
    h["bila"] = [k[:70] for k in pecah_kalimat(tanpa_kutipan)
                 if re.search(r"\bbila\b", k, re.I) and not k.rstrip().endswith("?")]
    return h


LABEL_KAIDAH = [
    ("subjek_hilang", "Preposisi menghilangkan subjek (Dalam penelitian ini menunjukkan)"),
    ("konjungsi_ganda", "Konjungsi berpasangan (Meskipun ..., tetapi; Karena ..., maka)"),
    ("rujukan_spasial", "Rujukan spasial semu (tabel di bawah ini, grafik di atas)"),
    ("tidak_baku", "Bentuk tidak baku dan bentuk terikat yang terpisah"),
    ("modal_ganda", "Modalitas bertumpuk (mungkin dapat, berpotensi dapat)"),
    ("otoritas", "Otoritas tanpa rujukan (banyak peneliti sepakat)"),
    ("sitasi_formula", "Sitasi formulaik (Senada dengan itu, Menurut X (tahun) berderet)"),
    ("residu_bot", "Residu percakapan chatbot (Tentu, berikut; Semoga membantu)"),
    ("rentang_semu", "Rentang semu (mulai dari X hingga Y)"),
    ("saya", "Kata ganti saya di luar kutipan (hanya preset akademik dan ajar)"),
    ("bila", "Konjungsi bila, ganti jika atau apabila (hanya preset akademik dan ajar)"),
]


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
    print("  Triplet (daftar tepat tiga butir, dengan atau tanpa 'seperti'): %d, %.2f per 1.000 kata"
          % (len(m["triplet"]), len(m["triplet"]) / m["kata"] * 1000))
    print("    Tanpa ambang. Sisakan hanya yang ketiga butirnya membawa informasi berbeda (D3).")
    for c in m["triplet"][:6]:
        print("    > " + c[:82])
    print("  Deret sejajar (4 butir ke atas, bentuk kata pertama seragam): %d" % len(m["sejajar"]))
    print("    Tanpa ambang. Pecah bentuknya atau jadikan daftar bernomor (D3).")
    for c in m["sejajar"][:6]:
        print("    > " + c[:82])
    print("  Kalimat pendek lepas (7 kata ke bawah, bukan penutup paragraf, tanpa penghubung): %d"
          % len(m["pendek_lepas"]))
    print("    Tanpa ambang. Beri penghubung atau gabungkan ke kalimat sesudahnya (2.15).")
    for c in m["pendek_lepas"][:6]:
        print("    > " + c[:82])
    print("  Penyangkalan antisipatif (bukan berarti, bukan X melainkan Y): %d   sasaran 0" % m["sangkal"])
    for c in m["contoh_sangkal"]:
        print("    > %s" % c)
    print("  Kaidah dan wacana (tambahan 7 November 2026, tanpa ambang, sasaran 0 kecuali")
    print("  rentang semu dan sitasi naratif yang memang konvensi jurnal):")
    for kunci, label in LABEL_KAIDAH:
        if kunci in ("saya", "bila") and nama_preset == "semiformal":
            continue
        isi = m["kaidah"][kunci]
        print("    %-74s %d" % (label, len(isi)))
        for c in isi[:4]:
            print("      > " + c[:78])
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
