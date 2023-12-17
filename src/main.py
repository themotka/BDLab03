from cfg import *
import psycopg2 as pg
import pandas as pd
import sqlalchemy as sa
import sqlite3 as s3


def main():
    toRename, toRename1 = "tpep_pickup_datetime", "tpep_dropoff_datetime"
    engine = sa.create_engine(postgres)
    if inNeedToCreatePG:
        create_postgres(toRename, toRename1, engine)
    if inNeedToCreateDB:
        create_local_db(toRename, toRename1)


def create_postgres(toRename, toRename1, engine):
    db = pd.read_csv(f"data\\{fileCSV}")
    db[toRename] = pd.to_datetime(db[toRename])
    db[toRename1] = pd.to_datetime(db[toRename1])
    db.to_sql(tableName, engine, if_exists="replace", chunksize=1000, index=False)
    engine.dispose()


def create_local_db(toRename, toRename1):
    sqlite = s3.connect(f"data\\{fileDB}")
    db = pd.read_csv(f"data\\{fileCSV}")
    db[toRename] = pd.to_datetime(db[toRename])
    db[toRename1] = pd.to_datetime(db[toRename1])
    db.to_sql(fileDB, sqlite, if_exists="replace", chunksize=1000, index=False)
    sqlite.close()


if __name__ == "__main__":
    main()
