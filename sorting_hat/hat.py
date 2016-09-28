import json
import random
from string import ascii_uppercase

answer_map = {letter: index for index, letter in enumerate(ascii_uppercase)}

class IllegalAnswerError(Exception):
    pass


class Hat:
    """
    So put me on! Don't be afraid!
    And don't get in a flap!
    You're in safe hands (though I have none)
    For I'm a Thinking Cap!
    """
    def __init__(self, filename, number=10):
        with open(filename, encoding='utf-8') as f:
            q = json.load(f)
        self.length = min(number, len(q))
        self.questions = random.sample(q, self.length)
        self.score = 0
        self.ask_index = -1
        self.done_index = 0

    def ask_question(self):
        if self.ask_index < self.length - 1:
            self.ask_index += 1
            return self.questions[self.ask_index]

    def answer_question(self, answer):
        if self.done_index == self.ask_index:
            try:
                answer_index = answer_map[answer.upper()]
                answer_score = self.questions[self.done_index]['scores'][answer_index]
            except (KeyError, IndexError) as e:
                raise IllegalAnswerError
            self.score += answer_score
            self.done_index += 1

    def calculate_house(self):
        if self.length <= self.score <= self.length * 2:
            return '格兰芬多!'
        elif self.length * 2 < self.score <= self.length * 2.5:
            return '赫奇帕奇!'
        elif self.length * 2.5 < self.score <= self.length * 3:
            return '拉文克劳!'
        elif self.score > self.length * 3:
            return '斯莱特林!'

        
