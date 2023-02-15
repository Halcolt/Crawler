import mysql.connector
from sklearn.cluster import KMeans
import numpy as np
import sqlite3

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

#drive
#---------------------------------
# Retrieve the data from the "Price" field
query = "SELECT GbPerPrice FROM ProviderDriveOption"
mycursor.execute(query)
prices = [price[0] for price in mycursor.fetchall()]

# Convert data to a NumPy array
prices = np.sort(prices, axis=0, kind='quicksort')[::-1]
prices = np.array(prices).reshape(-1, 1)

# Cluster data using KMeans
kmeans = KMeans(n_clusters=5, n_init=5)
clusters = kmeans.fit_predict(prices)

# Zip the data and labels together
clustered_data = list(zip(prices, kmeans.labels_))

# sort the prices and corresponding labels
sorted_prices, sorted_labels = zip(*sorted(clustered_data, key=lambda x: x[0], reverse=True))

#Re-labeling so that both data "Price" and "label" are in ascending order
old_label = -1
new_label = 0
for i, (price, label) in enumerate(clustered_data):
    if label != old_label:
        old_label = label
        new_label += 1
        label = new_label
        clustered_data[i] = (price, label)
    else:
        label = new_label
        clustered_data[i] = (price, label)

# print the re-labeled data
for element in clustered_data:
    print(element, end='\n')

    # Iterate through the re-labeled data and update the "PricePoint" field
for price, label in clustered_data:
    query = "UPDATE ProviderDriveOption SET PricePoint=%s WHERE ROUND(GbPerPrice, 7) = %s"
    values = (label, price[0])
    mycursor.execute(query, values)
    # Commit the changes to the database
    mydb.commit()

#----------------------------------------------------------------------
#Update point for number of ppl
# Retrieve the data from the "Price" field
query = "SELECT MaxPeople FROM ProviderDriveOption"
mycursor.execute(query)
peoples = [peoples[0] for peoples in mycursor.fetchall()]

# Convert data to a NumPy array
peoples = np.sort(peoples, axis=0)
#peoples = peoples.astype(int)
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
    #need to convert into int
    values = (label, int(people[0]))
    mycursor.execute(query, values)
    mydb.commit()

# Select all non-NULL values from GetAppPoint column
mycursor.execute("SELECT GetAppPoint FROM ProType WHERE GetAppPoint IS NOT NULL")

# Calculate the average of the selected values
result = mycursor.fetchall()
total = sum([row[0] for row in result])
num_values = len(result)
average = total / num_values

# Replace all NULL values with the calculated average
mycursor.execute("UPDATE ProType SET GetAppPoint = %s WHERE GetAppPoint IS NULL", (average,))
mydb.commit()


mycursor.execute("UPDATE ProviderDriveOption SET AveragePoint = (PricePoint + PeoplePoint)/2")
mydb.commit()

# Close the cursor and connection
mycursor.close()
mydb.close()