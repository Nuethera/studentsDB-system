import pymongo
import os

myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient.StudentsDB
class3 = mydb.class3


