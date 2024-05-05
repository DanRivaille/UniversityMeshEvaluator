class Prerequisite:
  def __init__(self, cod_prerequisite: str, connector: str | None):
    self.cod_prerequisite = cod_prerequisite
    self.connector = connector

  def __str__(self) -> str:
    return self.cod_prerequisite

  def __repr__(self) -> str:
    return self.cod_prerequisite
