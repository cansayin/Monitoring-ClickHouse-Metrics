# Monitoring-ClickHouse-Metrics
Python script to monitoring metrics in ClickHouse


Download file and edit following rows
<pre id="example"><code class="language-lang"  style="color: #333; background: #f8f8f8;"> 
conn = clickhouse_driver.connect(
    host='localhost',
    port=9000,
    user='default',
    password='',
    database='default'
)
</code></pre>

Run the script
<pre id="example"><code class="language-lang"  style="color: #333; background: #f8f8f8;"> 
python monitoring_clickhouse.py

or

python3 monitoring_clickhouse.py
</code></pre>

