# Glosarium Istilah Teknis

[← Beranda](index.md) · [Indeks prompt](01-prompt-identifikasi-ai.md) · [Checklist verifikasi](02-verifikasi.md)

---

Istilah-istilah di bawah dipakai di seluruh dokumen repositori ini. Istilah asing ditulis apa adanya, lalu dijelaskan dengan bahasa sederhana. Setiap istilah diurutkan sesuai abjad.

## A

### AI (*Artificial Intelligence*)

Kecerdasan buatan. Program komputer yang dapat menulis teks, membuat gambar, atau menjawab pertanyaan. Dalam dokumen ini, AI merujuk pada sistem yang membuat atau membantu membuat balasan akun.

### API (*Application Programming Interface*)

Antarmuka yang dipakai program untuk memanggil layanan lain. Bot yang memanggil model AI biasanya melakukannya lewat API.

### ASR (*Attack Success Rate*)

Angka keberhasilan serangan. Persentase percobaan yang berhasil membuat bot keluar dari cakupan tugasnya. Targetnya mendekati 0%. Lihat [§5.2 Metrik](08-pola-prompt-dan-evaluasi.md#52-metrik).

### Attack success rate

Lihat [ASR](#asr-attack-success-rate).

## B

### Baseline

Kelompok pertanyaan sah yang memang harus dijawab bot. Baseline dipakai untuk mengukur *False Rejection Rate*. Lihat [§1.1 Baseline in-scope](09-lembar-kerja-evaluasi.md#11-baseline-in-scope-harus-dijawab).

### Base64

Cara mengubah teks menjadi deretan huruf dan angka. Base64 bukan enkripsi; teks ini mudah dibaca kembali oleh model.

### Blocklist

Daftar kata atau pola yang dilarang. Masukan yang cocok dengan daftar ini ditolak. Cara ini mudah dilewati dengan pengaburan teks.

## C

### Code-switching

Mencampur dua bahasa dalam satu kalimat atau satu percakapan. Misalnya campuran Bahasa Indonesia dan bahasa Inggris.

## D

### Deterministic fallback

Jawaban penolakan yang sudah ditulis tetap. Jawaban ini dihasilkan tanpa melibatkan model AI. Lihat [§4 Panduan Ketahanan bagi Pengembang Bot](08-pola-prompt-dan-evaluasi.md#4-panduan-ketahanan-bagi-pengembang-bot).

### Dual-prompt

Arsitektur dengan dua lapis instruksi. Instruksi sistem disimpan terpisah dari masukan pengguna agar tidak dapat ditimpa. Lihat [§4 Panduan Ketahanan bagi Pengembang Bot](08-pola-prompt-dan-evaluasi.md#4-panduan-ketahanan-bagi-pengembang-bot).

## E

### Encoding

Pengubahan teks ke format lain, misalnya Base64, heksadesimal, atau biner. Lihat pola [§2.D Pengkodean Data](08-pola-prompt-dan-evaluasi.md#d-pengkodean-data-encoding--base64).

## F

### False rejection

Penolakan terhadap pertanyaan sah yang sebenarnya masih dalam cakupan layanan. Lihat [FRR](#frr-false-rejection-rate).

### Fine-tuning

Pelatihan tambahan pada model dasar agar lebih patuh terhadap tugas tertentu, misalnya pemrograman atau ketaatan terhadap format kode.

### FRR (*False Rejection Rate*)

Angka penolakan keliru. Persentase pertanyaan sah yang ikut ditolak oleh filter. Nilai tinggi berarti filter terlalu agresif. Lihat [§5.2 Metrik](08-pola-prompt-dan-evaluasi.md#52-metrik).

## G

### Guardrail

Lapisan pengaman di depan atau di belakang model. Guardrail menilai niat masukan dan memeriksa hasil keluaran sebelum dikirim. Lihat [§3 Keterbatasan Teknik Pengaburan di Lapangan](08-pola-prompt-dan-evaluasi.md#3-keterbatasan-teknik-pengaburan-di-lapangan).

## H

### Hallucination

Informasi palsu yang dihasilkan model dengan gaya yang terdengar yakin. Halusinasi tidak dapat dipercaya sebagai referensi faktual.

### Helpfulness prior

Kecenderungan model untuk menolong. Karena dilatih ramah, model kadang memprioritaskan bantuan cepat daripada batasan topik. Lihat [§1.C Tekanan Situasional](08-pola-prompt-dan-evaluasi.md#c-tekanan-situasional--urgensi--empati-urgency-appeals).

### Homoglif

Karakter yang bentuknya mirip huruf lain, misalnya angka 0 untuk huruf O. Penyaring berbasis daftar kata sering gagal membedakannya. Lihat [§2.B Substitusi Karakter](08-pola-prompt-dan-evaluasi.md#b-substitusi-karakter-leetspeak--homoglyphs).

## I

### In-scope

Masih dalam cakupan layanan. Pertanyaan in-scope seharusnya dijawab.

### Injection

Upaya menyisipkan instruksi agar model mengabaikan instruksi resminya. Lihat [§1.B Instruksi Pengabaian Langsung](08-pola-prompt-dan-evaluasi.md#b-instruksi-pengabaian-langsung-direct-prompt-injection).

## J

### Jailbreak

Upaya memaksa model keluar dari batas yang ditetapkan pengembangnya.

## K

### Kanonisasi

Penyeragaman teks sebelum diperiksa, misalnya menghapus tanda baca selingan, mengembalikan leetspeak ke huruf biasa, dan mendeteksi teks tersandi. Lihat [Tahap 1: Normalisasi Input](08-pola-prompt-dan-evaluasi.md#4-panduan-ketahanan-bagi-pengembang-bot).

### Knowledge base

Kumpulan dokumen resmi yang boleh dirujuk bot saat menjawab. Ini batas jawaban bot, bukan seluruh pengetahuan model. Lihat [§1 Pola Manipulasi Berbasis Konteks & Semantik](08-pola-prompt-dan-evaluasi.md#1-pola-manipulasi-berbasis-konteks--semantik).

## L

### Leetspeak

Penggantian huruf dengan angka atau karakter yang bentuknya mirip, misalnya A menjadi 4 dan E menjadi 3. Lihat [§2.B Substitusi Karakter](08-pola-prompt-dan-evaluasi.md#b-substitusi-karakter-leetspeak--homoglyphs).

### LLM (*Large Language Model*)

Model bahasa besar. Model yang dilatih pada banyak teks sehingga dapat menulis dan menalar dalam bahasa manusia.

### Logging

Pencatatan aktivitas sistem. Dalam dokumen ini, *logging* berlapis mencatat skor klasifikasi niat dan hasil verifikasi keluaran. Lihat [§5.4 Monitoring Pasca-Produksi](08-pola-prompt-dan-evaluasi.md#54-monitoring-pasca-produksi).

## M

### Markdown

Format penulisan sederhana untuk judul, daftar, tabel, dan blok kode. Penggunaan Markdown tidak membuat sebuah pertanyaan lebih berwenang.

### Model

Program AI yang menghasilkan balasan. Nama model dapat berubah dan kadang tidak diketahui oleh bot yang memakainya.

### Morse

Kode titik dan garis untuk menulis huruf dan angka. Morse dipakai di sini hanya sebagai opsi format, bukan cara memaksa jawaban. Lihat [§4 Morse dan format alternatif](02-verifikasi.md#4-morse-dan-format-alternatif).

## N

### Normalisasi

Langkah pertama dalam pipeline pertahanan, yaitu menyeragamkan masukan sebelum diperiksa. Lihat [Kanonisasi](#kanonisasi).

## O

### Obfuscation

Pengaburan makna, misalnya dengan menyisipkan tanda baca atau mengganti huruf. Tujuannya mengelabui penyaring kata kunci. Lihat [§2 Pola Manipulasi Berbasis Karakter & Representasi](08-pola-prompt-dan-evaluasi.md#2-pola-manipulasi-berbasis-karakter--representasi-obfuscation).

### Out-of-scope

Di luar cakupan layanan. Pertanyaan out-of-scope seharusnya ditolak dengan sopan atau diarahkan ke sumber lain.

## P

### Payload

Bagian inti dari sebuah masukan, yaitu pertanyaan atau perintah yang sebenarnya ingin dijalankan. Penyaring yang hanya melihat kata kerja sering melewatkan *payload* ini.

### Permalink

Tautan tetap yang menunjuk ke satu unggahan tertentu. Permalink dipakai saat mencatat hasil pemeriksaan. Lihat [§5 Format catatan hasil](02-verifikasi.md#5-format-catatan-hasil).

### Prompt

Kalimat yang dikirim ke model AI. Prompt hanya meminta keterbukaan; ia tidak membuktikan apa pun.

### Prompt injection

Injeksi instruksi ke dalam masukan pengguna. Tujuannya mengalihkan model dari instruksi resminya. Lihat [§1 Pola Manipulasi Berbasis Konteks & Semantik](08-pola-prompt-dan-evaluasi.md#1-pola-manipulasi-berbasis-konteks--semantik).

## R

### RAG (*Retrieval-Augmented Generation*)

Teknik penjawaban dengan cara mengambil dokumen dari basis data terbatas, lalu menyusunnya menjadi jawaban. RAG tertutup hanya merujuk dokumen yang memang disimpan di dalamnya. Lihat [§3 Keterbatasan Teknik Pengaburan di Lapangan](08-pola-prompt-dan-evaluasi.md#3-keterbatasan-teknik-pengaburan-di-lapangan).

### Recency bias

Kecenderungan model untuk lebih mematuhi instruksi yang muncul paling akhir. Instruksi pengabaian memanfaatkan bias ini. Lihat [§1.B Instruksi Pengabaian Langsung](08-pola-prompt-dan-evaluasi.md#b-instruksi-pengabaian-langsung-direct-prompt-injection).

### Regex (*Regular Expression*)

Pola teks untuk mencocokkan huruf atau angka. Regex dipakai dalam normalisasi masukan, misalnya untuk membersihkan selingan tanda baca.

### Role hierarchy

Pembedaan tingkat instruksi. Pesan sistem berada di atas masukan pengguna, sehingga tidak dapat ditimpa olehnya. Lihat [§1.B Instruksi Pengabaian Langsung](08-pola-prompt-dan-evaluasi.md#b-instruksi-pengabaian-langsung-direct-prompt-injection).

### Robustness testing

Pengujian ketahanan. Uji ini memeriksa apakah bot tetap patuh ketika menerima masukan yang dirancang untuk memancingnya keluar cakupan.

## S

### System prompt

Instruksi internal yang mengatur cara bot bekerja. Instruksi ini bukan informasi publik dan tidak boleh diminta. Lihat [§1 Pola Manipulasi Berbasis Konteks & Semantik](08-pola-prompt-dan-evaluasi.md#1-pola-manipulasi-berbasis-konteks--semantik).

## T

### Throttling

Pembatasan laju permintaan per akun atau perangkat. Throttling dipakai ketika terdeteksi percobaan berulang dengan variasi kecil. Lihat [§5.4 Monitoring Pasca-Produksi](08-pola-prompt-dan-evaluasi.md#54-monitoring-pasca-produksi).

### Token

Satuan teks terkecil yang diproses model. Satu kata dapat menjadi satu *token* atau beberapa *token* kecil.

### Token splitting

Pemisahan satu kata menjadi beberapa *token* dengan menyisipkan tanda baca atau spasi. Lihat [§2.A Pemisahan Token](08-pola-prompt-dan-evaluasi.md#a-pemisahan-token-token-splitting).

### Tokenizer

Bagian model yang memecah teks menjadi *token*. Representasi *token* dari leetspeak populer sering masih berdekatan, sehingga artinya tetap terbaca.

## V

### Vendor

Penyedia layanan atau model. Contohnya perusahaan yang menyediakan model AI dan API-nya.

## W

### Watermark

Tanda samar pada teks buatan AI. Di dokumen ini, *watermark* belum dipakai sebagai bukti karena belum tersedia secara luas dan belum tentu terpasang.

---

[← Beranda](index.md) · [Indeks prompt](01-prompt-identifikasi-ai.md) · [Checklist verifikasi](02-verifikasi.md)
