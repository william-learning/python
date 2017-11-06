import glob2
import datetime

now = datetime.datetime.now()

file_input = glob2.glob("*.txt")

with open(now.strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt", 'w+') as merge_file:
    for item in file_input:
        with open(item, 'r') as file:
            merge_file.write(file.read() + "\n")

        