class Vertex:
  def __init__(self, vertex_id: str, prev_vertices: [], next_vertices: []):
    self.id: str = vertex_id
    self.prev: [Vertex] = prev_vertices
    self.next: [Vertex] = next_vertices
