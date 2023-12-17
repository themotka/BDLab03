# Postgres
inNeedToCreatePG = False
tableName = "db"
usernamePG = "postgres"
passwordPG = "themotka"
hostnamePG = "localhost"
portPG = "5432"
dbPG = "taxi"
postgres = f"postgresql://{usernamePG}:{passwordPG}@{hostnamePG}:{portPG}/{dbPG}"

# data folder (must be created)
inNeedToCreateDB = False
fileDB = "tiny_taxi.db"
fileCSV = "tiny_data.csv"