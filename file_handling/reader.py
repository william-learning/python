#filename = input("Please enter file name: ")

#file = open(filename, 'r')
file = open('fruits.txt', 'r')
content = file.readlines()
content = [i.rstrip("\n") for i in content]
for i in content:
    print(len(i))
file.close()