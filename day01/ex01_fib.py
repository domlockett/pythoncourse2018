



# def fibo(num):
#     first = 0
#     second = 1
#     result = [0]
#     for i in range(0,num):
#         third = first + second
#         #print(second)
#         result.append(second)
#         first = second
#         second = third
#     print(result)
#     return
# fibo(10)


fib = []
for i in range(0,10):
    if i == 0:
        fib.append(0)
    elif i == 1:
        fib.append(1)
    else: (fib.append(fib[i-1]+fib[i-2]));



print(fib)
