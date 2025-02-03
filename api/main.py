from functools import partial
from flask import Flask, jsonify, request
import boto3
from boto3.dynamodb.conditions import Key
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

# DynamoDB client
dynamodb = boto3.resource('dynamodb', region_name=os.getenv('REGION'))  # Cambia la región según tu configuración
table_name = os.getenv('TABLE_NAME')  # Cambia esto por el nombre de tu tabla

def scan_dynamodb_table(table):
    """Función pura para escanear una tabla DynamoDB."""
    response = table.scan()
    return response.get('Items', [])

# preconfigure database's table
scan_table = partial(scan_dynamodb_table, dynamodb.Table(table_name))

#api
@app.route('/prices', methods=['GET'])
def consulta_dynamodb():
    data = scan_table()
    sorted_data = sorted(data, key=lambda x: x['date'], reverse=True)
    return jsonify(sorted_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    app.run(debug=True)
