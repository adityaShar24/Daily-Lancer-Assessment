job_application_schema = {
    "bsonType": "object",
    "required": ["job_id", "resume" , "applicant" ],
    "properties":{
        "applicant": {
            "bsonType": "objectId",
            "description": "must be an ObjectId and is required"
        },
        "job_id": {
            "bsonType": "objectId",
            "description": "must be a ObjectId and is required"
        },
        "resume": {
            "bsonType": "string",
            "description": "must be a string and is required"
        },
        "cover_letter": {
            "bsonType": "string",
            "description": "must be a string and is optional"
        }
    }
}