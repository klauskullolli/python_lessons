# # there are explained some operation that can be done with datatype
# # this datatypes are imutable that cannot save the current state  

# a = 2 + 3 
# a = a +3 
# a += 3
# a+3 # ?

# b  = a + 2.4
# print(b)
# print(type(b))

# a = a**2  # this represent the power  
# a = 1.2
# a = a**3  # => a*a*a
# print(a)
# a = a**1/3 # sqrt(a)
# print(a)

# a =  2.3 // 2
# print(a)

# str1 =  "hello word"
# print(str1)
# strList  = str1.split(" ") 
# print(strList)
# str2 =  "_".join(strList)
# print(str2)
# str2 = " " + str2
# print(str2)
# print(str2.strip())
# str2 =  str2 + 5*" "
# print(str2.lstrip())
# print(len(str2),  len(str2.rstrip()))

# str3 = str2.strip()
# str3 =  str3[1::]
# print(str3)
# str3 = str1[2:7:2] # the upper boundery do not couse an error    
# print(str3)
# str3 =  str1[20:30] # even the starting point do not cause any error 
# print(str3)
# import os 
# os.system("clear")
# # print(str1[50]) # cause an index error 
# print(str1[::-1])
# print(str1[::-2])
# print(str1[-10:-3:-1])
# print(str1[-10:-len(str1)-1:-1])


from datetime import datetime 

# class Hello : 
#     a =  2 


# date_format = "%d/%m/%Y"
# date_format1 = "%d/%m"

# new_date =  "12/02/2002" 

# data_dataime  = datetime.strptime(new_date , date_format)

# data2 = datetime.strptime(new_date , date_format1)

# day , month =  data_dataime.day , data_dataime.month

# # print(data_dataime)
# print(day , month)

dict1 = {"name":"Klaus" , "goals": 12}
dict2 = {"name":"John" , "goals": 22}



ls =  [dict1,  dict2]

goals  = 0 

for el in ls: 
    goals  = goals + el["goals"] 

print(f"total goals: {goals}" )