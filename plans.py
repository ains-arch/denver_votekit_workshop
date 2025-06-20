import gerrychain
import geopandas
import pandas as pd
from gerrychain import Graph, Partition
from gerrychain.tree import recursive_tree_part
from gerrychain.updaters import Tally, cut_edges
import networkx as nx
import matplotlib.pyplot as plt

precincts = Graph.from_file("Denver_all.geojson")

print("Is this dual graph connected? ", nx.is_connected(precincts))
print("Number of Nodes: ", len(precincts.nodes()))
print("Number of Edges: ", len(precincts.edges()))
print(precincts.nodes()[0])

tot_pop = 0
for v in precincts.nodes():
    tot_pop = tot_pop + precincts.nodes()[v]['tot_pop_20']
for node, attr in precincts.nodes(data=True):
    attr["nonwhite_vap_20"] = attr["tot_vap_20"] - attr["white_vap_20"]

print("Total Population: ", tot_pop)

num_dist = 11
ideal_pop = tot_pop/num_dist
pop_tolerance = 0.05

records = []

for i in range(20):
    assignment = recursive_tree_part(precincts,
                                     range(num_dist),
                                     ideal_pop,
                                     'tot_pop_20',
                                     pop_tolerance,
                                     10) # 10 is the node repeats
    
    partition = Partition(
        precincts, # dual graph
        assignment = assignment,
        updaters={
            "WVAP": Tally("white_vap_20", alias="WVAP"),
            "C-VAP": Tally("nonwhite_vap_20", alias="C-VAP")
            }
        )

    for district in range(11):
        records.append({
            "plan": i,
            "district": district,
            "WVAP": partition["WVAP"][district],
            "C-VAP": partition["C-VAP"][district],
        })

# Output to CSV
df = pd.DataFrame(records)
df.to_csv("random_plans_wvap_cvap.csv", index=False)

# To read in

import pandas as pd

df = pd.read_csv("random_plans_wvap_cvap.csv")

# Group by plan and build the list of [WVAP, C-VAP] pairs for each district
result = []
for plan_id, group in df.groupby("plan"):
    values = group[["WVAP", "C-VAP"]].values.tolist()  # list of [WVAP, C-VAP]
    result.append(values)

# `result` is a list of plans, each plan is a list of 11 [WVAP, C-VAP] pairs
print(result)
