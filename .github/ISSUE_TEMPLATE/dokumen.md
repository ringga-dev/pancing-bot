name: Dokumen
description: Tautan rusak, anchor tidak cocok, format tidak konsisten, atau situs tidak bisa dibangun
labels: [dokumentasi]
body:
  - type: markdown
    attributes:
      value: |
        Terima kasih sudah melaporkan. Isi di bawah membantu kami memperbaikinya lebih cepat.
  - type: input
    id: lokasi
    attributes:
      label: Lokasi
      description: Berkas dan baris atau bagian mana yang bermasalah.
      placeholder: docs/02-verifikasi.md §4
    validations:
      required: true
  - type: textarea
    id: masalah
    attributes:
      label: Apa yang bermasalah
      description: Jelaskan gejalanya. Untuk tautan atau anchor, sertakan output python3 scripts/check_docs.py jika ada.
      placeholder: Tautan ke docs/10-glosarium.md mengarah ke halaman 404.
    validations:
      required: true
  - type: textarea
    id: usulan
    attributes:
      label: Perbaikan yang diusulkan
      description: Opsional. Tautan atau teks apa yang seharusnya dipakai.
    validations:
      required: false
  - type: checkboxes
    id: cek
    attributes:
      label: Sudah diperiksa
      options:
        - label: Saya sudah mencari isu serupa dan belum ada yang sama
          required: true
        - label: Saya sudah menjalankan python3 scripts/check_docs.py (jika laporan tentang tautan atau anchor)
          required: false
