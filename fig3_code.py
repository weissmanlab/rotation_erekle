# Prepare data for bar chart visualization
overlap_summary = overlap_counts_df.sort_values(by='Shared Count', ascending=False)

# Plotting the bar chart for overlaps
plt.figure(figsize=(14, 6))
plt.bar(
    overlap_summary.apply(lambda x: f"{x['Original Cluster']} - {x['Reshuffled Cluster']}", axis=1),
    overlap_summary['Shared Count'],
    color='skyblue',
    edgecolor='black'
)
plt.title('Number of Overlapping Elements Between Cluster Pairs')
plt.xlabel('Cluster Pairs (Original - Reshuffled)')
plt.ylabel('Number of Shared Elements')
plt.xticks(rotation=90, fontsize=8, ha='center')
plt.tight_layout()

# Show the plot
plt.show()
