import json
import pymongo
from pymongo import MongoClient
import os
from core.classes import JsonApi


# database setup
password = os.environ.get("PW")
account = os.environ.get("ACCOUNT")
link = f"mongodb+srv://{account}:{password}@light-cube-cluster.5wswq.mongodb.net/sqcs?retryWrites=true&w=majority"
client = MongoClient(link)["sqcs-working"]

rsp = JsonApi().get_json('human')
