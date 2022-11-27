import pymongo
import os

myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient.StudentsDB
class2 = mydb.class2


