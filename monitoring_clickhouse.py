import time
import clickhouse_driver

# Connect to ClickHouse
conn = clickhouse_driver.connect(
    host='localhost',
    port=9000,
    user='default',
    password='',
    database='default'
)

# Queries to get various metrics
queries = [
    {
        'name': 'Query execution time',
        'query': 'SELECT avg(query_time) as avg_query_time FROM system.metrics WHERE event_date = today()',
    },
    {
        'name': 'Read operations',
        'query': 'SELECT sum(read_rows) as total_read_rows FROM system.metrics WHERE event_date = today()',
    },
    {
        'name': 'Written data size',
        'query': 'SELECT sum(written_bytes) as total_written_bytes FROM system.metrics WHERE event_date = today()',
    },
    {
        'name': 'Memory usage',
        'query': 'SELECT avg(memory_usage_physical) as avg_memory_usage FROM system.metrics WHERE event_date = today()',
    },
    {
        'name': 'CPU usage',
        'query': 'SELECT avg(cpu_user) as avg_cpu_user, avg(cpu_system) as avg_cpu_system FROM system.metrics WHERE event_date = today()',
    },
]

while True:
    for metric in queries:
        cursor = conn.cursor()
        cursor.execute(metric['query'])

        result = cursor.fetchone()

        if metric['name'] == 'Query execution time':
            print(f"Avg. query execution time: {result[0]}")
        elif metric['name'] == 'Read operations':
            print(f"Total read operations: {result[0]}")
        elif metric['name'] == 'Written data size':
            print(f"Total written data size: {result[0]}")
        elif metric['name'] == 'Memory usage':
            print(f"Avg. memory usage: {result[0]}")
        elif metric['name'] == 'CPU usage':
            print(f"Avg. CPU usage (user): {result[0]}, (system): {result[1]}")

    # Wait for 5 seconds before running the queries again
    time.sleep(5)
