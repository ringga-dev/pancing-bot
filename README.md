# pancing-bot

Panduan dan prompt untuk meminta transparansi dari akun atau layanan di media sosial: apakah akun itu memakai AI, siapa pengelolanya, model/vendor apa yang diumumkan, dan cara memeriksa jawabannya sebelum menarik kesimpulan.

> **Ini dokumentasi, bukan aplikasi.** Repositori ini tidak berisi kode bot dan tidak dapat menentukan identitas AI secara otomatis. Isinya prompt siap pakai, checklist verifikasi, dan lembar kerja evaluasi.

## Mulai di sini

| Saya ingin... | Baca |
|---|---|
| Langsung pakai prompt | [Indeks Prompt](docs/01-prompt-identifikasi-ai.md) |
| Memeriksa klaim sebuah akun | [Checklist Verifikasi](docs/02-verifikasi.md) |
| Tahu batas apa yang boleh ditanyakan | [Batas Prompt](docs/07-batas-prompt.md) |
| Tahu apa yang bisa dan tidak bisa dibuktikan | [Menduga vs Membuktikan](docs/13-menduga-vs-membuktikan.md) |
| Mengisi hasil pemeriksaan | [Template siap isi](docs/perkakas/README.md) |
| Istilah teknis yang dipakai | [Glosarium](docs/10-glosarium.md) |
| Diduga ada narasi yang sengaja menyebar atau diarahkan | [Informasi Salah dan Koordinasi](docs/18-informasi-salah-dan-koordinasi.md) |
| Cek tanda AI dari platformnya sendiri | [Label AI di Platform](docs/19-label-ai-platform.md) |

## Situs dokumentasi

Seluruh halaman di bawah `docs/` bisa dibaca langsung di GitHub. Selain itu repositori ini punya situs terbitan otomatis (MkDocs Material) yang dibangun dan diterbitkan ke GitHub Pages setiap kali ada *push* ke `main` — lihat [`docs/index.md`](docs/index.md).

## Kontribusi

Lihat [CONTRIBUTING.md](CONTRIBUTING.md). Sebelum mengirim *pull request*, jalankan pemeriksaan lokal:

```bash
pip install -r requirements.txt
python3 scripts/check_docs.py       # tautan, anchor, kode Morse, cakupan nav
python3 -m mkdocs build --strict    # pastikan situs tetap bisa dibangun
```

## Lisensi

[CC BY 4.0](LICENSE) — bebas dipakai dan disesuaikan dengan menyebut sumber.
