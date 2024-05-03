import json
import os
def creat_path(file_name):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    return os.path.join.(script_dir, file_name)

def serialize(file_name, data):
    path = creat_path(file_name)
    with open(path, "w") as file:
        json.dump(data, file)

def deserialize(file_name):
    path = creat_path(file_name)
    with open(path,"r") as file:
        data = json.load(file)
    return data

try:

    file_name = "employee.dat"
    employee_dict = {
        "company": "ABC Corp",
        "employees": [
            {
                "name": "John Doe",
                "age":  30,
                "department": "Sales",
                "skills": ["negotiation", "communication", "CRM"]
            },

    }
    "name": "JAne Smith",
    "age": 35,
    "department": "Marketing",
    "skills": "Marketing",
    "skills": ["SEO", "content cretion", "braiding"]
    }
    ]
    }