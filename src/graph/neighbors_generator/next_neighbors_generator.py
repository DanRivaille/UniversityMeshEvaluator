from src.graph.graph_params import GraphParams
from src.graph.neighbors_generator.neighbors_generator import NeighborsGenerator
from src.graph.vertex import Vertex


class NextNeighborsGenerator(NeighborsGenerator):
  def __init__(self, params: GraphParams):
    super().__init__(params)

  def get_neighbors(self, vertex: Vertex) -> [Vertex]:
    if self.params.check_continuity:
      return filter(lambda n: n.n_layer <= (vertex.n_layer + self.params.period), vertex.next)
    else:
      return vertex.next
