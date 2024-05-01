import json

from src.mesh_loader.mesh_loader import load_curricular_mesh


def load_jsonfile(pathfile: str) -> dict:
  with open(pathfile, 'r') as json_file:
    data = json.load(json_file)

  return data


instance_pathfile = 'instances/example.json'

instance = load_jsonfile(instance_pathfile)

mesh = load_curricular_mesh(instance)

print()

