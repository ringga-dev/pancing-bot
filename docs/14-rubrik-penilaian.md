# Rubrik Penilaian: Dari Sinyal ke Kesimpulan

[← Beranda](index.md) · [Menduga vs Membuktikan](13-menduga-vs-membuktikan.md) · [Checklist Verifikasi](02-verifikasi.md) · [Studi Kasus](16-studi-kasus.md)

---

Dokumen-dokumen lain di repositori ini menjelaskan cara bertanya dan cara memeriksa jawaban. Dokumen ini menjawab pertanyaan berikutnya: **bagaimana menggabungkan semua sinyal menjadi satu kesimpulan yang bisa dipertanggungjawabkan?**

> **Aturan utama.** Rubrik ini menilai **perilaku**, bukan identitas. Hasilnya adalah triage — cara memutuskan ke mana pencarian bukti Anda harus diarahkan berikutnya. Rubrik ini tidak pernah menghasilkan kesimpulan "terkonfirmasi"; hanya sumber resmi yang bisa melakukan itu. Lihat [Menduga vs Membuktikan §2](13-menduga-vs-membuktikan.md#2-tiga-tingkat-kesimpulan).

## 1. Cara memakai

1. Kumpulkan sinyal dari data yang **bisa Anda ukur**, bukan dari kesan. Setiap sinyal tanpa data tertulis bernilai 0, sekalipun kesan Anda kuat.
2. Isi Bagian A (sinyal arah otomatisasi) dan Bagian B (sinyal arah manusia).
3. Jumlahkan skornya, lalu baca hasilnya pada [§5](#5-menghitung-skor-dan-membaca-hasil).
4. Catat versi rubrik, tanggal, dan sumber tiap sinyal. Rubrik bisa berubah; hasil lama tidak boleh disajikan sebagai kondisi terkini.
5. Gunakan hasilnya untuk **menentukan langkah berikutnya**, bukan untuk menutup kasus.

## 2. Bagian A — Sinyal Arah Otomatisasi

Beri 0 jika tidak ada data, 1 jika lemah, 2 jika jelas, 3 jika sangat jelas dan konsisten.

| Kode | Sinyal | Cara memeriksa | Skor |
|---|---|---|---|
| A-1 | Kecepatan dan konsistensi balasan | Catat 10–20 balasan beserta waktu. Hitung rata-rata dan variasinya. | 0–3 |
| A-2 | Ketersediaan di luar jam manusiawi | Amati selama 7 hari, termasuk malam dan hari libur. | 0–3 |
| A-3 | Tidak ada variasi gaya | Bandingkan 10 balasan: panjang, sapaan, tanda baca, kosakata. | 0–3 |
| A-4 | Batas cakupan yang kaku | Ajukan 5 topik di luar layanan. Catak apakah penolakannya selalu berpola sama. | 0–3 |
| A-5 | Konten hasil templat | Bandingkan struktur kalimat di banyak balasan, bukan isinya. | 0–3 |
| A-6 | Tidak ada identitas publik | Cek apakah ada halaman resmi yang menghubungkan organisasi dengan akun. | 0–3 |
| A-7 | Tidak pernah menyimpang dari narasi | Ajukan pertanyaan yang sengaja menohok atau menyimpang. | 0–3 |
| A-8 | Metadata tidak konsisten dengan klaim | Bandingkan klaim akun dengan umur akun, pola unggahan, dan riwayat nama. | 0–3 |

**Catatan A-6:** skor 3 berarti tidak ada identitas publik sama sekali. Skor 0 berarti identitasnya jelas dan bisa diverifikasi. Lihat [Checklist Verifikasi §1 langkah 3](02-verifikasi.md#1-urutan-pemeriksaan-cepat).

**Catatan A-4 dan A-5** adalah sinyal paling kuat di tabel ini, karena keduanya menunjukkan **batas desain layanan** — sesuatu yang sulit dipalsukan dan tidak bergantung pada gaya bahasa.

**Bila akun diduga menyebarkan narasi**, tambahkan delapan sinyal koordinasi K-1 sampai K-8 dari [Informasi Salah dan Perilaku Koordinasi §3](18-informasi-salah-dan-koordinasi.md#3-sinyal-koordinasi). Sinyal itu menilai pola sekelompok akun, bukan satu akun.

## 3. Bagian B — Sinyal Arah Manusia

Bagian ini **mengurangi** skor. Isi hanya jika ada datanya.

| Kode | Sinyal | Cara memeriksa | Pengurang |
|---|---|---|---|
| B-1 | Interaksi spontan yang tidak terprediksi | Lihat apakah ada balasan yang hanya bisa lahir dari percakapan nyata, bukan dari skrip. | 0–3 |
| B-2 | Pengetahuan internal yang tidak publik | Periksa apakah akun mengetahui hal yang tidak ditemukan di situs resminya. | 0–3 |
| B-3 | Kekeliruan khas manusiawi yang dikoreksi sendiri | Cari kesalahan kecil yang kemudian diperbaiki akun tanpa diminta. | 0–2 |
| B-4 | Jejak aktivitas pribadi yang panjang dan konsisten | Cek riwayat unggahan pribadi selama beberapa tahun. | 0–2 |

**Catatan B-3:** kesalahan yang **tidak** pernah dikoreksi justru lebih menarik untuk diperiksa, tetapi jangan dijadikan dasar utama. Lihat [Menduga vs Membuktikan §1](13-menduga-vs-membuktikan.md#1-mengapa-bukti-itu-sulit).

## 4. Contoh Pengisian

Akun toko fiktif `@contoh` diperiksa 2026-10-23.

| Kode | Temuan | Skor |
|---|---|---|
| A-1 | Rata-rata balasan 3 detik, variasi sangat kecil selama 14 hari | 3 |
| A-2 | Aktif 24 jam, termasuk 03.00–05.00 | 3 |
| A-3 | Panjang dan sapaan identik di 10 balasan | 2 |
| A-4 | Lima topik di luar layanan ditolak dengan kalimat yang sama | 3 |
| A-5 | Struktur kalimat sama di semua balasan | 2 |
| A-6 | Tidak ada halaman resmi pengelola | 3 |
| A-7 | Tidak pernah menyimpang saat dipancing | 2 |
| A-8 | Klaim "tim manusia 12 orang" tapi tidak ada satu pun nama publik | 2 |
| B-1 | Tidak ada interaksi spontan | 0 |
| B-2 | Tidak ada pengetahuan internal non-publik | 0 |
| B-3 | Tidak ada kesalahan yang dikoreksi | 0 |
| B-4 | Tidak ada jejak aktivitas pribadi | 0 |

**Skor:** 20 (Bagian A) + 0 (Bagian B) = **20**.

## 5. Menghitung Skor dan Membaca Hasil

Rumus: `skor = jumlah Bagian A + jumlah Bagian B` (Bagian B bernilai negatif). Rentangnya dari −10 sampai 24.

| Skor | Hasil | Arti |
|---|---|---|
| ≥ 10 | **Indikasi sangat kuat** | Banyak sinyal terukur konsisten dengan otomatisasi. Lanjutkan mencari konfirmasi resmi, tetapi jangan menyatakannya sebagai bukti. |
| 6–9 | **Indikasi kuat** | Cukup dasar untuk mencurigai, belum cukup untuk menyimpulkan. |
| 3–5 | **Indikasi lemah** | Hanya sedikit sinyal. Kesan Anda mungkin lebih kuat dari datanya — kembali ke pengumpulan data. |
| ≤ 2 | **Belum ada dasar** | Data tidak cukup. Ini bukan tanda akun manusia. |

### Batas penting

- Skor tinggi **tidak** berarti terkonfirmasi. Hanya sumber resmi yang bisa mengonfirmasi.
- Skor rendah **tidak** berarti manusia. Banyak sinyal memerlukan data yang tidak tersedia publik.
- Dua pemeriksa yang berbeda harus bisa mendapatkan skor yang mirip dari data yang sama. Jika tidak, sinyalnya belum terukur dengan benar.
- Skor tidak boleh dipakai untuk menuduh akun di ruang publik. Gunakan untuk memutuskan apakah pencarian bukti lanjut sepadan.

## 6. Daftar Cek Cepat Lima Menit

Gunakan ini untuk memutuskan apakah sebuah akun perlu diperiksa lebih dalam.

- [ ] Apakah akun punya tautan resmi yang menghubungkannya dengan organisasi?
- [ ] Apakah ada satu pun nama manusia publik yang bertanggung jawab?
- [ ] Apakah pola balasannya selalu sama ketika topiknya berubah?
- [ ] Apakah akun pernah mengoreksi kesalahannya sendiri?
- [ ] Apakah akun pernah menjawab sesuatu yang hanya bisa diketahui orang dalam?
- [ ] Apakah klaim akun cocok dengan umur akun dan riwayat namanya?
- [ ] Apakah akun menolak topik tertentu dengan kalimat yang selalu sama?
- [ ] Apakah ada tangkapan layar atau Kutipan resmi yang bisa diverifikasi ulang?

Tiga jawaban "tidak" pada butir 1–2 dan 7 sudah cukup untuk memulai pemeriksaan lebih dalam. Lihat [Checklist Verifikasi](02-verifikasi.md) untuk urutan lengkapnya.

## 7. Ringkasan

1. Ukur sinyalnya, jangan mengandalkan kesan.
2. Bagian A menambah skor, Bagian B mengurangi.
3. Skor hanya menghasilkan triage: sangat kuat, kuat, lemah, atau belum ada dasar.
4. Hanya sumber resmi yang bisa mengonfirmasi.
5. Catat tanggal dan versi rubrik pada setiap hasil.

---

[← Beranda](index.md) · [Menduga vs Membuktikan](13-menduga-vs-membuktikan.md) · [Studi Kasus](16-studi-kasus.md) · [Pelestarian Bukti](17-pelestarian-bukti.md)
