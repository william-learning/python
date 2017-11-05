# file = open("temperature.txt", 'w')

# temperatures=[10,-20,-289,100]
# def c_to_f(c):
#     if c< -273.15:
#         return "That temperature doesn't make sense!"
#     else:
#         f=c*9/5+32
#         return f
# for t in temperatures:
#     if type(c_to_f(t)) == float:
#         file.write(str(c_to_f(t)) + "\n")
    
# file.close()

temperatures=[10,-20,-289,100]

def writer (temperatures):
    with open("temperature.txt", 'w') as file:
        for c in temperatures:
            if c > -273.15:
                f = c * 9 / 5 + 32
                file.write(str(f) + "\n")
                
writer(temperatures)