import geopandas as gpd
import maup

precincts = gpd.read_file("Denver_all.geojson").to_crs(4269)
districts = gpd.read_file("denver_city_council.gpkg").to_crs(4269)

precincts_to_district_assignment = maup.assign(precincts, districts)
precincts["DISTRICT"] = precincts_to_district_assignment
print(precincts["DISTRICT"])

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 10))
precincts.plot(ax=ax, edgecolor="black", facecolor="none", linewidth=1)
ax.set_title("Denver Precincts")
ax.axis("off")
plt.savefig("precincts.png", dpi=300, bbox_inches="tight")

fig, ax = plt.subplots(figsize=(10, 10))
districts.plot(column="DIST_NUM", categorical=True, legend=True, ax=ax, edgecolor="black", linewidth=0.2)
ax.set_title("Denver City Council Districts")
ax.axis("off")
plt.savefig("districts.png", dpi=300, bbox_inches="tight")

fig, ax = plt.subplots(figsize=(10, 10))
precincts.plot(column="DISTRICT", categorical=True, legend=True, ax=ax, edgecolor="black", linewidth=0.2)
ax.set_title("Precincts by Assigned District")
ax.axis("off")
plt.savefig("precincts_by_district.png", dpi=300, bbox_inches="tight")

# this doesn't work because the precincts are too coarse and the districts are too squiggly
# to fix:
# disag from precincts to census blocks
# maup blocks -> districts
# check maup help
