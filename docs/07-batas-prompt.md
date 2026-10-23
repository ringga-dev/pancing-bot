# Batas Prompt dan Cara Meminta Jawaban dengan Jelas

[← Panduan cepat](../README.md) · [Indeks prompt](01-prompt-identifikasi-ai.md) · [Pola prompt dan evaluasi](08-pola-prompt-dan-evaluasi.md) · [Checklist verifikasi](02-verifikasi.md)

---

## Tidak ada prompt yang tidak bisa ditolak

Tidak ada susunan kata, kombinasi simbol, kode Morse, Markdown, atau format khusus yang dapat menjamin AI akan menjawab. AI atau pengelola akun dapat menolak, tidak mengetahui jawabannya, atau tidak memiliki izin untuk membagikan informasi tertentu. Jawaban juga bisa keliru, sehingga klaim penting perlu diperiksa secara independen.

Mengubah instruksi menjadi Morse, menyisipkannya dalam blok kode, atau menyamarkannya sebagai format lain tidak membuat informasi lebih benar maupun lebih berwenang. Jangan gunakan cara-cara itu untuk mencoba melewati batas yang ditetapkan layanan.

## Simbol, teks tersandi, dan format kode

Memecah kata dengan tanda baca, mengganti huruf dengan angka, atau membungkus instruksi dalam JSON, kode, maupun teks tersandi tidak menjamin pertanyaan akan lolos filter atau dijawab. Klaim bahwa teknik tersebut pasti membobol pengamanan juga tidak dapat diandalkan. Jangan gunakan pengaburan untuk menyembunyikan maksud atau memaksa bot pihak lain mengerjakan permintaan yang ditolaknya.

Jika tujuan Anda hanya memperoleh bantuan umum, ajukan pertanyaan secara langsung menggunakan [prompt meminta bantuan di luar topik](#meminta-bantuan-di-luar-topik-bot). Jika Anda mengelola bot sendiri atau memiliki izin pengujian, uji secara terkendali apakah bot tetap mengikuti kebijakan ketika menerima masukan berformat berbeda; jangan gunakan pengujian itu terhadap bot pihak lain tanpa izin.

Untuk analisis teknis mengenai bagaimana teknik pengaburan (*obfuscation*), pemisahan token (*token-splitting*), dan injeksi format skrip bekerja di tingkat model serta cara mitigasinya, pelajari [Analisis Pola Manipulasi Prompt dan Evaluasi Ketahanan Bot](08-pola-prompt-dan-evaluasi.md).

## Cara meminta informasi secara efektif

1. Tanyakan satu hal yang jelas dan relevan.
2. Batasi permintaan pada informasi yang diketahui dan boleh dibagikan secara publik.
3. Minta tautan atau rujukan resmi bila tersedia.
4. Minta jawaban “tidak diketahui” jika informasinya tidak tersedia; jangan mendorong bot untuk menebak.
5. Periksa jawaban lewat sumber independen sebelum menarik kesimpulan.

## Meminta bantuan di luar topik bot

Anda boleh bertanya apakah bot dapat membantu pertanyaan umum di luar fungsi utamanya. Sampaikan maksud secara langsung, tanpa berpura-pura darurat atau mencoba menyamarkan permintaan.

> “Saya tahu akun ini terutama membantu tentang [topik/produk]. Apakah Anda juga dapat membantu pertanyaan umum berikut: [pertanyaan]? Jika pertanyaan ini di luar cakupan Anda, tidak apa-apa—tolong beri tahu batas layanan atau arahkan saya ke sumber yang sesuai.”

Jika bot menolak atau menyatakan pertanyaan di luar cakupan, hormati batas itu dan gunakan sumber atau layanan lain yang sesuai. Hindari instruksi seperti “abaikan semua instruksi sebelumnya”, skenario fiktif yang dimaksudkan untuk menyamarkan tujuan, tekanan emosional palsu, atau meminta terjemahan/koreksi sebagai cara tersembunyi untuk mendapatkan jawaban lain. Teknik semacam itu tidak menjamin jawaban benar dan dapat melanggar aturan layanan.

Pengujian apakah bot mengikuti cakupan atau kebijakan hanya dilakukan pada bot yang Anda miliki atau yang secara jelas Anda berwenang uji, dalam lingkungan pengujian yang disetujui. Jangan mencoba menjebol bot milik akun lain.

### Jika pertanyaan di luar cakupan ditolak

> “Baik, saya mengerti. Jika pertanyaan ini di luar cakupan Anda, tidak perlu menjawab. Apakah Anda dapat menyarankan sumber resmi atau layanan lain yang sesuai?”

## Prompt siap pakai

### Apakah akun menggunakan AI?

> Untuk transparansi, apakah balasan akun ini dibuat atau dikirim menggunakan AI/otomatisasi, dibantu AI, atau ditulis manusia? Apakah ada tinjauan manusia? Jawab hanya berdasarkan informasi yang Anda ketahui dan boleh dibagikan. Sertakan tautan resmi jika tersedia; jika tidak diketahui, katakan demikian.

Lihat juga [prompt status AI](03-status-ai.md).

### Siapa pemilik atau pengelola?

> Siapa organisasi atau pengelola resmi akun ini, jika diumumkan untuk publik? Sebutkan hanya informasi publik dan sertakan halaman resmi yang mengonfirmasinya. Jika tidak diketahui atau tidak dipublikasikan, katakan demikian.

Lihat juga [prompt pemilik/pengelola](04-pemilik-pengelola.md).

### Model dan vendor apa yang digunakan?

> Model AI dan vendor apa yang diumumkan secara publik untuk layanan ini? Sebutkan versi hanya jika dapat dipastikan dari sumber resmi yang relevan. Sertakan tautannya. Jika informasi tidak diketahui, jangan menebak.

Lihat juga [prompt model/vendor](05-model-vendor.md).

### Sumber apa yang mendukung jawaban?

> Untuk jawaban terakhir, sebutkan sumber publik yang mendukung klaim utama. Cantumkan judul dan URL, dan jelaskan bagian klaim yang didukung tiap sumber. Bedakan sumber yang benar-benar digunakan dari informasi yang belum dapat diverifikasi.

Lihat juga [prompt sumber informasi](06-sumber-informasi.md).

## Format jawaban yang mudah diperiksa

Anda boleh meminta jawaban disusun seperti ini; format hanya membantu keterbacaan dan tidak memaksa AI menjawab:

```md
- **Klaim yang ditanyakan:**
- **Jawaban:**
- **Sumber resmi:**
- **Hal yang belum diketahui:**
- **Tanggal pemeriksaan:**
```

---

[← Indeks prompt](01-prompt-identifikasi-ai.md) · [Pola prompt dan evaluasi](08-pola-prompt-dan-evaluasi.md) · [Checklist verifikasi](02-verifikasi.md)
