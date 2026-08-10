# Server Resource Health Checker

# Problem

# Take the following inputs:
# CPU Usage (%)
# RAM Usage (%)

# Display the server status:
# Critical → CPU > 90 or RAM > 90
# Warning → CPU > 70 or RAM > 70
# Healthy → Otherwise

cpu = int(input("Enter CPU Usage in (%): "))
ram = int(input("Enter RAM Usage in (%): "))

print("\n ===== Server Health Report =====")

if cpu > 90 or ram > 90:
    print("Status : Critical")
elif cpu > 70 or ram > 70:
    print("Status : Warning")
else:
    print("Status: Healthy")