# https://www.nowcoder.com/questionTerminal/a1c5a3bec29b427dbc0340aff192187b
# /Users/charleyzhao/code/Python/rush/ks_find_solution.py
# X+7+8=100

from queue import Queue

# 从左向右构建完整数字
def get_full_number(eq_str, p_start):
    number = 0
    while not (eq_str[p_start] in ['X', '+', '-', '*', '=']):
        number = number*10 + int(eq_str[p_start])
        p_start = p_start + 1
        if p_start >= len(eq_str):
            break
    return number, p_start

# 将str转换为queue，方便数字的表示
def str_to_queue(eq_str):
    eq_len = len(eq_str)
    eq_queue = Queue(maxsize=0)
    p_strat = 0
    while p_strat < eq_len:
        if not (eq_str[p_strat] in ['X', '+', '-', '*', '=']):
            number, p_strat = get_full_number(eq_str, p_strat)
            eq_queue.put(number)
        else:
            eq_queue.put(eq_str[p_strat])
            p_strat = p_strat + 1
    eq_queue.put('end')  # 终结标识
    return eq_queue


def main(eq_str):
    eq_queue = str_to_queue(eq_str)

    x_head = 0  # 记录系数
    y = 0  # 记录常数
    flag = 1  # 标记等号前后
    sol = -1  # 保存结果

    # 整个表达式由子表达式(+/-)(number/X)(*)(number/X)和=组成
    e1 = eq_queue.get()
    while e1 != 'end':
        x_head_i = 1
        y_i = 1
        if e1 == '=':
            flag = -1
            e1 = eq_queue.get()
            continue
        elif e1 == '+':
            flag_i = 1
        elif e1 == '-':
            flag_i = -1
        elif e1 == 'X':
            flag_i = 1
            y_i = 0
        else:  # 数字
            flag_i = 1
            x_head_i = e1
            y_i = e1
        
        e2 = eq_queue.get()
        while not (e2 in ['+', '-', '=', 'end']):
            if e2 == 'X':
                y_i = 0
                e2 = eq_queue.get()
            elif e2 == '*':
                e2 = eq_queue.get()
                continue
            else:
                y_i = y_i*e2
                x_head_i = x_head_i*e2
                e2 = eq_queue.get()
        if y_i != 0:
            x_head_i = 0
        x_head = x_head + flag*x_head_i
        y = y + flag*y_i
        e1 = e2

    if x_head == 0:
        sol = -1
    else:
        sol = int((-y)/x_head)
        e = (-y) % x_head
        if e != 0 or sol < 0:
            sol = -1

    return sol


if __name__ == '__main__':
    eq_str = input()
    print(main(eq_str))
