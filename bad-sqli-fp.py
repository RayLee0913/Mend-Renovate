import mysql.connector

## Define Function
def SELECT_ALL_FROM_TABLE(table_name):

    query = f"SELECT * FROM {table_name}"

    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="testuser",
        password="TestPassw0rd!",
        database="testdb",
        port=3306,
        autocommit=True
    )

    cursor = conn.cursor()

    cursor.execute(query)

    # print
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    table_name = input("table name > ")

    try:
        TBN = str(int(table_name))
        if len(TBN) <= 5:
            SELECT_ALL_FROM_TABLE(TBN)
        else:
            print("Table name is too long. Please enter a table name with 5 or fewer characters.")
    except ValueError:
        print("Invalid input. Please enter a valid table name.")
