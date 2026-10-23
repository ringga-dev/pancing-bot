# Penelitian dan Indikator

[← Beranda](index.md) · [Rubrik Penilaian](14-rubrik-penilaian.md) · [Label AI Platform](19-label-ai-platform.md) · [Informasi Salah dan Koordinasi](18-informasi-salah-dan-koordinasi.md)

---

Dokumen ini mengumpulkan temuan dari riset dan pengamatan lapangan tentang bagaimana akun sintetis dikenali — serta batas-batasnya. Isinya untuk menambah dasar [Rubrik Penilaian](14-rubrik-penilaian.md), bukan menggantikannya.

> **Yang paling penting dibaca lebih dulu:** kemampuan manusia untuk membedakan akun buatan AI dari manusia, diukur dalam riset, rata-rata hanya sekitar **42 persen**. Angka itu bukan alasan untuk menyerah, melainkan alasan untuk berhenti mengandalkan kesan dan beralih ke data yang bisa diukur.

## 1. Seberapa Sulitnya Membedakan

Riset yang dilaporkan *Tempo* (2024) pada pekerjaan Paul Brenner dan kolega dari Pusat Riset Komputasi, University of Notre Dame, menemukan bahwa kemampuan responden membedakan akun yang ditenagai AI dari manusia hanya sekitar **42 persen** secara rata-rata. Kemampuan itu **tidak meningkat** meskipun responden sudah diberi tahu bahwa mereka mungkin berinteraksi dengan bot.

Implikasinya langsung:

1. **Kesan pribadi bukan instrumen yang baik.** Bila lebih dari separuh orang salah, perasaan "ini jelas bot" atau "ini jelas manusia" tidak bisa dijadikan dasar.
2. **Yang bisa diukur harus menggantikan kesan.** Itu sebabnya [Rubrik Penilaian](14-rubrik-penilaian.md) menuntut data terukur, bukan tangkapan kesan.
3. **Buku ini tidak menjanjikan Anda akan selalu benar.** Ia menjanjikan proses yang bisa diaudit dan bisa diulang orang lain.

## 2. Lima Indikator yang Ditemukan Riset

Dari riset yang sama, ada lima hal yang membantu mengenali akun buatan AI:

| Indikator | Contoh yang perlu dicari |
|---|---|
| Emoji dan hashtag berlebihan | Pemakaian yang terasa dipaksakan untuk menampilkan kesan ramah |
| Frase, diksi, atau analogi yang tidak umum | Kata atau perumpamaan yang tidak lazim dipakai orang di konteks itu |
| Repetisi dan struktur kaku | Kalimat berulang dengan bentuk yang sama, atau pemakaian istilah slang secara berlebihan |
| Kurangnya pengetahuan lokal | Tidak memahami situasi, tempat, atau konteks setempat ketika ditanya |
| Identitas tidak pernah tervalidasi | Bukan kontak pribadi, dan identitasnya tidak pernah jelas atau terverifikasi |

Indikator keempat paling praktis: **bertanya tentang hal yang sangat lokal**. Akun yang mengaku tinggal di sebuah kota tetapi tidak memahami detail dasar kota itu patut diperiksa lebih dalam. Ini sejalan dengan [Rubrik Penilaian A-6](14-rubrik-penilaian.md#2-bagian-a--sinyal-arah-otomatisasi).

## 3. Pendekatan Stilometri

Selain membaca isi, gaya bahasa bisa diukur secara statistik. Penelitian Kumarage dan kawan-kawan (2023) menggunakan fitur stilometri — seperti panjang kalimat dan frekuensi tanda baca — untuk membedakan teks manusia dan teks buatan AI. Hasilnya: model gabungan RoBERTa dengan fitur stilometri mencapai **99,2 persen** pada *timeline* panjang dan **87,5 persen** pada satu unggahan.

Yang perlu dicatat:

- Angka tinggi itu berlaku pada **banyak unggahan**, bukan satu unggahan. Satu unggahan jauh lebih sulit.
- Metode ini memerlukan cukup teks dan alat bantu. Ini bukan sesuatu yang bisa dilakukan secara manual oleh pembaca biasa.
- Stilometri mengukur **gaya**, bukan identitas. Gaya yang mirip AI bukan bukti akun itu AI, dan gaya yang mirip manusia bukan bukti akun itu manusia.

Untuk pemeriksaan manual, pendekatan ini paling berguna sebagai alasan untuk mencari lebih banyak sampel — bukan sebagai dasar menyimpulkan.

## 4. Indikator dari Pengamatan Lapangan

Pengamatan terhadap jaringan akun di berbagai negara menghasilkan indikator yang konsisten. Contohnya, pada jaringan akun pendukung seorang pemimpin di X, peneliti memakai indikator seperti:

- Aktivitas unggahan tanpa henti 24 jam.
- Tanggal pembuatan akun yang masih sangat baru.
- Tidak ada foto profil.
- Akun baru muncul dalam jumlah besar pada waktu yang sama.

Laporan dari OpenAI menyebutkan pula pola lain: AI dipakai untuk mengelola **persona media sosial palsu**, menyusun biografi akun, menganalisis unggahan dan komentar, menyusun balasan dalam beberapa bahasa, dan memeriksa teks sebelum dipublikasikan. Laporan itu mengidentifikasi sekitar **150 akun** di X dan Facebook dengan pola aktivitas yang terkait.

Indikator-indikator ini cocok ditambahkan ke daftar sinyal koordinasi pada [Informasi Salah dan Koordinasi §3](18-informasi-salah-dan-koordinasi.md#3-sinyal-koordinasi).

## 5. Contoh yang Menjebak

Tidak semua akun yang mencurigakan adalah AI. Contoh yang banyak dibagikan: seorang peneliti di platform X menyelidiki puluhan akun beralamat IP Indonesia yang dioperasikan satu orang, dan menduga itu otomatisasi. Ternyata akun-akun itu dijalankan **manusia secara manual**.

Dua pelajarannya:

1. **Banyak akun sekaligus bukan bukti AI.** Manusia juga bisa mengoperasikan banyak akun, terutama dengan bantuan alat.
2. **Jangan memutarbalikkan temuan.** Bila setelah diperiksa akun itu ternyata manusia, hasilnya tetap dilaporkan apa adanya. Kesalahan yang segera dikoreksi lebih baik daripada keyakinan yang tidak pernah diuji.

Ini juga alasan [Rubrik Penilaian](14-rubrik-penilaian.md) memisahkan sinyal perilaku dari kesimpulan: perilaku bisa dijelaskan oleh lebih dari satu penyebab.

## 6. Cara Memakai Angka Ini Tanpa Menyesatkan

Angka seperti 42 persen dan 99,2 persen mudah disalahpakai. Patuhi hal berikut:

- **Sebut sumbernya**, bukan hanya angkanya. Angka tanpa sumber adalah pendapat.
- **Sebut cakupannya.** 99,2 persen berlaku untuk *timeline* panjang, bukan satu unggahan.
- **Jangan mengubah "sulit dibedakan" menjadi "tidak bisa diketahui".** Yang sulit adalah menebak dari satu interaksi; yang mungkin adalah mengumpulkan cukup data.
- **Jangan mengubah "banyak indikator cocok" menjadi "pasti AI".** Indikator adalah alasan untuk memeriksa lebih lanjut.
- **Catat kapan angka itu diperoleh.** Metode dan kebijakan berubah; angka lama tidak selalu berlaku sekarang.

## 7. Ringkasan

1. Kemampuan manusia menebak akun AI dari kesan rata-rata sekitar 42 persen — jangan andalkan kesan.
2. Lima indikator praktis: emoji berlebihan, diksi tidak umum, struktur kaku, kurangnya pengetahuan lokal, identitas tak tervalidasi.
3. Stilometri bisa sangat akurat pada banyak sampel, tetapi mengukur gaya, bukan identitas.
4. Indikator lapangan: aktivitas 24 jam, akun baru, tanpa foto profil, kemunculan bersamaan.
5. Tidak semua akun mencurigakan adalah AI. Laporkan apa yang sebenarnya ditemukan.

---

[← Beranda](index.md) · [Rubrik Penilaian](14-rubrik-penilaian.md) · [Label AI Platform](19-label-ai-platform.md) · [Informasi Salah dan Koordinasi](18-informasi-salah-dan-koordinasi.md)
