# -*- coding:utf-8 -*-
_author = 'wyp'
'''
Q:求斐波那契数列第N项， 0, 1, 1, 2, 3, 5, 8, 13
'''
#A1：递归函数，但是该解法有很严重的效率问题，比如fib(10)=fib(9)+fib(8);而fib(9)=fib(8)+fib(7)
#计算了很多的重复节点，随着n的增大而急剧增大，时间复杂度是n的指数
def fib(n):
    if n ==0:
        return 0
    elif n ==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print fib(10)
#A2：优化:利用循环，由小到大计算；
# 开始用一个临时的列表存储f(0)和f(1)的值，然后遍历（2,n+1）
# f（2）替换f0的位置
def fib2(n): #n:5
    temp_list = [0,1]  #temp_list [0,1]
    if n>=2:
        for i in range(2,n+1):
            result = temp_list[0]+temp_list[1]
            # temp_list[0] = result 第一次是temp_list[0]，第二次是temp_list[1]，第三次是0；和i关联后，应该是i%2取余数的值
            temp_list[i%2] = result
    #第N次应该是temp_list[n%2]
    return temp_list[n%2]
print fib2(10)

#A3:略
def jumpfloor(n):
    pass