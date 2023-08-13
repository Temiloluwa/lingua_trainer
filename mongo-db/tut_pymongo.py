import pymongo
from bson import ObjectId
import datetime

host = "localhost"
port = 27000       
username = "myadmin"  
password = "mypassword"
auth_source = "admin" 

# Create a MongoClient with authentication
uri = f"mongodb://{username}:{password}@{host}:{port}/{auth_source}"
client = pymongo.MongoClient(uri)

# Access the demodb database
db_name = "training_db"
db = client[db_name]

# Define JSON schema validators
user_schema = {
    "validator": {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["username", "email", "password", "created_at"],
            "properties": {
                "username": {"bsonType": "string"},
                "email": {"bsonType": "string"},
                "password": {"bsonType": "string"},
                "created_at": {"bsonType": "date"},
                "updated_at": {"bsonType": "date"}
            }
        }
    }
}

word_schema = {
    "validator": {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["text", "translation", "language", "user_id", "created_at"],
            "properties": {
                "text": {"bsonType": "string"},
                "translation": {"bsonType": "string"},
                "language": {"bsonType": "string"},
                "user_id": {"bsonType": "objectId"},
                "created_at": {"bsonType": "date"},
                "updated_at": {"bsonType": "date"}
            }
        }
    }
}

challenge_schema = {
    "validator": {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["user_id", "questions", "score", "created_at"],
            "properties": {
                "user_id": {"bsonType": "objectId"},
                "questions": {
                    "bsonType": "array",
                    "items": {
                        "bsonType": "object",
                        "required": ["word_id", "answer"],
                        "properties": {
                            "word_id": {"bsonType": "objectId"},
                            "answer": {"bsonType": "string"}
                        }
                    }
                },
                "score": {"bsonType": "int"},
                "created_at": {"bsonType": "date"}
            }
        }
    }
}

# Create collections with JSON schema validation
users = db["users"]
users.create_index([("username", pymongo.ASCENDING)], unique=True)
users.create_index([("email", pymongo.ASCENDING)], unique=True)
users.create_index([("created_at", pymongo.ASCENDING)])

words = db["words"]
words.create_index([("text", pymongo.ASCENDING)], unique=True)
words.create_index([("user_id", pymongo.ASCENDING)])
words.create_index([("created_at", pymongo.ASCENDING)])

challenges = db["challenges"]
challenges.create_index([("user_id", pymongo.ASCENDING)])
challenges.create_index([("created_at", pymongo.ASCENDING)])

# Insert sample data into the users collection
user_data = [
    {
        "username": "user1",
        "email": "user1@example.com",
        "password": "password123",
        "created_at": datetime.datetime.utcnow(),
        "updated_at": datetime.datetime.utcnow()
    },
    {
        "username": "user2",
        "email": "user2@example.com",
        "password": "password456",
        "created_at": datetime.datetime.utcnow(),
        "updated_at": datetime.datetime.utcnow()
    },
    {
        "username": "user3",
        "email": "user3@example.com",
        "password": "password789",
        "created_at": datetime.datetime.utcnow(),
        "updated_at": datetime.datetime.utcnow()
    }
]
users.insert_many(user_data)

# Insert sample data into the words collection
word_data = [
    {
        "text": "apple",
        "translation": "pomme",
        "language": "English",
        "user_id": users.find_one({"username": "user1"})["_id"],
        "created_at": datetime.datetime.utcnow(),
        "updated_at": datetime.datetime.utcnow()
    },
    {
        "text": "dog",
        "translation": "chien",
        "language": "English",
        "user_id": users.find_one({"username": "user2"})["_id"],
        "created_at": datetime.datetime.utcnow(),
        "updated_at": datetime.datetime.utcnow()
    },
    {
        "text": "cat",
        "translation": "chat",
        "language": "English",
        "user_id": users.find_one({"username": "user3"})["_id"],
        "created_at": datetime.datetime.utcnow(),
        "updated_at": datetime.datetime.utcnow()
    }
]
words.insert_many(word_data)

# Insert sample data into the challenges collection
challenge_data = [
    {
        "user_id": users.find_one({"username": "user1"})["_id"],
        "questions": [
            {"word_id": words.find_one({"text": "apple"})["_id"], "answer": "pomme"},
            {"word_id": words.find_one({"text": "dog"})["_id"], "answer": "chien"}
        ],
        "score": 10,
        "created_at": datetime.datetime.utcnow()
    },
    {
        "user_id": users.find_one({"username": "user2"})["_id"],
        "questions": [
            {"word_id": words.find_one({"text": "cat"})["_id"], "answer": "chat"},
            {"word_id": words.find_one({"text": "apple"})["_id"], "answer": "pomme"}
        ],
        "score": 5,
        "created_at": datetime.datetime.utcnow()
    },
    {
        "user_id": users.find_one({"username": "user3"})["_id"],
        "questions": [
            {"word_id": words.find_one({"text": "dog"})["_id"], "answer": "chien"},
            {"word_id": words.find_one({"text": "cat"})["_id"], "answer": "chat"}
        ],
        "score": 8,
        "created_at": datetime.datetime.utcnow()
    }
]
challenges.insert_many(challenge_data)

print("Inserted All data")

# Close the connection
client.close()
