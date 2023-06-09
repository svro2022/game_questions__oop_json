'''
– текст вопроса - self.text
– сложность вопроса - self.difficulty
– верный вариант ответа - self.right_answer

– задан ли вопрос (по умолчанию False) - self.is_asked
– ответ пользователя (по умолчанию None) - self.user_answer
– баллы за вопрос (вычисляется в момент инициализации) - self.score
'''

class Question:
    def __init__(self, text, difficulty, right_answer):
        self.text = text
        self.difficulty = difficulty
        self.right_answer = right_answer

        #поля по умолчанию:
        self.is_asked = False
        self.user_answer = None
        self.score = self.difficulty * 10

    def get_points(self):
        '''Возвращает int, количество баллов.
        Баллы зависят от сложности (self.difficulty):
        за 1 дается 10 баллов,
        за 5 дается 50 баллов.'''
        return self.score

    def is_correct(self):
        '''Возвращает True, если ответ пользователя совпадает с верным ответом.
        Иначе - False.'''
        return self.right_answer == self.user_answer

    def build_question(self):
        '''Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5'''
        return f'Вопрос: {self.text} \n' \
               f'Сложность {self.difficulty}/5'

    def build_feedback(self):
        '''Возвращает:
        Ответ верный, получено __ баллов
        Ответ неверный, верный ответ __
        '''
        if self.is_correct():
            return f'Ответ верный, получено {self.score} баллов'
        return f'Ответ неверный, верный ответ - {self.right_answer}'
