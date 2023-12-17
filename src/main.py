from cfg import *
import pandas as pd
import sqlalchemy as sa
import sqlite3 as s3
from benchmarks import psycorg_bench, sqlite_bench, duckdb_bench


def main():
    if inNeedToCreatePG:
        to_date = "tpep_pickup_datetime"
        to_date1 = "tpep_dropoff_datetime"
        engine = sa.create_engine(postgres)
        create_postgres(to_date, to_date1, engine)
    if inNeedToCreateDB:
        to_date = "tpep_pickup_datetime"
        to_date1 = "tpep_dropoff_datetime"
        create_local_db(to_date, to_date1)
    if inNeedToTestPsycorg2: print(psycorg_bench.bench())
    if inNeedToTestSQLite: print(sqlite_bench.bench())
    if inNeedToTestDuckDB: print(duckdb_bench.bench())


def create_postgres(to_date, to_date1, engine):
    db = pd.read_csv(f"data\\{fileCSV}")
    db[to_date] = pd.to_datetime(db[to_date])
    db[to_date1] = pd.to_datetime(db[to_date1])
    db.to_sql(tableName, engine, if_exists="replace", chunksize=1000, index=False)
    engine.dispose()


def create_local_db(to_date, to_date1):
    sqlite = s3.connect(f"data\\{fileDB}")
    db = pd.read_csv(f"data\\{fileCSV}")
    db[to_date] = pd.to_datetime(db[to_date])
    db[to_date1] = pd.to_datetime(db[to_date1])
    db.to_sql(tableName, sqlite, if_exists="replace", chunksize=1000, index=False)
    sqlite.close()


if __name__ == "__main__":
    main()
