import json
import random
from string import ascii_uppercase

answer_map = {letter: index for index, letter in enumerate(ascii_uppercase)}

class IllegalAnswerError(Exception):
    pass

def load_questions(filename, number=10):
    with open(filename, encoding='utf-8') as f:
        q = json.load(f)
    chosen_ones = random.sample(q, min(number, len(q)))
    return chosen_ones

def ask_question(question):
    print(question['question'])
    for a in question['answers']:
        print(a)
    answer = input('回答：')
    try:
        answer_index = answer_map[answer.upper()]
        answer_score = question['scores'][answer_index]
    except (KeyError, IndexError) as e:
        raise IllegalAnswerError
    return answer_score
