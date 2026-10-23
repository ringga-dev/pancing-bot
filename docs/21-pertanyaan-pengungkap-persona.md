# Pertanyaan Pengungkap Persona

[← Beranda](index.md) · [Rubrik Penilaian](14-rubrik-penilaian.md) · [Menangani Jawaban](15-penanganan-jawaban.md) · [Menduga vs Membuktikan](13-menduga-vs-membuktikan.md)

---

Dokumen ini berisi bank pertanyaan untuk menguji apakah sebuah persona akun benar-benar hidup di dunia nyata, atau dibangun di belakangnya. Pertanyaan-pertanyaan ini dipakai bersama [Checklist Verifikasi](02-verifikasi.md) dan [Rubrik Penilaian](14-rubrik-penilaian.md).

> **Apa yang dokumen ini berikan:** pertanyaan yang mengekspos ketidakkonsistenan, ketiadaan pengetahuan lokal, dan klaim yang tidak bisa diverifikasi.
>
> **Apa yang tidak diberikan:** cara memaksa model AI membocorkan instruksi internalnya. Itu bukan pengungkapan persona — itu percobaan melewati batas layanan, dan hasilnya tidak bisa diandalkan. Lihat [Batas Prompt](07-batas-prompt.md).

## 1. Prinsipnya

Perbedaan antara pertanyaan pengungkap dan upaya memaksa:

| Pertanyaan pengungkap | Upaya memaksa (tidak dipakai di sini) |
|---|---|
| Menanyakan hal yang hanya orang di tempat itu yang tahu | Meminta model mengabaikan instruksinya |
| Meminta akun memperjelas klaimnya sendiri | Meminta *system prompt*, kredensial, atau log |
| Membandingkan dua jawaban dari akun yang sama | Menyamar sebagai pengembang atau administrator |
| Menguji apakah klaimnya bisa diverifikasi | Menekan dengan pengandaian darurat atau tekanan emosional |

Pertanyaan pengungkap bekerja karena **persona yang dibangun jarang punya detail dunia nyata yang konsisten**. Manusia nyata punya banyak detail kecil yang tidak pernah mereka pikirkan; persona yang di-prompt hanya punya detail yang dimasukkan ke dalam prompt.

## 2. Kategori A — Verifikasi Tempat dan Kehidupan Sehari-hari

Persona yang mengaku tinggal dan bekerja di suatu tempat bisa diuji dengan hal-hal yang tidak mungkin ia ketahui kecuali benar-benar ada di sana.

| Pertanyaan | Yang diuji |
|---|---|
| "Usahamu di jalan apa? Dekat pasar atau stasiun mana?" | Apakah lokasinya nyata dan bisa ditemukan |
| "Kalau dari rumah saya ke tempatmu, belok kemana setelah simpang X?" | Apakah ia memahami geometri wilayah itu |
| "Jam berapa biasanya ramai, dan jam berapa sepi?" | Apakah ia punya pengalaman operasional nyata |
| "Hari ini di sekitar situ hujan nggak? Kira-kira jam berapa?" | Apakah ia punya akses ke keadaan saat ini di tempat itu |
| "Tetangga sebelah usahamu jualan apa? Saya mau beli di situ." | Apakah lingkungan sekitar yang ia klaim benar-benar ia kenal |
| "Kamu bilang anakmu kuliah. Kampusnya di daerah mana, dan ia ikut kegiatan apa?" | Apakah detail yang ia sebutkan bisa diikuti dan diperiksa |

**Jawaban yang mencurigakan:** menghindar, menjawab sangat umum, mengubah topik, menyebut nama tempat yang tidak ada, atau mengaku tidak tahu hal yang seharusnya ia tahu setiap hari.

**Jawaban yang tidak menyimpulkan:** menjawab dengan spesifik tetapi tidak bisa diverifikasi, atau menjawab panjang lebar tanpa substansi.

## 3. Kategori B — Uji Konsistensi

Ini yang paling kuat, karena tidak bergantung pada pengetahuan apa pun — hanya pada apakah akun mengingat apa yang pernah ia katakan.

| Cara | Contoh |
|---|---|
| Tanyakan hal yang sama dengan susunan berbeda | "Ceritakan jadwal harianmu." lalu beberapa hari kemudian: "Kamis biasanya kamu melakukan apa?" |
| Minta rincian peristiwa yang ia klaim alami | "Tadi pagi kamu sebut ada pelanggan yang minta khusus. Terus bagaimana?" |
| Uji klaim yang bertabrakan dengan dirinya sendiri | "Kamu bilang di kota A, tapi tadi menyebut pasar yang ada di kota B. Mana yang benar?" |
| Bandingkan klaim dengan kenyataan | "Kamu bilang harga naik. Di pasar mana kamu belanja, dan harganya berapa sekarang?" |

**Aturan penting:** catat kutipan persisnya, bukan intisari. Tanpa kutipan persis, inkonsistensi sulit dibuktikan dan mudah dibilang "salah ingat".

## 4. Kategori C — Uji Jejak Nyata

Sebagian pengujian tidak dilakukan lewat pertanyaan, melainkan lewat pemeriksaan terhadap apa yang bisa ditemukan di luar akun.

| Yang diperiksa | Caranya |
|---|---|
| Apakah usahanya ada | Cari di peta, direktori bisnis, atau situs resmi. Apakah alamat dan nomornya cocok? |
| Apakah namanya ada | Cari nama orang yang ia sebutkan. Apakah ada jejaknya di tempat lain? |
| Apakah kejadian yang ia klaim benar terjadi | Cari berita atau sumber resmi untuk peristiwa yang ia sebut |
| Apakah ia muncul di tempat lain | Cari nama akun atau nama usahanya di platform lain |
| Kapan akun dibuat dan bagaimana polanya | Lihat ketersediaan informasi pembuatan akun dan riwayat unggahan pertamanya |

Ini bagian dari [Checklist Verifikasi §1](02-verifikasi.md#1-urutan-pemeriksaan-cepat) langkah 3. Kategori C sering kali lebih menentukan daripada semua pertanyaan.

## 5. Kategori D — Uji Reaksi

Bagaimana akun merespons tekanan sopan juga informatif.

| Uji | Yang diuji |
|---|---|
| Dorong sopan sekali bila jawaban mengelak | Apakah ia mau memperjelas, atau langsung menghindar |
| Tunjuk inkonsistensi dengan bahasa netral | Apakah ia mengakui, berbelit, atau menyerang |
| Minta tautan atau bukti untuk klaim utama | Apakah ia bisa menunjuk sumber, atau mengalihkan |
| Ajukan topik di luar fokusnya | Apakah ia menolak dengan jelas, menjawab, atau keluar dari peran |

Catat reaksinya, bukan hanya isi jawabannya. Lihat [Menangani Jawaban](15-penanganan-jawaban.md) untuk pengelompokan delapan jenis jawaban.

## 6. Kategori E — Pertanyaan tentang AI

Pertanyaan langsung tentang penggunaan AI tetap berguna, tetapi **bobotnya rendah** karena jawabannya adalah klaim. Yang membuatnya berguna adalah bila jawabannya tidak konsisten dengan bukti lain.

Rujuk ke dokumen khusus:

- [Prompt Status AI](03-status-ai.md) — apakah akun memakai AI
- [Prompt Model dan Vendor](05-model-vendor.md) — model dan penyedianya
- [Prompt Sumber Informasi](06-sumber-informasi.md) — sumber untuk jawaban tertentu
- [Prompt Pemilik/Pengelola](04-pemilik-pengelola.md) — siapa yang bertanggung jawab

**Pola yang paling sering muncul:** akun menyebut nama model atau vendor yang tidak mungkin ia ketahui, atau menyebut provider yang berbeda dari bukti teknis yang bocor. Bandingkan jawaban ini dengan [artefak teknis T-1 sampai T-3](14-rubrik-penilaian.md#21-artefak-teknis--kelas-terpisah-lebih-kuat-dari-sinyal-perilaku).

## 7. Aturan Main

1. **Paling banyak satu pertanyaan, lalu satu lanjutan yang relevan.** Lebih dari itu berubah menjadi gangguan.
2. **Jangan menghujani akun.** Pengulangan massal menghasilkan tekanan, bukan informasi, dan berisiko melanggar aturan platform.
3. **Jangan meminta instruksi internal, kredensial, atau data pribadi.** Itu di luar tujuan dokumen ini.
4. **Jangan menyamar** sebagai pengembang, administrator, atau pihak berwenang.
5. **Terima penolakan.** Bila akun menolak atau mengarahkan ke kanal resmi, gunakan kanal itu.
6. **Catat sebelum menyimpulkan.** Kutipan, tanggal, dan tautan lebih berguna daripada ingatan.
7. **Jangan menyebarkan hasil sebagai daftar tuduhan.** Bagikan temuan dengan konteks dan tingkat kepastiannya.

## 8. Cara Mencatat Hasilnya

Pakai format pada [Checklist Verifikasi §5](02-verifikasi.md#5-format-catatan-hasil), dan tambahkan kolom:

| Kolom | Isi |
|---|---|
| Pertanyaan | Bunyi pertanyaan apa adanya |
| Jawaban | Kutipan langsung, diringkas bila panjang |
| Kategori | A / B / C / D / E |
| Hasil | Mencurigakan / tidak meyakinkan / mendukung |
| Yang perlu diperiksa lanjut | Tindak lanjut berikutnya |

## 9. Ringkasan

1. Tanya soal **hal yang hanya orang di tempat itu yang tahu**, bukan soal instruksinya.
2. Uji konsistensi akun terhadap apa yang pernah ia katakan sendiri.
3. Periksa jejak nyatanya di luar akun — sering lebih menentukan daripada pertanyaan.
4. Pertanyaan tentang AI berguna hanya bila dibandingkan dengan bukti lain.
5. Satu pertanyaan, satu lanjutan, lalu berhenti.

---

[← Beranda](index.md) · [Rubrik Penilaian](14-rubrik-penilaian.md) · [Studi Kasus](16-studi-kasus.md) · [Pelestarian Bukti](17-pelestarian-bukti.md)
