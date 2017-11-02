# Syntax Errors 

# Exception Handling

def divide(a,b): 
    try: 
        return a/b
    except ZeroDivisionError:   # Other types of exceptions will not be caught
        return "Zero Division is meaningless"
        
print(divide(1,0))
print("End of program")