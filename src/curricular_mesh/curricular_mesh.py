from src.curricular_mesh.semester import Semester


class CurricularMesh:
  def __init__(self, name: str, academic_catalog: str, program: str, semesters: [Semester]):
    self.name = name
    self.academic_catalog = academic_catalog
    self.program = program
    self.semesters = semesters

  def __str__(self) -> str:
    return self.name

  def __repr__(self) -> str:
    return f'{self.program}-{self.academic_catalog}'
