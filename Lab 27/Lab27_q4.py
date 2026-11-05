# (4) GC Content Distribution of Organisms

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(3)

organisms = [
    "E. coli",
    "S. cerevisiae",
    "P. falciparum",
    "S. coelicolor"
]

mean_gc = [51, 38, 19, 72]

# Create 2x2 subplot grid
fig, axes = plt.subplots(
    2, 2,
    sharex=True,
    sharey=True,
    figsize=(10, 8)
)

bins = np.arange(0, 101, 2)

# Plot histogram for each organism
for ax, organism, gc in zip(axes.flat, organisms, mean_gc):

    # Simulate GC values
    values = rng.normal(gc, 4, size=1000)

    # Draw histogram
    ax.hist(
        values,
        bins=bins,
        color='skyblue',
        edgecolor='black'
    )

    # Mark mean
    ax.axvline(gc, color='red', linestyle='--')

    ax.set_title(f'{organism} (Mean GC = {gc}%)')

# Label only outer axes
axes[1, 0].set_xlabel('GC Content (%)')
axes[1, 1].set_xlabel('GC Content (%)')

axes[0, 0].set_ylabel('Frequency')
axes[1, 0].set_ylabel('Frequency')

# Overall title
fig.suptitle('GC Content Distribution of Organisms', fontsize=14)

plt.tight_layout()

plt.show()
