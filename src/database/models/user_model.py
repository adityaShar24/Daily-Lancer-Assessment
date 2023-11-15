user_schema = {
    'bsonType': 'object',
    'required': ['username' , 'password' , "email"],
    'properties': {
        'username': {
            'bsonType': 'string',
            'description': 'must be a string and is required'
        },
        'password': {
            'bsonType': 'string',
            'description': 'must be a string and is required'
        },
        "email": {
            "bsonType": "string",
            'description': 'must be a string and is required'
        }
    }
}