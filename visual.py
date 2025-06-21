import glob
import json
import matplotlib.pyplot as plt
import re
from collections import defaultdict

def parse_filename(filename):
    # Extract metadata from filename
    pattern = r'^(plurality|stv)_([\w]+(?:_[\w]+)*)_voters.*?_wc_\(([\dp\.p]+)_([\dp\.p]+)\)'
    match = re.search(pattern, filename)
    if not match:
        return None
    method, label, w1, w2 = match.groups()
    w1 = float(w1.replace('p', '.'))
    w2 = float(w2.replace('p', '.'))
    x = 0.25 * w1 + 0.7 * w2
    return method, label.replace('_', ' '), x

def count_c_winners(filepath):
    count = 0
    with open(filepath) as f:
        for line in f:
            winners = json.loads(line)["winners"]
            count += sum(1 for w in winners if w.startswith("C"))
    return count / 10  # assuming 10 lines per file

data = defaultdict(list)

for filepath in glob.glob("parallel_plan_all/Parallel_runs/results/*.jsonl"):
    parsed = parse_filename(filepath)
    if not parsed:
        continue
    method, label, x = parsed
    y = count_c_winners(filepath)
    data[method].append((x, y, label))

from matplotlib.cm import get_cmap
from matplotlib.colors import ListedColormap

# Plotting and saving
for method in ["plurality", "stv"]:
    if method not in data:
        continue
    xs, ys, labels = zip(*data[method])
    unique_labels = sorted(set(labels))  # consistent order
    label_to_index = {lbl: i for i, lbl in enumerate(unique_labels)}
    indices = [label_to_index[lbl] for lbl in labels]
    cmap = get_cmap("tab10", len(unique_labels))

    fig, ax = plt.subplots()
    scatter = ax.scatter(xs, ys, c=indices, cmap=cmap)

    if method == "stv":
        method = "irv"

    ax.set_title(f"Simulated Denver City Council {method.upper()} Results (n={len(xs)})")
    ax.set_xlabel("Combined Support for Non-white Candidates")
    ax.set_ylabel("Proportion Non-white Candidate Winners")

    handles = [plt.Line2D([0], [0], marker='o', color='w',
               label=lbl, markerfacecolor=cmap(i), markersize=10)
               for lbl, i in label_to_index.items()]
    ax.legend(handles=handles, title="Label")
    ax.grid(True)

    fig.savefig(f"{method}_scatterplot.png", dpi=300)
    plt.close(fig)
