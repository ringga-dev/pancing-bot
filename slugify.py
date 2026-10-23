"""Slug heading yang kompatibel dengan GitHub.

MkDocs memakai slugify bawaan Python-Markdown yang melipat beberapa spasi
menjadi satu tanda hubung, sedangkan GitHub mengganti setiap spasi dengan satu
tanda hubung. Akibatnya anchor seperti `#2-pola-manipulasi-berbasis-karakter--representasi-obfuscation`
(hasil dari `&` yang dibuang) hanya cocok di salah satu dari keduanya.

Modul ini dipakai lewat mkdocs.yml:

    markdown_extensions:
      - toc:
          slugify: !!python/name:slugify.github_slugify

Dengan begitu anchor di situs MkDocs identik dengan anchor di GitHub, dan
tautan antar-dokumen tidak perlu ditulis dua versi.
"""

import re

_WORD = re.compile(r"[^\w\s\-]", flags=re.UNICODE)


def github_slugify(value: str, separator: str = "-") -> str:
    """Replika github-slugger: huruf kecil, buang tanda baca, spasi -> separator."""
    text = value.strip().lower()
    text = _WORD.sub("", text)
    return text.replace(" ", separator)


def slugify(value: str, separator: str = "-") -> str:
    """Alias supaya bisa dipakai sebagai pengganti slugify bawaan."""
    return github_slugify(value, separator)
