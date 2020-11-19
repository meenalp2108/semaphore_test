
from flask import Flask, request
from flask_cors import CORS
import pyodbc
import json

app = Flask(__name__)
@app.route("/")

def index():
    return "Hello, World !"
    
def new_function():
    return 2 + 3

@app.route('/get_data_test_val', methods=['POST'])
def get_data_test_val():
    #data = (request.get_data()).decode()
    #request_input_data = json.loads(data)
    #db_string = 'Driver=SQL Server;Server=15.206.26.2;Database=PSS_SEGMENT4_Aug2020;uid=service;pwd=service@123;Trusted_Connection=no;integratedSecurity=false'
    #conn = pyodbc.connect(db_string)
    #cursor = conn.cursor()
    #cursor.execute('select min(starttime) from AugmentedStateTransactions')
    #return_list = list(cursor.fetchall())
    return 'ok'

if __name__ == "__main__":
   app.run(debug=False, port=4000, host='0.0.0.0')

