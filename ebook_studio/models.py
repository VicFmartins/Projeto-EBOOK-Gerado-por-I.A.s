from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Chapter:
    title: str
    objective: str
    key_points: list[str]
    code_example_title: str
    code_example_language: str
    code_example: str
    summary: str


@dataclass
class EbookSpec:
    title: str
    subtitle: str
    author: str
    audience: str
    theme: str
    tone: str
    cover_prompt: str
    call_to_action: str
    chapters: list[Chapter]
