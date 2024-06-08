from src.curricular_mesh.curricular_mesh import CurricularMesh
from src.utils.utils import load_jsonfile
from src.excel_builder.excel_builder import ExcelBuilder
from src.graph.graph_builder import GraphBuilder
from src.graph.graph_params import GraphParams
from src.mesh_loader.mesh_loader import load_curricular_mesh

# Check the graph updater implementation, it must be updated with the new period logic
# GraphUpdater(params).advance_vertex(graph, 'F')
# GraphUpdater.update_delayed_vertex(graph, graph.vertices_set.get('M'))


def evaluate_mesh(instance_pathfile: str) -> None:
  instance = load_jsonfile(instance_pathfile)

  mesh = load_curricular_mesh(instance)

  graph = GraphBuilder.build_from_mesh(mesh, GraphParams(True, extract_period(mesh)))
  critic_path = graph.get_critic_path()
  graph.update_critical_score()

  excel_builder = ExcelBuilder()
  excel_builder.build_excel(mesh, graph, critic_path)
  excel_builder.save_excel(instance_pathfile.replace('instances', 'output').replace('json', 'xlsx'))


def extract_period(mesh: CurricularMesh) -> int:
  if 'SEM' in mesh.semesters[0].area:
    period = 2
  elif 'TRI' in mesh.semesters[0].area:
    period = 3
  else:
    print("Semester's area invalid, the period is set to 1")
    period = 1

  return period
