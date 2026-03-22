from pathlib import Path

from ebook_studio.generator import load_spec, render_html, render_markdown


def test_load_spec_reads_example() -> None:
    spec = load_spec(Path("examples/css-selectors-book.json"))
    assert spec.title == "Dominando Seletores CSS"
    assert len(spec.chapters) == 4


def test_render_markdown_contains_key_sections() -> None:
    spec = load_spec(Path("examples/css-selectors-book.json"))
    content = render_markdown(spec)
    assert "# Dominando Seletores CSS" in content
    assert "## Sumario" in content
    assert "```css" in content


def test_render_html_contains_document_shell() -> None:
    spec = load_spec(Path("examples/css-selectors-book.json"))
    html = render_html(spec)
    assert "<!doctype html>" in html
    assert "<h1>Dominando Seletores CSS</h1>" in html
    assert "<pre><code>" in html
    assert "```" not in html
