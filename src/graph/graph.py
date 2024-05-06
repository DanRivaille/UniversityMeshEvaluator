from collections import deque

from src.graph.neighbors_generator.neighbors_generator import NeighborsGenerator
from src.graph.neighbors_generator.next_neighbors_generator import NextNeighborsGenerator
from src.graph.neighbors_generator.prev_neighbors_generator import PrevNeighborsGenerator
from src.graph.vertex import Vertex


def backward(vertices_to_process: deque, vertices_already_process: set, check_continuity: bool) -> None:
  depth_first_search(vertices_to_process, vertices_already_process, PrevNeighborsGenerator(check_continuity))


def forward(vertices_to_process: deque, vertices_already_process: set, check_continuity: bool) -> None:
  depth_first_search(vertices_to_process, vertices_already_process, NextNeighborsGenerator(check_continuity))


def depth_first_search(vertices_to_process: deque, vertices_already_process: set,
                       neighs_generator: NeighborsGenerator) -> None:
  if not vertices_to_process:
    return

  current_vertex: Vertex = vertices_to_process.pop()
  vertex_id = current_vertex.id

  if vertex_id not in vertices_already_process:
    vertices_already_process.add(vertex_id)

  for prev_vertex in neighs_generator.get_neighbors(current_vertex):
    if prev_vertex.id not in vertices_already_process:
      vertices_to_process.append(prev_vertex)

  depth_first_search(vertices_to_process, vertices_already_process, neighs_generator)


class Graph:
  def __init__(self, layers: [[Vertex]], vertices_set: dict[Vertex], check_continuity: bool):
    self.layers: [[Vertex]] = layers
    self.vertices_set: dict = vertices_set
    self.check_continuity: bool = check_continuity

  def get_critic_path(self) -> set[str]:
    critic_path_set = set()
    vertices_to_process = deque(self.layers[-1])

    backward(vertices_to_process, critic_path_set, self.check_continuity)
    return critic_path_set

  def update_critical_score(self) -> None:
    for layer in self.layers:
      for vertex in layer:
        vertices_already_process = set()
        vertices_to_process = deque([vertex])
        forward(vertices_to_process, vertices_already_process, self.check_continuity)

        total_critical_score = len(vertices_already_process) - 1
        direct_critical_score = len(list(NextNeighborsGenerator(True).get_neighbors(vertex)))
        indirect_critical_score = total_critical_score - direct_critical_score

        vertex.direct_critical_score = direct_critical_score
        vertex.indirect_critical_score = indirect_critical_score
