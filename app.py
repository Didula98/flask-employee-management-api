
# E/18/022
# AMARASINGHE D.I.
# CO528 - ASSIGNMENT 01

from flask import Flask, jsonify, request

app = Flask(__name__)

employees = [
    {"id": 1, "name": "Didula Induwara", "department": "HR", "position": "Manager"},
    {"id": 2, "name": "Anushanga Pavith", "department": "IT", "position": "Developer"},
    {"id": 3, "name": "Chamara Dilshan", "department": "Finance", "position": "Analyst"},
    {"id": 4, "name": "Chamudi Jayasumana", "department": "Marketing", "position": "Specialist"},
    {"id": 5, "name": "Ruchira Tharaka", "department": "Security", "position": "Officer"},
]



#------------------------ Create a new employee ------------------------
@app.route('/employees', methods=['POST'])
def create_employee():
    new_employee = request.get_json()

    # Check for empty input
    if not new_employee:
        return jsonify({"error": "No data provided"}), 400

    # Validate required fields
    if 'id' not in new_employee or 'name' not in new_employee or 'department' not in new_employee or 'position' not in new_employee:
        return jsonify({"error": "Missing required fields: id, name, department, position"}), 400

    # Check ID
    if any(employee['id'] == new_employee['id'] for employee in employees):
        return jsonify({"error": "An employee with this ID already exists"}), 400

    # Add new employee
    employees.append(new_employee)
    return jsonify(new_employee), 201



#------------------------ Read all employees ------------------------
@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)



#---------------------- Read a specific employee by ID ------------------------
@app.route('/employees/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    employee = next((emp for emp in employees if emp['id'] == employee_id), None)
    
    if employee:
        return jsonify(employee)
    else:
        return jsonify({"error": "Employee not found"}), 404



#------------------------ Update an existing employee ------------------------
@app.route('/employees/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    updated_data = request.get_json()

    # Find the employee to update
    employee = next((emp for emp in employees if emp['id'] == employee_id), None)

    if not employee:
        return jsonify({"error": "Employee not found"}), 404

    # Check ID
    if 'id' in updated_data and updated_data['id'] != employee_id:
        if any(emp['id'] == updated_data['id'] for emp in employees):
            return jsonify({"error": "An employee with this ID already exists"}), 400

    # Update the employee with the provided data
    employee.update(updated_data)
    return jsonify(employee)



#------------------------ Delete an employee ------------------------
@app.route('/employees/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    global employees
    employee = next((emp for emp in employees if emp['id'] == employee_id), None)

    if employee:
        employees = [emp for emp in employees if emp['id'] != employee_id]
        return jsonify({"message": "Employee deleted"}), 200
    else:
        return jsonify({"error": "Employee not found"}), 404




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
