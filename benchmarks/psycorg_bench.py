import time
from src.cfg import *
import psycopg2 as pg

db_params = {"dbname": dbPG,
             "user": usernamePG,
             "password": passwordPG,
             "host": hostnamePG,
             "port": portPG}

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
    connection = pg.connect(**db_params)
    cursor = connection.cursor()
    for i in range(len(queries)):
        for j in range(10):
            start = time.perf_counter()
            cursor.execute(queries[i])
            finish = time.perf_counter()
            timer_arr[i] += finish - start
        timer_arr[i] = timer_arr[i] / 10
    cursor.close()
    connection.close()
    return timer_arr
