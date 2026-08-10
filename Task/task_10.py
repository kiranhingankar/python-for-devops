# Basic Log File Parser

# Problem

# Given a log entry:
# ERROR: Disk usage exceeded 90%

# Print:
# Log Level
# Log Message


log = input("Enter log level: Enter Log error message :")

parts = log.split(":")

print("Log Level :", parts[0])
print("Message :", parts[1].strip())