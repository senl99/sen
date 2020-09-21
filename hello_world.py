# l=[1,2,3,4,'a','b','c']
# l[2]=4
# print(l,l[0])
#
# t=(1,6,7,9,8,4)
# print(t)
#
# s={1,3,5,4,2}
# print(s)
#
# a=10
# b="5.9"
# c=None
# d=True
# print(a+float(b))
# print(str(a)+b)
# print(b+str(c))
# print(a+d)
# print(float(b)+d)
#
# k={'name':'123','age':18}
# print(k)
# print(k['name'])
#
# s='124731'
# print(list(s))
# print(tuple(s))
#
# t='135687'
# print(list(t))
# print(set(t))
#
# l='147258369'
# print(set(l))
# print(tuple(l))
#
# a=('hello')
# l=['1','2','3','4','5']
# s={'1','2','3','4','5'}
# t=('1','2','h')
# d={'name':'abc','age':'18'}
#
# print('o' in a)
# print('1' in l)
# print('2' in s)
# print('h' in t)
# print('name' in d)
#
# d={'name':'abc','age':'18'}
# print('name')

# money=10000
# if (money<999):
#     print('买四个窝窝头')
# elif(money<9999):
#     print('买一箱辣条')
# elif(money<99999):
#     print('谁tm买小米')
# else:
#     print('找富婆')
#
# for i in range(1000000000):
#     print(i)
#     print ('找富婆')
#




#print(list(range(100,0,-2)))

# i=2
# while(i<100):
#     print('找富婆')
#     i+=1
# for i in range(1,100):
#    if(i%10==7 or i%7==0):
#        continue
#    else:
#        print(i)

# for i in range(1,10):
#     for j in range(1,i+1):
#         d = i * j
#         print('%d*%d=%-2d'%(i,j,d),end = ' ' )
#     print()   #99乘法表
#
#
# print("------------------hhhhhhhhhhhhhh------------")
# for i in range(1,10):
#     for j in range(1,10):
#         d = i * j
#         print('%d*%d=%d'%(i,j,d),end = ' ' )
#         if (i<=j):
#             break
#     print()   #99乘法表
# print("------------------hhhhhhhhhhhhhh------------")

#
# def hanshu(n):
#     m = n
#     sums = 0
#     for j in range(1,n+1):
#         sums = m*j
#         print("%d*%d=%-2d"%(m,j,sums),end = " ")
#     print("")
# def hanshu1():
#     for i in range(9,0,-1):
#         hanshu(i)
# hanshu1()  #99
#
#
# def bubbleSort(arr):
#     n = len(arr)
#
#     # 遍历所有数组元素
#     for i in range(n):
#
#         # Last i elements are already in place
#         for j in range(0, n - i - 1):
#
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#
#
# arr = [64, 34, 25, 12, 22, 11, 90]
#
# bubbleSort(arr)
#
# print("排序后的数组:")
# for i in range(len(arr)):
#     print("%d" % arr[i])   #冒泡


# def sen(s):
#     res='查询结果'
#     return res
#
# result = sen('查询结果')
# print(result)
#
# def sen(a,b):
#     return a+b
# print (sen(5,10)) #位置参数
#
# def sen(a,b=15):
#     return a+b
# print (sen(5)) #关键字参数

# for i in range(1,1000):
#    if(i%10==5 or i//100==5 or i//10%10==5):
#        continue
#    else:
#        print(i)


# def s(*args,**kwargs):
#     print(args)
#     print(kwargs)
#
# s(1,2,3,4,a=10,b=20)
#
# f = open('a.txt','w')
# f.write('asdf')
# f.close
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,'*',i,'=',i*j,end='\t')
#     print()
#
# a=15
#
# def s():
#     global c
#     c = 20
#
# s()
# print(c)

# a='1234567890'
# b='abc'
# print(a[:10])
# print(a[0:])
# print(a[-2:])
# print(a[:-1])
# print(a[0:3],b[0:3])

# line="用例名,账户名,充值金额,预期结果"
# line= line.replace('用例名','name')
# print(line)
# print(line.split(','))
#
# print(line.find('结果'))
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{} x {} = {}'.format(j,i,i*j),end='\t') #format 格式化字符串
#     print()



#
# class sen():
#     s='fdsfa'
#
#     def replace(self):
#         print('13857asd')
#
#     def split(self):
#         print('asd45')
#
# sd=sen()
# sd.s='abc'
# sd.replace()
# sd.split()
# print(sd.s)

# class sen():
#     _a=None
#
#     def set_a(self,value):
#         self._a=value
#     def get_a(self):
#         return self._a
#
# p=sen()
# p.set_a('abc')
# print(p.get_a())
#
# import random
#  def phone():
#      l =random.choices("123456789",k=8)
#      a='189'+''.join(l)
#      print(a)
#  phone()  随机手机号
#
# def abc123(n,s):
#     l = random.choices(s,k=n)
#     print(''.join(l))
# abc123(8,"asdhgqiuwgriqeb") #随机字符串
#
# def name(x,m):
#     x1= random.choice(x)
#     m2= random.choice(m)
#     print(x1+m2)
# x="赵钱孙李王刘"
# m="一二三四五六七八能"
# name(x,m)
# print('开始')
#
#
# except (FileNotFoundError,) as e:
#    #print(1/0)
#    print('程序执行遇到了问题')
#    print('重新打开文件')
# except ZeroDivisionError as e:
#    print('除数不能为0')
# else:
#    print('程序运行没报错')
# finally:
#    print('不管程序有没有报错都会运行')
