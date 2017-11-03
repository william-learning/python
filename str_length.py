def str_length(string):
    if type(string) == str:
        return len(string)
    elif type(string) == int: 
        return "Sorry, integers don't have length"
    elif type(string) == float: 
        return "Sorry, floats don't have length"
    
print(str_length("Hello"))