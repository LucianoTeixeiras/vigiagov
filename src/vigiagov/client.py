"""Cliente HTTP assíncrono para a API de Dados do Portal da Transparência (CGU)."""

import asyncio
from typing import Any
import httpx
from rich.console import Console

from vigiagov.config import settings

console = Console()


class CGUClient:
    """Cliente com rate limiting e tratamento robusto de erros."""

    def __init__(self, api_key: str | None = None, base_url: str | None = None):
        self.api_key = api_key or settings.cgu_api_key
        self.base_url = (base_url or settings.cgu_base_url).rstrip("/")
        if not self.api_key:
            raise ValueError(
                "CGU_API_KEY não configurada. Defina no arquivo .env ou passe como parâmetro."
            )
        self.headers = {
            "chave-api-dados": self.api_key,
            "Accept": "application/json",
            "User-Agent": "VigiaGov-AuditoriaCivica/0.1.0",
        }

    async def get(
        self,
        endpoint: str,
        params: dict[str, Any] | None = None,
        max_retries: int = 3,
        backoff_seconds: float = 1.0,
    ) -> list[dict[str, Any]]:
        """Executa GET com retries e paginação segura."""
        clean_endpoint = endpoint if endpoint.startswith("/") else f"/{endpoint}"
        url = f"{self.base_url}{clean_endpoint}"

        async with httpx.AsyncClient(timeout=30.0) as client:
            for attempt in range(1, max_retries + 1):
                try:
                    resp = await client.get(url, headers=self.headers, params=params)
                    if resp.status_code == 200:
                        data = resp.json()
                        return data if isinstance(data, list) else [data]
                    if resp.status_code == 429:
                        delay = backoff_seconds * (2 ** (attempt - 1))
                        console.print(
                            f"[yellow]Rate limit atingido (429). Aguardando {delay:.1f}s...[/yellow]"
                        )
                        await asyncio.sleep(delay)
                        continue
                    if resp.status_code >= 500:
                        delay = backoff_seconds * attempt
                        console.print(
                            f"[yellow]Erro {resp.status_code} no servidor CGU. Tentativa {attempt}/{max_retries}...[/yellow]"
                        )
                        await asyncio.sleep(delay)
                        continue

                    resp.raise_for_status()
                except httpx.RequestError as exc:
                    if attempt == max_retries:
                        raise exc
                    await asyncio.sleep(backoff_seconds * attempt)

            raise RuntimeError(f"Falha ao consultar {url} após {max_retries} tentativas.")
