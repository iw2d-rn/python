#!/usr/bin/python
# -*- coding: utf-8 -*-

# class Matrix:

#     def __init__(self) -> None:
#         pass

#     def matrixAddition(*args):
#         print(args)


def addFor1d(m1, m2):
    ans = []
    for i in range(len(m1)):
        ans.append(m1[i] + m2[i])
    return ans


def addFor2d(m1, m2):
    ans = []
    ans1 = []
    for i in range(len(m1)):
        if len(m1[i]) == len(m2[i]):
            for j in range(len(m1[i])):
                ans1.append(m1[i][j] + m2[i][j])

                # print ('s', j)

            ans.append(ans1)
            ans1 = []
        else:
            return i
    return ans


def subFor1d(m1, m2):
    ans = []
    for i in range(len(m1)):
        ans.append(m1[i] - m2[i])
    return ans


def subFor2d(m1, m2):
    ans = []
    ans1 = []
    for i in range(len(m1)):
        if len(m1[i]) == len(m2[i]):
            for j in range(len(m1[i])):
                ans1.append(m1[i][j] - m2[i][j])

                # print ('s', j)

            ans.append(ans1)
            ans1 = []
        else:
            return i
    return ans


def transposed1d(m1):
    ans = []
    for i in range(len(m1)):
        ans.append([m1[i]])
    return ans


def transposed2d(m1):
    ans = []
    ans1 = []
    for i in range(len(m1[0])):
        for j in range(len(m1)):
            ans1.append(m1[j][i])
        print(ans1)
        ans.append(ans1)
        ans1 = []
    return ans


# def multipication2d(m1,m2):
#     ans = []
#     ans1 = []
#     for i in range(len(m1[0])):
#         for j in range(len(m1)):
#             ans1.append(m1[j][i])
#         print(ans1)
#         ans.append(ans1)
#         ans1 = []
#     return ans


    # [    j  j  j
    #  i  [1, 3, 2],
    #  i  [2, 4, 7]
    # ]

def multipication2d(m1, m2):
    if len(m1[0]) == len(m2):
        ans = [[0] * len(m1) for i in range(len(m2[0]))]
        for i in range(len(m1)):
            for j in range(len(ans)):
                sum = 0
                for k in range(len(m2)):
                    print(i, k, '|', k, j)
                    sum += m1[i][k] * m2[k][j]
                print(sum)
                ans[i][j] = sum
        print(ans)
    elif len(m1) == len(m2[0]):
        ans = [[0] * len(m2) for i in range(len(m1))]
        for i in range(len(m1)):
            for j in range(len(ans)):
                sum = 0
                for k in range(len(m2)):
                    print(i, k, '|', k, j)
                    sum += m1[i][k] * m2[k][j]
                print(sum)
                ans[i][j] = sum
        print(ans)
    else:
        print('cant multiply un matched matrixes')


def add(add1, add2):
    if len(add1) == len(add2):
        if type(add1[0]) is list:
            if type(add1[0][0]) is list:
                return 'greater than 2d arr'
            else:
                if type(add1[0][0]) is not int:
                    return 'not integer'
                print('2d arr')

                # return transposed2d(add1)

                return (addFor2d(add1, add2), '|', subFor2d(add1,
                        add2), '|', transposed2d(add1))
        elif type(add1[0]) is not int:
            return 'not integer'
        else:
            print('1d arr')
            return (addFor1d(add1, add2), '|', subFor1d(add1, add2), '|'
                    , transposed1d(add1))
    else:
        return 'matrix dimension do not match'


# def sub():

# print(add([1, 3, 2], [0, 1, 5]))
print(multipication2d([1, 3, 2], [0, 1, 5]))

print(multipication2d([[1, 3, 2], [2, 4, 7]], [[0, 3], [1, -2], [5, 8]]))

# print(add([[1, 3,2],[2, 4,7]],[[0, 1,5],[3, -2,8]]))

# print(add(['1', '3', 'a'], ['0', '1', '5']))
# print(add([['1', '3', '2'], ['2', '4', '7']], [['0', '1', '5'], ['3', '2', '8']]))

# add([[[1]]],[[[2]]])

# ([[1, 3, 2], [2, 4, 7]], [[0, 1, 5], [3, -2, 8]])

([[1, 3, 2], [2, 4, 7]], [[0, 1, 5], [3, -2, 8]])
