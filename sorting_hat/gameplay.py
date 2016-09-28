#!/usr/bin/env python3

from hat import load_questions, ask_question, IllegalAnswerError
from sys import exit

questions_filename = '../data/questions.json'

def play():
    total_score = 0
    num = input('请输入你能接受的最大题数：')
    try:
        questions = load_questions(questions_filename, int(num))
    except ValueError:
        print('输入的不是合法数字！')
        exit()

    for question in questions:
        while True:
            try:
                score = ask_question(question)
                break
            except IllegalAnswerError:
                print('没有这个选项吧...\n')
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


if __name__ == '__main__':
    play()
