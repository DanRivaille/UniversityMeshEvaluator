import json

from src.graph.graph_builder import GraphBuilder
from src.graph.graph_params import GraphParams
from src.graph.graph_updater.graph_updater import GraphUpdater
from src.mesh_loader.mesh_loader import load_curricular_mesh


def load_jsonfile(pathfile: str) -> dict:
  with open(pathfile, 'r', encoding='UTF-8') as json_file:
    data = json.load(json_file)

  return data


instance_pathfile = 'instances/example.json'

instance = load_jsonfile(instance_pathfile)

mesh = load_curricular_mesh(instance)

params = GraphParams(True, 1)
graph = GraphBuilder.build_from_mesh(mesh, params)

#GraphUpdater(True).advance_vertex(graph, 'F')
GraphUpdater.update_delayed_vertex(graph, graph.vertices_set.get('M'))

critic_path = graph.get_critic_path()

print(critic_path)

graph.update_critical_score()

print()

