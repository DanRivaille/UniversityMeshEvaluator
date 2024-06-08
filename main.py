import sys

from src.mesh_evaluator import evaluate_mesh


instance_pathfile = sys.argv[1]

evaluate_mesh(instance_pathfile)
