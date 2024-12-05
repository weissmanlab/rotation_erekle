# Adjusting both ANI and Genes Compared ranges to be consistent across both subplots
ani_range = (df["ANI"].min(), df["ANI"].max())
genes_range = (df["GenesCompared"].min(), df["GenesCompared"].max())

# Plot
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Hexbin for different CC (red scale)
hb1 = axes[0].hexbin(
    different_cc["ANI"], different_cc["GenesCompared"], gridsize=30, cmap="Reds", 
    extent=(ani_range[0], ani_range[1], genes_range[0], genes_range[1])
)
axes[0].set_title("Strains in Different CC")
axes[0].set_xlabel("ANI")
axes[0].set_ylabel("Genes Compared")
cb1 = fig.colorbar(hb1, ax=axes[0])
cb1.set_label("Count in bin (Red: Strains in different CC)")

# Hexbin for same CC (green scale)
hb2 = axes[1].hexbin(
    same_cc["ANI"], same_cc["GenesCompared"], gridsize=30, cmap="Greens", 
    extent=(ani_range[0], ani_range[1], genes_range[0], genes_range[1])
)
axes[1].set_title("Strains in Same CC")
axes[1].set_xlabel("ANI")
axes[1].set_ylabel("Genes Compared")
cb2 = fig.colorbar(hb2, ax=axes[1])
cb2.set_label("Count in bin (Green: Strains in the same CC)")

plt.tight_layout()
plt.show()
