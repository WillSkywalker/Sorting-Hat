#!/usr/bin/env python3

total_score = 0

def ask_question(question, a, b, c, d):
    print(question)
    print(a)
    print(b)
    print(c)
    print(d)

    answer = input('回答：')
    if answer == 'A':
        return 1
    elif answer == 'B':
        return 4
    elif answer == 'C':
        return 2
    elif answer == 'D':
        return 3


total_score += ask_question('戴上分院帽的那一刻，你在想什么？', 
                            'A. 好担心啊，我究竟会分到哪一个学院呢？', 
                            'B. 整个学校的人都在看我吗？', 
                            'C. 这里用开家长会吗？', 
                            'D. 学院桌上的东西看起来好好吃啊！')
total_score += ask_question('你最不喜欢别人说你怎样？', 'A. 胆小', 'B. 普通', 'C. 自私', 'D. 无知')
total_score += ask_question('你想选哪种动物做宠物？', 'A. 猫头鹰', 'B. 蟾蜍', 'C. 老鼠', 'D. 猫')


if 3 <= total_score <= 5:
    print('格兰芬多!')
elif 6 <= total_score <= 8:
    print('赫奇帕奇!')
elif 9 <= total_score <= 11:
    print('拉文克劳!')
elif 12 <= total_score <= 14:
    print('斯莱特林!')
