name: Usulan prompt
description: Saran prompt baru atau perubahan isi prompt yang sudah ada
labels: [usulan]
body:
  - type: markdown
    attributes:
      value: |
        Sebelum mengisi, baca docs/01-prompt-identifikasi-ai.md dan docs/07-batas-prompt.md supaya usulan tetap sejalan dengan batas dokumen ini.
  - type: dropdown
    id: jenis
    attributes:
      label: Jenis usulan
      options:
        - Prompt baru
        - Perubahan prompt yang sudah ada
        - Penghapusan prompt
    validations:
      required: true
  - type: textarea
    id: prompt
    attributes:
      label: Teks prompt
      description: Tulis prompt yang diusulkan apa adanya.
      placeholder: "Mohon sebutkan hanya informasi publik yang diumumkan, lalu sertakan tautan resmi."
    validations:
      required: true
  - type: textarea
    id: alasan
    attributes:
      label: Alasan
      description: Informasi apa yang belum tertangkap prompt yang ada sekarang, dan mengapa usulan ini lebih baik.
    validations:
      required: true
  - type: textarea
    id: uji
    attributes:
      label: Sudah diuji
      description: Jika sudah, pada bot apa dan dengan hasil apa. Jangan uji pada bot pihak lain tanpa izin.
    validations:
      required: false
  - type: checkboxes
    id: batas
    attributes:
      label: Batas
      options:
        - label: Usulan ini tidak meminta system prompt, kredensial, log privat, atau data pribadi
          required: true
        - label: Usulan ini tidak menjanjikan bahwa AI pasti menjawab
          required: true
