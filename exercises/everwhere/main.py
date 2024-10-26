from datetime import datetime   


#  now  = h->1, m->30    
#  add  = h->1, m->30   
#  now + add = h->2, m->0

import re 

a = "My name is {name} and I am {age} years old"    

b = r'\{\}'      


# Just a simple class to  calculate hours and minutes addition and subtraction  
class Time_Class:  
    def __init__(self,  hour=None, minute=None):
        one_none = hour is None and minute is not None  
        
        if one_none:
            if hour is None:    
                self.hour = datetime.now().hour
            if minute is None:
                self.minute = datetime.now().minute 
            self.day = 0    
            return  
        
        extra_hour = minute // 60   
        self.minute = minute % 60   
        self.hour = hour  + extra_hour  
        extra_day = self.hour // 24 
        self.hour = self.hour % 24  
        self.day = 0 + extra_day         

    # this is a magic method that allows us to add two objects of the class A   
    def __add__(self, other: 'Time_Class') -> 'Time_Class':
        new = Time_Class(self.hour, self.minute)    
        new.minute += other.minute
        extra_hour = new.minute // 60
        new.minute = new.minute % 60
        new.hour += other.hour + extra_hour
        extra_day = new.hour // 24
        new.hour = new.hour % 24
        new.day += other.day + extra_day
        return new         

    def __sub__(self, other: 'Time_Class') -> 'Time_Class':   
        new = Time_Class(self.hour, self.minute)    
        if new.minute < other.minute:  
            new.minute += 60  
            new.hour -= 1  
        new.minute -= other.minute

        if new.hour < other.hour:  
            new.hour += 24  
            new.day -= 1   

        new.hour -= other.hour    
        
        return new     

    def check_day(self):
        if self.day  == 0:  
            return "Today"  
        if self.day == 1: 
            return "Tomorrow"
        if self.day == -1: 
            return "Yesterday"
        if self.day > 1: 
            return f"{self.day} days from now"  
        if self.day < -1:   
            return f"{abs(self.day)} days ago"
    
    def __str__(self):
        return f"{self.check_day()} {self.hour}:{self.minute}"  
      

a =   Time_Class(1, 30) 
b =  Time_Class(18, 45)

c = a - b 
a = a + b
  

print(a) 
print(c)   

# print(a.strftime("%Y-%m-%d %H:%M:%S"))

# a + 1   

# print(a)    

