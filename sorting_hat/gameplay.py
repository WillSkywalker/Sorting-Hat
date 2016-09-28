#!/usr/bin/env python3

from hat import Hat, IllegalAnswerError
from sys import exit

questions_filename = '../data/questions.json'

def print_question(q):
    print(q['question'])
    for answer in q['answers']:
        print(answer)

def play():
    num = input('请输入你能接受的最大题数：')
    try:
        your_hat = Hat(questions_filename, int(num))
    except ValueError:
        print('输入的不是合法数字！')
        exit()

    q = your_hat.ask_question()
    while q:
        while True:
            try:
                print_question(q)
                your_hat.answer_question(input())
                break
            except IllegalAnswerError:
                print('没有这个选项吧...\n')
        q = your_hat.ask_question()

    print(your_hat.calculate_house())


if __name__ == '__main__':
    play()
