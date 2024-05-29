from collections import deque

from src.graph.graph_params import GraphParams
from src.graph.graph_traversal.graph_traversal import GraphTraversal
from src.graph.neighbors_generator.next_neighbors_generator import NextNeighborsGenerator
from src.graph.vertex import Vertex


class Graph:
  def __init__(self, layers: [[Vertex]], vertices_set: dict[Vertex], params: GraphParams):
    self.layers: [[Vertex]] = layers
    self.vertices_set: dict = vertices_set
    self.params: GraphParams = params

  def get_critic_path(self) -> set[str]:
    critic_path_set = set()
    vertices_to_process = deque(self.layers[-1])

    GraphTraversal.backward(vertices_to_process, critic_path_set, self.params)
    return critic_path_set

  def compute_critical_score(self) -> None:
    for layer in self.layers:
      for vertex in layer:
        vertices_already_process = set()
        vertices_to_process = deque([vertex])
        GraphTraversal.forward(vertices_to_process, vertices_already_process, self.params)

        total_critical_score = len(vertices_already_process) - 1
        direct_critical_score = len(list(NextNeighborsGenerator(self.params).get_neighbors(vertex)))
        indirect_critical_score = total_critical_score - direct_critical_score

        vertex.direct_critical_score = direct_critical_score
        vertex.indirect_critical_score = indirect_critical_score

  def normalize_critical_score(self) -> None:
    total_critical_score = 0
    for layer in self.layers:
      for vertex in layer:
        total_critical_score += vertex.direct_critical_score + vertex.indirect_critical_score

    for layer in self.layers:
      for vertex in layer:
        total_critical_score_from_vertex = vertex.direct_critical_score + vertex.indirect_critical_score
        vertex.normalized_critical_score = total_critical_score_from_vertex / total_critical_score

  def update_critical_score(self) -> None:
    self.compute_critical_score()
    self.normalize_critical_score()
