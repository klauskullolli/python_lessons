import abc 

class  Shape(abc.ABC): 
    
    @abc.abstractmethod
    def surface(): 
        pass 
    
    