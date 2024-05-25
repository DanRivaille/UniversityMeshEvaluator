class GraphParams:
  def __init__(self, check_continuity: bool, period: int):
    self.__check_continuity: bool = check_continuity
    self.__period: int = period

  @property
  def check_continuity(self) -> bool:
    return self.__check_continuity

  @property
  def period(self) -> int:
    return self.__period
