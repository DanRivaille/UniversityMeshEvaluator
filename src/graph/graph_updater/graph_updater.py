from src.graph.graph import Graph
from src.graph.vertex import Vertex


class GraphUpdater:
  def __init__(self, check_continuity: bool):
    self.check_continuity: bool = check_continuity

  def advance_vertex(self, graph: Graph, vertex_id: str):
    vertex: Vertex = graph.vertices_set.get(vertex_id, None)

    if vertex.n_layer > 0:
      graph.layers[vertex.n_layer].remove(vertex)
      vertex.n_layer -= 1
      graph.layers[vertex.n_layer].append(vertex)

  def delay_vertex(self, graph: Graph, vertex_id: str):
    vertex: Vertex = graph.vertices_set.get(vertex_id, None)

  @staticmethod
  def update_delayed_vertex(graph: Graph, vertex: Vertex):
    graph.layers[vertex.n_layer].remove(vertex)

    vertex.n_layer += 1
    if vertex.n_layer == len(graph.layers):
      graph.layers.append([])

    graph.layers[vertex.n_layer].append(vertex)
