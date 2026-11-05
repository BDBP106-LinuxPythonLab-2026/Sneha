# (2) Gene Expression: Control vs Treated

import numpy as np
import matplotlib.pyplot as plt

genes = ["GAPDH", "ACTB", "TP53", "MYC", "EGFR"]

control = np.array([950, 1200, 310, 150, 420])

treated = np.array([940, 1180, 610, 75, 430])

# X positions
x = np.arange(len(genes))

width = 0.4

# Plot bars
fig, ax = plt.subplots()

ax.bar(x - width/2, control, width, label='Control',
       color='blue')

ax.bar(x + width/2, treated, width, label='Treated',
       color='orange')

# Set gene names
ax.set_xticks(x, labels=genes)

ax.set_xlabel('Genes')
ax.set_ylabel('Expression Level')
ax.set_title('Gene Expression: Control vs Treated')

ax.legend()
plt.show()

# Calculate fold change
fold_change = treated / control

print("Fold Change (Treated/Control):")

for gene, fc in zip(genes, fold_change):
    print(gene, ":", round(fc, 2))
