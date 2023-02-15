import mysql.connector

# Connect to the MySQL server
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Bill1567",
        database="crawler"
    )

if(mydb):
    print("Connection Successful\n")
else:
    print("Connection Fail")
    exit()

# Create a cursor object to execute SQL statements
mycursor = mydb.cursor()

# Use the SELECT DISTINCT statement to retrieve unique values from the MOption column
mycursor.execute("SELECT DISTINCT MOption FROM MoreHostOption")

# Fetch the results using the cursor's fetchall() method
results = mycursor.fetchall()

# Iterate through the results and print each MOption value
print("Here is all the addition option we have in our database:\n")
for result in results:
    print("+ ",result[0])

