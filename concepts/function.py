

# def fun1():
#     print("hello word")
#     pass


# def fun2(a, b):
#     print(f"a -> {a}; b -> {b}")


# def fun3(a=2, b=5):
#     print(f"a -> {a}; b -> {b}")


# def func4(a, b, /, c, d, *, e, f):
#     print(f"a -> {a}; b -> {b}; c -> {c}; d -> {d}; e -> {e}; f -> {f}")


# # fun2(7, 3)
# # fun2(b=2, a=3)

# func4(1, 3, 3, d=4, e=4, f=9)

# #  fibonaci numebr
# # 1, 1, 2, 3, 5

# def fibo(n): 
    
#     if n == 1 or n ==2 : 
#         return 1 
#     else:
#         return fibo(n-1) + fibo(n-2)


# print(fibo(5))


# def  func6(*arg,  **kwrgs): 
#     print(arg)
#     print(kwrgs)


# this is function creation 

# def function1(): 
#     print("hello word")
#     # return 10   

# def func2(): 
#     pass

# # function calling
# retuned_value  = function1()
# print(retuned_value)


# a =  42 

# b = 323 
# str1 =  f" value of b is {b} and value of a is: {a}"  # using string formatting 
# print(str1)

# str2 =  "value of b is " + str(b) + " value of a is: " + str(a)  # without using string formatting
# print(str1)

# function can be with params or without params 
def fun2(a, b):
    print(f"a -> {a}; b -> {b}")
    

def fun3(a=3, b=21):
    print(f"a -> {a}; b -> {b}")

# fun2("hello" , 34.4)

# fun3(a="Hello word" , b= "Hello too")
# fun3(b= "Hello too")


#  can call nested function inside a function 
def func3(): 
    print("I am func3")
    fun2(12, 4)
    print("I called func 2")

# func3()

action = lambda x,y,z : (x+y)*z
value  =  action(2,3,4)
print(value)
