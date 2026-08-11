# Log Analyzer

# Now we'll make the script more useful.

# Instead of simply displaying logs, we want to count:

# INFO messages
# WARNING messages
# ERROR messages

# For our file:
#  - INFO: Server started
#  - INFO: Application deployed
#  - WARNING: CPU usage reached 75%
#  - ERROR: Database connection failed
#  - INFO: Database connection recovered
#  - WARNING: Memory usage reached 80%
#  - ERROR: API request failed
#  - INFO: Server health check completed

# The expected result is:
#  - INFO    : 4
#  - WARNING : 2
#  - ERROR   : 2



info_count = 0
warning_count = 0
error_count = 0

with open("server.log", "r") as file:
    for line in file:
        line = line.strip()

        if line.startswith("INFO"):
            info_count += 1
        elif line.startswith("WARNING"):
            warning_count += 1
        elif line.startswith("ERROR"):
            error_count +=1

print("Log Analysis Report")
print("-------------------")

print("INFO    :", info_count)
print("WARNING :", warning_count)
print("ERROR   :", error_count)
