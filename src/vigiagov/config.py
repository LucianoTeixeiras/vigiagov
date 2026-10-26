"""Configurações globais do VigiaGov."""

from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configurações extraídas do ambiente (.env)."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    cgu_api_key: str = ""
    cgu_base_url: str = "https://api.portaldatransparencia.gov.br/api-de-dados"
    data_dir: Path = Path("data")

    @property
    def raw_data_dir(self) -> Path:
        """Diretório de dados brutos (JSON / Parquet)."""
        p = self.data_dir / "raw"
        p.mkdir(parents=True, exist_ok=True)
        return p

    @property
    def duckdb_path(self) -> Path:
        """Caminho do arquivo do banco DuckDB."""
        self.data_dir.mkdir(parents=True, exist_ok=True)
        return self.data_dir / "vigiagov.duckdb"


settings = Settings()
