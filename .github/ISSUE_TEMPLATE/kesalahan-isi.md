name: Kesalahan isi
description: Klaim yang keliru, contoh yang menyesatkan, atau sumber yang tidak cocok
labels: [koreksi]
body:
  - type: markdown
    attributes:
      value: |
        Laporan ini untuk isi yang salah atau menyesatkan, bukan untuk kesalahan ketik biasa. Untuk tautan rusak, pakai templat Dokumen.
  - type: input
    id: lokasi
    attributes:
      label: Lokasi
      description: Berkas dan bagian mana yang keliru.
      placeholder: docs/13-menduga-vs-membuktikan.md §4
    validations:
      required: true
  - type: textarea
    id: klaim
    attributes:
      label: Klaim yang keliru
      description: Kutip kalimatnya, lalu jelaskan mengapa keliru.
    validations:
      required: true
  - type: textarea
    id: sumber
    attributes:
      label: Sumber pendukung
      description: Tautkan sumber resmi atau dokumentasi yang mendukung koreksi Anda. Tanpa sumber, laporan mungkin tidak dapat ditindaklanjuti.
      placeholder: https://example.com/resmi
    validations:
      required: true
  - type: textarea
    id: perbaikan
    attributes:
      label: Perbaikan yang diusulkan
      description: Opsional. Kalimat pengganti yang Anda usulkan.
    validations:
      required: false
