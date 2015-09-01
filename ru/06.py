#!/usr/bin/env python3

import sys

def yearly_savings(chores, paper, spending):
    print ('>>> yearly_savings (%s, %s, %s)' % (chores, paper, spending))
    savings = 0
    for week in range(1, 10):
        savings = savings + chores + paper - spending
        print('К концу недели № %s накопится %s руб.' % (week, savings))
    print ('(... и так далее ...)')

def your_age():
    print('>>> your_age()')
    print('Сколько тебе лет? Введи число и нажми Enter:')
    age = int(sys.stdin.readline())
    if age >= 10 and age <= 13:
        print('Я знаю, тебе %s лет' % age)
    else:
        print('Столько люди не живут.')

def interest (capital, years, percent):
    print ('>>> calculate_interest (%d, %d, %d)' % (capital, years, percent))
    for i in range (0, years):
        print ('%s: %s' % (i, capital))
        capital *= (1 + percent/100)
    print (capital)

interest (1000, 1, 11)
interest (1200, 5, 13)
interest (1500, 10, 15)
interest (50000, 5, 18)
