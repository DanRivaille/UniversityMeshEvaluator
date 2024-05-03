from collections import deque


from src.graph.vertex import Vertex


def backward(vertices_to_process: deque, critic_path_set: set):
  if not vertices_to_process:
    return

  current_vertex: Vertex = vertices_to_process.pop()
  vertex_id = current_vertex.id

  if vertex_id not in critic_path_set:
    critic_path_set.add(vertex_id)

  for prev_vertex in current_vertex.prev:
    if prev_vertex.id not in critic_path_set:
      vertices_to_process.append(prev_vertex)

  backward(vertices_to_process, critic_path_set)


class Graph:
  def __init__(self, layers: [[Vertex]], vertices_set: dict[Vertex]):
    self.layers: [[Vertex]] = layers
    self.vertices_set: dict = vertices_set

  def get_critic_path(self) -> set[str]:
    critic_path_set = set()
    vertices_to_process = deque(self.layers[-1])

    backward(vertices_to_process, critic_path_set)

    return critic_path_set
