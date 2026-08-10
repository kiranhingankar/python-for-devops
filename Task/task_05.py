# Server Health Checker

# Problem

# Write a program that:
# Takes CPU usage (%) from the user.
# If CPU usage is greater than 80%, print High CPU Usage!
# Otherwise, print CPU Usage is Normal.

cpu_usage = int(input("Enter CPU Usage (%): "))

if cpu_usage > 80:
    print("\nAlert: High CPU Usage!")
else:
    print("\nCPU Usage is Normal.")