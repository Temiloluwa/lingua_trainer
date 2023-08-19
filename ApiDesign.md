# Api Design
I would like to create an api that utilizes an LLM as a language trainer.
## Introduction
A client uploads new words they are learning and challenges are generated based on the words.
This concept can be expanded to any domain where an llm can serve as a trainer

## Challenges

1. Fill in the Blank(level 1) `fill_in_the_blank_one`
``` python
"""
Given a word, the following occurs:

word = "Gelegenheit"

# gather information about the word
# e.g parts of speech, is_stop_word, tense(if a verb), gender (if a noun), synonyms
word_info = get_word_info(word)
print(word_info)
{
    "word": "Gelegenheit",
    "mutable": {
        "part_of_speech" : "Noun",
        "tense_word" : None,
    },
    "immutable": {
        "is_stop_word" : False,   
        "gender" : "Female",
        "synonyms" : ["Moeglichkeit"],
    }
    
}

# def create_challenge(word_info):
    # get all the props
    props = (word_info["mutable"].values()) + list(word_info["immutable"].values())
    # choose one of the props
    prop = random.choice(prop)

    ################################
    # call llm to generate sentence and scenario
    word_sentence, word_translation, scenario = prompt_for_sentence(word, prop)

    challenge = {
        "word": word,
        "word_sentence": word_sentence,
        "scenario": scenario,
        "prop" : prop
    }

    return challenge

# create challenge from word
challenge = create_challenge(word_info)

# tutor student
# def tutor_student(challenge, student_response):
    # RETURN TUTOR RESPONSE
    return tutor_response

"""

```

## Api Endpoints

1. **User Authentication and Authorization:**
   - `/api/register` (POST): Register a new user account.
   - `/api/login` (POST): Authenticate and log in a user.
   - `/api/logout` (POST): Log out the currently authenticated user.
   - `/api/user/profile` (GET, PUT): Get or update user profile information.

2. **Word and Phrase Management:**
   - `/api/words` (GET, POST): Get a list of uploaded words and phrases or upload new ones.
   - `/api/words/:id` (GET, PUT, DELETE): Get, update, or delete a specific word/phrase by ID.

3. **Challenge Generation:**
   - `/api/challenges` (GET): Generate a list of challenges based on uploaded words and phrases.

4. **Challenge Submission:**
   - `/api/challenges/:id/submit` (POST): Submit a user's answer to a challenge for evaluation.

5. **Challenge History:**
   - `/api/user/challenges` (GET): Get a user's challenge history and results.

6. **Leaderboard and Statistics:**
   - `/api/leaderboard` (GET): Get a list of top users based on challenge performance.
   - `/api/user/statistics` (GET): Get user-specific language learning statistics.

7. **User Data Management:**
   - `/api/user/words` (GET, POST): Get a user's uploaded words and phrases or upload new ones.
   - `/api/user/words/:id` (GET, PUT, DELETE): Get, update, or delete a specific user-uploaded word/phrase.

8. **Feedback and Support:**
   - `/api/feedback` (POST): Allow users to provide feedback or support requests.




## Prompt Design