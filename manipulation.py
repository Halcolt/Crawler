import mysql.connector
from sklearn.cluster import KMeans
import numpy as np

def print_top_five(People,Money,Capacity):
    # Create a cursor object
    mycursor = mydb.cursor()
    #----------------------------------------------------------------------
    query = "UPDATE ProviderDriveOption SET AveragePoint = (PricePoint + PeoplePoint)/2"
    mycursor.execute(query)
    mydb.commit()
    mycursor.execute("""
    SELECT ProviderDriveOption.ProverderOpID, ProviderDriveOption.ProviderName, AVG(((PricePoint + PeoplePoint)/2 + GetAppPoint)/2) as average
    FROM ProviderDriveOption
    JOIN ProType ON ProType.ProviderName = ProviderDriveOption.ProviderName
    WHERE MaxPeople <= %s AND Price <= %s And Capacity >= %s
    GROUP BY ProviderDriveOption.ProverderOpID, ProviderDriveOption.ProviderName
    """, (People, Money,Capacity))

    result = mycursor.fetchall()
    if not result:
        print("There are no suitable provider for you now, please Re-Enter the value you want for Cloud option")
        mycursor.close()
        return

    update_list = []
    for row in result:
        proverder_op_id = row[0]
        provider_name = row[1]
        average = row[2]
        update_list.append((average, proverder_op_id, provider_name))

    update_list.sort(reverse=True, key=lambda x: x[0])
    top_five = update_list[:5]
    for avg, proverder_op_id, provider_name in top_five:
        print("Provider Name: {}, ProverderOpID: {}, Average: {}".format(provider_name, proverder_op_id, avg))

    mycursor.close()

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

print("If you NOT SURE how many or DON'T CARE of any question, press Enter\n")
try:
    People = int(input("Maximum people you work with \n(only you then enter 1): "))
except ValueError:
    People = 1000000
Money = int(input("The maximum amount of money you want to spend per_month per_person(in $): "))
if(People != 1000000):
    Money = Money*People
Capacity = int(input("Minimum capacity you need(in Gb): "))
print_top_five(People,Money,Capacity)

# Close the cursor and connection
mydb.close()