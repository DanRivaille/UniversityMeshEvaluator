from collections import deque

from src.graph.neighbors_generator.neighbors_generator import NeighborsGenerator
from src.graph.neighbors_generator.next_neighbors_generator import NextNeighborsGenerator
from src.graph.neighbors_generator.prev_neighbors_generator import PrevNeighborsGenerator
from src.graph.vertex import Vertex


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


class GraphTraversal:
  @staticmethod
  def backward(vertices_to_process: deque, vertices_already_process: set, check_continuity: bool) -> None:
    depth_first_search(vertices_to_process, vertices_already_process, PrevNeighborsGenerator(check_continuity))

  @staticmethod
  def forward(vertices_to_process: deque, vertices_already_process: set, check_continuity: bool) -> None:
    depth_first_search(vertices_to_process, vertices_already_process, NextNeighborsGenerator(check_continuity))
