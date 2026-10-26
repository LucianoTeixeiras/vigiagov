# VigiaGov — Dossiê de Transição de Sessão & Referência Canônica de Engenharia

- **Data do Host:** 2026-10-25 (domingo)
- **Status do Projeto:** Ativo / Repositório Público Inicializado / Jira Orquestrado
- **Chave do Projeto no Jira:** `VIGIA` (ID: 10284)
- **Repositório GitHub:** `https://github.com/LucianoTeixeiras/vigiagov` (Público)
- **Caminho Local do Repositório:** `D:\0000-repositorios-dev\c3\vigiagov`
- **Caminho Local do Acervo / Documentos Originais:** `C:\Users\lteixeira\OneDrive\01-Projects\01-Agents2AI\Projetos-Hermes\00-API-GOV-BR-Portal-da-Transparencia`
- **Ficha na Horta de Ideias:** `C:\Users\lteixeira\OneDrive\01-Projects\01-Agents2AI\Projetos-Hermes\99-Inbox-Ideias\20261025-001-portal-transparencia-gov-br-auditoria-civica.md`

---

## 1. O Propósito Cívico e Doutrina do Projeto

O **VigiaGov** não é um projeto comercial nem busca faturamento/lucro. É uma **iniciativa cívica independente de controle social e fiscalização orçamentária**.
- **Missão:** Expor a verdade matemática sobre o comportamento das instituições e agentes públicos federais brasileiros, alertando a sociedade sobre descontrole fiscal, desperdício, privilégios corporativos, emendas sem transparência e fornecedores inidôneos que continuam faturando dinheiro público.
- **Princípio da Neutralidade Técnica:** Todo alerta, indicador ou laudo deve ter lastro factual rastreável com link para o documento original da CGU (Nota de Empenho - NE, Ordem Bancária - OB, Termo de Contrato ou Código Siafi). Não se interpolam números nem se criam juízos sem evidência contábil.
- **Acesso à API:** Baseado na API de Dados Abertos do Portal da Transparência (CGU).

---

## 2. Topologia do Jira Cloud (Projeto VIGIA)

- **Instância:** `lucianoteixeiras-1773934569563.atlassian.net`
- **Projeto:** `VIGIA` (ID: 10284)
- **Estrutura de Épicos & Backlog Inicial:**
  - `VIGIA-1`: **EP1 — Fundação, Ingestão & Infraestrutura Analítica Soberana**
    - `VIGIA-6`: *Setup do Repositório vigiagov, uv, DuckDB e Contrato de Qualidade* (CONCLUÍDA no commit `c3fa60b`)
    - `VIGIA-7`: *Cliente Assíncrono da API CGU com Rate Limiting e Cache Local*
  - `VIGIA-2`: **EP2 — Malha 1: Cartões de Pagamento (CPGF) & Gastos Sigilosos**
    - `VIGIA-8`: *Pipeline de Ingestão e Normalização de Cartões CPGF (2023-2024)*
    - `VIGIA-9`: *Motor de Detecção: Fracionamento de Despesa e Fornecedores Recorrentes*
  - `VIGIA-3`: **EP3 — Malha 2: Emendas Parlamentares & Rastreamento de Repasses**
    - `VIGIA-10`: *Ingestão e Cruzamento de Emendas Parlamentares com Municípios Favorecidos*
  - `VIGIA-4`: **EP4 — Malha 3: Fornecedores Sancionados (CEIS, CNEP, CEPIM) & Cruzamentos**
    - `VIGIA-11`: *Cruzamento de Pagamentos Federais com Base CEIS/CNEP*
  - `VIGIA-5`: **EP5 — Camada de Publicação & Alerta Cívico à População**
    - `VIGIA-12`: *Gerador de Relatórios Cívicos em Markdown e PDF com Fatos Auditáveis*

---

## 3. Estado Factual do Código & Repositório Git

- **Branch Ativa:** `feat/scaffold-core-client-cgu`
- **Último Commit:** `c3fa60b` (`feat(scaffold): inicializacao do vigiagov com uv, cliente cgu e suite pytest (VIGIA-6)`)
- **Remoto Origin:** Sincronizado (`git push -u origin feat/scaffold-core-client-cgu` concluído com sucesso).
- **Regra de Ouro Git:** **NUNCA** commitar na `main`. Todo desenvolvimento segue via feature branches e Pull Requests.
- **Stack Tecnológica do Repositório (`D:\0000-repositorios-dev\c3\vigiagov`):**
  - Gerenciamento de dependências via `uv` (exclusivo, sem comandos python/pip globais).
  - Python 3.11+ / CPython 3.14.7 isolado em `.venv`.
  - Pacotes instalados: `duckdb`, `httpx`, `pydantic`, `pydantic-settings`, `pyarrow`, `python-dotenv`, `rich`, `typer`, `pytest`, `ruff`.
  - Suíte de testes: `pytest` verde (2/2 testes passando em `tests/test_basic.py`).

---

## 4. Estrutura do Código Desenvolvido

```
D:\0000-repositorios-dev\c3\vigiagov/
├── .env                  # Chave da CGU configurada localmente (IGNORADO PELO GIT)
├── .env.example          # Modelo público sem chave
├── .gitignore            # Blindagem de .env, data/, *.duckdb, *.parquet, .venv
├── LICENSE               # Licença MIT
├── README.md             # Manifesto cívico, 4 malhas explicadas, diagrama Mermaid
├── pyproject.toml        # Metadados e dependências via uv
├── uv.lock               # Determinismo estrito de pacotes
├── src/
│   └── vigiagov/
│       ├── __init__.py   # Versão 0.1.0
│       ├── config.py     # Settings via pydantic-settings (caminhos data/ e DuckDB)
│       ├── client.py     # CGUClient assíncrono com retries, backoff e tratamento 429
│       └── cli.py        # Typer CLI com comando 'vigiagov check'
└── tests/
    └── test_basic.py     # Testes unitários do settings e client
```

---

## 5. Endpoints & Comportamento da API da CGU (Validados Factualmente)

- **Base URL:** `https://api.portaldatransparencia.gov.br/api-de-dados`
- **Autenticação:** Header `chave-api-dados: <CHAVE>`
- **Testes Reais Executados com 200 OK:**
  - `/orgaos-siafi?pagina=1`: Órgãos do SIAFI (retorna 15 itens por página).
  - `/ceis?pagina=1`: Cadastro de Empresas Inidôneas e Suspensas.
  - `/cartoes?mesExtratoInicio=01/2024&mesExtratoFim=01/2024&pagina=1`: Cartão de Pagamento do Governo Federal (CPGF). Testamos até a página 1000 — paginação fluida e dados ricos incluindo favorecido, CNPJ, órgão máximo e unidade gestora.

---

## 6. Comandos Canônicos para a Nova Sessão

Para rodar qualquer comando no repositório a partir da nova sessão:
```bash
# Entrar no repositório
cd /d/0000-repositorios-dev/c3/vigiagov

# Rodar a CLI do projeto
uv run vigiagov check

# Rodar os testes
uv run pytest

# Iniciar uma nova feature branch (exemplo para VIGIA-8)
git checkout -b feat/ingestao-cartoes-cpgf
```

---

## 6.1. Atualização de Sessão (2026-10-25, fechamento)

- **Branch ativa ao fechar:** `docs/fundamentos-civicos` (limpa, pushada, commit `83e5fb9`).
- **Ambiente revalidado:** `uv run vigiagov check` → 3 endpoints 200 OK; `uv run pytest` → 2 passed.
- **Acervo criado:** `docs/fundamentos/` (README com regras de fontes, CATALOGO_FONTES_OFICIAIS.md e síntese factual de regimes sociais em `202610/25/`). Regra persistida em memória: **toda síntese de valor social/político/econômico exige fonte oficial linkada com data de acesso**.
- **Payload real de `/cartoes` confirmado:** lista pura de 15 itens/página (paginar até lista vazia); `valorTransacao` string BR (`"97,89"`); datas DD/MM/YYYY; CNPJ com máscara (limpar para join com CEIS); esquema aninhado `estabelecimento`/`unidadeGestora`/`orgaoVinculado`/`orgaoMaximo`/`portador`.
- **Plano da VIGIA-8 aprovado na forma** (6 fases TDD, branch `feat/ingestao-cartoes-cpgf`).
- **Relatório de fechamento:** `docs/reports/202610/25/2026-10-25-fechamento-diario.md`.

**Decisões pendentes para a próxima sessão:**
1. Ordem de merge (PR VIGIA-6 antes do PR docs).
2. VIGIA-7 (cache) subsumida pelo Parquet na VIGIA-8, ou executada antes?
3. Manter `portador.nome` no schema com nota de base legal?

---

## 7. Próxima Ação Imediata Recomendada (Roadmap do Turno)

1. **Atacar a tarefa `VIGIA-8` (Malha 1 de Cartões CPGF):**
   - Criar módulo `vigiagov/ingestion/cartoes.py` para iterar páginas de determinado mês/ano.
   - Salvar os dados brutos em Parquet particionado por ano/mês (`data/raw/cartoes/ano=2024/mes=01/...`).
   - Carregar no DuckDB local (`data/vigiagov.duckdb`) para possibilitar queries SQL de auditoria em milissegundos.
2. **Atacar a tarefa `VIGIA-9` (Detecção de Anomalias):**
   - Query SQL no DuckDB para identificar estabelecimentos com múltiplos pagamentos no mesmo dia/semana (fracionamento de despesa) ou saques expressivos em espécie.
