from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(docs_url='/docs')

class QuestionCreate(BaseModel):
    text: str
    answer: str


questions_db = [
    {'id': 1, 'text': "Что означает Fast api", 'answer': 'Фреймворк'},
    {'id': 2, 'text': "Что означает telebot", 'answer': 'Фреймворк для телеграм бота'}
]

@app.get('/')
def read_root():
    return {'message': 'Добро пожаловать, перейдите на /docs'}

@app.get('/questions')
def get_questions():
    return questions_db

@app.get('/questions/questions_id')
def get_question(questions_id: int):
    for q in questions_db:
        if q['id'] == questions_id:
            return q
    raise HTTPException(status_code=404, detail='Вопрос не найден')

current_id = 2

@app.post('/questions')
def create_question(question: QuestionCreate):
    global current_id
    current_id += 1
    new_question = {
        'id': current_id,
        'text': question.text,
        'answer': question.answer
    }
    questions_db.append(new_question)
    return new_question