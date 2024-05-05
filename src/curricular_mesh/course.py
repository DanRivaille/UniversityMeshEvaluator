from src.curricular_mesh.prerequisite import Prerequisite


class Course:
  def __init__(self, course_id: str, course_title: str, prerequisites: [Prerequisite]):
    self.course_id: str = course_id
    self.course_title: str = course_title
    self.prerequisites: [Prerequisite] = prerequisites

  def __str__(self) -> str:
    return self.course_id

  def __repr__(self) -> str:
    return self.course_id
