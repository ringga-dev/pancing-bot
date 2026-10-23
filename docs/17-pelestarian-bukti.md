# Pelestarian Bukti

[← Beranda](index.md) · [Indeks prompt](01-prompt-identifikasi-ai.md) · [Checklist verifikasi](02-verifikasi.md)

---

Dokumen ini adalah rujukan lanjut dari [Checklist Verifikasi §1](02-verifikasi.md#1-urutan-pemeriksaan-cepat) dan [Format Catatan Hasil](02-verifikasi.md#5-format-catatan-hasil). Isinya: cara menyimpan temuan sebelum bukti itu hilang, bagaimana catatan itu tetap dapat diperiksa ulang, batas pelestarian arsip pihak ketiga, dan kapan sebuah catatan boleh dipakai sebagai dasar kesimpulan.

> **Inti dokumen ini.** Temuan hanya bernilai selama buktinya masih ada dan masih dapat diperiksa orang lain. Tangkapan layar tanpa permalink, tanggal, dan konteks pertanyaan adalah catatan yang sudah mati sebelum dipakai.

## 1. Mengapa bukti hilang

Hal-hal berikut membuat sebuah bukti menghilang atau kehilangan nilainya. Semuanya umum terjadi, bukan teori.

| Penyebab | Akibat pada bukti |
|---|---|
| Akun dihapus, diubah nama, atau diprivasi | Tautan mati; kutipan kehilangan subjeknya |
| Konten dihapus atau disunting setelah dibalas | Kutipan tidak dapat dicocokkan dengan kondisi saat itu |
| Platform membatasi akses tanpa log masuk | Pemeriksa lain tidak dapat mengulang pemeriksaannya |
| Tangkapan layar tanpa permalink dan tanggal | Sumber tidak dapat ditentukan, tanggal tidak dapat diverifikasi |
| Platform berhenti beroperasi atau mengubah kebijakan konten | Arsip daring yang mengandalkan tayangan langsung menjadi tidak tersedia |
| Salinan hanya tersimpan di satu perangkat | Kegagalan perangkat menghapus seluruh catatan |
| Arsip pihak ketiga diblokir atau dihapus oleh pemegang hak | Salinan arsip tidak dapat diandalkan sebagai satu-satunya salinan |

Dua baris terakhir sering diabaikan. Arsip daring adalah bantuan, bukan jaminan; ketersediaan layanannya berubah seiring waktu. Karena itu, prinsipnya sederhana: **simpan sumber utama, lalu simpan salinan kerja**, dan anggap salinan sebagai pelengkap.

## 2. Apa yang harus disimpan

Pedoman ini melanjutkan langkah pertama [Checklist Verifikasi §1](02-verifikasi.md#1-urutan-pemeriksaan-cepat): simpan hanya informasi yang diperlukan dan dapat diakses secara sah.

| Unsur | Kenapa perlu | Catatan |
|---|---|---|
| Permalink dan identitas akun | Menentukan sumber dan subjek temuan | Permalink lebih tahan daripada tautan pendek |
| Tanggal dan zona waktu | Konfigurasi akun dapat berubah | Catat kapan pemeriksaan dilakukan, bukan kapan catatan dibuat |
| Konteks pertanyaan | Jawaban hanya bermakna bersama pertanyaannya | Catat pertanyaan sebagaimana diajukan |
| Kutipan langsung | Dasar dari setiap pernyataan | Ringkas; jangan menyalin percakapan utuh |
| Lokasi berkas salinan | Memungkinkan pemeriksaan ulang | Sertakan nama berkas dan nilai cek |
| Kondisi akses | Menjelaskan bagaimana sumber dapat dilihat | Terbuka, perlu log masuk, atau terbatas |

### 2.1 Larangan yang berlaku

Pelestarian bukti tidak membatalkan klasifikasi data pada [Privasi dan Retensi Data §2](12-privasi-dan-retensi-data.md#2-klasifikasi-data). Yang **tidak** disimpan dalam salinan bukti:

1. Data pribadi pada §2.3 — nama pengguna, surel, nomor kontak, alamat IP, pengidentifikasi perangkat, dan kutipan yang masih memuat data pribadi pihak ketiga.
2. Data terlarang pada §2.4 — *system prompt* produksi, kredensial, token, kunci API, data pelanggan, dan berkas template yang sudah terisi data nyata.

Jika sebuah salinan terlanjur memuat keduanya, laporkan sebagai insiden dan jalankan prosedur penghapusan pada [Privasi dan Retensi Data §7](12-privasi-dan-retensi-data.md#7-prosedur-penghapusan). Menyimpan bukti bukan alasan untuk menahan data yang seharusnya dihapus.

## 3. Tangkapan layar, permalink, dan nilai cek

Tangkapan layar paling sering disimpan dan paling sering tidak berguna. Empat kesalahan berikut hampir selalu terjadi: tanpa permalink, tanpa tanggal yang terlihat, tanpa konteks pertanyaan, dan tanpa nama berkas salinan pada catatan.

### 3.1 Urutan penangkapan

1. Buka halaman sumber pada kondisi aslinya. Jangan menangkap dari halaman hasil arsip, karena alamat pada bilah peramban sudah tidak lagi menunjuk sumber.
2. Lihat permalinknya dan salin ke catatan. Jika platform tidak menyediakan permalink, catat URL penuh dan identitas akun sebagaimana tertera.
3. Pastikan stempel waktu terlihat pada gambar, atau catat tanggal dan zona waktu secara terpisah.
4. Simpan berkas gambar, lalu catat nama berkasnya pada catatan.
5. Hitung nilai cek berkas dan catat hasilnya.

### 3.2 Nilai cek berkas

Nilai cek (hash) memungkinkan pemeriksa lain membuktikan bahwa salinan masih utuh. Algoritma yang lazim dan tersedia di hampir semua sistem adalah `md5sum`, `sha1sum`, dan `sha256sum`.

```text
sha256sum bukti-2026-10-23.png
```

Catat nilai cek pada catatan bersama nama berkas dan tanggal penangkapan. Jika nilai cek berubah saat diperiksa ulang, salinan itu sudah tidak sama dengan yang direkam.

### 3.3 Batas tangkapan layar

Tangkapan layar adalah bukti yang lemah terhadap klaim orang lain, karena gambar dapat disunting. Karena itu tangkapan layar hanya dipakai untuk pendukung visual; bukti utama tetap permalink dan kutipan. Jika platform membatasi akses tanpa log masuk, sebutkan kondisi itu pada catatan, karena pemeriksa lain mungkin tidak dapat mengulang pemeriksaan dengan cara yang sama.

## 4. Arsip pihak ketiga

Layanan arsip daring dapat menyimpan salinan halaman di luar kendali platform asal. Prinsipnya: jadikan arsip sebagai pelengkap, bukan pengganti sumber utama, dan kutipan sebagai bukti utama, bukan gambar tayangannya.

| Layanan arsip | Peran | Batas yang perlu diingat |
|---|---|---|
| Internet Archive (Wayback Machine) | Menyimpan tayangan halaman pada satu waktu | Tayangan bergantung pada robot pengarsip; konten yang dimuat dinamis sering tidak ikut tersimpan |
| Archive.today | Menyimpan tayangan alternatif | Sering diblokir platform; tayangan dapat dihapus |
| Layanan arsip institusi atau perpustakaan | Rujukan jangka panjang untuk terbitan | Cakupan terbatas pada koleksinya |

Ketersediaan layanan arsip dapat berubah: tayangan dapat dihapus, akses dapat dibatasi, dan layanan dapat berhenti. Sebelum mengandalkan sebuah layanan, periksa kebijakan resminya dan, bila perlu, hubungi pengelolanya. Jika Anda menyerahkan masalah hukum kepada penasihat, ikuti nasihat itu, bukan dokumen ini.

## 5. Format catatan pelestarian

Catatan pelestarian melengkapi tabel pada [Format Catatan Hasil](02-verifikasi.md#5-format-catatan-hasil); ia menambahkan bagian teknis di belakangnya, bukan menggantinya.

```md
**Diamati:** <fakta yang terukur atau kutipan langsung>
**Sumber:** <permalink, plus tanggal akses>
**Berkas:** <nama berkas tangkapan layar, plus nilai cek>
**Kondisi akses:** terbuka / perlu log masuk / terbatas
**Tingkat kepastian:** terkonfirmasi / indikasi kuat / belum diketahui
**Yang belum terbukti:** <apa pun yang masih terbuka>
```

Label **tingkat kepastian** mengikuti pembagian tiga tingkat pada [Menduga vs Membuktikan §2](13-menduga-vs-membuktikan.md#2-tiga-tingkat-kesimpulan). Menambah label di antaranya hanya menimbulkan kesan lebih pasti dari yang sebenarnya.

### 5.1 Kapan catatan itu boleh dipakai

Sebuah catatan layak dipakai sebagai dasar kesimpulan bila:

1. Permalink dan tanggal tercantum, sehingga sumber dan waktu pemeriksaan jelas.
2. Konteks pertanyaan tersimpan, sehingga kutipan tidak diputar-balikkan.
3. Salinan berkas tercantum beserta nilai ceknya, sehingga integritasnya dapat diperiksa ulang.
4. Kondisi akses disebutkan, sehingga pembaca tahu batas pemeriksaan ulang.
5. Klasifikasi data pada [Privasi dan Retensi Data §2](12-privasi-dan-retensi-data.md#2-klasifikasi-data) terpenuhi.

Bila satu dari lima syarat itu belum terpenuhi, catat statusnya sebagai **belum lengkap**, bukan sebagai temuan yang selesai.

## 6. Masa simpan dan penghapusan

Pelestarian bukti tidak berarti penyimpanan tanpa batas. Jadwal retensi mengatur berapa lama setiap kategori boleh disimpan, dan penghapusan dijalankan sebagai pekerjaan terjadwal, bukan bergantung pada ingatan penanggung jawab.

| Kategori bukti | Masa simpan | Alasan |
|---|---|---|
| Tangkapan layar dan kutipan hasil pemeriksaan akun | 90 hari | Cukup untuk tinjauan ulang dan deteksi pola berulang |
| Hasil pengujian ketahanan bot | 180 hari | Menyediakan jendela perbandingan antar-versi konfigurasi |
| Laporan ringkasan dan set uji regresi | 1 tahun | Menjaga kesinambungan set uji tanpa menyimpan data mentah |
| Bukti pelanggaran kebijakan | Sampai investigasi selesai, maksimal 180 hari | Membatasi paparan data yang tidak lagi diperlukan |

Tabel di atas adalah **rekomendasi pilihan default**, bukan ketentuan hukum; angka retensi pada [Privasi dan Retensi Data §3](12-privasi-dan-retensi-data.md#3-jadwal-retensi) tetap menjadi acuan utamanya. Sesuaikan dengan kebijakan organisasi Anda dan kewajiban hukum di yurisdiksi yang berlaku.

Setelah batas terlampaui, salinan dihapus dan penghapusannya dicatat. Jangan memperpanjang masa simpan hanya karena catatan masih terlihat berguna; perpanjangan hanya boleh dilakukan dengan alasan tertulis.

## 7. Kendali teknis

1. **Kontrol akses:** berikan akses berdasarkan kebutuhan. Pisahkan peran peninjau, penanggung jawab retensi, dan administrator.
2. **Salinan kerja terpisah:** simpan salinan bukti di lokasi yang berbeda dari catatan kerjanya.
3. **Nilai cek dicatat sekali saat penangkapan:** hitung segera, lalu verifikasi ulang sebelum catatan dipakai.
4. **Enkripsi:** terapkan enkripsi saat disimpan dan saat dikirim, termasuk pada cadangan data.
5. **Pencatatan akses:** simpan jejak siapa mengakses catatan apa dan kapan, khususnya catatan yang memuat data pribadi.
6. **Pemindaian berkala:** jalankan pemindaian berkala untuk menemukan surel, nomor kontak, token, dan kredensial yang tertinggal pada salinan.
7. **Hapus berkas sementara:** bersihkan berkas kerja, hasil ekspor sementara, dan salinan tangkapan yang tidak dipakai.

Enkripsi dan kontrol akses pada dokumen ini sejalan dengan [Perlindungan Teknis](12-privasi-dan-retensi-data.md#5-perlindungan-teknis). Keduanya berlaku pada salinan bukti sebagaimana berlaku pada catatan lainnya.

## 8. Pemeriksaan ulang

Temuan yang baik adalah temuan yang dapat diperiksa ulang oleh orang lain. Sebelum sebuah catatan disebar atau dipakai sebagai dasar, periksa lima hal berikut.

1. Buka permalink. Apakah sumber masih ada? Jika tautan mati, apakah salinan arsip masih tersedia?
2. Bandingkan kutipan dengan sumber. Apakah kutipan masih sama dengan kondisi yang direkam?
3. Periksa nilai cek salinan. Apakah berkas masih sama dengan yang direkam?
4. Sebutkan kondisi akses dan tanggal pemeriksaan. Konfigurasi akun dapat berubah; jangan sajikan hasil lama sebagai kondisi terkini.
5. Konfirmasi klasifikasi data. Apakah ada data pribadi atau data terlarang yang perlu dikeluarkan?

Jika sumber sudah tidak ada dan tidak ada salinan, catatan itu tetap sah sebagai catatan bahwa pemeriksaan pernah dilakukan, tetapi tidak lagi dapat dipakai untuk membuktikan isi sumber. Tuliskan statusnya dengan jelas.

## 9. Kesalahan umum

- Menyimpan tangkapan layar tanpa permalink, tanggal, atau konteks pertanyaan.
- Menjadikan layanan arsip sebagai satu-satunya salinan sumber.
- Menyimpan kutipan yang memuat data pribadi atau data terlarang.
- Mencatat nilai cek tetapi tidak pernah memverifikasi ulang.
- Memperpanjang masa simpan tanpa alasan tertulis.
- Menyebar catatan yang belum memenuhi kelima syarat pada §5.1.
- Menyajikan hasil lama sebagai kondisi terkini tanpa menyebutkan tanggal pemeriksaan.

## 10. Ringkasan

1. Simpan permalink, tanggal, konteks pertanyaan, kutipan, nama berkas, dan nilai cek.
2. Anggap tangkapan layar sebagai pendukung visual; bukti utama tetap permalink dan kutipan.
3. Salinan arsip pihak ketiga adalah pelengkap; ketersediaannya bisa berubah.
4. Pelestarian bukti tetap tunduk pada klasifikasi data dan jadwal retensi.
5. Sebelum dipakai, pastikan catatan dapat diperiksa ulang oleh orang lain.

---

[← Beranda](index.md) · [Checklist verifikasi](02-verifikasi.md) · [Privasi dan Retensi Data](12-privasi-dan-retensi-data.md) · [Template](perkakas/README.md)
