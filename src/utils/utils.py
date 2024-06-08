import json


def load_jsonfile(pathfile: str) -> dict:
  with open(pathfile, 'r', encoding='UTF-8') as json_file:
    data = json.load(json_file)

  return data
