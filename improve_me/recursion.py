"""
递归
"""


# nums = [1, 3, 5, 7, 9]
#
#
# def list_sum(num_list):
#     if len(num_list) == 1:
#         return num_list[0]
#     else:
#         return num_list[0] + list_sum(num_list[1:])
#
#
# sum = list_sum(nums)
# print(sum)

"""
我现在要做的事情是计算一个人要上100层的阶梯，他只能一次迈一步或者两步，有多少种走法
"""

# # 递归思想很吊，但是其实执行效率很低
# def ways(numbers_of_steps):
#     if numbers_of_steps <= 2:
#         return numbers_of_steps
#     else:
#         return ways(numbers_of_steps - 1) + ways(numbers_of_steps - 2)
#
#
# num_way = ways(40)
# print(num_way)


def myf(n):
    f1 = 1
    f2 = 2
    res1 = [f1, f2]
    for i in range(n-2):
        f3 = res1[-1]+res1[-2]

        del res1[0]
        res1.append(f3)
    return f3

print(myf(100))
a = [1,2]
del a[0]
a.append(3)
print(a)