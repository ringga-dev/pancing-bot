# Cara Berkontribusi

Terima kasih sudah ingin membantu. Repositori ini murni dokumentasi, jadi kontribusi yang paling berguna adalah memperbaiki kejelasan, kelengkapan, dan keakuratan isi — bukan menambahkan kode.

## Sebelum mulai

1. Baca [docs/index.md](docs/index.md) dan [docs/07-batas-prompt.md](docs/07-batas-prompt.md) supaya nada dan batas dokumen ini jelas.
2. Cek [CHANGELOG.md](CHANGELOG.md) untuk memastikan perubahan Anda belum ada.
3. Untuk perubahan besar, buka *issue* dulu supaya arah tidak salah.

## Aturan isi

- **Bahasa Indonesia baku.** Istilah asing ditulis apa adanya lalu dijelaskan.
- **Jangan menjanjikan kepastian yang tidak ada.** Dokumen ini sengaja menolak klaim bahwa identitas AI bisa dibuktikan hanya dari gaya bahasa atau kecepatan balasan. Lihat [docs/13-menduga-vs-membuktikan.md](docs/13-menduga-vs-membuktikan.md).
- **Jangan menambah instruksi manipulatif.** Pola di [docs/08-pola-prompt-dan-evaluasi.md](docs/08-pola-prompt-dan-evaluasi.md) didokumentasikan untuk evaluasi ketahanan bot milik sendiri, bukan untuk dipakai pada bot pihak lain.
- **Jangan menyebutkan akun, orang, atau organisasi nyata** sebagai contoh kecuali memang sudah dipublikasikan sendiri oleh pihak terkait. Pakai penanda seperti `@contoh`.
- **Jangan mengutip aturan platform secara verbatim dari ingatan.** Sebut prinsipnya, lalu tautkan sumber resminya.

## Pemeriksaan lokal

Wajib dijalankan sebelum mengirim *pull request*:

```bash
pip install -r requirements.txt
python3 scripts/check_docs.py     # tautan internal, anchor, kode Morse, cakupan nav
python3 -m mkdocs build --strict  # pastikan situs tetap bisa dibangun
npx markdownlint-cli2             # konsistensi format markdown
yamllint -s .                     # konsistensi berkas YAML
```

> **Penting:** jalankan `python3 -m mkdocs`, bukan `mkdocs`. Fungsi `slugify` khusus
> di [`slugify.py`](slugify.py) harus bisa diimpor dari direktori kerja; `python -m`
> menaruh direktori kerja di `sys.path`, sedangkan skrip `mkdocs` biasa tidak.

`scripts/check_docs.py` akan gagal jika ada tautan rusak, anchor yang tidak cocok dengan heading, atau blok Morse yang isinya tidak sama dengan pertanyaan di atasnya.

## Konvensi format

- Satu `H1` per berkas, diikuti baris tautan navigasi lalu `---`.
- Isi memakai `##` bernomor.
- Berkas diakhiri newline, tanpa spasi di akhir baris.
- Tautan internal memakai jalur relatif dari lokasi berkas, misalnya `[Checklist verifikasi](02-verifikasi.md)`.
- Penamaan berkas mengikuti pola yang ada: `docs/NN-judul-kecil.md`.

## Proses

1. Buat *branch* dari `main`, misalnya `docs/perbaiki-anchor`.
2. Lakukan perubahan, jalankan pemeriksaan lokal.
3. Kirim *pull request* dengan mengisi templat yang tersedia.
4. CI `lint-docs` harus hijau. Jika merah, perbaiki dulu — jangan meminta *bypass*.
5. Seorang pengelola akan meninjau dan menggabungkan.

## Melaporkan masalah

- Tautan rusak atau anchor tidak cocok → buka *issue* dengan templat "Dokumen".
- Saran prompt baru → buka *issue* dengan templat "Usulan prompt".
- Salah fakta atau penyesatan → buka *issue* dengan templat "Kesalahan isi", sebutkan sumber yang Anda pakai.

## Lisensi kontribusi

Dengan mengirim kontribusi, Anda setuju bahwa kontribusi itu berlisensi [CC BY 4.0](LICENSE), sama seperti isi repositori ini.
