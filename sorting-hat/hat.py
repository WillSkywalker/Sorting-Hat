#!/usr/bin/env python3

import json
import random
from string import ascii_uppercase

total_score = 0
answer_map = {letter: index for index, letter in enumerate(ascii_uppercase)}
questions_filename = '../data/questions.json'

def load_questions(filename, number=10):
    with open(filename, encoding='utf-8') as f:
        q = json.load(f)
    chosen_ones = random.sample(q, number)
    return chosen_ones

def ask_question(question):
    print(question['question'])
    for a in question['answers']:
        print(a)
    answer = input('回答：')
    answer_index = answer_map[answer.upper()]
    return question['scores'][answer_index]

questions = load_questions(questions_filename)

for question in questions:
    score = ask_question(question)
    total_score += score

length = len(questions)
if length <= total_score <= length * 2:
    print('格兰芬多!')
elif length * 2 < total_score <= length * 2.5:
    print('赫奇帕奇!')
elif length * 2.5 < total_score <= length * 3:
    print('拉文克劳!')
elif total_score > length * 3:
    print('斯莱特林!')
