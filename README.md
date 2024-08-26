# flask-employee-management-api
# Employee Management API

## Description

This is a RESTful API for managing employee data, built with Flask and Docker. The API supports CRUD operations (Create, Read, Update, Delete) to manage a collection of employees. It is designed to handle basic operations for adding, retrieving, updating, and deleting employee records and is dockerized for easy deployment.

## Features

- **Create an Employee**: Add a new employee to the collection.
- **Retrieve Employees**: Get a list of all employees or retrieve a specific employee by their ID.
- **Update an Employee**: Modify the details of an existing employee.
- **Delete an Employee**: Remove an employee from the collection.
## Installation

### Prerequisites

- Docker: Make sure Docker is installed on your machine. You can download it from [Docker's official website](https://www.docker.com/products/docker-desktop).

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Didula98/flask-employee-management-api.git
   cd flask-employee-management-api
2. **Build the Docker Image**
   ```bash
   docker build -t employee-management-api .
4. **Run the Docker Container**
   ```bash
   docker run -d -p 5000:5000 employee-management-api
6. **Access the API**
   The API will be available at http://localhost:5000 or http://127.0.0.1:5000.
