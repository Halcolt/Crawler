import mysql.connector
import numpy as np

def print_top_five_drive():
    try:
        People = int(input("Maximum people you work with \n(only you then enter 1): "))
    except ValueError:
        People = 1000000
    print("\n")
    try:
        Money = int(input("The maximum amount of money you want to spend per_month(in $): "))
    except:
        Money = 100000000
    print("\n")
    try:
        Capacity = int(input("Minimum capacity you need(in Gb): "))
    except:
        Capacity = 0
    print("\n")
    # Create a cursor object
    mycursor = mydb.cursor()
    #----------------------------------------------------------------------

    mydb.commit()
    mycursor.execute("""
    SELECT ProviderDriveOption.ProverderOpID, ProviderDriveOption.ProviderName, ProviderDriveOption.Price, ProviderDriveOption.Capacity, AVG(((PricePoint + PeoplePoint)/2 + GetAppPoint)/2) as average
    FROM ProviderDriveOption
    JOIN ProType ON ProType.ProviderName = ProviderDriveOption.ProviderName
    WHERE MaxPeople <= %s AND Price <= %s And Capacity >= %s
    GROUP BY ProviderDriveOption.ProverderOpID, ProviderDriveOption.ProviderName
    """, (People, Money, Capacity))

    result = mycursor.fetchall()
    if not result:
        print("There are no suitable provider for you now, please Re-Enter the value you want for Cloud option")
        mycursor.close()
        return

    update_list = []
    for row in result:
        proverder_op_id = row[0]
        provider_name = row[1]
        price = row[2]
        capacity = row[3]
        average = row[4]
        update_list.append((average, proverder_op_id, provider_name, price, capacity))

    update_list.sort(reverse=True, key=lambda x: x[0])
    top_five = update_list[:5]
    for avg, proverder_op_id, provider_name, price, capacity  in top_five:
        print("Provider Name: {}, ProverderOpID: {}, Price: {}, Capacity: {}, Average: {}".format(provider_name, proverder_op_id ,price, capacity , avg))
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
    exit()

print("If you NOT SURE how many or DON'T CARE of any question, press Enter\n")

print_top_five_drive()

# Close the cursor and connection
mydb.close()