# Dominando Seletores CSS

## Um guia pratico para estilizar interfaces com mais clareza

**Autor:** Vic F. Martins
**Publico:** Estudantes e desenvolvedores iniciantes em front-end
**Tema:** CSS
**Tom editorial:** Didatico e objetivo

## Prompt de capa

Crie uma capa de ebook moderna sobre CSS, com atmosfera espacial, tipografia forte, tons de azul e ciano, interface futurista e destaque para a frase Dominando Seletores CSS.

## Sumario

1. Seletores basicos que voce realmente usa
2. Combinadores para estilizar com contexto
3. Pseudo-classes para estados reais da interface
4. Atributos e boas praticas para CSS escalavel

## Seletores basicos que voce realmente usa

**Objetivo:** Entender os seletores mais comuns para ganhar fluidez no dia a dia.

### Pontos-chave

- Seletores por elemento sao bons para estruturas simples.
- Classes ajudam a reutilizar estilos sem acoplar ao HTML especifico.
- IDs devem ser usados com moderacao para evitar rigidez.

### Exemplo: Estilizando cards de produto

```css
.product-card {
  border: 1px solid #dbe2ea;
  padding: 16px;
}

.product-card h2 {
  margin-bottom: 8px;
}

#featured-product {
  border-color: #0ea5e9;
}
```

### Fechamento

Com esses seletores basicos, voce ja cobre boa parte das interfaces comuns sem complicar o CSS.

## Combinadores para estilizar com contexto

**Objetivo:** Aprender a selecionar elementos pela relacao entre eles.

### Pontos-chave

- O combinador de descendencia seleciona elementos dentro de outro bloco.
- O combinador filho evita estilizar niveis inesperados.
- Irmaos adjacentes e gerais ajudam em formularios e listas.

### Exemplo: Melhorando um formulario

```css
.signup-form label {
  font-weight: 600;
}

.signup-form > input {
  display: block;
  margin-bottom: 12px;
}

input + small {
  color: #64748b;
}
```

### Fechamento

Quando o contexto importa, os combinadores deixam o estilo mais preciso e evitam efeitos colaterais.

## Pseudo-classes para estados reais da interface

**Objetivo:** Aplicar estilos que respondem ao comportamento do usuario.

### Pontos-chave

- Use :hover e :focus para feedback visual imediato.
- Use :first-child e :last-child para ajustes finos em listas.
- Estados como :disabled ajudam a comunicar a regra da interface.

### Exemplo: Botoes com feedback

```css
.cta-button:hover {
  background: #0284c7;
}

.cta-button:focus {
  outline: 3px solid #bae6fd;
}

.plan-card:last-child {
  margin-bottom: 0;
}
```

### Fechamento

Pseudo-classes aproximam o CSS do comportamento real da interface e melhoram a experiencia do usuario.

## Atributos e boas praticas para CSS escalavel

**Objetivo:** Usar seletores de atributo com criterio e manter o codigo legivel.

### Pontos-chave

- Seletores por atributo funcionam bem em formularios e componentes reutilizaveis.
- Evite especificidade desnecessaria para facilitar manutencao.
- Nomear classes com clareza vale mais do que truques complexos.

### Exemplo: Campos por tipo

```css
input[type="email"] {
  border-color: #38bdf8;
}

button[aria-expanded="true"] {
  background: #082f49;
  color: #f8fafc;
}

[data-status="warning"] {
  color: #b45309;
}
```

### Fechamento

Seletores poderosos sao mais uteis quando aparecem em uma base organizada, previsivel e facil de manter.

## Proximo passo

Revise seu projeto atual, identifique onde voce esta usando seletores excessivamente genericos e reescreva pelo menos tres trechos com mais clareza e contexto.
