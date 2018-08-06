#
#
#
#
# def fibo(num):
#     first = 0
#     second = 1
#     result = []
#     for i in range(0,num):
#         third = first + second
#         result.append(second)
#         first = second
#         second = third
#     print(result)
#     return
# fibo(10)


def fib(num):
    fib=[]
    for i in range(0,num):
        if i == 0:
            fib.append(0)
        elif i == 1:
            fib.append(1)
        else:
            fib.append(fib[i-1]+fib[i-2])
    return(fib)
#
#
#





fib(10)
