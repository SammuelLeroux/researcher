import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from distances import distance_jaccard

print(distance_jaccard("PLACE", "CRAIE"))
print(distance_jaccard("AVRIL", "LAIT"))
print(distance_jaccard("ESPOIR", "PROIE"))
print(distance_jaccard("STATUE", "ETAT"))
print(distance_jaccard("NOIR", "BLANC"))
print(distance_jaccard("OBTENIR", "ROBINET"))
print(distance_jaccard("CHIEN", "NICHE"))