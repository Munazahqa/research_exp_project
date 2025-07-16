from dis import hasconst
from django.db import models
#connecting to mongoDB
import pymongo
from pymongo.synchronous import mongo_client

#from db_connection import client
mongodb_url = "mongodb://localhost:27017"
client = pymongo.MongoClient(mongodb_url)
databaseconnecting = client["research"] #database
experiment_collection = databaseconnecting["experiment"] #collections


experiment_collection.create_index("experiment_id")


import psycopg2
#connecting to postgresql
def postgresql_connection():
    return psycopg2.connect(
        dbname = "new_research",
        user = "postgres",
        password="asCN@$31",
        host="127.0.0.1",
        port="5432"



    )
