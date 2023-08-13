
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from model import process_answer

app = FastAPI()


class AnswerInput(BaseModel):
    answer: str

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/evaluate_answer/")
def evaluate_answer(answer_input: AnswerInput):
    # Get the answer from the request
    answer = answer_input.answer

    # Process the answer and generate feedback
    feedback = process_answer(answer)

    return {"feedback": feedback}
