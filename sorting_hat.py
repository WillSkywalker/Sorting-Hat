#!/usr/bin/env python3

total_score = 0
answer_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3}

def load_questions(filename):
    with open(filename) as f:
        q = eval(f.read())
    return q

def ask_question(question):
    print(question['question'])
    for a in question['answers']:
        print(a)
    answer = input('回答：')
    answer_index = answer_map[answer]
    return question['scores'][answer_index]

questions = load_questions('questions.txt')
# 这样做有什么安全隐患吗？你能通过修改 question.txt 来破坏程序的运行吗？

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
