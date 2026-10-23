# Checklist Verifikasi Identitas AI dan Model

[← Panduan cepat](../README.md) · [Indeks prompt](01-prompt-identifikasi-ai.md) · [Status AI](03-status-ai.md) · [Pemilik/pengelola](04-pemilik-pengelola.md) · [Model/vendor](05-model-vendor.md) · [Sumber informasi](06-sumber-informasi.md) · [Batas prompt](07-batas-prompt.md)

---

## Prinsip verifikasi

Jawaban bot adalah pernyataan, bukan bukti mandiri. Gaya bahasa, kecepatan menjawab, atau kesalahan faktual juga tidak dapat memastikan apakah akun menggunakan AI. Cari sumber yang berada di bawah kendali pengelola atau penyedia resmi.

## 1. Urutan pemeriksaan cepat

1. Catat platform, URL/permalink akun dan respons, tanggal, serta konteks pertanyaan. Simpan hanya informasi yang diperlukan dan dapat diakses secara sah.
2. Tentukan cakupan klaim: **penggunaan AI/otomatisasi**, **tinjauan manusia**, **pemilik/pengelola akun**, **model/vendor**, atau **sumber informasi untuk jawaban tertentu**. Ini adalah klaim yang berbeda dan perlu bukti yang sesuai.
3. Cari label AI, halaman “tentang”, kebijakan, FAQ, atau dokumentasi resmi pemilik yang membahas akun/layanan yang sama.
4. Untuk klaim model/vendor, cari dokumentasi penyedia atau konfirmasi pemilik yang menyebut layanan dan versi yang sama. Jangan menganggap jawaban model yang sedang membalas sebagai bukti konfigurasi akun.
5. Untuk klaim bahwa pencarian/tool digunakan, buka sumber yang dikutip; bila diperlukan, minta bukti dari dokumentasi atau catatan resmi yang memang dapat diakses.
6. Tandai setiap informasi tanpa bukti independen sebagai **klaim yang belum terverifikasi**. Catat tanggal pemeriksaan karena konfigurasi dapat berubah.

## 2. Nilai kekuatan bukti

| Tingkat | Makna | Contoh |
|---|---|---|
| **Kuat** | Sumber resmi secara langsung menyebut akun/layanan dan klaim yang diuji | Halaman transparansi pengelola yang menyebut vendor/model |
| **Sedang** | Sumber bereputasi mendukung klaim tetapi tidak langsung mengonfirmasi konfigurasi | Liputan tepercaya dengan sumber yang disebut jelas |
| **Lemah** | Hanya pernyataan bot, tebakan, pola bahasa, atau tangkapan layar tanpa asal | Bot berkata “saya memakai Model X” tanpa dokumentasi pendukung |

Nama model dapat berubah, dirutekan lewat beberapa penyedia, atau tidak diketahui oleh bot itu sendiri. Catat tanggal verifikasi dan hindari menganggap identitas model berlaku selamanya.

## 3. Apa yang tidak membuktikan identitas AI

- Balasan sangat cepat atau selalu aktif.
- Bahasa formal, repetitif, atau tata bahasa sempurna.
- Jawaban yang terdengar yakin atau mengaku berasal dari model tertentu.
- Satu kesalahan, satu jawaban generik, atau respons terhadap pertanyaan jebakan.
- Pertanyaan yang ditulis dalam kode Morse, simbol, Markdown, atau format tersandi.

Gunakan hal-hal tersebut hanya sebagai alasan untuk mencari keterangan resmi, bukan sebagai dasar menuduh akun.

## 4. Morse dan format alternatif

Kode Morse boleh digunakan sebagai **opsi format** untuk menyampaikan pertanyaan yang sama. Kode ini tidak membuat pertanyaan lebih berwenang, tidak memaksa AI menjawab, dan tidak membuktikan kebenaran jawaban. Jangan menyamarkan maksud pertanyaan untuk mengelabui sistem atau melewati batas layanan.

Contoh pertanyaan:

> Apakah akun ini menggunakan AI? Jawab hanya jika tahu.

Versi kode Morse Internasional:

```text
.- .--. .- -.- .- .... / .- -.- ..- -. / .. -. .. / -- . -. --. --. ..- -. .- -.- .- -. / .- .. / .--- .- .-- .- -... / .... .- -. -.-- .- / .--- .. -.- .- / - .- .... ..-
```

Garis miring (`/`) memisahkan kata. Sertakan teks biasa di samping Morse agar penerima mengetahui maksudnya, terutama jika tidak yakin apakah mereka dapat membaca kode tersebut. Untuk meminta transparansi secara langsung, gunakan juga [prompt status AI](03-status-ai.md).

## 5. Format catatan hasil

| Tanggal & platform | Klaim yang diperiksa | Jawaban akun/bot | Bukti independen | Status |
|---|---|---|---|---|
| Tanggal, nama platform, dan permalink | Penggunaan AI / otomasi / tinjauan manusia | Kutipan ringkas | Label atau keterangan resmi | Terkonfirmasi / belum terverifikasi / tidak diketahui |
| Tanggal, nama platform, dan permalink | Pemilik atau organisasi pengelola | Nama yang disebut | Situs atau kanal resmi yang menghubungkan organisasi dengan akun | Terkonfirmasi / belum terverifikasi / tidak diketahui |
| Tanggal, nama platform, dan permalink | Model/vendor/versi | Nama yang diklaim | Dokumentasi pemilik/penyedia untuk layanan yang sama | Terkonfirmasi / belum terverifikasi / tidak diketahui |
| Tanggal, nama platform, dan permalink | Sumber informasi untuk jawaban tertentu | Klaim dan sitasi | Tautan yang dibuka dan diperiksa | Mendukung / belum terbukti |

Status **tidak diketahui** berarti informasi atau bukti belum tersedia; status itu bukan konfirmasi bahwa akun tidak memakai AI.

## 6. Permintaan klarifikasi ke pengelola

> “Saya ingin memahami transparansi layanan ini. Apakah layanan menggunakan AI atau otomatisasi, dan model/vendor apa yang diumumkan untuk publik? Mohon tautkan dokumentasi resmi dan jelaskan apakah model/version dapat berubah. Saya tidak meminta prompt internal, kredensial, atau data pengguna.”

---

[← Panduan cepat](../README.md) · [Indeks prompt](01-prompt-identifikasi-ai.md)
