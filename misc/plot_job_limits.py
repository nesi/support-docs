#!/usr/bin/env python3


# Makes a silly lil' plot.


import numpy as np
import matplotlib.pyplot as plt

# Limits
MAX_NODES = 10
MAX_DAYS = 21
MAX_NODE_DAYS = 21

SAVE_PATH = "docs/assets/images/job_limits.png"
plt.rcParams.update({'font.size': 20})
# Domain for plotting
days = np.linspace(0.01, MAX_DAYS, 500)
node_limit_curve = MAX_NODE_DAYS / days

# Clip the curve to max nodes (so the region is bounded)
node_limit_curve_clipped = np.minimum(node_limit_curve, MAX_NODES)

fig, ax = plt.subplots(figsize=(8,6))

# Too many nodes (nodes > 10)
ax.fill_between(
    days,
    MAX_NODES,
    15,
    where=(days >= 0),
    alpha=0.3,
    color='red',
)

# Too many days (days > 21)
ax.axvspan(
    MAX_DAYS,
    MAX_DAYS + 2,
    alpha=0.3,
    color='red',
)

# Too many node-days (above the curve)
ax.fill_between(
    days,
    node_limit_curve_clipped,
    15,                 # extend high visually
    where=node_limit_curve_clipped < 15,
    alpha=0.2,
    color='yellow',
)

ax.plot(days, node_limit_curve_clipped)
ax.axhline(MAX_NODES, color="red",)
ax.axvline(MAX_DAYS, color="red")

# Labels
ax.text(10, 10.3, "Too Large", color="red")
ax.text(21.4, 4, "Too Long", color="red", rotation='vertical')
ax.text(8, 6, "Too many\nnode-days", color=(0.7, 0.7, 0), fontsize=24)

# Axes

xticks = list(ax.get_xticks())
xticks[-2] = MAX_DAYS
ax.set_xticks(sorted(xticks))

ax.set_xlim(0, MAX_DAYS + 2)
ax.set_ylim(0, MAX_NODES + 1)
ax.set_xlabel("Days")
ax.set_ylabel("Nodes")
ax.grid(True)

plt.tight_layout()
plt.savefig(SAVE_PATH, dpi=200)
plt.close()
