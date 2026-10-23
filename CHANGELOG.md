# CHANGELOG

Semua perubahan penting pada repositori ini dicatat di berkas ini. Format mengikuti [Keep a Changelog](https://keepachangelog.com/id-ID/1.1.0/) dan versi memakai [Semantic Versioning](https://semver.org/lang/id/).

Versi di sini merujuk pada **isi dokumen**, bukan perangkat lunak, karena repositori ini tidak berisi kode yang dijalankan.

## [Unreleased]

### Ditambahkan

- `docs/14-rubrik-penilaian.md` — rubrik berbobot untuk mengubah sinyal perilaku menjadi skor dan tingkat kepastian.
- `docs/15-penanganan-jawaban.md` — delapan jenis jawaban akun, artinya, dan langkah berikutnya.
- `docs/16-studi-kasus.md` — contoh jalan-periksa lengkap dari pertanyaan sampai kesimpulan.
- `docs/17-pelestarian-bukti.md` — cara menyimpan dan membuktikan temuan sebelum buktinya hilang.
- `docs/18-informasi-salah-dan-koordinasi.md` — cara memeriksa informasi salah dan perilaku koordinasi, termasuk delapan sinyal K-1 sampai K-8.
- `docs/19-label-ai-platform.md` — label AI yang dipasang platform (AI Info, AI-generated profile), cara memeriksanya, dan batasnya.
- `docs/20-penelitian-dan-indikator.md` — temuan riset dan indikator lapangan, termasuk batas kemampuan manusia membedakan akun AI.
- `docs/21-pertanyaan-pengungkap-persona.md` — bank pertanyaan untuk menguji apakah sebuah persona hidup di dunia nyata, beserta aturan mainnya.

### Diubah

- Penekanan bergeser: pernyataan akun diperlakukan sebagai sinyal terlemah, dan verifikasi ke sumber primer naik menjadi langkah utama.
- Pemeriksaan label platform ditambahkan sebagai langkah tetap dalam alur pemeriksaan.
- Rubrik Penilaian mendapat kelas artefak teknis (T-1 sampai T-4) yang lebih kuat dari sinyal perilaku.
- Navigasi dan indeks diperbarui untuk dokumen 14–20.
- Aksi GitHub dinaikkan ke versi terbaru (checkout v7, setup-python v6, setup-node v7, upload-pages-artifact v5, deploy-pages v5).

## [0.1.0] - 2026-10-23

Rilis pertama: panduan identifikasi akun AI dan evaluasi ketahanan bot.

### Ditambahkan

- Beranda `docs/index.md` sebagai halaman pembuka situs dokumentasi.
- `docs/10-glosarium.md` — glosarium istilah teknis.
- `docs/11-panduan-per-platform.md` — panduan bertanya di tiap platform media sosial.
- `docs/12-privasi-dan-retensi-data.md` — kebijakan privasi dan retensi untuk log pemeriksaan dan pengujian.
- `docs/13-menduga-vs-membuktikan.md` — batas apa yang bisa dibuktikan dan apa yang hanya bisa diduga.
- `docs/perkakas/` — lembar verifikasi, log kegagalan, dan contoh catatan lengkap.
- `scripts/check_docs.py` — pemeriksa tautan internal, anchor, kode Morse, dan cakupan navigasi.
- `mkdocs.yml` — situs dokumentasi MkDocs Material berbahasa Indonesia.
- `.github/workflows/lint-docs.yml` — CI validasi tautan, anchor, Morse, YAML, dan markdown.
- `.github/workflows/deploy-docs.yml` — penerbitan otomatis ke GitHub Pages.
- `.github/ISSUE_TEMPLATE/` dan `.github/PULL_REQUEST_TEMPLATE.md`.
- `LICENSE` (CC BY 4.0), `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`.
- `.yamllint.yml` dan `.markdownlint-cli2.jsonc`.

### Diubah

- `README.md` menjadi pointer pendek; isi lengkapnya pindah ke `docs/index.md`.
- Tautan `../README.md` di seluruh dokumen menjadi `index.md`.
- `docs/02-verifikasi.md` §4: diperjelas bahwa Morse adalah alternatif penyampaian, bukan cara menghindari penyaring.
- Rujukan silang ke `docs/13-menduga-vs-membuktikan.md` ditambahkan di dokumen terkait.

[Unreleased]: https://github.com/ringga-dev/pancing-bot/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/ringga-dev/pancing-bot/releases/tag/v0.1.0
