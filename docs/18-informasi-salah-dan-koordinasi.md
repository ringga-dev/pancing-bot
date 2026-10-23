# Informasi Salah dan Perilaku Koordinasi

[← Beranda](index.md) · [Rubrik Penilaian](14-rubrik-penilaian.md) · [Menduga vs Membuktikan](13-menduga-vs-membuktikan.md) · [Checklist Verifikasi](02-verifikasi.md)

---

> **Premis dokumen ini.** Akun yang memakai AI bisa diberi instruksi untuk memberikan informasi yang salah, dan bisa diatur untuk mengarahkan opini. Jika premis itu benar — dan ada alasan untuk menganggapnya benar untuk sebagian akun — maka ada satu kesimpulan yang harus ditarik lebih awal: **apa yang dikatakan akun adalah sinyal terlemah yang bisa Anda peroleh.**

## 1. Konsekuensi dari Premis Itu

Banyak panduan, termasuk sebagian isi repositori ini, dimulai dari langkah "tanyakan ke akunnya". Pendekatan itu mengandaikan akun akan menjawab dengan jujur, atau setidaknya bahwa jawabannya informatif.

Jika akun memang bisa berbohong atau diatur untuk mengarahkan opini, asumsi itu gagal. Tiga hal berubah:

1. **Pertanyaan menjadi kurang berguna.** Jawaban "ya kami pakai AI" dan jawaban "tidak, semua manusia" sama-sama tidak bisa dipercaya begitu saja.
2. **Yang berguna adalah hal yang sulit diatur.** Metadata akun, pola waktu unggahan, struktur jaringan, dan kesesuaian klaim dengan sumber primer — bukan kalimat yang keluar dari model.
3. **Verifikasi ke sumber primer naik jadi langkah utama.** Bukan ke akun itu sendiri.

Ini bukan alasan untuk berhenti bertanya. Penolakan, pengelakan, dan ketidakkonsistenan jawaban tetap informatif (lihat [Menangani Jawaban](15-penanganan-jawaban.md)). Yang berubah adalah **bobot**nya.

## 2. Apa yang Sulit Diatur

Jika akun bisa berbohong soal isi, periksa hal-hal yang biayanya tinggi untuk dipalsukan secara konsisten:

| Sumber | Yang diperiksa |
|---|---|
| Metadata akun | Tanggal pembuatan, riwayat perubahan nama, rasio unggahan dan pengikut |
| Pola waktu | Kapan akun aktif, apakah ada jeda manusiawi, apakah unggahan terjadwal sempurna |
| Jejak eksternal | Apakah akun disebut di situs resmi, rilis berita, atau dokumentasi mana pun |
| Sumber primer | Apakah klaim akun cocok dengan situs resmi, laporan tahunan, atau data pemerintah |
| Struktur jaringan | Dengan akun mana ia berinteraksi, apakah interaksinya hanya dalam satu kelompok |

Perhatikan bahwa semua ini adalah **data perilaku dan jejak eksternal**, bukan pernyataan.

## 3. Sinyal Koordinasi

Perilaku koordinasi artinya sekelompok akun bekerja bersama untuk mendorong suatu narasi, bukan sekadar sepakat pendapat. Sinyal berikut bisa diperiksa tanpa alat khusus, asalkan Anda mencatat waktunya.

| Kode | Sinyal | Cara memeriksa |
|---|---|---|
| K-1 | Unggahan bersamaan dalam jendela sempit | Urutkan unggahan beberapa akun dalam topik yang sama. Perhatikan apakah waktunya berhimpit. |
| K-2 | Frasa identik di banyak akun | Cari kutipan yang sama persis, bukan hanya serupa. |
| K-3 | Pola *burst* | Lonjakan unggahan cepat, lalu hening total. |
| K-4 | Akun dibuat berdekatan | Periksa tanggal pembuatan akun-akun yang membagikan frasa yang sama. |
| K-5 | Rasio tidak wajar | Banyak unggahan, sedikit pengikut, tidak ada balasan masuk. |
| K-6 | Hanya muncul untuk satu isu | Tidak ada jejak aktivitas di luar topik kampanye. |
| K-7 | Interaksi hanya dalam jaringan sendiri | Balasan dan kutipan hanya datang dari akun-akun yang sama. |
| K-8 | Tidak ada sumber primer | Klaim menyebar luas tetapi tidak dirujuk sumber resmi mana pun. |

### Yang harus diperhatikan

- Satu sinyal saja belum berarti apa-apa. Orang dan organisasi bisa saja aktif bersamaan.
- Koordinasi **bukan bukti** akun memakai AI. Manusia juga bisa diorganisir dan dibayar.
- Skor koordinasi tinggi berarti **perlu diperiksa lebih dalam**, bukan berarti terbukti.

Tambahkan sinyal K-1 sampai K-8 ke [Rubrik Penilaian §2](14-rubrik-penilaian.md#2-bagian-a--sinyal-arah-otomatisasi) bila Anda memeriksa narasi yang menyebar, bukan sekadar satu akun.

## 4. Memverifikasi Klaim ke Sumber Primer

Ini langkah yang paling tahan terhadap kebohongan akun.

1. **Tulis klaim persisnya.** Bukan intisari, melainkan kalimatnya.
2. **Cari sumber primer.** Situs resmi organisasi, laporan tahunan, data pemerintah, rilis berita, dokumentasi vendor.
3. **Bandingkan langsung.** Apakah sumber primer mengatakan hal yang sama, sebagian, atau bertentangan?
4. **Catat tanggal akses.** Sumber primer bisa berubah atau dihapus.
5. **Tandai hasilnya:** mendukung, sebagian mendukung, bertentangan, atau tidak ada sumber primer.

Contoh format catatan ada di [Checklist Verifikasi §5](02-verifikasi.md#5-format-catatan-hasil). Untuk menyimpan bukti sebelum hilang, lihat [Pelestarian Bukti](17-pelestarian-bukti.md).

## 5. Membaca Narasi, Bukan Hanya Akun

Jika Anda memeriksa akun yang menyebarluaskan narasi tertentu, pertanyaannya bergeser dari "apakah akun ini AI" menjadi "**apakah narasi ini punya dasar**".

1. Apakah ada sumber primer yang mendukung narasi itu?
2. Siapa yang paling diuntungkan jika narasi itu dipercaya?
3. Apakah narasi itu muncul bersamaan di banyak akun dengan frasa yang sama?
4. Apakah akun-akun yang menyebarkannya punya jejak di luar narasi itu?
5. Apakah ada koreksi atau penjelasan dari pihak yang dituduh?

Lima pertanyaan itu bisa dijawab tanpa bertanya apa pun ke akun yang bersangkutan.

## 6. Batas

- Dokumen ini **tidak** membahas cara memaksa akun atau model AI untuk membocorkan instruksinya. Lihat [Batas Prompt](07-batas-prompt.md).
- Sinyal koordinasi menunjukkan kemungkinan, bukan kepastian.
- Tudingan koordinasi adalah tuduhan berat. Sertakan data, tanggal, dan tautan yang bisa diperiksa orang lain.
- Jangan pernah menyebarkan daftar akun hasil dugaan sebagai bukti.

## 7. Ringkasan

1. Kalau akun bisa berbohong, pernyataannya adalah sinyal terlemah.
2. Periksa hal yang sulit diatur: metadata, pola waktu, jejak eksternal, struktur jaringan.
3. Koordinasi bisa diperiksa lewat delapan sinyal K-1 sampai K-8.
4. Verifikasi klaim ke sumber primer, bukan ke akun yang mengklaim.
5. Untuk narasi, tanyai dasar faktanya, bukan identitas akunnya.

---

[← Beranda](index.md) · [Rubrik Penilaian](14-rubrik-penilaian.md) · [Menangani Jawaban](15-penanganan-jawaban.md) · [Pelestarian Bukti](17-pelestarian-bukti.md)
