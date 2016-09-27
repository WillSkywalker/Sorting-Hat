#!/usr/bin/env python3

score = 0

print('戴上分院帽的那一刻，你在想什么？')
print('A. 好担心啊，我究竟会分到哪一个学院呢？')
print('B. 整个学校的人都在看我吗？')
print('C. 这里用开家长会吗？')
print('D. 学院桌上的东西看起来好好吃啊！')

answer = input('回答：')
if answer == 'A':
    score += 1
elif answer == 'B':
    score += 4
elif answer == 'C':
    score += 2
elif answer == 'D':
    score += 3

print('你最不喜欢别人说你怎样？')
print('A. 胆小')
print('B. 普通')
print('C. 自私')
print('D. 无知')

answer = input('回答：')
if answer == 'A':
    score += 1
elif answer == 'B':
    score += 4
elif answer == 'C':
    score += 2
elif answer == 'D':
    score += 3

print('你想选哪种动物做宠物？')
print('A. 猫头鹰')
print('B. 蟾蜍')
print('C. 老鼠')
print('D. 猫')

answer = input('回答：')
if answer == 'A':
    score += 1
elif answer == 'B':
    score += 4
elif answer == 'C':
    score += 2
elif answer == 'D':
    score += 3


if 3 <= score <= 5:
    print('格兰芬多!')
elif 6 <= score <= 8:
    print('赫奇帕奇!')
elif 9 <= score <= 11:
    print('拉文克劳!')
elif 12 <= score <= 14:
    print('斯莱特林!')
