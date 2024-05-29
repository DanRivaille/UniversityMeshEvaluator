from collections import deque

from src.graph.graph import Graph
from src.graph.graph_params import GraphParams
from src.graph.graph_traversal.graph_traversal import GraphTraversal
from src.graph.vertex import Vertex


class GraphUpdater:
  def __init__(self, params: GraphParams):
    self.params: GraphParams = params

  def advance_vertex(self, graph: Graph, vertex_id: str):
    vertex: Vertex = graph.vertices_set.get(vertex_id, None)

    if vertex.n_layer > 0:
      graph.layers[vertex.n_layer].remove(vertex)
      vertex.n_layer -= 1
      graph.layers[vertex.n_layer].append(vertex)

  def delay_vertex(self, graph: Graph, vertex_id: str):
    vertex: Vertex = graph.vertices_set.get(vertex_id, None)

    vertices_to_update = set()
    vertices_to_process = deque([vertex])
    GraphTraversal.forward(vertices_to_process, vertices_to_update, self.params)

    for vertex_to_update in vertices_to_update:
      GraphUpdater.update_delayed_vertex(graph, vertex_to_update)

  @staticmethod
  def update_delayed_vertex(graph: Graph, vertex_id: str):
    vertex: Vertex = graph.vertices_set.get(vertex_id, None)
    graph.layers[vertex.n_layer].remove(vertex)

    vertex.n_layer += 1
    if vertex.n_layer == len(graph.layers):
      graph.layers.append([])

    graph.layers[vertex.n_layer].append(vertex)
