import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://<username>:<password>@30daysofpython.vwfjxjl.mongodb.net/?appName=30DaysOfPython"

# Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

from flask import Flask, render_template
import os
MONGODB_URI = 'mongodb+srv://<username>:<password>@30daysofpython.vwfjxjl.mongodb.net/?appName=30DaysOfPython'
client = pymongo.MongoClient(MONGODB_URI)
# print(client.list_database_names())

#create database
db = client.thirty_days_of_python

# #create students collection and insert
# db.students.insert_one({'name': 'Kaziu', 'country': 'Poland', 'city': 'Poznan', 'age': 20})
# # print(client.list_database_names)


#inserting many students at once
students = [
        {'name':'David','country':'UK','city':'London','age':34},
        {'name':'John','country':'Sweden','city':'Stockholm','age':28},
        {'name':'Sami','country':'Finland','city':'Helsinki','age':25},
    ]

# for student in students:
#     db.students.insert_one(student)


#find_one() = SELECT in SQL - first entry
# student = db.students.find_one()
# print(student) #{'_id': ObjectId('69039440929597ab7f251438'), 'name': 'Kaziu', 'country': 'Poland', 'city': 'Poznan', 'age': 20}


#find() - returns all entries
# students = db.students.find()
# for student in students:
#     print(student)


# query = {'country': 'Poland'}   #we can use modifiers - country, city ext. we can also use a few modifiers at once with , 
# students = db.students.find(query)
# for student in students:
#     print(student)


#by default sort in ascending order, we can add parameters
# students = db.students.find().sort('name')
# for student in students:
#     print(student)

# students = db.students.find().sort('name',-1)
# for student in students:
#     print(student)

# students = db.students.find().sort('age')
# for student in students:
#     print(student)

# students = db.students.find().sort('age',-1)
# for student in students:
#     print(student)



#update with query - set
# query = {'age':250}
# new_value = {'$set':{'age':38}}

# db.students.update_one(query, new_value)
# for student in db.students.find():
#     print(student)


#drop - deletes a collection
db.students.drop()

app = Flask(__name__)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

