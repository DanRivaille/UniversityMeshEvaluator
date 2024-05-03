class Vertex:
  def __init__(self, vertex_id: str, prev_vertices: [], next_vertices: []):
    self.id: str = vertex_id
    self.prev: [Vertex] = prev_vertices
    self.next: [Vertex] = next_vertices
    self.direct_critical_score = 0
    self.indirect_critical_score = 0

  def __str__(self) -> str:
    return self.id

  def __repr__(self) -> str:
    return f'Vertex({self.id})'

  @staticmethod
  def get_next_vertices(vertex):
    return vertex.next

  @staticmethod
  def get_prev_vertices(vertex):
    return vertex.prev
