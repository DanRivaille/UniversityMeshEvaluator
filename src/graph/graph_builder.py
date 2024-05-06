from src.curricular_mesh.course import Course
from src.curricular_mesh.curricular_mesh import CurricularMesh
from src.curricular_mesh.semester import Semester
from src.graph.graph import Graph
from src.graph.vertex import Vertex


def build_layer_from_semester(semester: Semester, vertices_set: dict[Vertex]) -> [Vertex]:
  new_layer = []

  for course in semester.courses:
    vertex_id = course.course_id

    if vertex_id not in vertices_set:
      vertices_set[vertex_id] = create_new_vertex(course, semester.num_semester, vertices_set)

    new_layer.append(vertices_set[vertex_id])

  return new_layer


def create_new_vertex(course: Course, n_semester: int, vertices_set: dict[Vertex]) -> Vertex:
  vertex_id = course.course_id
  prev_vertices = []
  next_vertices = []

  new_vertex = Vertex(vertex_id, n_semester - 1, prev_vertices, next_vertices)

  for prerequisite in course.prerequisites:
    prerequisite_id = prerequisite.cod_prerequisite

    vertex_previous = vertices_set[prerequisite_id]
    prev_vertices.append(vertex_previous)

    vertex_previous.next.append(new_vertex)

  return new_vertex


class GraphBuilder:
  @staticmethod
  def build_from_mesh(mesh: CurricularMesh, check_continuity: bool) -> Graph:
    vertices_set: dict[Vertex] = dict()
    layers = []

    for semester in mesh.semesters:
      new_layer = build_layer_from_semester(semester, vertices_set)
      layers.append(new_layer)

    return Graph(layers, vertices_set,check_continuity)
