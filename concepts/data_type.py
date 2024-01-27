
# import os 
# import time

# def clear_line(): 
#     os.system('clear')
#     time.sleep(2)

#  there is not defined data type in python so no need definition but can cast data in python 


# a  = 1 # this is considered as an int python is able to determine that is an int
# a + 1 # what mean this 
# a = int(2)  # this is more precise to make sure that is considered as int 
# print(a, a+2, sep="\n")  # what is the outcome of this
# # there is mentioned even the print function that prints char to the console has some extra param that are sep , end 


# b = 1.2 # this is a floating point numer 
# c = float(2.3)
# c = float("3.4") 
# print(type(b), type(a))

# d =  True
# e =  bool(34)
# d = bool(None)  # none datatype mean a null value that is not allocated at all 

# print(e, d, bool(""))

# # there other type of representation related to binary octal or hexadecimal number 
# #  bin -> '0b1101'
# # octal -> '0O3422324'
# # hexadecimal -> '0xF2A11'  form 1, 2, 3.., F
# a = 0o33434
# print(hex(a))
# print(a)
# print(int(a))



# # all chars are considered string in python 
# a = 'a'

# # clear_line()
# print(5*"-------------")
# print(a, type(a), type(a[0]))   # even is obiously a char by python is considered string 

# a = chr(64)  # so to convert the  int to ascii value char
# print(a, type(a))

# b = ord("A")   # covert the ascii char value to string
# print(b)

# d  = "Hello Word"

# print(d,  type(d), len(d), sep='; ')  # len is used to return the length of string 

# e = 'hey hello word again'

# print(e)
# e = '''Test example 
# example test 
# example test 
# test test hello word'''

# # e = '

# # fdfdfdf
# # dfdf'

# print(5*"----------------------")
# k = 2.3
# d = 12.4
# str1  =  f'{k}, {d}, {k+d}'
# str2 = "%0.2f, %0.2f, %0.2f" % (k, d, k + d) 
# str3 = "{:0.2f}, {:0.2f}, {:0.2f}".format(k, d, k+d)
# print(str1)
# print(str2)
# print(str3)

# print(5*"----------------------")

# header =  "{:10s} {:10s} {:10s}".format("a", "b", "sum")
# print(header)

# values = "{:10s} {:10s} {:10s}".format(str(k), str(d), str(k+d))
# values2=  f'{k:.1f} {d:10.1f} {(k+d):10.1f}'
# print(values)
# print(values2)


a = 1  # it is an int
print(a , "Hello word" , "etc", sep="_") 
 
a = 2.4 # float 
print(type(a))

str1 = "I am a string"
char1 = "A"
print(type(str1), type(char1))

el = "44"
a =  int(el)  # so int is used to convert a datatype into an integer value 
print(a, type(a))

b =  int(3.4444)
print(b)

# b =  int("err")  
# print(b)

str2 =  str(3.4445)   # used for string convertion

