# Postgres
usernamePG = "postgres"
passwordPG = "themotka"
hostnamePG = "localhost"
portPG = "5432"
dbPG = "taxi"
postgres = f"postgresql://{usernamePG}:{passwordPG}@{hostnamePG}:{portPG}/{dbPG}"

# data folder (must be created)
fileDB = "tiny_taxi.db"
fileCSV = "tiny_data.csv"

# for both local and postgres
tableName = "db"

# benchmark configuration
inNeedToCreatePG = False
inNeedToCreateDB = False
inNeedToTestPsycorg2 = True
inNeedToTestSQLite = True
inNeedToTestDuckDB = True

