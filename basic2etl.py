

import pandas as pd
import openpyxl 
from tabulate import tabulate
from sqlalchemy import create_engine
import pymysql


# Example: Extract data from a CSV file
file_path= r"D:\internshipwork\webscraping\linkedin20.xlsx"
df = pd.read_excel(file_path, sheet_name='sheet1')

print(tabulate(df, headers='keys', tablefmt='pretty'))
col=df.columns
print(col)
print(tabulate(df))
'''
rows=len(df)
print(rows)

df = df.sort_values(by=['company', 'title'], ascending=[True, True])
print(tabulate(df))

df=df.fillna('NaN')
df['S.No'] = pd.RangeIndex(start=1, stop=1899, step=1)
print(tabulate(df))

#df=df[df['company'] != 'Texas Instruments']
#print(df)

#df['company']=df['company'].replace('Wipro', 'Nokia')
#print(tabulate(df))

rows = len(df)
print(rows)



#df_sorted = df.sort_values(by='company', ascending=True)
#print(tabulate(df_sorted)

#with pd.ExcelWriter('loading1.xlsx') as writer:
 #   df.to_excel(writer, sheet_name = 'company')

'''

import mysql.connector
connection  = mysql.connector.connect(host = 'localhost', password = 'Sarath@1', user = 'root')
if connection.is_connected:
    print("Success")

cur = connection.cursor()  
query = "show databases;"
cur.execute(query) 
database = cur.fetchall() 
      
for db in database: 
    print(db)
query = "use etl;"
cur.execute(query)

create_table_query = "CREATE TABLE IF NOT EXISTS linkedin040720241 (S_no INT PRIMARY KEY,job_title VARCHAR(255), Company_name VARCHAR(255), location VARCHAR(255),hiring_information VARCHAR(255),posted_when VARCHAR(255));"

cur.execute(create_table_query)

query = "show tables;"
cur.execute(query) 
table = cur.fetchall() 
      
for tab in table: 
    print(tab)
    

try:
    # Iterate over DataFrame rows
    for index, row in df.iterrows():
        # SQL query to insert row into 'company_data' table
        sql = "INSERT INTO linkedin040720241(S_no, job_title, company_name, location, hiring_information, posted_when ) VALUES (%s, %s, %s ,%s, %s , %s)"
        # Execute the SQL query
        cur.execute(sql, tuple(row))
        # Commit changes to the database
        connection.commit()
    print("Data inserted successfully!")
    
except Exception as e:
    print(f"Error inserting data: {str(e)}")
    # Rollback changes if an error occurs
    connection.rollback()

finally:
    # Close cursor and connection
    cur.close()
    connection.close()


    

# Create a SQLAlchemy engine
# Replace 'username', 'password', 'localhost', '3306', and 'mydatabase' with your actual database credentials
#

# Load DataFrame into SQL table named 'my_table'
# if_exists='replace' will replace the table if it already exists
#df.to_sql('my_table', con=engine, index=False, if_exists='replace')

print("DataFrame loaded into SQL database successfully.")
