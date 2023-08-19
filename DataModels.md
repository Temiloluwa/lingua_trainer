# MongoDB Database Model

I am designing a language tutor app with the following features

1. users can upload words they are currently learning
2. the tutor creates challenges for the student to solve and provides feedback
3. each challange is a list of questions for the student to solve.
4. the questions are based on words the users upload
5. the app keeps track of the words whose associated questions the student  found difficult to solve
6. The user see a dashboard indicating their learning progress
7. the app stores the following features about each uploaded word

{
    "word": <the word itself>,
    "mutable": {
        "part_of_speech" : "<the part of speech>",
        "tense": <the tense of the word if it is a verb>,
    },
    "immutable": {
        "is_stop_word" : <a boolean indicating if it is a stop word or not>,   
        "gender" : "<the gender of the word>",
        "synonyms" : <a list of synonyms of the word>
    }
    
}

for example: 

{
    "word": "Gelegenheit",
    "mutable": {
        "part_of_speech" : "Noun",
        "tense" : None,
    },
    "immutable": {
        "is_stop_word" : False,   
        "gender" : "Female",
        "synonyms" : ["Moeglichkeit"],
    }
    
}


Design a mongodb schema for this application. Use pymongo schema

1. **User**
   ``` python

   from pymongo import MongoClient

    client = MongoClient("mongodb://localhost:27017/")
    db = client["language_trainer"]
    users_collection = db["users"]

    user_schema = {
        "username": {"type": "string", "required": True, "unique": True},
        "email": {"type": "string", "required": True, "unique": True},
        "password": {"type": "string", "required": True},
        "createdAt": {"type": "datetime", "default": "datetime.utcnow"}
    }

    users_collection.create_index("username", unique=True)
    users_collection.create_index("email", unique=True)
   
   ```

2. **User Profile**

``` python
user_profiles_collection = db["user_profiles"]

user_profile_schema = {
    "user": {"type": "objectId", "required": True},
    "firstName": {"type": "string", "required": True},
    "lastName": {"type": "string", "required": True},
    "languages": {"type": "array", "items": {"type": "string"}},
    "profilePicture": {"type": "string"},
    "birthDate": {"type": "datetime"}
    "updatedAt": {"type": "datetime"}
    "createdAt": {"type": "datetime", "default": "datetime.utcnow"}
}

user_profiles_collection.create_index("user")


3.  **Words**

```python

from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["language_tutor"]

words_collection = db["words"]

word_schema = {

    "word": {"type": "string", "required": True},
    "user": {"type": "objectId", "required": True},
    "mutable": {
        "part_of_speech": {"type": "string"},
        "tense": {"type": "string"}
    },
    "immutable": {
        "is_stop_word": {"type": "boolean"},
        "gender": {"type": "string"},
        "synonyms": {"type": "array"}
    },
    "createdAt": {"type": "datetime", "default": datetime.utcnow}
}

words_collection.create_index("user")
```

4. **Challenge**

``` python

from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["language_tutor"]

challenges_collection = db["challenges"]

challenge_schema = {
    "name": {"type": "string", "required": True},  
    "questions": [{
        "word": {"type": "objectId", "required": True},  
        "questionText": {"type": "string"} 
    }]
}

challenges_collection.create_index("name")

5. **ChallengeAttempt**

``` python

from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["language_tutor"]

challenge_attempts_collection = db["challenges_attempts"]

challenge_attempt_schema = {
    "word": {"type": "objectId", "required": True},
    "user": {"type": "objectId", "required": True},
    "attempts": [
        {
            "question": {"type": "string"},
            "value": {"type": "string"},
            "feedback": {"type": "string"}, 
            "attemptedAt": {"type": "datetime", "default": datetime.utcnow}
        }
    ]
}

challenge_attempts_collection.create_index("user")


```

5. **Question Schema**

``` python
from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["language_tutor"]

questions_collection = db["questions"]

question_schema = {
    "challenge": {"type": "objectId", "required": True},
    "word": {"type": "objectId", "required": True},
    "questionText": {"type": "string", "required": True},
    "answer": {"type": "string", "required": True},
    "createdAt": {"type": "datetime", "default": datetime.utcnow}
}

questions_collection.create_index("challenge")
questions_collection.create_index("word")


```

6. **Learning Progress**

``` python

from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["language_tutor"]

learning_progress_collection = db["learning_progress"]

learning_progress_schema = {
    "user": {"type": "objectId", "required": True},
    "word": {"type": "objectId", "required": True},
    "learned": {"type": "boolean", "default": False},
    "createdAt": {"type": "datetime", "default": datetime.utcnow}
}

learning_progress_collection.create_index([("user", 1), ("word", 1)], unique=True)

```