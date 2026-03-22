# Projeto EBOOK Gerado por IAs

Este repositorio deixou de ser apenas um PDF com um resumo dos prompts usados. Agora ele funciona como um kit pratico para criar, organizar e publicar ebooks com apoio de IA.

O projeto combina:

- um exemplo real de ebook sobre seletores CSS
- prompts reutilizaveis para ideacao, escrita e acabamento
- um gerador em Python que transforma um arquivo JSON em ebook Markdown e HTML
- um workflow claro para usar ChatGPT, GitHub Copilot e revisao manual

O PDF original continua no repositorio como artefato final publicado, enquanto o restante da estrutura serve como fonte editavel e reaproveitavel para novos ebooks.

## O que o projeto entrega

- gerador de ebook em Python sem dependencias pesadas
- saida em Markdown e HTML
- estrutura baseada em metadados e capitulos
- exemplo completo de ebook sobre CSS
- prompts prontos para acelerar producao com IA
- testes automatizados

## Estrutura

- `ebook_studio/cli.py`: interface de linha de comando
- `ebook_studio/generator.py`: motor de renderizacao
- `ebook_studio/models.py`: modelos de dados do ebook
- `examples/css-selectors-book.json`: ebook de exemplo em formato editavel
- `examples/ebook-css-selectors.md`: saida Markdown gerada
- `examples/ebook-css-selectors.html`: saida HTML gerada
- `prompts/chatgpt-prompts.md`: prompts para ideacao e escrita
- `docs/workflow.md`: fluxo recomendado de producao

## Como executar

### 1. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 2. Gerar um ebook a partir do exemplo

```bash
python -m ebook_studio.cli ^
  --config examples/css-selectors-book.json ^
  --markdown-out examples/ebook-css-selectors.md ^
  --html-out examples/ebook-css-selectors.html
```

### 3. Criar seu proprio ebook

Duplique `examples/css-selectors-book.json`, ajuste titulo, publico, tom e capitulos, depois gere um novo arquivo com o mesmo comando.

## Formato do JSON

O gerador espera um arquivo com:

- metadados do ebook
- prompt de capa
- CTA final
- lista de capitulos

Cada capitulo aceita:

- `title`
- `objective`
- `key_points`
- `code_example_title`
- `code_example_language`
- `code_example`
- `summary`

## Validacao

```bash
pytest
```

Os testes cobrem:

- carregamento do JSON de exemplo
- renderizacao Markdown
- renderizacao HTML

## Por que isso melhora o projeto

Em vez de mostrar apenas o resultado final, o repositorio agora mostra processo, estrutura e reaproveitamento. Isso deixa o projeto mais forte para GitHub, estudos e portfolio, porque fica claro como a IA entrou no fluxo e como o material pode ser reproduzido.

## Proximos passos

- adicionar exportacao para DOCX ou PDF
- criar temas visuais para landing pages de ebook
- gerar paginas de venda e posts de divulgacao a partir do mesmo JSON
- adicionar validacao de estilo editorial
