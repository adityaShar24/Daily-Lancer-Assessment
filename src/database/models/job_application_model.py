job_application_schema = {
    "bsonType": "object",
    "required": ["job_id", "resume" , "contact_no" , "email" ],
    "properties":{
        "username": {
            "bsonType": "string",
            "description": "must be a string and is optional"
        },
        "job_id": {
            "bsonType": "string",
            "description": "must be a string and is required"
        },
        "email": {
            "bsonType": "string",
            "description": "must be a string and is required"
        },
        "resume": {
            "bsonType": "string",
            "description": "must be a string and is required"
        },
        "contact_no": {
            "bsonType": "string",
            "description": "must be a string and is required"
        },
        "cover_letter": {
            "bsonType": "string",
            "description": "must be a string and is optional"
        }
    }
}