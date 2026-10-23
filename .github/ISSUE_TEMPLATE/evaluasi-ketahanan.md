name: Evaluasi ketahanan
description: Hasil pengujian, pola baru yang ditemukan, atau usulan mitigasi untuk bot
labels: [evaluasi]
body:
  - type: markdown
    attributes:
      value: |
        > [!IMPORTANT]
        > Laporkan hanya hasil pengujian pada bot yang Anda miliki atau yang Anda berwenang uji secara tertulis. Lihat docs/08-pola-prompt-dan-evaluasi.md §5 dan docs/09-lembar-kerja-evaluasi.md.
  - type: input
    id: target
    attributes:
      label: Target pengujian
      description: Sebutkan jenis bot dan status otorisasi. Jangan sebutkan akun pihak lain.
      placeholder: Bot layanan pelanggan milik sendiri, lingkungan staging.
    validations:
      required: true
  - type: input
    id: versi
    attributes:
      label: Versi konfigurasi
      description: Tag atau hash commit prompt sistem dan guardrail saat diuji.
      placeholder: v1.3.0 / commit abc123
    validations:
      required: true
  - type: textarea
    id: hasil
    attributes:
      label: Hasil
      description: Metrik (ASR, FRR), jumlah percobaan, dan ringkasan temuan. Lampirkan lembar kerja jika memungkinkan.
    validations:
      required: true
  - type: textarea
    id: pola
    attributes:
      label: Pola yang terlibat
      description: Sebutkan pola dari docs/08 §1–§2 yang berhasil atau gagal, dan tahap pipeline yang bocor.
    validations:
      required: false
  - type: textarea
    id: mitigasi
    attributes:
      label: Usulan mitigasi
      description: Perubahan apa yang Anda usulkan di tahap normalisasi, moderasi, atau verifikasi output.
    validations:
      required: false
  - type: checkboxes
    id: privasi
    attributes:
      label: Privasi
      options:
        - label: Lampiran tidak memuat data pribadi pengguna, kredensial, token, atau isi system prompt produksi
          required: true
