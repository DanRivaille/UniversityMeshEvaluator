from src.curricular_mesh.course import Course
from src.curricular_mesh.curricular_mesh import CurricularMesh
from src.curricular_mesh.prerequisite import Prerequisite
from src.curricular_mesh.semester import Semester


def load_curricular_mesh(json_mesh: dict) -> CurricularMesh:
  name = json_mesh.get('name')
  academic_catalog = json_mesh.get('academic_catalog')
  program = json_mesh.get('program')
  semesters = load_semesters_list(json_mesh)

  return CurricularMesh(name, academic_catalog, program, semesters)


def load_semesters_list(json_mesh: dict) -> [Semester]:
  semesters = []

  for current_semester_json in json_mesh.get('curricular_mesh', []):
    new_semester = load_semester(current_semester_json)
    semesters.append(new_semester)

  return semesters


def load_semester(semester_json: dict) -> Semester:
  num_semester = semester_json.get('semester')
  area = semester_json.get('area')
  area_desc = semester_json.get('area_desc')
  courses = load_courses_list(semester_json)

  return Semester(num_semester, area, area_desc, courses)


def load_courses_list(semester_json: dict) -> [Course]:
  courses = []

  for course_json in semester_json.get('courses', []):
    new_course = load_course(course_json)
    courses.append(new_course)

  return courses


def load_course(course_json: dict) -> Course:
  course_id = course_json.get('course_id')
  course_title = course_json.get('course_title')
  prerequisites = load_prerequisites(course_json)

  return Course(course_id, course_title, prerequisites)


def load_prerequisites(course_json: dict) -> [Prerequisite]:
  prerequisites = []

  for prerequisite_json in course_json.get('prerequisites', []):
    cod_prerequisite = prerequisite_json.get('cod_prereq')
    connector = prerequisite_json.get('connector')

    prerequisites.append(Prerequisite(cod_prerequisite, connector))

  return prerequisites
