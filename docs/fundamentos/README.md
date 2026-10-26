# Fundamentos — Acervo Factual Cívico do VigiaGov

> **Propósito:** esta pasta é o acervo canônico de informações de valor **social, político e econômico** que sustentam a doutrina de neutralidade técnica do VigiaGov. Aqui vivem sínteses, análises comparativas e marcos históricos com **lastro factual rastreável**, usados para embasar relatórios cívicos, decisões de engenharia analítica e a régua ética do projeto.

## O que esta pasta É

- **Acervo de fatos verificáveis** sobre instituições, regimes, políticas públicas e fenômenos econômicos/sociais relevantes ao controle social dos gastos federais.
- **Base de doutrina**: toda alegação de peso em relatórios do VigiaGov deve poder apontar para os documentos aqui consolidados ou diretamente para as fontes oficiais neles citadas.

## O que esta pasta NÃO é

- **Não é espaço de opinião ou de militância.** O VigiaGov é apartidário por construção. Análises aqui registram fatos mensuráveis e suas fontes, não juízos de valor.
- **Não é repositório de dados brutos.** Dados (Parquet, DuckDB, JSON) vivem em `data/` (ignorado pelo Git). Aqui ficam sínteses e referências.

## Regras de Entrada (mandatórias)

1. **Fonte idônea obrigatória.** Toda alegação numérica ou factual exige fonte primária oficial ou agência multilateral credenciada: OMS, Banco Mundial, FMI, PNUD, ACNUR, OCDE, IBGE, IPEA, TCU, CGU, censos nacionais, tribunais internacionais — ou estudo acadêmico peer-reviewed com DOI. O catálogo completo está em [`CATALOGO_FONTES_OFICIAIS.md`](CATALOGO_FONTES_OFICIAIS.md).
2. **Link verificável com data de acesso.** Nenhum número sem URL da fonte. Wikipedia pode ser ponteiro, nunca fonte.
3. **Régua única.** O mesmo critério de evidência se aplica a qualquer governo, partido, ideologia ou país — incluindo o Brasil.
4. **Partição temporal estrita.** Documentos datados seguem `YYYYMM/DD/NOME_DO_DOCUMENTO.md` (pastas e arquivos em lowercase). Arquivos perenes (este README, catálogos) ficam na raiz da pasta.
5. **Neutralidade de linguagem.** Fatos com números e fontes; adjetivos e juízos morais ficam fora do texto.

## Índice do Acervo

| Documento | Tema | Data |
|---|---|---|
| [`CATALOGO_FONTES_OFICIAIS.md`](CATALOGO_FONTES_OFICIAIS.md) | Instituições idôneas por domínio (perene) | — |
| [`202610/25/SINTESE_REGIMES_SOCIALISTAS_COMUNISTAS_FATOS_E_FONTES.md`](202610/25/SINTESE_REGIMES_SOCIALISTAS_COMUNISTAS_FATOS_E_FONTES.md) | Benefícios e custos de regimes socialistas/comunistas para seus povos | 2026-10-25 |

## Vínculo com a Doutrina do Projeto

O VigiaGov expõe **fatos matemáticos** sobre gastos públicos federais — mesma régua aplicada a qualquer governo. Este acervo existe para que a régua nunca seja improvisada: cada juízo emitido em nome do projeto precisa de uma fonte que qualquer cidadão possa abrir e conferir.
