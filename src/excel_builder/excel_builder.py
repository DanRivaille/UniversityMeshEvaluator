import pandas as pd

from src.curricular_mesh.curricular_mesh import CurricularMesh
from src.graph.graph import Graph
from src.graph.vertex import Vertex
from src.utils.utils import compute_percentile


class ExcelBuilder:
  def __init__(self):
    self.excel_dataframe: pd.DataFrame | None = None

  def build_excel(self, mesh: CurricularMesh, graph: Graph, critic_path: set[str]):
    courses_title_column = []
    courses_id_column = []
    semester_column = []
    critic_path_column = []
    normalized_critic_score_column = []
    direct_critic_score_column = []
    indirect_critic_score_column = []
    total_critic_score_column = []
    n_courses = 0

    for index_semester, semester in enumerate(mesh.semesters):
      percentile_90 = compute_percentile(graph, index_semester, 90)

      for course in semester.courses:
        semester_column.append(f'{semester.num_semester} SEM {mesh.name}')
        courses_id_column.append(course.course_id)
        courses_title_column.append(course.course_title)
        critic_path_column.append('Si' if course.course_id in critic_path else 'No')

        vertex_of_course: Vertex = graph.vertices_set.get(course.course_id)
        direct_score_vertex = vertex_of_course.direct_critical_score
        indirect_score_vertex = vertex_of_course.indirect_critical_score
        direct_critic_score_column.append(direct_score_vertex)
        indirect_critic_score_column.append(indirect_score_vertex)
        total_critic_score_column.append(direct_score_vertex + indirect_score_vertex)
        normalized_critic_score_column.append(vertex_of_course.normalized_critical_score)

        n_courses += 1

    excel_info = {
      'PROGRAM': [mesh.program] * n_courses,
      'PROGRAM_DESC': [mesh.name] * n_courses,
      'CATALOG_ACADEMIC_PERIOD': [mesh.academic_catalog] * n_courses,
      'AREA_DESC': semester_column,
      'COURSE_IDENTIFICATION': courses_id_column,
      'COURSE_TITLE': courses_title_column,
      'CRITIC_PATH': critic_path_column,
      'NORMALIZED_CRITIC_SCORE': normalized_critic_score_column,
      'TOTAL_CRITIC_SCORE': total_critic_score_column,
      'DIRECT_CRITIC_SCORE': direct_critic_score_column,
      'INDIRECT_CRITIC_SCORE': indirect_critic_score_column
    }

    self.excel_dataframe = pd.DataFrame(data=excel_info)

  def save_excel(self, output_path: str):
    self.excel_dataframe.to_excel(output_path, index=False)
