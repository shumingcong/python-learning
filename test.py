#/usr/bin/python
# for i  in  range(1,5):
#    for j in range(1,5):
#        if (i==j):
#            continue
#        else:
#          for k in range(1,5):
#                 if (i==k)or(j==k):
#                     continue
#                 else:
#                    print(i,j,k)
# 排列组合，4个数组成三位数

# 企业发放奖金题
#
# i =int(input('净利润：'))
# arr = [ 1000000, 600000, 400000, 200000, 100000,0]
# rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
# r = 0
# for idx in range(0,6):
#     if i>arr[idx]:
#         r+=(i-arr[idx])*rat[idx]
#         print(r)
#         i=arr[idx]

# #  整数计算
# #! /usr/bin/python
# for i in range(1,85):
#     if  168%i ==0:
#         j = 168/i;
#         if i > j and (i+j)%2 ==0 and (i-j)%2==0:
#             m=(i+j)/2
#             n=(i-j)/2
#             x=n*n -100
#             print(x,i,j)

# #判断天数
# #!/usr/bin/python
#
# year=int(input('year:\n'))
# month=int(input('month:\n'))
# day=int(input('day:\n'))
#
# d_months=(31,28,31,30,31,30,31,30,31,30,31,30)
# if 0<month<=12:
#     month=month-2
# else:
#     print('data error')
# sum=0
# while month>=0:
#     sum+=d_months[month]
#     month=month-1
# sum+=day
# leap =0
# if (year%400==0)or((year%4==0)and (year%100!=0)):
#     leap=1
# if (1==leap)and (month>2):
#     sum+=1
# print('it is the %dth day.' %sum)
#0722
# # 斐波那契数列
# #!/usr/bin/python
# def fib(n):
#     if n==1 or n==2:
#         return  1
#
#     return fib(n-1)+fib(n-2)
# # print (fib(10))
# def fib(n):
#     a,b=1,1
#     i=5
#     for i in range(n-1):
#         a,b=b,a+b
#         print(a,b)
#     return a
# print(fib(10))
#
# def fib(n):
#
#  x,y=0,1
#
#  while(n):
#
#   x,y,n=y,x+y,n-1
#
#  return x
# print(fib(10))

# #复制列表
# a=[1,2,3,'shumingcong']
# b=a[:]
# print(b)

#0723
# #输出乘法口诀表
# for i in range(1,10):
#         for j in range(1,i+1):
#          print("%d*%d=%d"%(i,j,i*j),)

# #暂停一秒输出
# import  time
# print("开始时间：%s"% time.ctime())
# time.sleep(5)
# print("结束时间：%s"% time.ctime())

# #格式化输出时间
# # import time
# # print (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
# # time.sleep(20)
# # print (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

# #兔子总数问题，数列1、1、2、3、5、8、13、21.。。。对数
# def rabnum(n):
#     if n==1 or n==2:
#         return 1
#     else: return rabnum(n-1)+rabnum(n-2)
#     print(rabnum(n))
# for i in range (1,22):
#   print(rabnum(i))