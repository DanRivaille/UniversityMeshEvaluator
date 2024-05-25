from collections import deque

from src.graph.graph_params import GraphParams
from src.graph.neighbors_generator.neighbors_generator import NeighborsGenerator
from src.graph.neighbors_generator.next_neighbors_generator import NextNeighborsGenerator
from src.graph.neighbors_generator.prev_neighbors_generator import PrevNeighborsGenerator
from src.graph.vertex import Vertex


def depth_first_search(vertices_to_process: deque, vertices_already_process: set,
                       neighbors_generator: NeighborsGenerator) -> None:
  if not vertices_to_process:
    return

  current_vertex: Vertex = vertices_to_process.pop()
  vertex_id = current_vertex.id

  if vertex_id not in vertices_already_process:
    vertices_already_process.add(vertex_id)

  for prev_vertex in neighbors_generator.get_neighbors(current_vertex):
    if prev_vertex.id not in vertices_already_process:
      vertices_to_process.append(prev_vertex)

  depth_first_search(vertices_to_process, vertices_already_process, neighbors_generator)


class GraphTraversal:
  @staticmethod
  def backward(vertices_to_process: deque, vertices_already_process: set, params: GraphParams) -> None:
    depth_first_search(vertices_to_process, vertices_already_process, PrevNeighborsGenerator(params))

  @staticmethod
  def forward(vertices_to_process: deque, vertices_already_process: set, params: GraphParams) -> None:
    depth_first_search(vertices_to_process, vertices_already_process, NextNeighborsGenerator(params))
