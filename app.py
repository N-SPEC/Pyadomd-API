from sys import path
path.append('\\Program Files\\Microsoft.NET\\ADOMD.NET\\160')

from pyadomd import Pyadomd
from flask import Flask, jsonify

# Create a Flask app
app = Flask(__name__)

# Define an API endpoint
@app.route('/alpino')
def alpino():

# Connect to Power BI and execute query | Provide your Power-BI Connection String here
    conn_str = 'Provider=MSOLAP;User ID=Alexw@dettol.com;Data Source=powerbi://api.powerbi.com/v1.0/myorg/Power BI Model [Test];initial catalog=PBI_Model_20230121;Password=Alexw#2023;Persist Security Info=True;Impersonation Level=Impersonate;'
    query = 'EVALUATE ROW("ProjectRowCount",COUNTROWS(Project) )'

    with Pyadomd(conn_str) as conn:
        with conn.cursor().execute(query) as cur:
            data = cur.fetchall()
            column_names = [column[0] for column in cur.description]
            # Convert query result to a list of dictionaries
            result = [dict(zip(column_names, row)) for row in data]
            # Convert the list of dictionaries to a JSON string
            json_result = jsonify(result)
            return json_result

if __name__ == '__main__':
    app.run()
