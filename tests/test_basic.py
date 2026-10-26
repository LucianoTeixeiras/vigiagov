"""Testes unitários do cliente e da configuração do VigiaGov."""

from vigiagov.client import CGUClient
from vigiagov.config import Settings


def test_settings_initialization():
    """Valida leitura e propriedades de caminhos do Settings."""
    cfg = Settings(cgu_api_key="teste_chave_123")
    assert cfg.cgu_api_key == "teste_chave_123"
    assert "api-de-dados" in cfg.cgu_base_url
    assert cfg.duckdb_path.name == "vigiagov.duckdb"


def test_client_header_building():
    """Valida montagem de cabeçalhos de autenticação da CGU."""
    client = CGUClient(api_key="token_secreto_abc")
    assert client.headers["chave-api-dados"] == "token_secreto_abc"
    assert client.headers["Accept"] == "application/json"
