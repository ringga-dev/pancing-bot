# Validasi dokumen: tautan internal, anchor heading, kode Morse, dan cakupan nav.
#
# Dipakai CI (.github/workflows/lint-docs.yml) dan bisa dijalankan lokal:
#   python3 scripts/check_docs.py
# Keluar dengan kode 1 jika ada yang gagal.
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
MD_DIRS = [ROOT, DOCS, ROOT / "templates"]
EXCLUDE_PARTS = {".venv", "site", ".git", "node_modules", ".cache"}

MORSE = {
    ".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e",
    "..-.": "f", "--.": "g", "....": "h", "..": "i", ".---": "j",
    "-.-": "k", ".-..": "l", "--": "m", "-.": "n", "---": "o",
    ".--.": "p", "--.-": "q", ".-.": "r", "...": "s", "-": "t",
    "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y",
    "--..": "z", "-----": "0", ".----": "1", "..---": "2",
    "...--": "3", "....-": "4", ".....": "5", "-....": "6",
    "--...": "7", "---..": "8", "----.": "9",
}


def slug(heading: str) -> str:
    """Replika github-slugger: huruf kecil, buang tanda baca, tiap spasi jadi '-'."""
    t = re.sub(r"<[^>]+>", "", heading.strip().lower())
    t = re.sub(r"[^\w\s\-]", "", t, flags=re.UNICODE)
    return t.replace(" ", "-")


def alnum(text: str) -> str:
    return re.sub(r"[^a-z0-9]", "", text.lower())


def markdown_files() -> list[Path]:
    found: list[Path] = []
    for base in MD_DIRS:
        if not base.is_dir():
            continue
        for path in sorted(base.rglob("*.md")):
            if EXCLUDE_PARTS & set(path.parts):
                continue
            found.append(path)
    # ROOT juga menelusuri docs/, jadi buang duplikatnya.
    return sorted(set(found))


def headings(text: str) -> list[str]:
    out = []
    in_fence = False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            out.append(m.group(2))
    return out


def nav_pages() -> list[str]:
    """Baca daftar halaman dari nav: di mkdocs.yml (kalau ada)."""
    mkdocs = ROOT / "mkdocs.yml"
    if not mkdocs.is_file():
        return []
    pages: list[str] = []
    in_nav = False
    for line in mkdocs.read_text(encoding="utf-8").splitlines():
        if re.match(r"^nav:\s*$", line):
            in_nav = True
            continue
        if in_nav:
            if not line.startswith((" ", "\t")) and line.strip():
                in_nav = False
                continue
            m = re.search(r":\s*([^\s#]+\.md)\s*$", line)
            if m:
                pages.append(m.group(1))
    return pages


def strip_code(text: str) -> str:
    """Buang blok kode dan inline code supaya tidak salah terbaca sebagai tautan."""
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"`[^`\n]*`", "", text)
    return text


def decode_morse(block: str) -> str:
    words = []
    for word in block.split():
        if word == "/":
            words.append(" ")
            continue
        words.append(MORSE.get(word, f"[{word}]"))
    return "".join(words)


def main() -> int:
    files = markdown_files()
    texts = {f: f.read_text(encoding="utf-8") for f in files}
    anchors = {f: [slug(h) for h in headings(t)] for f, t in texts.items()}

    errors: list[str] = []
    warnings: list[str] = []
    links = 0

    for path, text in texts.items():
        rel = path.relative_to(ROOT)
        prose = strip_code(text)
        for m in re.finditer(r"\[([^\]]*)\]\(([^)]+)\)", prose):
            target = m.group(2).split()[0]
            if target.startswith(("http://", "https://", "mailto:", "#")):
                if target.startswith("#"):
                    frag = target[1:]
                    if frag and frag not in anchors[path]:
                        errors.append(f"{rel}: anchor '#' tidak ada di file itu sendiri: {frag}")
                continue
            links += 1
            file_part, _, frag = target.partition("#")
            resolved = (
                (path.parent / file_part).resolve() if file_part else path.resolve()
            )
            if file_part and not resolved.is_file():
                errors.append(f"{rel}: berkas tidak ditemukan -> {target}")
                continue
            if not resolved.is_file():
                continue
            if frag and frag not in anchors.get(resolved, []):
                errors.append(
                    f"{rel}: anchor tidak ditemukan -> {target} "
                    f"(tersedia: {', '.join(anchors[resolved][:6])}...)"
                )

        # Kode Morse: ```text yang isinya hanya titik, garis, dan garis miring.
        # Blok ```text lain (diagram, tabel) dilewati.
        for m in re.finditer(r"```text\n(.*?)```", text, re.S):
            block = m.group(1).strip()
            if not re.fullmatch(r"[.\-/ ]+", block):
                continue
            decoded = decode_morse(block)
            before = text[: m.start()][-800:]
            quotes = re.findall(r"^>\s*(.+)$", before, re.M)
            if not quotes:
                warnings.append(f"{rel}: blok Morse tanpa pertanyaan pembanding")
                continue
            expected = alnum(quotes[-1])
            got = alnum(decoded)
            if expected != got:
                errors.append(
                    f"{rel}: isi Morse tidak cocok dengan pertanyaan.\n"
                    f"        pertanyaan: {quotes[-1]}\n"
                    f"        hasil decode: {decoded}"
                )

    # Cakupan nav MkDocs
    pages = nav_pages()
    if pages:
        known = {str(p.relative_to(DOCS)) for p in DOCS.rglob("*.md")}
        listed = set(pages)
        for missing in sorted(known - listed):
            warnings.append(f"docs/{missing} tidak terdaftar di nav mkdocs.yml")

    print(f"berkas markdown : {len(files)}")
    print(f"tautan internal : {links}")
    print(f"peringatan      : {len(warnings)}")
    for w in warnings:
        print(f"  ! {w}")
    print(f"kesalahan       : {len(errors)}")
    for e in errors:
        print(f"  x {e}")

    if errors:
        print("\nGAGAL.")
        return 1
    print("\nLULUS.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
