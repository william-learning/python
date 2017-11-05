numbers = [1, 2, 3]

file = open("numbers.txt", 'w')

for item in numbers:
    file.write(str(item) + "\n")
    
file.close()