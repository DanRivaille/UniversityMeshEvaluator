from collections import deque

from src.graph.vertex import Vertex


def backward(vertices_to_process: deque, vertices_already_process: set) -> None:
  depth_first_search(vertices_to_process, vertices_already_process, Vertex.get_prev_vertices)


def forward(vertices_to_process: deque, vertices_already_process: set) -> None:
  depth_first_search(vertices_to_process, vertices_already_process, Vertex.get_next_vertices)


def depth_first_search(vertices_to_process: deque, vertices_already_process: set, edges_generator) -> None:
  if not vertices_to_process:
    return

  current_vertex: Vertex = vertices_to_process.pop()
  vertex_id = current_vertex.id

  if vertex_id not in vertices_already_process:
    vertices_already_process.add(vertex_id)

  for prev_vertex in edges_generator(current_vertex):
    if prev_vertex.id not in vertices_already_process:
      vertices_to_process.append(prev_vertex)

  depth_first_search(vertices_to_process, vertices_already_process, edges_generator)


class Graph:
  def __init__(self, layers: [[Vertex]], vertices_set: dict[Vertex]):
    self.layers: [[Vertex]] = layers
    self.vertices_set: dict = vertices_set

  def get_critic_path(self) -> set[str]:
    critic_path_set = set()
    vertices_to_process = deque(self.layers[-1])

    backward(vertices_to_process, critic_path_set)

    return critic_path_set

  def update_critical_score(self) -> None:
    for layer in self.layers:
      for vertex in layer:
        vertices_already_process = set()
        vertices_to_process = deque([vertex])
        forward(vertices_to_process, vertices_already_process)

        total_critical_score = len(vertices_already_process) - 1
        direct_critical_score = len(vertex.next)
        indirect_critical_score = total_critical_score - direct_critical_score

        vertex.direct_critical_score = direct_critical_score
        vertex.indirect_critical_score = indirect_critical_score
