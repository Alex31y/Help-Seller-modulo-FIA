import csv
import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='helpseller',
                                         user='root',
                                         password='root')

    sql_select_Query = "select * from recensione"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    print("Total number of rows in table: ", cursor.rowcount)

    print("\nPrinting each row")
    for row in records:
        print("Id = ", row[0], )
        print("testo = ", row[1])
        print("voto  = ", row[2])
        print("idProdotto  = ", row[4])
        print("idDistributore  = ", row[5], "\n")

except mysql.connector.Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if connection.is_connected():
        connection.close()
        cursor.close()
        print("MySQL connection is closed")

        # Create the csv file
        with open('bigData.csv', 'w', newline='') as f_handle:
            writer = csv.writer(f_handle)
            # Add the header/column names
            header = ['id', 'testo', 'voto', 'data', 'idProdotto', 'idDistributore']
            writer.writerow(header)
            # Iterate over `data`  and  write to the csv file
            for row in records:
                writer.writerow(row)
