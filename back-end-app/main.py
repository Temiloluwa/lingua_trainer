import uvicorn
from fastapi import FastAPI
from .auth import auth_router
from .user import users_router
from .words import words_router
from .challenges import challenges_router


app =  FastAPI(
        title="Lingua Trainer",
        description="An AI based language trainer",
        summary="""
            This is an application that assists in mastering a target language.
            Users are offered challenges based on words and phrases they provide to the trainer.
        """,
        version="0.0.1",
        terms_of_service="http://linguatrainer.hifeyinc.com/terms/",
        contact={
            "name": "Temiloluwa Adeoti",
            "url": "https://temiloluwa.github.io/",
            "email": "temmiecvml@gmail.com",
        },
        license_info={
            "name": "Apache 2.0",
            "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
        },
        openapi_tags = [
        {
            "name": "User",
            "description": "Person learning a language using the Lingua trainer API",
        },
        {
            "name": "Words",
            "description": "Words that a user is learning or learnt",
            "externalDocs": {
                "description": "Words that guide a user's experience on the app",
                "url": "https://fastapi.tiangolo.com/",
            },
        },
        {
            "name": "Challenges",
            "description": "The challenges offered by the Lingua trainer helps improve the user's language competence",
        },
        ]
    )

app.include_router(auth_router, prefix="/api/v1", tags=["Authentication"])
app.include_router(users_router, prefix="/api/v1/user", tags=["User"])
app.include_router(words_router, prefix="/api/v1/words", tags=["Words"])
app.include_router(challenges_router, prefix="/api/v1/words/challenges", tags=["Challenges"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
