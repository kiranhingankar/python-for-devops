# Read a Server Log File

# Problem : Write a Python program that:
#  - Opens server.log
#  - Reads every line
#  - Prints each log line
#  - Removes unnecessary whitespace

with open("server.log", "r") as file:
    for line in file:
        print(line.strip())
