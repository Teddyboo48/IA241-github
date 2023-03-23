 #Class
 #A funstion that is defined inside a class definition
 #Is invoked on instances of that class 
 #class attribute
# One of the named values associated with an object
 
class car: #define a class
    maker = 'toyota' #define an attribute
    
    def report_maker(self):
        return(self.maker)
    def __init__(self,input_model):
        def report(self):
            return self.maker,self.model
        self.model = input_model 
my_highlander = car('highlander')
my_corolla = car('corolla')
print(my_highlander.maker)
print(my_highlander.model)
print(my_corolla.maker)
print(my_corolla.model)
