import json

import numpy as np

from src.curricular_mesh.curricular_mesh import CurricularMesh
from src.graph.graph import Graph


def load_jsonfile(pathfile: str) -> dict:
  with open(pathfile, 'r', encoding='UTF-8') as json_file:
    data = json.load(json_file)

  return data


def compute_percentile(graph: Graph, index_semester: int, percentile: float) -> float:
  critic_scores = []

  for layer in graph.layers[index_semester:]:
    for vertex in layer:
      critic_scores.append(vertex.indirect_critical_score + vertex.direct_critical_score)

  return np.percentile(np.array(critic_scores), percentile)
