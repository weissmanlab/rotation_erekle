import seaborn as sns
import matplotlib.pyplot as plt

# Prepare data for heatmap
heatmap_data = overlap_counts_df.pivot(index='Original Cluster', 
                                       columns='Reshuffled Cluster', 
                                       values='Shared Count').fillna(0)

# Plot the heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_data, annot=True, fmt=".0f", cmap="Blues", cbar_kws={'label': 'Shared Elements'})
plt.title('Overlap Intensity Between Clusters (Original vs Reshuffled)')
plt.xlabel('Reshuffled Clusters')
plt.ylabel('Original Clusters')
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()

# Show the plot
plt.show()
