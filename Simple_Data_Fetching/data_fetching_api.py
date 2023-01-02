from flask import Flask, request, jsonify
import mysql.connector as conn
import pymongo

app = Flask(__name__)

# Fetching data from sql database, (choosen mysql)
# choosen local database

@app.route('/mysql', methods =['POST'])
def fetch_data_from_mysql():
    mydb = conn.connect(host = 'localhost', user='root', password = 'root') # connecting with server
    cursor = mydb.cursor() # creating a cursor
    cursor.execute('use world') # selecting database
    cursor.execute('select * from world.country') # selecting data from a table
    return jsonify(cursor.fetchall()) # fetching & returning all data



# Fetching data from mongodb database
# For mongodb database virtural database is choosen
@app.route('/mongodb', methods = ['POST'])
def fetch_data_from_mongodb():
    # connecting with mongodb
    
    client = pymongo.MongoClient("mongodb+srv://project1:project1@project1.b8m3npm.mongodb.net/?retryWrites=true&w=majority")
    db = client['database1'] # accessing the database
    db_collection = db['first_collection'] # accessing collection

    data =  {"result": str(list(db_collection.find().limit(100)))} # getting data from collection 
    
    return data
    

if __name__ == '__main__':
    app.run()


# mongodb://localhost:27017