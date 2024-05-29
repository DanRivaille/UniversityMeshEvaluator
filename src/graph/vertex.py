class Vertex:
  def __init__(self, vertex_id: str, n_layer: int, prev_vertices: [], next_vertices: []):
    self.id: str = vertex_id
    self.n_layer: int = n_layer
    self.prev: [Vertex] = prev_vertices
    self.next: [Vertex] = next_vertices
    self.direct_critical_score: int = 0
    self.indirect_critical_score: int = 0
    self.normalized_critical_score: float = 0.0

  def __str__(self) -> str:
    return self.id

  def __repr__(self) -> str:
    return f'Vertex({self.id})'
