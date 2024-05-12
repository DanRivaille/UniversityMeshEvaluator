from src.graph.graph import Graph
from src.graph.vertex import Vertex


class GraphUpdater:
  def __init__(self, check_continuity: bool):
    self.check_continuity: bool = check_continuity

  @staticmethod
  def advance_vertex(graph: Graph, vertex_id: str):
    vertex: Vertex = graph.vertices_set.get(vertex_id, None)

    if vertex.n_layer > 0:
      graph.layers[vertex.n_layer].remove(vertex)
      vertex.n_layer -= 1
      graph.layers[vertex.n_layer].append(vertex)

  def delay_vertex(self):
    pass
