from __future__ import annotations

import html
import json
from pathlib import Path

from ebook_studio.models import Chapter, EbookSpec


def load_spec(path: str | Path) -> EbookSpec:
    raw_data = json.loads(Path(path).read_text(encoding="utf-8"))
    chapters = [
        Chapter(
            title=item["title"],
            objective=item["objective"],
            key_points=item["key_points"],
            code_example_title=item["code_example_title"],
            code_example_language=item["code_example_language"],
            code_example=item["code_example"],
            summary=item["summary"],
        )
        for item in raw_data["chapters"]
    ]
    return EbookSpec(
        title=raw_data["title"],
        subtitle=raw_data["subtitle"],
        author=raw_data["author"],
        audience=raw_data["audience"],
        theme=raw_data["theme"],
        tone=raw_data["tone"],
        cover_prompt=raw_data["cover_prompt"],
        call_to_action=raw_data["call_to_action"],
        chapters=chapters,
    )


def render_markdown(spec: EbookSpec) -> str:
    lines = [
        f"# {spec.title}",
        "",
        f"## {spec.subtitle}",
        "",
        f"**Autor:** {spec.author}",
        f"**Publico:** {spec.audience}",
        f"**Tema:** {spec.theme}",
        f"**Tom editorial:** {spec.tone}",
        "",
        "## Prompt de capa",
        "",
        spec.cover_prompt,
        "",
        "## Sumario",
        "",
    ]

    for index, chapter in enumerate(spec.chapters, start=1):
        lines.append(f"{index}. {chapter.title}")

    for chapter in spec.chapters:
        lines.extend(
            [
                "",
                f"## {chapter.title}",
                "",
                f"**Objetivo:** {chapter.objective}",
                "",
                "### Pontos-chave",
                "",
            ]
        )
        for point in chapter.key_points:
            lines.append(f"- {point}")
        lines.extend(
            [
                "",
                f"### Exemplo: {chapter.code_example_title}",
                "",
                f"```{chapter.code_example_language}",
                chapter.code_example.rstrip(),
                "```",
                "",
                "### Fechamento",
                "",
                chapter.summary,
            ]
        )

    lines.extend(
        [
            "",
            "## Proximo passo",
            "",
            spec.call_to_action,
            "",
        ]
    )
    return "\n".join(lines)


def render_html(spec: EbookSpec) -> str:
    html_lines = [
        "<!doctype html>",
        '<html lang="pt-BR">',
        "<head>",
        '  <meta charset="utf-8">',
        f"  <title>{html.escape(spec.title)}</title>",
        "  <style>",
        "    body { font-family: Georgia, serif; margin: 40px auto; max-width: 860px; line-height: 1.6; color: #1f2933; padding: 0 20px; background: #f8fafc; }",
        "    main { background: #ffffff; border-radius: 18px; padding: 40px; box-shadow: 0 14px 40px rgba(15, 23, 42, 0.08); }",
        "    h1, h2, h3 { color: #0f172a; }",
        "    pre { background: #0f172a; color: #e2e8f0; padding: 16px; overflow-x: auto; border-radius: 12px; }",
        "    code { font-family: Consolas, monospace; }",
        "    ul, ol { padding-left: 24px; }",
        "    .meta { color: #475569; margin-bottom: 24px; }",
        "  </style>",
        "</head>",
        "<body>",
        "  <main>",
        f"    <h1>{html.escape(spec.title)}</h1>",
        f"    <h2>{html.escape(spec.subtitle)}</h2>",
        '    <p class="meta">',
        f"      <strong>Autor:</strong> {html.escape(spec.author)}<br>",
        f"      <strong>Publico:</strong> {html.escape(spec.audience)}<br>",
        f"      <strong>Tema:</strong> {html.escape(spec.theme)}<br>",
        f"      <strong>Tom editorial:</strong> {html.escape(spec.tone)}",
        "    </p>",
        "    <h2>Prompt de capa</h2>",
        f"    <p>{html.escape(spec.cover_prompt)}</p>",
        "    <h2>Sumario</h2>",
        "    <ol>",
    ]

    for chapter in spec.chapters:
        html_lines.append(f"      <li>{html.escape(chapter.title)}</li>")

    html_lines.append("    </ol>")

    for chapter in spec.chapters:
        html_lines.extend(
            [
                f"    <h2>{html.escape(chapter.title)}</h2>",
                f"    <p><strong>Objetivo:</strong> {html.escape(chapter.objective)}</p>",
                "    <h3>Pontos-chave</h3>",
                "    <ul>",
            ]
        )
        for point in chapter.key_points:
            html_lines.append(f"      <li>{html.escape(point)}</li>")
        html_lines.extend(
            [
                "    </ul>",
                f"    <h3>Exemplo: {html.escape(chapter.code_example_title)}</h3>",
                "    <pre><code>",
                html.escape(chapter.code_example.rstrip()),
                "    </code></pre>",
                "    <h3>Fechamento</h3>",
                f"    <p>{html.escape(chapter.summary)}</p>",
            ]
        )

    html_lines.extend(
        [
            "    <h2>Proximo passo</h2>",
            f"    <p>{html.escape(spec.call_to_action)}</p>",
        ]
    )

    html_lines.extend(["  </main>", "</body>", "</html>"])
    return "\n".join(html_lines)


def write_outputs(spec: EbookSpec, markdown_path: str | Path | None, html_path: str | Path | None) -> None:
    if markdown_path:
        markdown_target = Path(markdown_path)
        markdown_target.parent.mkdir(parents=True, exist_ok=True)
        markdown_target.write_text(render_markdown(spec), encoding="utf-8")
    if html_path:
        html_target = Path(html_path)
        html_target.parent.mkdir(parents=True, exist_ok=True)
        html_target.write_text(render_html(spec), encoding="utf-8")
