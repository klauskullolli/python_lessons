a =  True and True
print("True and True: " , a)
a =  True and False
print("True and False: " , a)
a =  False and False
print("False and False: " , a)

b =  True or True
print("True or True: " , b)
b =  True or False
print("True or False: " , b)
b =  False or False
print("False or False: ", b)


b =  True ^ True
print("True xor True: ", b)
b =  True ^ False
print("True xor False: " , b)
b =  False ^ False
print("False xor False: " , b)

a = not True # !True
print(a)
a = not False
print(a)

# condition in python 

a = 20

if a > 30 : 
    print(f"a is bigger than 30")
elif a == 30:
    print(f"a is equal 30") 
else: 
    print(f"a is smaller than 30")

# check if number is odd or even 
# if is even compare if is procudet of 4 
# if is ood check if is product of 3
    
# this example put into work the nested condition 

if a%2==0:
    print(f"{a} is even")
    if a%4 == 0: pass 
    else:
        pass       
    
else: 
    print(f"{a} is odd") 
    if a%3 == 0: 
        pass 
    else:
        pass  

a= 1
match a : 
    case 1 :
        print(f"a is 0") 
    case _ :
        print(f"number is differnt from 1")







