from flask import jsonify, request
from . import app1_blueprint

@app1_blueprint.route('/hello')
def hello_app1():
    return jsonify({"message": "Hello from App 1!"})

@app1_blueprint.route('/data', methods=['GET'])
def app1_data():
    data = {"key": "value from App 1"}
    return jsonify(data)


@app1_blueprint.route('/create', methods=['POST'])
def create_resource():

    data = request.get_json()

    if not data or 'name' not in data or 'age' not in data:
        return jsonify({"error": "Invalid input"}), 400

    new_resource = {
        "id": 1,  # Simulated auto-generated ID
        "name": data['name'],
        "age": data['age']
    }

    # Return success response
    return jsonify({
        "message": "Resource created successfully",
        "data": new_resource
    }), 201
    
    
    
@app1_blueprint.route('/update', methods=['PUT'])
def Update_resource():

    data = request.get_json()

    if not data or 'name' not in data or 'age' not in data or 'id' not in data:
        return jsonify({"error": "Invalid input"}), 400

    if data['id'] == 1:
        print("okk")
        pass
    
    new_resource = {
        "id": 1,  # Simulated auto-generated ID
        "name": data['name'],
        "age": data['age']
    }

    # Return success response
    return jsonify({
        "message": "Resource Update successfully",
        "data": new_resource
    }), 200