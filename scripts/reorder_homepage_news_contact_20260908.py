from pathlib import Path
import subprocess

INDEX = Path("index.html")
START = "<!-- TNS_AUTO_NEWS_START -->"
END = "<!-- TNS_AUTO_NEWS_END -->"
CONTACT_MARKER = '<style id="tns-contact-only-style">'


def ensure_news_block() -> str:
    text = INDEX.read_text(encoding="utf-8")
    if START in text and END in text:
        return text

    subprocess.run(["python", "scripts/install_news_section.py"], check=True)
    text = INDEX.read_text(encoding="utf-8")
    if START not in text or END not in text:
        raise SystemExit("Homepage news block could not be generated")
    return text


def main() -> None:
    text = ensure_news_block()
    if CONTACT_MARKER not in text:
        raise SystemExit("Homepage contact marker not found")

    start = text.index(START)
    end = text.index(END, start) + len(END)
    news_block = text[start:end].strip()

    # Remove the current news block first, wherever it lives.
    remaining = (text[:start] + text[end:]).strip() + "\n"

    # Put news immediately before the contact section. This creates the desired
    # bottom-of-homepage flow: FAQ -> News -> Contact -> Footer.
    remaining = remaining.replace(
        CONTACT_MARKER,
        news_block + "\n\n" + CONTACT_MARKER,
        1,
    )

    INDEX.write_text(remaining, encoding="utf-8")
    print("Homepage order enforced: FAQ -> News -> Contact -> Footer")


if __name__ == "__main__":
    main()
