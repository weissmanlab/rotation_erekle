import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# Generate linkage matrix for average linkage
linkage_matrix_avg = linkage(condensed_dist_matrix, method='average')

# Create and save a high-resolution dendrogram
plt.figure(figsize=(30, 15), dpi=300)
dendrogram(linkage_matrix_avg, labels=points, leaf_rotation=90)
plt.title("Dendrogram for Agglomerative Clustering (Average Linkage) - High Resolution")
plt.xlabel("Points")
plt.ylabel("Distance")

# Save the dendrogram
plt.savefig("high_res_dendrogram_avg_linkage.png", format='png', bbox_inches='tight')
plt.show()
