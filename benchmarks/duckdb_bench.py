import time
from src.cfg import *
import duckdb

queries = [
    f"""SELECT "VendorID", COUNT(*)
        FROM "{tableName}" GROUP BY 1;""",
    f"""SELECT "passenger_count", AVG("total_amount")
       FROM "{tableName}" GROUP BY 1;""",
    f"""SELECT "passenger_count", EXTRACT(year FROM "tpep_pickup_datetime"), COUNT(*)
       FROM "{tableName}" GROUP BY 1, 2;""",
    f"""SELECT "passenger_count", EXTRACT(year FROM "tpep_pickup_datetime"), ROUND("trip_distance"), COUNT(*)
       FROM "{tableName}" GROUP BY 1, 2, 3 ORDER BY 2, 4 DESC;""",
]


def bench():
    timer_arr = [0] * len(queries)
    duckdb.install_extension("sqlite")
    db = duckdb.connect(f"data\\{fileDB}")
    for i in range(len(queries)):
        for j in range(10):
            start = time.perf_counter()
            db.execute(queries[i])
            finish = time.perf_counter()
            timer_arr[i] += finish - start
        timer_arr[i] = timer_arr[i] / 10
    db.close()
    return timer_arr