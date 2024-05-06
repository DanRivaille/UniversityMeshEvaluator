from abc import ABC, abstractmethod

from src.graph.vertex import Vertex


class NeighborsGenerator(ABC):
  def __init__(self, check_continuity: bool):
    self.check_continuity = check_continuity

  @abstractmethod
  def get_neighbors(self, vertex: Vertex):
    pass
