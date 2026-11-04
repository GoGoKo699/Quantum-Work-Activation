#!/usr/bin/env python3
"""Plot the saved numerical checks; no exponent fit or new simulation."""

import json
from collections import defaultdict
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parent
rows = json.loads((ROOT / "data" / "scaling.json").read_text())["results"]
FIGURES = ROOT / "figures"
FIGURES.mkdir(exist_ok=True)

plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False,
                     "pdf.fonttype": 42, "savefig.facecolor": "white"})
fig, axes = plt.subplots(1, 3, figsize=(12.6, 3.9), layout="constrained")
colors = ("#1565A6", "#D16A14")
markers = ("o", "s")

for axis, family, xkey, xlabel, title in (
    (axes[0], "rational_scaling", "n_delta_squared", r"$n\delta^2$", r"Fixed harmonic spectrum: $\alpha=2$"),
    (axes[1], "golden_convergent_window", "n_delta", r"$n\delta$", r"Fixed golden spectrum: $\alpha=\varphi$"),
):
    grouped = defaultdict(list)
    for row in rows:
        if row["family"] == family:
            grouped[row["delta"]].append(row)
    for index, (delta, group) in enumerate(grouped.items()):
        group.sort(key=lambda x: x[xkey])
        label = rf"$\delta={float(delta):.6g}$"
        axis.plot([x[xkey] for x in group], [x["fraction"] for x in group],
                  color=colors[index], marker=markers[index], lw=1.7, ms=6, label=label)
    axis.set_xlabel(xlabel)
    axis.set_title(title, fontsize=11, pad=11)
    axis.legend(frameon=False, fontsize=9, loc="lower right")
    axis.grid(axis="y", color="#DDE2E6", linewidth=0.6)
    axis.set_ylim(0, 1)

detuned = sorted((x for x in rows if x["family"] == "two_copy_detuning"), key=lambda x: float(x["delta"]))
axes[2].plot([float(x["delta"]) for x in detuned], [x["fraction"] for x in detuned],
             color="#287C63", marker="D", lw=1.7, ms=6)
axes[2].set_xscale("log", base=2)
axes[2].set_xticks([0.0125, 0.025, 0.05, 0.1], labels=["0.0125", "0.025", "0.05", "0.1"])
axes[2].set_xlabel(r"$\delta$")
axes[2].set_title(r"Two copies: $\alpha(\delta)=2+\delta/2$", fontsize=11, pad=11)
axes[2].set_ylim(0, 1)
axes[2].grid(axis="y", color="#DDE2E6", linewidth=0.6)
axes[2].text(0.5, 0.55, r"$W_2/(2w_\infty)\simeq0.434$", transform=axes[2].transAxes,
             ha="center", color="#235C4C", fontsize=10)
axes[0].set_ylabel(r"Extracted mean-work fraction $W_n/(n w_\infty)$")
for label, axis in zip(("A", "B", "C"), axes):
    axis.text(-0.10, 1.10, label, transform=axis.transAxes, fontsize=12, fontweight="bold")
fig.savefig(FIGURES / "work_scaling.png", dpi=180)
fig.savefig(FIGURES / "work_scaling.pdf")
plt.close(fig)
