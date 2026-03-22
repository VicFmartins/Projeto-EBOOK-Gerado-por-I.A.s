from __future__ import annotations

import argparse

from ebook_studio.generator import load_spec, write_outputs


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Gera ebooks em Markdown e HTML a partir de um JSON.")
    parser.add_argument("--config", required=True, help="Caminho para o arquivo JSON do ebook.")
    parser.add_argument("--markdown-out", help="Arquivo de saida em Markdown.")
    parser.add_argument("--html-out", help="Arquivo de saida em HTML.")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    spec = load_spec(args.config)
    write_outputs(spec, markdown_path=args.markdown_out, html_path=args.html_out)


if __name__ == "__main__":
    main()
