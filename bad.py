import mysql.connector

if __name__ == "__main__":
    table_name = input("table name > ")
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

#     ----------------
# Language: Python
# Tested 1 project files
# Detected 2 findings (1 High, 1 Medium, 0 Low)

# ┌──────────┬─────────┬────────────────────────────────┬───────┐
# │ SEVERITY │   CWE   │       VULNERABILITY TYPE       │ COUNT │
# ├──────────┼─────────┼────────────────────────────────┼───────┤
# │ High     │ CWE-89  │ SQL Injection                  │     1 │
# ├──────────┼─────────┼────────────────────────────────┼───────┤
# │ Medium   │ CWE-798 │ Hardcoded Password/Credentials │     1 │
# └──────────┴─────────┴────────────────────────────────┴───────┘
