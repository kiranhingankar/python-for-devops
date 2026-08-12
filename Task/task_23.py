# Server Health Report Generator

# Problem : Create a Python program that:
#  - Takes server name from the user.
#  - Takes CPU usage.
#  - Takes RAM usage.
#  - Determines server health.
#  - Writes the result into server_report.txt.
# 
# Rules
#  - CPU > 90 OR RAM > 90 → CRITICAL
#  - CPU > 70 OR RAM > 70 → WARNING
#  - Otherwise → HEALTHY

server_name = input("Enter Server Name: ")
cpu = int(input("Enter CPU Usage (%): "))
ram = int(input("Enter RAM Usage (%): "))

if cpu >= 90 or ram >= 90:
    status = "CRITICAL"
elif cpu >= 70 or ram >= 70:
    status = "WARNING"
else:
    status = "HEALTHY"

with open("server_report.txt", "w") as file:
    file.write("Server Health Report\n")
    file.write("--------------------\n")
    file.write(f"Server Name: {server_name}\n")
    file.write(f"CPU Usage: {cpu}%\n")
    file.write(f"RAM Usage: {ram}%\n")
    file.write(f"Status: {status}\n")

print("Report generated successfully.")