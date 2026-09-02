#step 4 Nested if statement
# age = 20
# has_id = True

# if age >= 18:
#      if has_id:
#          print("entry allowed")
#      else:
#          print("ID requird")
# else:
#     print("entry denied: must be 18+")            


 #step 1: for loop with range()
# for i in range(1,6):
#      print("Interation:",1)

# A = 50
# B = 40
# if A>B:
#     A+=1
#     print(A)
# m = 2
# x = 3
# c = 1
# y = (m*x)+(c^2)
# print(y)

# fruit = ["apple", "banana", "mango", "grspes"]
# for fruit in fruit:
#     print("fruit:", fruit)


# for i in range(1, 100):
#      print("number:",i)

# for ch in "python":
    #  print(ch, end="   ")


# count = 1

# while count <= 10:
#      print("count is:", count)
#      count += 1

# a = "hello"
# b = "world"
# print(a+" "+ b)

# for num in range(1, 10):
#     if num == 5: 
#       break
# print(num)

# list = [10,20,30,40,50]
# print(min(list))
# print(max(list))


# lst = [20,50,65]
# print(list(enumerate(lst)))


# lst = [80,20,40,60,56]
# #index position and element meet together
# for index, num in enumerate(lst):
#     print(f"position {index}: {num}")



    #function with parameters

# def add(a,b):
#     result = a+b     
#     print(result)


# def sub(a,b):    
#     result = a-b
#     print(result)

 #function calling
# add(34,54)
# sub(20,40)


# def check_odd(num):
#     if num % 2 != 0:
#         return "odd"
#     else:
#        return "Even"
# n= int(input("enter a number:"))
# result = check_odd(n)
# print(result)

 



# def check_prime(num):
#     if num % 2 != 0:
#         return "prime" 
#     else:
#         return "not prime"
# n = int(input("enter a number:"))
# result = check_prime(n)
# print(result)    
    



    #wap to check number prime or not with the help of user defind function
# def check_prime(num):
#     if num <2:       
#         return False
#     for i in range(2 , num):
#         if num % i == 0:
#              return False
#         return True
#      #takeuser input
# n= int(input("enter a number:"))
# result = check_prime(n)
# print(result)


# def check_prime(num):
#     if num <2:
#       return False
#     for i in range(2 , num):
#         if num % i == 0:
#             return False
#         return True
# n= int(input("enter a number:"))
# if check_prime(n):
#     print(n, "is prime number")
# else:
#      print(n, "is not prime number")


#wap to print tringle pattern
# *
# **
# ***
# ****
# *****

# rows = int(input("enter row:"))

# #outer loop

# for i in range(1, 6):
#     for j in range(1, i+1)
#        print("*", end= " ")
#     print()    
    



# rows = int(input("enter row:"))
# for i in range(6, 0,-1):
#     for j in range(i,0,-1):
#        print("*", end= " ")
#     print()


# row = int(input("enter row:"))
# for i in range(5):
#     for j in range(5):
#         print("*", end= " ")
#     print()





# lst=[1,2,3,4,5]
# print(lst)
#  #traverse the array each of element
# for i in range(len(lst)):
#     print(lst[i])


# lst.remove(4)
# print(lst)

# lst.extend([6,7,8])
# print(lst)


# lst.pop(4)
# print(lst)


# lst.insert(1,4)
# print(lst)

# lst.append(3)
# print(lst)

# arr = [
#     [10,20,30,40],
#     [50,60,70,80],
#     [90,10,20,30],
# ]
# print(arr)


# print(arr[0][0])
# print(arr[1][2])
# print(arr[2][3])


# def is_prime(n):
#     if n<=1:
#         return False
    
#     for i in range(2, int(n**0.5) + 1):
#         if n%i==0:
#             return False
#     return True


#     for num in range(1,31):
#         if is_prime(num):
#             print(num)



for i in range(1,6):
    if i<5:
      print("*",end = " ")
    else:
       print("****")