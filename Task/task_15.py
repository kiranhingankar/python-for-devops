# Server Status Checker Function

# Problem : Create a function that checks server CPU usage.

# Rules:
# CPU > 80 → High CPU Usage
# Otherwise → CPU Usage Normal

def check_cpu(cpu):
    if cpu > 80:
        print("Alert: High CPU Usage!")
    else:
        print("CPU Usage Normal.")

cpu = int(input("Enter CPU Usage (%): "))

check_cpu(cpu)