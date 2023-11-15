job_schema = {
    "bsonType": "object",
    "required": ["title" , "description" , "company_name" , "skills" , "posted_by" , "salary"],
    "properties": {
        "title": {
            "bsonType": "string",
            "description": "must be a string and is required"
        },
        "description": {
            "bsonType": "string",
            "description": "must be a string and is required"
        },
        "skills": {
            "bsonType": "array",
            "description": "must be an array and is required",
            "items": {
                "bsonType": "string"
            }
        },
        "salary": {
            "bsonType": "int",
            "description": "must be an integer and is required"
        },
        "posted_by": {
            "bsonType": "objectId",
            "description": "must be an ObjectId and is required"
        },
        "company_name": {
            "bsonType": "string",
            "description": "must be a string"
        },    
    }
}