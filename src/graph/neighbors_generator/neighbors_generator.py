from abc import ABC, abstractmethod

from src.graph.graph_params import GraphParams
from src.graph.vertex import Vertex


class NeighborsGenerator(ABC):
  def __init__(self, params: GraphParams):
    self.params: GraphParams = params

  @abstractmethod
  def get_neighbors(self, vertex: Vertex):
    pass
