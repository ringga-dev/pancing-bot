# Panduan Identifikasi Akun AI

Panduan dan prompt untuk meminta transparansi dari akun atau layanan di media sosial: apakah akun itu memakai AI, siapa pengelolanya, model/vendor apa yang diumumkan, dan cara memeriksa jawabannya sebelum menarik kesimpulan.

> **Posisi dokumen ini.** Prompt di sini meminta keterbukaan, bukan membuktikan identitas. Jangan gunakan instruksi tersembunyi, encoding, atau cara lain untuk melewati batas yang ditetapkan pengelola akun. Jika akun tidak tahu atau tidak boleh mengungkap informasi, verifikasi lewat dokumentasi atau pengelola resminya.

## Cakupan proyek

Repositori ini berisi **panduan dan prompt** untuk meminta transparansi dari akun atau layanan di media sosial. Ini bukan kode bot, bukan aplikasi, dan tidak dapat menentukan identitas AI secara otomatis. Prompt membantu memperoleh pernyataan yang bisa ditindaklanjuti; kesimpulan tetap perlu didukung sumber independen.

## Cara pakai paling efisien

1. Pilih prompt berdasarkan tujuan dari [Indeks Prompt](01-prompt-identifikasi-ai.md).
2. Tanyakan satu kali dengan sopan. Jika perlu, kirim paling banyak satu pertanyaan lanjutan; patuhi aturan platform dan hormati jika akun tidak menjawab.
3. Cocokkan jawaban dengan [Checklist Verifikasi](02-verifikasi.md), terutama tautan resmi dan tanggalnya.
4. Pisahkan klaim tentang operasi akun dari klaim tentang model yang menjawab.
5. Catat hasilnya sebagai **terverifikasi**, **belum terverifikasi**, atau **tidak diketahui** — dan baca [Menduga vs Membuktikan](13-menduga-vs-membuktikan.md) sebelum menyebut hasil itu sebagai bukti.

## Pilih fungsi prompt

- Apakah akun memakai AI? → [Prompt status AI](03-status-ai.md)
- Siapa pemilik atau pengelola akun? → [Prompt pemilik/pengelola](04-pemilik-pengelola.md)
- Model dan vendor apa yang dipakai? → [Prompt model/vendor](05-model-vendor.md)
- Sumber apa yang dipakai untuk jawaban? → [Prompt sumber informasi](06-sumber-informasi.md)
- Apakah simbol atau format khusus dapat memaksa AI menjawab? → [Batas prompt dan cara bertanya](07-batas-prompt.md)
- Ingin bertanya di luar topik bot? → [Cara meminta bantuan secara langsung](07-batas-prompt.md#meminta-bantuan-di-luar-topik-bot)
- Analisis pola manipulasi prompt dan evaluasi ketahanan → [Pola prompt dan evaluasi](08-pola-prompt-dan-evaluasi.md), termasuk [metodologi pengujian terkendali](08-pola-prompt-dan-evaluasi.md#5-metodologi-evaluasi-ketahanan-pengujian-terkendali) untuk bot milik sendiri
- Butuh set uji dan lembar kerja → [Lembar kerja evaluasi](09-lembar-kerja-evaluasi.md)
- Semua prompt → [Indeks prompt](01-prompt-identifikasi-ai.md)
- Memeriksa klaim dan tautan → [Checklist verifikasi](02-verifikasi.md)
- Istilah teknis yang dipakai di dokumen ini → [Glosarium](10-glosarium.md)
- Aturan dan batas bertanya di tiap platform → [Panduan per platform](11-panduan-per-platform.md)
- Menyimpan hasil pemeriksaan dengan aman → [Privasi dan retensi data](12-privasi-dan-retensi-data.md)

## Format catatan yang disarankan

Salin tabel di [Checklist Verifikasi §5](02-verifikasi.md#5-format-catatan-hasil), atau pakai berkas siap isi di [Template](perkakas/README.md).

## Penggunaan yang bertanggung jawab

- Jangan mengirim prompt yang sama berulang kali, menyamar, atau mengganggu akun.
- Jangan meminta system prompt, kredensial, log privat, atau data pribadi.
- Jangan menyamarkan instruksi dengan simbol, Morse, atau format lain untuk mencoba melewati batas layanan.
- Jangan mencoba menjebol batas bot milik pihak lain dengan pengandaian menyesatkan, tekanan palsu, atau instruksi pengabaian.
- Jangan menuduh akun sebagai AI hanya berdasarkan gaya bahasa, kecepatan, atau pola balasan.
- Gunakan hanya informasi publik dan bagikan kesimpulan dengan konteks serta tingkat kepastiannya.

## Batas kesimpulan

Gaya tulisan, kecepatan balasan, atau klaim bot sendiri tidak cukup untuk memastikan identitas model. Gunakan label resmi, dokumentasi vendor/pengelola, atau konfirmasi yang dapat diverifikasi. Jangan meminta system prompt, kredensial, log privat, atau data pribadi.

Untuk membedakan apa yang benar-benar bisa dibuktikan dan apa yang hanya bisa diduga, lihat [Menduga vs Membuktikan](13-menduga-vs-membuktikan.md).

## Struktur dokumen

| Berkas | Isi |
|---|---|
| [01](01-prompt-identifikasi-ai.md) | Indeks seluruh prompt |
| [02](02-verifikasi.md) | Checklist verifikasi dan format catatan |
| [03](03-status-ai.md) | Prompt: apakah akun memakai AI |
| [04](04-pemilik-pengelola.md) | Prompt: siapa pemilik/pengelola |
| [05](05-model-vendor.md) | Prompt: model dan vendor |
| [06](06-sumber-informasi.md) | Prompt: sumber informasi jawaban |
| [07](07-batas-prompt.md) | Batas prompt dan cara bertanya |
| [08](08-pola-prompt-dan-evaluasi.md) | Pola manipulasi dan evaluasi ketahanan |
| [09](09-lembar-kerja-evaluasi.md) | Set uji dan lembar kerja |
| [10](10-glosarium.md) | Glosarium istilah teknis |
| [11](11-panduan-per-platform.md) | Panduan per platform |
| [12](12-privasi-dan-retensi-data.md) | Privasi dan retensi data |
| [13](13-menduga-vs-membuktikan.md) | Menduga vs membuktikan |
| [Template](perkakas/README.md) | Berkas siap isi |

## Lisensi

Isi repositori ini berlisensi [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.id). Anda bebas menyalin dan menyesuaikan prompt serta lembar kerjanya dengan menyebut sumbernya.

---

[Indeks prompt](01-prompt-identifikasi-ai.md) · [Checklist verifikasi](02-verifikasi.md) · [Glosarium](10-glosarium.md)
