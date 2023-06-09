import json
from question import Question

def load_questions(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    questions = []
    for item in data:
        #итерируем по java списку: q-вопрос, d-сложность, a-правильный ответ
        text = item['q']
        difficulty = int(item['d'])
        right_answer = item['a']
        question = Question(text, difficulty, right_answer)
        questions.append(question)

    return questions


def build_statistics(questions):
    score = 0 #количество баллов
    count = 0 #количество правильных ответов

    for question in questions:
        if question.is_correct():
            score = score + question.score
            count = count + 1

    return f'Вот и все! \n' \
           f'Отвечено {count} вопроса из 5 \n' \
           f'Набрано баллов: {score}'
