# Section 1, 2, and 3 
#greeting = input("Write a greeting: ")
#print(greeting)

#number = 20 - 10 / 5 * 3 **2 
#print(number)

#string = "Here"
#string.replace("e","i")
#print(string.replace("e","i"))




# Section 4

def age_foo(age): 
    new_age = float(age) + 50
    return new_age
    
age = float(input("Enter your age: ")) # input function always outputs a string

if age < 150: 
    print(age_foo(age))
else: 
    print("How is that possible?")
