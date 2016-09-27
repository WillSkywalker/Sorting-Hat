#!/usr/bin/env python3

total_score = 0
questions = [
    {'question': '戴上分院帽的那一刻，你在想什么？',
     'answers': ('A. 好担心啊，我究竟会分到哪一个学院呢？',
                 'B. 这里用开家长会吗？',
                 'C. 整个学校的人都在看我吗？',
                 'D. 学院桌上的东西看起来好好吃啊！'),
     'scores': (1, 2, 4, 3)},

    {'question': '你最不喜欢别人说你怎样？',
     'answers': ('A. 胆小', 'B. 普通', 'C. 自私', 'D. 无知'),
     'scores': (1, 4, 2, 3)},

    {'question': '你想选哪种动物做宠物？',
     'answers': ('A. 猫头鹰', 'B. 蟾蜍', 'C. 老鼠', 'D. 猫'),
     'scores': (1, 4, 2, 3)},

    {'question': '你最希望在魁地奇运动中扮演的角色是什么？',
     'answers': ('A. 守门员', 'B. 找球手', 'C. 追球手', 'D. 击球手'),
     'scores': (2, 1, 4, 3)},

    {'question': '如果你有机会发明一种可以给你某种能力的魔药，你会选择哪一种？',
     'answers': ('A. 爱', 'B. 荣耀', 'C. 智慧', 'D. 力量'),
     'scores': (2, 1, 3, 4)},
]
answer_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3}

def ask_question(question):
    print(question['question'])
    for a in question['answers']:
        print(a)
    answer = input('回答：')
    answer_index = answer_map[answer]
    return question['scores'][answer_index]


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
