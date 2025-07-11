from itertools import product
import json
from pathlib import Path


if __name__ == "__main__":
    #wc_pairs = [(1.0, 0.0), (0.95, 0.05), (0.9, 0.1), (0.85, 0.15),(0.8, 0.2),(0.75, 0.25), (0.7, 0.3),(0.65, 0.35),(0.6, 0.4), (0.55, 0.45),  (0.5, 0.5) ]
    wc_pairs = [(0.24,0.76),(0.63,0.37),(0.57,0.43),(0.81,0.19),(0.69,0.31),(0.73,0.27),
    (0.43,0.57),(0.74,0.26),(0.73,0.27),(0.79,0.21),(0.71,0.29)]
    
    #coh_dict = { (0.9, 0.1, 0.9, 0.1),(0.8, 0.2, 0.8, 0.2), (0.7, 0.3, 0.7, 0.3), (0.6, 0.4, 0.6, 0.4), (0.5, 0.5, 0.5, 0.5),(0.4, 0.6, 0.4, 0.6), }
    coh_dict= {(0.75,0.25,0.3,0.7)}
    
    for wc_pair, coh_tup in product(wc_pairs, coh_dict):
        output_settings = dict(
            bloc_voter_prop={"W": wc_pair[0], "C": wc_pair[1]},
            cohesion_parameters={
                "W": {"W": coh_tup[0], "C": coh_tup[1]},
                "C": {"W": coh_tup[2], "C": coh_tup[3]},
            },
            alphas={"W": {"W": 1, "C": 0.5}, "C": {"W": 2, "C": 0.5}},
            slate_to_candidates={"W": ["W1", "W2","W3"], "C": ["C1", "C2","C3"]},
        )

        output_dir = Path("./vk_run_settings")
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = "." / Path(
            f"vk_run_settings/wc_({wc_pair[0]}_{wc_pair[1]})_cohesion_({coh_tup[0]}_{coh_tup[1]}_{coh_tup[2]}_{coh_tup[3]})".replace(
                ".", "p"
            )
            + ".json"
        )

        with open(output_path, "w") as f:
            json.dump(output_settings, f, indent=4)
