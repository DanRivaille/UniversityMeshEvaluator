import sys
import os

from src.mesh_evaluator import evaluate_mesh


instances_folder_path = sys.argv[1]

for filename in os.listdir(instances_folder_path):
  filepath = os.path.join(instances_folder_path, filename)
  if os.path.isfile(filepath):
    evaluate_mesh(filepath)
