# Catálogo de Fontes Oficiais e Idôneas

> **Regra geral:** fonte aceita para alegações factuais = (1) fonte primária oficial de Estado ou de agência multilateral; (2) estudo acadêmico peer-reviewed com DOI; (3) tribunais internacionais/nacionais em matéria de seus veredictos. Wikipedia e imprensa servem como ponteiro de descoberta, **nunca** como fonte de número.

## Critérios de Idoneidade

1. **Primária:** o dado vem de quem mede (instituto oficial, agência estatística, organização multilateral).
2. **Auditável:** URL permanente, data de acesso registrada, metodologia publicada.
3. **Apartidária:** instituição técnica, não partido, campanha ou think tank engajado. Think tanks (ex.: Heritage, Ipea enquanto pesquisa) podem ser citados como análise secundária apenas com ressalva explícita de orientação.

## Instituições por Domínio

### Saúde Global e Nacional
| Instituição | Escopo | URL |
|---|---|---|
| OMS — Organização Mundial da Saúde | Indicadores de saúde, expectativa de vida, cobertura | `https://www.who.int` / `https://data.who.int` |
| OPAS/PAHO | Saúde nas Américas | `https://www.paho.org` |
| Ministério da Saúde (Brasil) | DATASUS, vigilância, políticas | `https://datasus.saude.gov.br` |
| UNICEF | Infância, mortalidade infantil, educação | `https://data.unicef.org` |

### Economia, Pobreza e Finanças Públicas
| Instituição | Escopo | URL |
|---|---|---|
| Banco Mundial | Pobreza, PIB, desenvolvimento (WDI, Poverty & Equity Briefs) | `https://data.worldbank.org` |
| FMI | Contas macroeconômicas, crises, supervisão | `https://www.imf.org` |
| OCDE | Políticas públicas, bem-estar, tributação | `https://www.oecd.org` |
| BIS | Sistema financeiro e bancos centrais | `https://www.bis.org` |
| Tesouro Nacional (Brasil) | Execução orçamentária, dívida | `https://www.tesourotransparente.gov.br` |
| Banco Central do Brasil | Inflação, câmbio, crédito | `https://www.bcb.gov.br` |

### Desenvolvimento Humano e Demografia
| Instituição | Escopo | URL |
|---|---|---|
| PNUD — ONU | IDH e relatórios de desenvolvimento humano | `https://hdr.undp.org` |
| UN DESA — Divisão de População | Demografia, projeções | `https://population.un.org` |
| IBGE (Brasil) | Censos, PNAD, estatísticas oficiais | `https://www.ibge.gov.br` |
| IPEA (Brasil) | Pesquisa econômica aplicada, políticas públicas | `https://www.ipea.gov.br` |

### Crise Humanitária, Refúgio e Conflito
| Instituição | Escopo | URL |
|---|---|---|
| ACNUR — UNHCR | Refugiados e deslocados | `https://www.unhcr.org` |
| R4V | Resposta interagencial à crise venezuelana | `https://www.r4v.info` |
| OCHA | Coordenação humanitária ONU | `https://www.unocha.org` |
| Tribunal Penal Internacional / tribunais ad hoc (ex.: ECCC Camboja) | Veredictos judiciais em genocídio e crimes contra a humanidade | `https://www.icc-cpi.int` / `https://www.eccc.gov.kh` |

### Estudos Acadêmicos e Programas de Referência
| Instituição | Escopo | URL |
|---|---|---|
| Yale Genocide Studies Program | Documentação de genocídios (Camboja, Holodomor, etc.) | `https://macmillan.yale.edu/gsp` |
| Harvard Ukrainian Research Institute (HURI) | Holodomor e estudos ucranianos | `https://huri.harvard.edu` |
| Periódicos peer-reviewed (Population and Development Review, Canadian Studies in Population, Nationalities Papers, etc.) | Demografia histórica com DOI | via `https://doi.org` |

### Transparência e Controle (núcleo do VigiaGov)
| Instituição | Escopo | URL |
|---|---|---|
| CGU — Portal da Transparência | Dados abertos de execução orçamentária (API de Dados) | `https://portaldatransparencia.gov.br` / `https://api.portaldatransparencia.gov.br` |
| TCU | Auditoria de contas públicas | `https://portal.tcu.gov.br` |
| SIAFI/Sistema Siafi | Registro contábil da execução federal | via Portal da Transparência |
| Receita Federal (CNPJ, CEIS) | Cadastros de empresas e sanções | `https://dados.gov.br` / CEIS via API CGU |

## Como citar no acervo

Formato padrão em todo documento de `docs/fundamentos/`:

```markdown
- **Fato:** <alegação factual com número>
  - **Fonte:** <Instituição — Título/Indicador>
  - **URL:** <link permanente>
  - **Acesso:** <YYYY-MM-DD>
```

Números sem esse bloco não entram no acervo. Exceção única: quando o próprio documento é o registro primário (ex.: laudo de transcrição de script Qlik no acervo do projeto), o laudo informa sua própria natureza de fonte.
