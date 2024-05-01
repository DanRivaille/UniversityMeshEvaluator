from src.graph.vertex import Vertex


class Graph:
  def __init__(self, layers: [[Vertex]], vertices_set: dict[Vertex]):
    self.layers: [[Vertex]] = layers
    self.vertices_set: dict = vertices_set
