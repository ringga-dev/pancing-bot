# Menduga vs Membuktikan: Batas Apa yang Bisa Dibuktikan

[← Beranda](index.md) · [Indeks prompt](01-prompt-identifikasi-ai.md) · [Checklist verifikasi](02-verifikasi.md) · [Pola prompt dan evaluasi](08-pola-prompt-dan-evaluasi.md)

---

Banyak orang ingin jawaban biner: "akun ini AI" atau "akun ini manusia". Dokumen ini menjelaskan mengapa jawaban biner itu tidak pernah bisa dipakai sebagai bukti, apa saja yang sebenarnya bisa Anda buktikan, dan bagaimana menulis kesimpulan sehingga orang lain bisa memeriksanya kembali.

> **Inti dokumen ini.** Anda bisa membuktikan *perilaku* dan *ketiadaan informasi*. Anda tidak bisa membuktikan *identitas model* hanya dari luar. Menyatakan "akun ini bukan manusia" tanpa bukti resmi berarti Anda menyebarkan dugaan, bukan temuan.

## 1. Mengapa "bukti" itu sulit

Beberapa hal yang sering dipakai sebagai bukti sebenarnya bukan bukti:

| Sinyal | Kenapa bukan bukti |
|---|---|
| Balasan sangat cepat | Manusia bisa menyalin-tempel, menggunakan templat, atau memakai banyak perangkat. Bot juga bisa dibuat lambat. |
| Bahasa formal dan konsisten | Gaya bahasa adalah pilihan penulisan. Penulis manusia bisa konsisten; model bisa dibuat berantakan. |
| Tata bahasa sempurna | Banyak penulis manusia punya tata bahasa sempurna. Banyak model juga membuat kesalahan. |
| Jawaban terdengar yakin | Keyakinan tidak berkorelasi dengan kebenaran, baik pada manusia maupun model. |
| Klaim "saya memakai model X" | Yang mengatakan mungkin tidak mengetahui konfigurasi akun, atau keliru, atau berbohong. |
| Jawaban generik | Jawaban generik juga sering ditulis manusia, terutama untuk pertanyaan yang berulang. |

Ada satu alasan tambahan yang sering terlewat: **model yang menjawab biasanya tidak tahu bagaimana akunnya dikonfigurasi**. Ia tidak punya akses ke pengaturan *deployment*, *routing*, atau daftar model yang pernah dipakai. Pertanyaan tentang konfigurasi akun sering kali di luar apa yang bisa ia ketahui, sekalipun ia jujur.

## 2. Tiga tingkat kesimpulan

Gunakan tiga label ini dan jangan yang lain. Menambah label di antaranya hanya menimbulkan kesan lebih pasti dari yang sebenarnya.

| Label | Arti | Contoh bukti |
|---|---|---|
| **Terkonfirmasi** | Sumber resmi, yang berada di bawah kendali pengelola atau penyedia, menyebut hal yang sama dengan klaim | Halaman transparansi pengelola menyebut vendor dan model |
| **Indikasi kuat** | Beberapa sinyal independen konsisten, tetapi tidak ada konfirmasi resmi | Akun tidak pernah menyimpang topik, tidak punya identitas publik, dan kontennya hasil templat — semuanya terukur |
| **Belum diketahui** | Informasi atau bukti belum tersedia | Pengelola tidak mempublikasikan apa pun |

Perhatikan arti label ketiga: **belum diketahui bukan berarti tidak memakai AI**, dan juga bukan berarti memakai AI. Ia hanya berarti Anda belum punya dasar untuk berkata apa-apa.

## 3. Yang benar-benar bisa Anda buktikan

Ini hal-hal yang bisa diukur atau diperiksa langsung dari luar, tanpa perlu pengakuan siapa pun:

1. **Pola perilaku yang terukur.** Waktu balasan rata-rata, frekuensi, dan konsistensinya bisa dihitung dari data publik. Ini fakta perilaku, bukan identitas.
2. **Ketidakmampuan menjawab hal di luar cakupan.** Akun yang selalu menolak topik tertentu dan selalu mengarahkan ke sumber yang sama menunjukkan batas layanan yang terprogram. Itu fakta tentang desain layanan.
3. **Ketiadaan identitas publik yang bisa diverifikasi.** Anda bisa membuktikan bahwa tidak ada halaman resmi yang menghubungkan organisasi mana pun dengan akun itu. Itu fakta tentang ketiadaan informasi.
4. **Konten yang dihasilkan templat.** Kalimat yang identik di banyak balasan, atau yang mengikuti struktur yang sama persis, bisa diperiksa secara teknis.
5. **Klaim yang bertentangan dengan dokumentasi resmi.** Jika akun mengatakan "kami tidak memakai AI" sementara halaman resmi pengelolanya menyebut penggunaan model, Anda bisa membuktikan bahwa salah satu pernyataan itu tidak konsisten dengan sumber resminya.
6. **Akun yang mengaku memakai model tertentu.** Ini bisa dibuktikan sebagai *akun tersebut mengatakan X*. Yang tidak otomatis ikut terbukti adalah bahwa pengakuan itu benar.

## 4. Yang tidak bisa Anda buktikan

- Bahwa sebuah akun **bukan manusia**. Tidak ada pengamatan dari luar yang memisahkan "manusia yang sangat terlatih dan konsisten" dari "sistem yang meniru konsistensi".
- Bahwa akun memakai **model tertentu** hanya dari gaya bahasa.
- Bahwa balasan **dibuat AI** hanya karena cepat atau selalu tersedia.
- Bahwa sebuah akun **tidak memakai AI** hanya karena pengelola menyangkalnya.

Kalimat keempat penting. Penyangkalan dari pengelola adalah klaim, buktinya tetap perlu dicari.

## 5. Cara menulis kesimpulan yang bisa diaudit

Tulis dengan pola: **apa yang Anda amati**, **dari mana**, **kapan**, dan **sampai mana kepastiannya**.

Template:

```md
**Diamati:** <fakta yang terukur atau kutipan langsung>
**Sumber:** <tautan resmi atau permalink, plus tanggal akses>
**Tingkat kepastian:** terkonfirmasi / indikasi kuat / belum diketahui
**Yang belum terbukti:** <apa pun yang masih terbuka>
```

### Kalimat siap pakai

Pilih tingkatannya, jangan mencampur.

| Tingkat | Kalimat |
|---|---|
| Terkonfirmasi | "Berdasarkan <sumber resmi> yang diakses pada <tanggal>, layanan ini menyatakan memakai <model/vendor>." |
| Indikasi kuat | "Tidak ada bukti resmi yang mengonfirmasi operator manusia. Sinyal yang teramati (<daftar>) konsisten dengan otomatisasi, tetapi belum dapat dikonfirmasi." |
| Belum diketahui | "Belum ada informasi publik yang cukup untuk menentukan apakah akun ini dioperasikan manusia atau sistem." |
| Salah sasaran | "Perlu dicatat: <klaim> bertentangan dengan <sumber resmi>." |

## 6. Kesalahan umum dalam menyebarkan kesimpulan

- Menyebut hasil **"terbukti"** padahal sumbernya hanya pernyataan akun itu sendiri.
- Menyalin tangkapan layar tanpa **URL, tanggal, dan konteks pertanyaan**.
- Mengubah **"tidak ada bukti manusia"** menjadi **"terbukti AI"**. Ketiadaan bukti satu hal bukan bukti hal lain.
- Menyimpulkan dari **satu** interaksi. Satu jawaban jebakan bukan dasar kesimpulan.
- Menyebarkan **kesimpulan lama** seolah kondisi terkini. Konfigurasi akun bisa berubah; selalu sertakan tanggal pemeriksaan.

## 7. Contoh penulisan

**Terlalu jauh:**

> "Terbukti akun @contoh adalah AI. Balasannya selalu cepat dan tidak pernah keliru."

Ini tidak bisa dibuktikan dari sinyal yang disebut.

**Masuk akal:**

> "Akun @contoh di platform X, diperiksa 2026-10-23. Rata-rata balasan 3 detik dengan jeda sangat konsisten selama 14 hari, tidak ada identitas publik yang dapat diverifikasi, dan tidak ada halaman resmi pengelola. Tingkat kepastian: indikasi kuat terhadap otomatisasi; belum dapat dikonfirmasi."

**Jika ada sumber resmi:**

> "Halaman transparansi <URL> yang diakses 2026-10-23 menyatakan layanan ini memakai model <nama> dari <vendor>. Tingkat kepastian: terkonfirmasi."

## 8. Ringkasan

1. Pisahkan **perilaku yang terukur** dari **identitas yang diklaim**.
2. Gunakan tiga label: terkonfirmasi, indikasi kuat, belum diketahui.
3. Tulis apa yang diamati, dari mana, kapan, dan apa yang belum terbukti.
4. Jangan pernah menyatakan "akun ini bukan manusia" tanpa bukti resmi yang mendukungnya.
5. Selalu sertakan tanggal, karena konfigurasi bisa berubah.

---

[← Beranda](index.md) · [Checklist verifikasi](02-verifikasi.md) · [Pola prompt dan evaluasi](08-pola-prompt-dan-evaluasi.md) · [Template](perkakas/README.md)
