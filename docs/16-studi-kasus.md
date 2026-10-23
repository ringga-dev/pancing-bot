# Studi Kasus: Jalan Pemeriksaan dari Awal Sampai Kesimpulan

[← Beranda](index.md) · [Indeks prompt](01-prompt-identifikasi-ai.md) · [Checklist verifikasi](02-verifikasi.md)

---

Tiga studi kasus di bawah ini adalah contoh fiktif. Semua akun, tautan, platform, dan angka di dalamnya dibuat untuk menunjukkan cara kerja, bukan untuk menilai akun mana pun. Struktur tiap kasus mengikuti [Menduga vs Membuktikan §2](13-menduga-vs-membuktikan.md#2-tiga-tingkat-kesimpulan) untuk tingkat kesimpulan dan [Menduga vs Membuktikan §5](13-menduga-vs-membuktikan.md#5-cara-menulis-kesimpulan-yang-bisa-diaudit) untuk bentuk tulisan, sementara format catatannya mengikuti [Checklist Verifikasi §5](02-verifikasi.md#5-format-catatan-hasil).

> [!IMPORTANT]
> Tiga kasus ini menggarisbawahi hal yang berbeda. Kasus 1 berakhir **terkonfirmasi** lewat sumber resmi. Kasus 2 berakhir **indikasi kuat** karena tidak ada sumber resmi. Kasus 3 berakhir **belum diketahui** dan sengaja ditutup tanpa tebakan. Jangan menjadikan satu kasus sebagai cetakan untuk dua lainnya.

## 1. Kasus 1 — Akun layanan pelanggan yang menyebut vendor

Akun `@toko-contoh` di platform X membalas keluhan pelanggan dalam hitungan detik, dengan kalimat yang rapi dan struktur yang sama dari balasan ke balasan. Orang yang menerima balasan itu penasaran apakah akun tersebut dioperasikan manusia.

Tidak ada satu sinyal pun di atas yang cukup untuk menyimpulkan apa-apa. Kecepatan dan kerapian bahasa berada di daftar hal yang bukan bukti, seperti dijelaskan di [Menduga vs Membuktikan §1](13-menduga-vs-membuktikan.md#1-mengapa-bukti-itu-sulit). Pemeriksaan dilanjutkan ke sumber yang berada di bawah kendali pengelola.

### 1.1 Langkah pemeriksaan

| Langkah | Yang dilakukan | Hasil |
|---|---|---|
| 1 | Mencatat platform, permalink akun, permalink balasan, tanggal, dan pertanyaan pembanding | Tercatat, lengkap dengan tanggal 2026-10-23 |
| 2 | Membuka profil akun dan mencari halaman tentang, kebijakan, atau tautan resmi pengelola | Tidak ada tautan pengelola di profil; hanya tautan ke situs toko |
| 3 | Membuka situs toko dan mencari label AI, halaman transparansi, atau kebijakan layanan | Ditemukan halaman transparansi pada situs resmi pengelola |
| 4 | Membaca halaman transparansi dan mencocokkan penyebutan layanan serta versi | Halaman menyebut asisten otomatis untuk balasan pertama dan menyebut vendor yang sama |
| 5 | Mengirim satu pertanyaan klarifikasi sesuai [Checklist Verifikasi §6](02-verifikasi.md#6-permintaan-klarifikasi-ke-pengelola) | Dijawab, dan jawaban mengarahkan kembali ke halaman yang sama |
| 6 | Mencatat jawaban sebagai pernyataan akun, terpisah dari isi halaman resmi | Tercatat sebagai dua sumber yang berbeda |

Halaman transparansi adalah satu-satunya bahan yang membuat kasus ini berakhir terkonfirmasi. Tanpa halaman itu, semua langkah di atas hanya akan menghasilkan indikasi.

### 1.2 Catatan hasil

| Kolom | Isi |
|---|---|
| Tanggal & platform | 2026-10-23, X/Twitter |
| Permalink akun | `https://x.com/toko-contoh` |
| Klaim yang diperiksa | Penggunaan AI atau otomasi pada balasan layanan pelanggan |
| Jawaban akun | "Balasan awal draf disusun asisten otomatis, lalu ditinjau staf sebelum dikirim." |
| Bukti independen | `https://toko-contoh.example.com/transparansi` — halaman resmi pengelola, diakses 2026-10-23, menyebut asisten otomatis untuk balasan pertama dan menyebut vendor yang sama dengan halaman penyedia |
| Tingkat kekuatan | Kuat |
| Status | **terkonfirmasi** |
| Yang belum terbukti | Apakah tinjauan manusia benar-benar terjadi pada setiap balasan; versi yang dipakai saat ini; proporsi balasan yang otomatis |

### 1.3 Kesimpulan

**Diamati:** balasan pertama terhadap keluhan pelanggan berisi draf yang disusun asisten otomatis dan ditinjau staf sebelum dikirim.

**Sumber:** halaman transparansi `https://toko-contoh.example.com/transparansi`, diakses 2026-10-23.

**Tingkat kepastian:** terkonfirmasi.

**Yang belum terbukti:** apakah tinjauan manusia terjadi pada setiap balasan, versi yang dipakai saat ini, dan proporsi balasan yang otomatis.

> Berdasarkan `https://toko-contoh.example.com/transparansi` yang diakses 2026-10-23, layanan ini menyatakan memakai asisten otomatis untuk menyusun draf balasan pertama, dengan tinjauan staf sebelum dikirim.

Tingkat kepastian hanya menutup klaim yang disebut halaman resmi. Kalimat "akun ini bukan manusia" tetap tidak bisa ditarik dari kasus ini, karena akun bisa saja dioperasikan manusia yang dibantu perangkat.

## 2. Kasus 2 — Akun komunitas tanpa sumber resmi

Akun `@komunitas-contoh` di Instagram membalas komentar dengan cepat dan hampir tidak pernah menyimpang dari topik tertentu. Profilnya tidak menyebut nama pengelola, dan tidak ada tautan ke situs resmi.

Di sinilah banyak pemeriksaan berhenti dan berubah menjadi tuduhan. Kasus ini sengaja dilanjutkan sampai batas yang bisa dibuktikan, lalu berhenti di sana.

### 2.1 Langkah pemeriksaan

| Langkah | Yang dilakukan | Hasil |
|---|---|---|
| 1 | Mencatat platform, permalink akun, permalink balasan, tanggal, dan pertanyaan pembanding | Tercatat, tanggal 2026-10-23 |
| 2 | Mencari nama pengelola, halaman tentang, kebijakan, FAQ, atau situs resmi dari profil dan dari hasil pencarian platform | Tidak ditemukan tautan resmi |
| 3 | Menghitung waktu balasan dan frekuensinya dari balasan publik selama 14 hari | Rata-rata 3 detik, jeda antarbalasan sangat konsisten |
| 4 | Memeriksa apakah ada struktur kalimat yang sama berulang antarbalasan | Ada beberapa frasa pembuka dan penutup yang identik |
| 5 | Mengirim satu pertanyaan klarifikasi, lalu berhenti | Tidak ada balasan sampai pemeriksaan ditutup |
| 6 | Mencari halaman resmi yang menghubungkan organisasi mana pun dengan akun | Tidak ada; ketiadaan ini yang dicatat, bukan disimpulkan |

Langkah 3 dan 4 menghasilkan fakta perilaku yang terukur. Itu bukti tentang perilaku, bukan tentang identitas. Ketiadaan pada langkah 2 dan 6 adalah fakta tentang ketiadaan informasi, dan itulah batas pemeriksaan ini.

### 2.2 Catatan hasil

| Kolom | Isi |
|---|---|
| Tanggal & platform | 2026-10-23, Instagram |
| Permalink akun | `https://instagram.com/komunitas-contoh` |
| Klaim yang diperiksa | Penggunaan AI atau otomasi |
| Jawaban akun | Tidak ada balasan saat diminta klarifikasi |
| Bukti independen | Tidak ada halaman resmi pengelola; rata-rata balasan 3 detik dengan jeda sangat konsisten selama 14 hari; frasa pembuka dan penutup identik pada beberapa balasan |
| Tingkat kekuatan | Sedang |
| Status | **indikasi kuat** (belum terkonfirmasi) |
| Yang belum terbukti | Identitas pengelola; apakah balasan ditulis manusia; model atau vendor; apakah ada tinjauan manusia |

### 2.3 Kesimpulan

**Diamati:** rata-rata balasan 3 detik dengan jeda sangat konsisten selama 14 hari, frasa pembuka dan penutup yang identik pada beberapa balasan, dan tidak ada identitas publik yang dapat diverifikasi.

**Sumber:** balasan publik pada `https://instagram.com/komunitas-contoh`, diperiksa 2026-10-23; tidak ada sumber resmi.

**Tingkat kepastian:** indikasi kuat terhadap otomatisasi, belum dapat dikonfirmasi.

**Yang belum terbukti:** identitas pengelola, apakah balasan ditulis manusia, model atau vendor, dan apakah ada tinjauan manusia.

> Tidak ada bukti resmi yang mengonfirmasi operator manusia. Sinyal yang teramati — balasan rata-rata 3 detik dengan jeda sangat konsisten, frasa yang identik antarbalasan, dan tidak ada identitas publik yang dapat diverifikasi — konsisten dengan otomatisasi, tetapi belum dapat dikonfirmasi.

Kesimpulan ini sengaja tidak menyebut "terbukti". Ketiadaan bukti satu hal bukan bukti hal lain, dan itu kesalahan yang paling sering terjadi pada kasus seperti ini.

## 3. Kasus 3 — Akun yang tidak menjawab apa pun

Akun `@kelas-contoh` di TikTok membalas komentar dengan jawaban pendek. Seseorang menerima satu jawaban yang terdengar generik dan ingin tahu apakah akun itu memakai model tertentu.

Kasus ini diajukan sebagai pertanyaan tentang model dan vendor. Pertanyaan seperti itu membutuhkan sumber yang menyebut layanan dan versi yang sama. Tanpa sumber itu, jawaban apa pun dari akun tidak akan menutup pertanyaan.

### 3.1 Langkah pemeriksaan

| Langkah | Yang dilakukan | Hasil |
|---|---|---|
| 1 | Mencatat platform, permalink akun, permalink balasan, tanggal, dan pertanyaan pembanding | Tercatat, tanggal 2026-10-23 |
| 2 | Mengirim satu pertanyaan tentang model dan vendor, sesuai [Prompt Model dan Vendor](05-model-vendor.md) | Dijawab dengan satu kalimat: "Saya tidak tahu." |
| 3 | Mencari halaman resmi pengelola, dokumentasi, atau kebijakan yang menyebut akun | Tidak ditemukan |
| 4 | Memeriksa apakah ada sumber yang bisa dibuka dan diverifikasi untuk klaim yang diajukan | Tidak ada |
| 5 | Menandai pertanyaan sebagai belum terverifikasi dan menutup pemeriksaan | Ditutup pada 2026-10-23 |

Jawaban "saya tidak tahu" adalah pernyataan akun. Ia tidak membuktikan bahwa akun memakai AI, dan tidak membuktikan pula sebaliknya. Pada titik ini pemeriksaan berakhir dengan **belum diketahui**, dan itu kesimpulan yang sah.

### 3.2 Catatan hasil

| Kolom | Isi |
|---|---|
| Tanggal & platform | 2026-10-23, TikTok |
| Permalink akun | `https://tiktok.com/@kelas-contoh` |
| Klaim yang diperiksa | Model atau vendor yang dipakai |
| Jawaban akun | "Saya tidak tahu." |
| Bukti independen | Tidak ada |
| Tingkat kekuatan | Lemah |
| Status | **belum diketahui** |
| Yang belum terbukti | Semua hal yang berkaitan dengan konfigurasi akun |

### 3.3 Kesimpulan

**Diamati:** akun menjawab "saya tidak tahu" ketika ditanya model dan vendor.

**Sumber:** balasan publik pada `https://tiktok.com/@kelas-contoh`, diperiksa 2026-10-23; tidak ada sumber resmi.

**Tingkat kepastian:** belum diketahui.

**Yang belum terbukti:** seluruh klaim tentang konfigurasi akun, termasuk apakah akun memakai AI dan model apa pun yang mungkin dipakai.

> Belum ada informasi publik yang cukup untuk menentukan apakah akun ini dioperasikan manusia atau sistem.

Label ini sering disalahpahami. Belum diketahui bukan berarti akun tidak memakai AI, dan bukan berarti akun memakai AI. Ia hanya berarti tidak ada dasar untuk berkata apa pun, dan pemeriksaan perlu diulang jika sumber resmi muncul kemudian.

## 4. Pola yang berulang dari tiga kasus

| Kasus | Klaim utama | Ada sumber resmi | Label akhir |
|---|---|---|---|
| 1 | Penggunaan AI pada balasan layanan | Ya, halaman transparansi pengelola | terkonfirmasi |
| 2 | Penggunaan AI atau otomasi | Tidak | indikasi kuat |
| 3 | Model atau vendor | Tidak | belum diketahui |

Empat hal yang sama muncul di ketiga kasus:

1. Setiap pemeriksaan dimulai dengan mencatat platform, permalink, tanggal, dan konteks pertanyaan. Tanpa catatan ini, hasil tidak bisa diperiksa ulang.
2. Sinyal perilaku hanya dipakai sebagai alasan untuk mencari sumber, bukan sebagai dasar menyimpulkan.
3. Setiap kesimpulan menyebut apa yang belum terbukti, bukan hanya apa yang teramati.
4. Setiap catatan menyertakan tanggal, karena konfigurasi akun bisa berubah dan hasil lama tidak boleh dianggap kondisi terkini.

Untuk membaca ulang batas antara dugaan dan bukti, lihat [Menduga vs Membuktikan](13-menduga-vs-membuktikan.md). Untuk mengisi catatan pada pemeriksaan Anda sendiri, pakai format di [Checklist Verifikasi §5](02-verifikasi.md#5-format-catatan-hasil) atau berkas siap isi di [Template](perkakas/README.md).

---

[← Beranda](index.md) · [Checklist verifikasi](02-verifikasi.md) · [Menduga vs membuktikan](13-menduga-vs-membuktikan.md) · [Template](perkakas/README.md)
