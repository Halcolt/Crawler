import mysql.connector
from sklearn.cluster import KMeans
import numpy as np

# Connect to the MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Bill1567",
    database="crawler"
)

if(mydb):
    print("Connection Successful")
else:
    print("Connection Fail")

# Create a cursor object
mycursor = mydb.cursor()
#----------------------------------------------------------------------
#Update point for number of ppl
# Retrieve the data from the "Price" field
query = "SELECT MaxPeople FROM ProviderDriveOption"
mycursor.execute(query)
peoples = [peoples[0] for peoples in mycursor.fetchall()]

# Convert data to a NumPy array
peoples = np.sort(peoples, axis=0)
peoples = np.array(peoples).reshape(-1, 1)

# Cluster data using KMeans
kmeans = KMeans(n_clusters=5, n_init=5)
clusters = kmeans.fit_predict(peoples)

# Zip the data and labels together
clustered_data = list(zip(peoples, kmeans.labels_))

# sort the peoples and corresponding labels
sorted_peoples, sorted_labels = zip(*sorted(clustered_data, key=lambda x: x[0], reverse=True))

#Re-labeling so that both data "Price" and "label" are in ascending order
old_label = -1
new_label = 0
for i, (people, label) in enumerate(clustered_data):
    if label != old_label:
        old_label = label
        new_label += 1
        label = new_label
        clustered_data[i] = (people, label)
    else:
        label = new_label
        clustered_data[i] = (people, label)

# print the re-labeled data
for element in clustered_data:
    print(element, end='\n')

    # Iterate through the re-labeled data and update the "peoplePoint" field
for people, label in clustered_data:
    query = "UPDATE ProviderDriveOption SET PeoplePoint=%s WHERE MaxPeople = %s"
    values = (label, people[0])
    mycursor.execute(query, values)
    mydb.commit()

# Close the cursor and connection
mycursor.close()
mydb.close()