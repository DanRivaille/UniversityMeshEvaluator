from src.graph.vertex import Vertex


class CurricularGraph:
  def __init__(self, semesters: [[Vertex]]):
    self.semesters: [[Vertex]] = semesters
