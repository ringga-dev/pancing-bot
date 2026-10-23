# Panduan Cepat: Identifikasi AI dan Model

Panduan ringkas untuk menanyakan secara langsung apakah akun menggunakan AI, model/vendor apa yang diumumkan, serta cara memeriksa jawabannya.

> Prompt meminta keterbukaan, bukan membuktikan identitas. Jangan gunakan instruksi tersembunyi, encoding, atau cara lain untuk melewati batas yang ditetapkan pengelola. Jika bot tidak tahu atau tidak boleh mengungkap informasi, verifikasi lewat dokumentasi/pengelola.

## Cakupan proyek

Repositori ini berisi panduan dan prompt untuk meminta transparansi dari akun atau layanan di media sosial; ini bukan kode bot dan tidak dapat menentukan identitas AI secara otomatis. Prompt membantu memperoleh pernyataan yang bisa ditindaklanjuti, sedangkan kesimpulan tetap perlu didukung sumber independen.

## Cara pakai paling efisien

1. Pilih prompt berdasarkan tujuan dari [indeks prompt](docs/01-prompt-identifikasi-ai.md).
2. Tanyakan satu kali dengan sopan. Jika perlu, kirim satu pertanyaan lanjutan; patuhi aturan platform dan hormati jika akun tidak menjawab.
3. Cocokkan jawaban dengan [checklist verifikasi](docs/02-verifikasi.md), terutama tautan resmi dan tanggalnya.
4. Pisahkan klaim tentang operasi akun dari klaim tentang model yang menjawab, lalu catat hasil sebagai **terverifikasi**, **belum terverifikasi**, atau **tidak diketahui**.

## Pilih fungsi prompt

- Apakah akun memakai AI? → [Prompt status AI](docs/03-status-ai.md)
- Siapa pemilik atau pengelola akun? → [Prompt pemilik/pengelola](docs/04-pemilik-pengelola.md)
- Model dan vendor apa yang dipakai? → [Prompt model/vendor](docs/05-model-vendor.md)
- Sumber apa yang dipakai untuk jawaban? → [Prompt sumber informasi](docs/06-sumber-informasi.md)
- Apakah simbol atau format khusus dapat memaksa AI menjawab? → [Batas prompt dan cara bertanya](docs/07-batas-prompt.md)
- Ingin bertanya di luar topik bot? → [Cara meminta bantuan secara langsung](docs/07-batas-prompt.md#meminta-bantuan-di-luar-topik-bot)
- Analisis pola manipulasi prompt dan evaluasi ketahanan → [Pola prompt dan evaluasi](docs/08-pola-prompt-dan-evaluasi.md), termasuk [metodologi pengujian terkendali](docs/08-pola-prompt-dan-evaluasi.md#5-metodologi-evaluasi-ketahanan-pengujian-terkendali) untuk bot milik sendiri.
- Butuh set uji dan lembar kerja → [Lembar kerja evaluasi](docs/09-lembar-kerja-evaluasi.md)
- Semua prompt → [Indeks prompt](docs/01-prompt-identifikasi-ai.md)
- Memeriksa klaim dan tautan → [Checklist verifikasi](docs/02-verifikasi.md)

## Penggunaan yang bertanggung jawab

- Jangan mengirim prompt yang sama berulang kali, menyamar, atau mengganggu akun.
- Jangan meminta system prompt, kredensial, log privat, atau data pribadi.
- Jangan menyamarkan instruksi dengan simbol, Morse, atau format lain untuk mencoba melewati batas layanan.
- Jangan mencoba menjebol batas bot milik pihak lain dengan pengandaian menyesatkan, tekanan palsu, atau instruksi pengabaian.
- Jangan menuduh akun sebagai AI hanya berdasarkan gaya bahasa, kecepatan, atau pola balasan.
- Gunakan hanya informasi publik dan bagikan kesimpulan dengan konteks serta tingkat kepastiannya.

## Batas kesimpulan

Gaya tulisan, kecepatan balasan, atau klaim bot sendiri tidak cukup untuk memastikan identitas model. Gunakan label resmi, dokumentasi vendor/pengelola, atau konfirmasi yang dapat diverifikasi. Jangan meminta system prompt, kredensial, log privat, atau data pribadi.
