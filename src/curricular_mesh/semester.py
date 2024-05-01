from src.curricular_mesh.course import Course


class Semester:
  def __init__(self, num_semester: int, area: str, area_desc: str, courses: [Course]):
    self.num_semester: int = num_semester
    self.area: str = area
    self.area_desc: str = area_desc
    self.courses: [Course] = courses

  def __str__(self) -> str:
    return self.area
