import geopandas as gpd
import pandas as pd

# GeoPackage
print("\n--- denver_city_council.gpkg ---")
gdf = gpd.read_file("denver_city_council.gpkg")
print(gdf.info())
print(gdf.head())

# List of Parquet files
parquet_files = [
    "Denver_pop.parquet",
    "Denver_vap.parquet",
    "Denver_elections.parquet",
    "Denver_precincts.parquet",
]

for file in parquet_files:
    print(f"\n--- {file} ---")
    df = pd.read_parquet(file)
    print(df.info())
    print(df.head())

# Load and clean up keys on the other dataframes
def load_and_clean(path):
    df = pd.read_parquet(path)
    df = df.copy()
    df.index = df.index.str.replace("vtd:", "")
    return df

pop = load_and_clean("Denver_pop.parquet")
vap = load_and_clean("Denver_vap.parquet")
elections = load_and_clean("Denver_elections.parquet")

# Merge by matching 'GEOID20' in gdf to cleaned index
gdf = gdf.set_index("GEOID20")
merged = gdf.join([pop, vap, elections], how="left")

# Check result - haven't actually verified this yet
print(merged.info())
print(merged.head())

# Save
merged.to_file("merged_denver_precincts.gpkg", driver="GPKG")
