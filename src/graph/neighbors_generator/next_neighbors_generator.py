from neighbors_generator import NeighborsGenerator
from src.graph.vertex import Vertex


class NextNeighborsGenerator(NeighborsGenerator):
  def __init__(self, check_continuity: bool):
    super().__init__(check_continuity)

  def get_neighbors(self, vertex: Vertex) -> [Vertex]:
    if self.check_continuity:
      return filter(lambda n: n.n_layer == (vertex.n_layer + 1), vertex.next)
    else:
      return vertex.next
