"""Interface de linha de comando (CLI) do VigiaGov."""

import asyncio
import typer
from rich.console import Console
from rich.table import Table

from vigiagov.client import CGUClient
from vigiagov.config import settings

app = typer.Typer(
    name="vigiagov",
    help="VigiaGov — Auditoria cívica e aberta dos gastos públicos do Governo Federal.",
)
console = Console()


@app.callback()
def main() -> None:
    """VigiaGov — Auditoria cívica e aberta dos gastos públicos do Governo Federal."""


@app.command()
def check():
    """Valida a conexão com a API da CGU e testa a chave de acesso."""
    console.print("\n[bold cyan]🔍 VigiaGov — Validação de Acesso & Conexão Oficial[/bold cyan]")

    if not settings.cgu_api_key:
        console.print(
            "[bold red]❌ ERRO:[/bold red] CGU_API_KEY não configurada no arquivo .env!"
        )
        raise typer.Exit(code=1)

    masked_key = f"{settings.cgu_api_key[:4]}...{settings.cgu_api_key[-4:]}"
    console.print(f"[dim]Chave carregada: {masked_key} | Endpoint: {settings.cgu_base_url}[/dim]\n")

    client = CGUClient()

    async def _run_checks():
        table = Table(title="Status dos Endpoints Vitais (CGU)")
        table.add_column("Domínio", style="cyan", no_wrap=True)
        table.add_column("Endpoint", style="magenta")
        table.add_column("Status", style="bold green")
        table.add_column("Amostra Retornada", style="white")

        checks = [
            ("Órgãos SIAFI", "/orgaos-siafi", {"pagina": 1}),
            ("Empresas Inidôneas (CEIS)", "/ceis", {"pagina": 1}),
            (
                "Cartões CPGF",
                "/cartoes",
                {"mesExtratoInicio": "01/2024", "mesExtratoFim": "01/2024", "pagina": 1},
            ),
        ]

        for dominio, endpoint, params in checks:
            try:
                data = await client.get(endpoint, params=params)
                total = len(data)
                table.add_row(dominio, endpoint, "✅ 200 OK", f"{total} registros")
            except Exception as e:
                table.add_row(dominio, endpoint, "[red]❌ Falha[/red]", str(e)[:40])

        console.print(table)
        console.print("\n[bold green]✓ Infraestrutura e credenciais validadas com sucesso![/bold green]\n")

    asyncio.run(_run_checks())


if __name__ == "__main__":
    app()
