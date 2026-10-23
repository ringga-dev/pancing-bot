# Privasi dan Retensi Data

[← Beranda](index.md) · [Indeks prompt](01-prompt-identifikasi-ai.md) · [Checklist verifikasi](02-verifikasi.md) · [Lembar kerja evaluasi](09-lembar-kerja-evaluasi.md)

---

Dokumen ini adalah rujukan lanjut dari [Monitoring Pasca-Produksi](08-pola-prompt-dan-evaluasi.md#54-monitoring-pasca-produksi) dan [Aturan Penyimpanan Hasil](09-lembar-kerja-evaluasi.md#5-aturan-penyimpanan-hasil). Isinya: prinsip pembatasan data, klasifikasi data, jadwal retensi yang dapat disesuaikan, prosedur penghapusan, perlindungan terhadap subjek data, dan tata kelola dokumen.

> [!IMPORTANT]
> Angka retensi pada dokumen ini adalah **rekomendasi pilihan default**, bukan ketentuan hukum. Sesuaikan dengan kebijakan organisasi Anda dan kewajiban hukum yang berlaku di yurisdiksi terkait.

---

## 1. Prinsip Pembatasan Data

Pembatasan data berlaku pada seluruh catatan yang dihasilkan kegiatan pemeriksaan akun dan pengujian ketahanan bot, baik dalam bentuk berkas, basis data, maupun log sistem.

1. **Minimisasi:** simpan hanya data yang diperlukan untuk tujuan yang dinyatakan. Jika sebuah catatan dapat dipakai tanpa nama pengguna, kutipan panjang, atau nilai mentah, gunakan versi ringkas tersebut.
2. **Tujuan tunggal:** data yang dikumpulkan untuk pemeriksaan akun tidak dipakai untuk keperluan lain, seperti profilasi, penjualan, atau pelatihan model.
3. **Pembatasan penyimpanan:** setiap catatan punya tanggal kedaluwarsa. Batas itu dijalankan sebagai pekerjaan terjadwal, bukan bergantung pada ingatan penanggung jawab.
4. **Ketepatan:** koreksi atau tandai ulang catatan yang salah, lalu catat koreksinya. Jangan menimpa riwayat tanpa jejak.
5. **Akuntabilitas:** setiap catatan menyimpan identitas penanggung jawab dan versi konfigurasi, agar hasil lama tidak disalahartikan sebagai kondisi terkini.

Prinsip ini sejalan dengan larangan menyimpan data pribadi pengguna dan isi *system prompt* produksi pada [Aturan Penyimpanan Hasil](09-lembar-kerja-evaluasi.md#5-aturan-penyimpanan-hasil).

---

## 2. Klasifikasi Data

Klasifikasi menentukan cara menyimpan, membatasi akses, dan menghapus. Empat tingkat berikut digunakan di seluruh dokumen ini.

### 2.1 Data publik

**Isi:** kutipan jawaban akun, label AI, tautan resmi, nama pengelola yang dipublikasikan, dan klaim model/vendor yang sudah diumumkan.

**Penyimpanan:** boleh disimpan selama diperlukan untuk rujukan, dengan permalink dan tanggal pemeriksaan.

**Akses:** tim pemeriksaan.

**Catatan:** meski berstatus publik, catatan ini tetap disimpan hanya dalam jumlah yang diperlukan untuk kesimpulan yang diambil.

### 2.2 Metadata teknis

**Isi:** skor klasifikasi niat (Tahap 2), hasil verifikasi *output* (Tahap 4), keputusan tiap tahap, identitas perangkat, dan stempel waktu.

**Penyimpanan:** disimpan sebagai referensi numerik atau label, bukan sebagai salinan percakapan utuh.

**Akses:** tim pemeriksaan dan tim keamanan.

**Catatan:** metadata ini adalah bahan analisis pada [Monitoring Pasca-Produksi](08-pola-prompt-dan-evaluasi.md#54-monitoring-pasca-produksi). Jika metadata memadai untuk analisis, simpan metadata dan hapus isi mentahnya.

### 2.3 Data pribadi

**Isi:** nama pengguna, nomor kontak, alamat surel, alamat IP, pengidentifikasi perangkat, serta kutipan percakapan yang masih memuat data pribadi pihak ketiga.

**Penyimpanan:** dihapus atau dianonimkan segera setelah tidak diperlukan. Bukan bahan arsip.

**Akses:** penanggung jawab retensi, tanpa akses Tim analisis.

**Catatan:** jangan mengaitkan data pribadi dengan hasil pengujian. Jika kaitan itu tidak terhindarkan, catat alasannya dan batasi aksesnya.

### 2.4 Data terlarang

**Isi:** *system prompt* produksi, kredensial, token, kunci API, data pelanggan, serta berkas template yang sudah terisi data nyata.

**Penyimpanan:** tidak disimpan di lembar kerja, log pemeriksaan, atau kumpulan set uji.

**Akses:** tidak ada.

**Catatan:** kejadian yang memuat data terlarang wajib dilaporkan dan dibersihkan, lalu dicatat pada Log Insiden §8.

---

## 3. Jadwal Retensi

Jadwal berikut adalah **rekomendasi pilihan default**. Nilainya dapat dipangkas sesuai kebijakan organisasi, jenis pengujian, dan yurisdiksi yang berlaku; perpanjangan hanya boleh dilakukan dengan alasan tertulis.

| Kategori data | Rekomendasi retensi default | Alasan |
|---|---|---|
| Log pemeriksaan akun, termasuk metadata teknis | 90 hari | Cukup untuk tinjauan ulang dan deteksi pola berulang |
| Hasil pengujian ketahanan bot | 180 hari | Menyediakan jendela perbandingan antar-versi konfigurasi |
| Laporan ringkasan dan set uji regresi | 1 tahun | Menjaga kesinambungan set uji tanpa menyimpan data mentah |
| Berkas template yang sudah terisi | Hapus setelah dipakai | Template hanya alat kerja, bukan arsip |
| Bukti pelanggaran kebijakan | Sampai investigasi selesai, maksimal 180 hari | Membatasi paparan data yang tidak lagi diperlukan |
| Catatan penghapusan dan log insiden | 1 tahun | Jejak audit terhadap eksekusi kebijakan ini |

Setelah melewati batas retensi, data dihapus atau dianonimkan. Hasil pengujian lama tidak boleh disajikan sebagai kondisi terkini; selalu cantumkan tanggal dan versi konfigurasi seperti pada [Lembar Kerja Evaluasi §2](09-lembar-kerja-evaluasi.md#2-lembar-kerja-per-percobaan).

### 3.1 Anonimisasi sebagai pengganti penghapusan

Anonimisasi dipilih ketika hasil masih dibutuhkan untuk analisis jangka panjang tetapi identitasnya tidak relevan. Anonimisasi wajib:

1. Menghapus atau mengganti pengidentifikasi langsung: nama pengguna, surel, nomor kontak, dan alamat IP.
2. Mengganti pengidentifikasi tidak langsung yang masih dapat merujuk ke seseorang, seperti nama akun unik atau nama panggilan yang khas.
3. Mengaburkan atau meringkas kutipan hingga tidak dapat ditelusuri kembali ke percakapan aslinya.
4. Mencatat tanggal dan metode anonimisasi pada catatan yang tersisa.

Anonimisasi bukan alasan untuk memperpanjang retensi data pribadi yang seharusnya sudah dihapus.

### 3.2 Larangan menyimpan data terlarang

Tidak ada pengecualian jadwal retensi untuk kategori Data terlarang pada §2.4. Kategori itu tidak disimpan sama sekali, termasuk dalam salinan cadangan kerja, tangkapan layar, atau berkas arsip.

---

## 4. Pemilik Data dan Hak Subjek Data

Pengelola log pemeriksaan dan hasil pengujian bertindak sebagai pihak yang menentukan tujuan dan cara pemrosesan data. Pihak yang datanya tercatat adalah subjek data.

### 4.1 Ruang lingkup kewajiban

- **Indonesia:** UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi mengatur kewajiban pemroses dan pengendali data pribadi. Dokumen ini tidak memuat rincian pasal dan tidak menggantikan nasihat hukum.
- **Uni Eropa:** GDPR berlaku jika subjek data berada di UE atau pemrosesan dilakukan di wilayah tersebut.
- **Yurisdiksi lain:** terapkan aturan yang paling ketat ketika beberapa yurisdiksi berlaku sekaligus.

Ketentuan di atas berlaku pada umumnya. Karena ketentuan hukum dapat berubah, verifikasi kembali sebelum menetapkan kebijakan retensi resmi.

### 4.2 Hak subjek data

Subjek data dapat meminta keterangan, pembetulan, pembaruan, dan penghapusan data pribadinya. Prosedurnya:

1. Catat permintaan beserta identitas pemohon dan tanggal terima.
2. Verifikasi identitas pemohon sebelum menindaklanjuti.
3. Jawab dalam jangka waktu yang wajar dan sesuai ketentuan yang berlaku.
4. Jika permintaan ditolak, sampaikan alasannya secara tertulis dan sebutkan jalur pengajuan keberatan.
5. Catat penyelesaian permintaan pada Log Permintaan Akses dan Penghapusan §8.

Permintaan penghapusan atas data yang menjadi bagian dari set uji regresi dijalankan dengan anonimisasi, bukan dengan mempertahankan data pribadi dalam set uji.

---

## 5. Perlindungan Teknis

1. **Kontrol akses:** berikan akses berdasarkan kebutuhan. Pisahkan peran peninjau, penanggung jawab retensi, dan administrator.
2. **Enkripsi:** terapkan enkripsi saat disimpan dan saat dikirim, termasuk pada cadangan data.
3. **Pencatatan akses:** simpan jejak siapa mengakses data apa dan kapan, khususnya pada kategori Data pribadi.
4. **Pemindaian otomatis:** jalankan pemindaian berkala terhadap berkas catatan untuk menemukan surel, nomor kontak, token, dan kredensial yang tertinggal.
5. **Pemisahan lingkungan:** data pengujian dikelola terpisah dari data produksi.
6. **Hapus berkas sementara:** bersihkan berkas kerja, tangkapan layar, dan hasil ekspor sementara setelah selesai dipakai.

---

## 6. Berbagi Data

1. Data hanya dibagikan kepada pihak yang membutuhkannya untuk tujuan yang dinyatakan.
2. Sebelum berbagi ke pihak luar, hapus atau anonimkan data pribadi dan data terlarang.
3. Gunakan kanal terenkripsi dan kirim hanya jumlah minimum yang diperlukan.
4. Catat setiap pembagian: penerima, tanggal, isi yang dibagikan, dan tujuannya.
5. Penyebaran set uji atau varian pengaburan ke pihak lain hanya dilakukan setelah data pribadi dan isi *system prompt* dikeluarkan, dan hanya untuk bot yang berizin diuji.

---

## 7. Prosedur Penghapusan

1. **Identifikasi:** daftar catatan yang telah melewati batas retensi atau termasuk kategori Data pribadi dan Data terlarang.
2. **Tinjau:** pastikan tidak ada permintaan akses, keberatan, atau investigasi yang masih membuka catatan tersebut.
3. **Hapus:** hapus catatan dan salinan kerjanya, termasuk tangkapan layar dan hasil ekspor sementara.
4. **Catat:** catat tanggal penghapusan, metode yang dipakai, dan penanggung jawabnya pada Log Penghapusan §8.
5. **Verifikasi:** periksa ulang setelah penghapusan untuk memastikan tidak ada salinan tertinggal.

Penghapusan pada media cadangan mengikuti siklus retensi cadangan. Jika siklusnya lebih panjang dari batas retensi, lindungi cadangan dengan enkripsi dan batasi aksesnya.

---

## 8. Log dan Dokumentasi

Tiga log berikut mendukung audit kebijakan ini.

### 8.1 Log Penghapusan

| Tanggal | Kategori data | Jumlah catatan | Metode | Penanggung jawab | Verifikasi |
|---|---|---|---|---|---|
| n/a | n/a | 0 | n/a | n/a | n/a |

### 8.2 Log Permintaan Akses dan Penghapusan

| Tanggal terima | Jenis permintaan | Tindakan | Tanggal selesai | Penanggung jawab |
|---|---|---|---|---|
| n/a | n/a | n/a | n/a | n/a |

### 8.3 Log Insiden

| Tanggal | Jenis insiden | Data terlibat | Tindakan | Status | Tanggal verifikasi ulang |
|---|---|---|---|---|---|
| n/a | n/a | n/a | n/a | n/a | n/a |

Log ini menyimpan ringkasan, bukan salinan data yang dihapus. Log Penghapusan dan Log Permintaan disimpan selama 1 tahun; Log Insiden disimpan selama 1 tahun sejak insiden ditutup.

---

## 9. Implementasi dan Peninjauan Berkala

1. **Penanggung jawab:** tunjuk satu pihak sebagai penanggung jawab retensi yang menjalankan dan memantau kebijakan ini.
2. **Otomasi:** jadwalkan penghapusan dan anonimisasi otomatis sesuai tabel §3, lalu verifikasi hasilnya secara berkala.
3. **Pelatihan:** pastikan setiap anggota tim yang menangani catatan memahami klasifikasi §2 dan larangan §2.4.
4. **Audit:** tinjau pelaksanaan kebijakan minimal satu kali dalam setahun, atau setelah ada perubahan lingkungan pemrosesan.
5. **Pembaruan dokumen:** revisi dokumen ini ketika ada perubahan kebijakan organisasi, perangkat, atau ketentuan hukum yang berlaku.

---

## 10. Ringkasan Kebijakan

| Isi | Ketentuan |
|---|---|
| Prinsip utama | Minimisasi, tujuan tunggal, pembatasan penyimpanan |
| Retensi log pemeriksaan | 90 hari |
| Retensi hasil pengujian ketahanan | 180 hari |
| Retensi laporan dan set uji regresi | 1 tahun |
| Data pribadi | Dihapus atau dianonimkan, bukan bahan arsip |
| Data terlarang | Tidak disimpan sama sekali |
| Dokumen hukum rujukan | UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi |

---

[← Beranda](index.md) · [Lembar kerja evaluasi](09-lembar-kerja-evaluasi.md) · [Pola prompt dan evaluasi](08-pola-prompt-dan-evaluasi.md)
