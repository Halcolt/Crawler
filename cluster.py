
import numpy as np
from sklearn.cluster import KMeans

# Load data from file
with open('data.txt', 'r') as f:
    data = [float(line) for line in f]

# Convert data to a NumPy array
data = np.array(data).reshape(-1, 1)

# Cluster data using K-Means
kmeans = KMeans(n_clusters=5, n_init=5)

# Fit and predict the cluster labels for the data
labels = kmeans.fit_predict(data)
print(labels)
# Zip the data and labels together
clustered_data = zip(data, labels)

# Sort the data by value
sorted_data = sorted(clustered_data, key=lambda x: x[0])

for element in sorted_data:
    print(element, end='\n')


# Print the sorted list
#print(sorted_data)

"""
# Assign labels to the data in order
labels = []
for i, (value, _) in enumerate(sorted_data):
    labels.append(i)

# Print out the data with labels
for (value, _), label in zip(sorted_data, labels):
    print(f'{value[0]: f} : {label}')
"""