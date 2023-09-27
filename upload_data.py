
from pymongo.mongo_client import MongoClient
import pandas as pd
import json
#uniform resource identifier
uri = "mongodb+srv://aasheshkaran20:capbottle@cluster0.olqizwt.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

#create database name and collection name
DATABASE_NAME = "PWProject"
COLLECTION_NAME = "waferfault"

#read data as a dataframe\
df = pd.read_csv("F:\Data Science Projects\Sensor Fault Detection\Notebooks\wafer_23012020_041211.csv")
df = df.drop('Unnamed: 0', axis = 1)

#convert the data into json
json_record = list(json.loads(df.T.to_json()).values())

#now dump the data into the dataabase
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
