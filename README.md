# Task management using Fast API

This project is a FastAPI application designed to perform **CRUD** operations for **Items** and User **Clock-In** Records. It leverages the power of MongoDB to manage data and offers a robust set of features to enhance functionality and usability. 

## Features

- **CRUD Operations** for Items and Clock-In Records.
- **Filtering and Aggregation**: Filter items based on criteria like Email, Expiry Date, Quantity, etc., and use MongoDB aggregation to group item counts by email.
- **API Documentation**: Swagger UI for easy interaction with APIs.

## Installation

To run this project locally, follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/Pgangothri/vodex.ai.git
cd your project
```
### 2. Create a virutal environment
To create and activate a virtual environment, follow the steps based on your operating system:
```bash
python -m venv venv
.\venv\Scripts\activate
```
Macos/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Install Dependencies
With the virtual environment activated, install the required dependencies:
```bash
pip install -r requirements.txt
```
### 4. Database setup
In database.py according to requirement use Mondodb(or Atlas Account) 

### 5. Running locally
```bash
uvicorn main:app --reload
```
## Live Deployment
Your FastAPI application is hosted on Kayeb and can be accessed via the following URL:
- **API Documentation (Swagger UI):**https://uneven-guanaco-vinn-150096d5.koyeb.app/docs
## Endpoints

### Items API
#### 1. **Create Item** - POST /items:
#### 2. **Get Item by ID** - GET /items/{id}
#### 3. **Filter Items** - GET /items/filter
#### 4. **Update Item** - PUT /items/{id}
#### 5. **Delete Item** - DELETE /items/{id}
#### 6. **MongoDB Aggregation** - GET /items/aggregate:
### User Clock-In Records API
#### 1. **Create clock-in** - POST /clock-in:
#### 2. **Get clock-in by ID** - GET /clock-in/{id}
#### 3. **Filter clock-in** - GET /clock-in/filter:
#### 4. **Update clock-in** - PUT /clock-in/{id}
#### 5. **Delete clock-in** - DELETE /clock-in/{id}
## Swagger
The API will be accessible locally at
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc
## Notes
- Ensure your repository contains the necessary files, including the requirements.txt, to install dependencies.
- You can customize the deployment process further using Kayeb's features, such as scaling and custom domains

