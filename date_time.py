"""
This script returns current date and time
2 modules providing date and time functionality
"""

import datetime
print(datetime.datetime.now())     # module.class.function()

now = datetime.datetime.now()
filename=now.strftime("%Y-%m-%d-%H-%M-%S") + ".txt"

# Creates empty file
def create_file(): 
    with open(filename, 'w') as file:
        file.write("")  # Writes an empty string
        
create_file()