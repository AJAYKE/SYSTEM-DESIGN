import random
import string
import time

import pyodbc
import redis

# Connect to Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

conn_str = (
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'DATABASE=test;'
    'UID=sa;'
    'PWD=reallyStrongPwd123'
)

# Connect to Azure SQL Edge
try:
    sql_conn = pyodbc.connect(conn_str)
    cursor = sql_conn.cursor()

    cursor.execute("IF OBJECT_ID('test_table', 'U') IS NOT NULL DROP TABLE test_table")
    cursor.execute("CREATE TABLE test_table (key NVARCHAR(50), value NVARCHAR(50))")
    sql_conn.commit()
except pyodbc.Error as ex:
    print("Error in connection: ", ex)

# Function to generate random strings
def random_string(length=10):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

# Performance test for Redis
def test_redis(n=1000):
    start_time = time.time()
    for _ in range(n):
        key = random_string()
        value = random_string()
        redis_client.set(key, value)
        redis_client.get(key)
    end_time = time.time()
    return end_time - start_time

# Performance test for SQL
def test_sql(n=1000):
    start_time = time.time()
    for _ in range(n):
        key = random_string()
        value = random_string()
        cursor.execute("INSERT INTO test_table (key, value) VALUES (?, ?)", (key, value))
        cursor.execute("SELECT value FROM test_table WHERE key=?", (key,))
        cursor.fetchone()
    sql_conn.commit()
    end_time = time.time()
    return end_time - start_time

# Number of operations to test
num_operations = 1000

# Measure performance
redis_time = test_redis(num_operations)
sql_time = test_sql(num_operations)

print(f"Time taken for {num_operations} set and fetch operations:")
print(f"Redis: {redis_time:.2f} seconds")
print(f"SQL: {sql_time:.2f} seconds")

# Clean up
cursor.execute("DROP TABLE test_table")
sql_conn.close()
redis_client.flushdb()
